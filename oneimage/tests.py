from django.test import TestCase, Client
from django.conf import settings
from rest_framework.test import APIClient
import os
from PIL import Image
import json
from tubcheck.ml import DenseNet121, load_model
from tubcheck import ml_model
import torch


class MLModelTest(TestCase):

    def test_can_load_model(self):
        model = load_model()

        self.assertIsInstance(model.module, DenseNet121)

    def test_can_do_forward_pass(self):
        input_ = Image.open(os.path.join(settings.BASE_DIR, 'xray.jpg'))

        output = ml_model(input_)

        self.assertIsInstance(output, dict)
        self.assertIsInstance(output['tensor'], torch.Tensor)


class RESTfulAPITest(TestCase):

    def test_check_endpoint_returns_json(self):
        c = Client()
        with open(os.path.join(settings.BASE_DIR, 'xray.jpg'), 'rb') as fp:
            output = ml_model(Image.open(fp))

        with open(os.path.join(settings.BASE_DIR, 'xray.jpg'), 'rb') as fp:
            response = c.post(
                '/oneimage/check',
                {'image': fp},
            )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['results'], output['results'])
