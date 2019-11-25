from django.test import TestCase
from django.conf import settings
import os
from PIL import Image
from .ml import DenseNet121, load_model
import torch


class MLModelTest(TestCase):

    def test_can_load_model(self):
        model = load_model()

        self.assertIsInstance(model.module, DenseNet121)

    def test_can_do_forward_pass(self):
        model = load_model()
        input_ = Image.open(os.path.join(settings.BASE_DIR, 'xray.jpg'))

        output = model(input_)

        self.assertIsInstance(output, torch.Tensor)
