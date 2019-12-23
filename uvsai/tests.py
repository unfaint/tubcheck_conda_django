from django.test import TestCase, Client
from glob import glob
import os
from django.conf import settings
from .models import XRayImage, Competitor


class SmokeTest(TestCase):

    def test_start_page_returns_html(self):
        c = Client()

        response = c.get('/uvsai/')

        self.assertIn(b'html', response.content)

    def test_redirect_on_enter(self):
        c = Client()

        response = c.post(
            '/uvsai/enter',
            data={
                'id_input': 'test@test',
            }
        )

        self.assertEqual(response.status_code, 302)


class ModelSmokeTest(TestCase):

    def test_can_create_image_objects_for_files(self):
        file_list = glob(os.path.join(settings.STATIC_URL, 'images'))

        user = Competitor()
        user.save()

        for f in file_list:
            xray = XRayImage()
            xray.file = f
            xray.user = user
            xray.save()

        saved_user = Competitor.objects.first()
        self.assertEqual(user, saved_user)

        saved_xrays = XRayImage.objects.all()
        self.assertEqual(saved_xrays.count(), len(file_list))


class XRayImageListTest(TestCase):

    def test_create_new_competitor_on_first_enter(self):
        c = Client()
        email = 'test@test'
        _ = c.post(
            '/uvsai/enter',
            data={
                'id_input': email,
            }
        )

        saved_user = Competitor.objects.first()

        self.assertEqual(saved_user.email, email)
