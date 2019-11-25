from torch import nn, load
from torchvision.models import densenet121
from torchvision import transforms
import re
import os
from django.conf import settings


def fix_state_dict(state_dict):
    remove_data_parallel = False

    pattern = re.compile(
        r'^(.*denselayer\d+\.(?:norm|relu|conv))\.((?:[12])\.(?:weight|bias|running_mean|running_var))$')
    for key in list(state_dict.keys()):
        match = pattern.match(key)
        new_key = match.group(1) + match.group(2) if match else key
        new_key = new_key[7:] if remove_data_parallel else new_key
        state_dict[new_key] = state_dict[key]

        if match or remove_data_parallel:
            del state_dict[key]
    return state_dict


def load_model():
    model = DenseNet121(2)
    model = nn.DataParallel(model)

    checkpoint = load(os.path.join(settings.BASE_DIR, 'TB_cpu.model'))
    state_dict = fix_state_dict(checkpoint)
    model.load_state_dict(state_dict)

    return model


class DenseNet121(nn.Module):

    def __init__(self, out_size=2):
        super(DenseNet121, self).__init__()
        self.densenet121 = densenet121(pretrained=True)
        num_ftrs = self.densenet121.classifier.in_features
        self.densenet121.classifier = nn.Sequential(
            nn.Linear(num_ftrs, out_size),
            nn.Sigmoid()
        )
        self.transforms = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Lambda(
                lambda x: x.unsqueeze(0)
            )
        ])

    def forward(self, x):
        x = self.transforms(x)
        x = self.densenet121(x)
        x = {
            'tensor': x,
            'results': round(float(x[0, 1]), 2),
        }
        return x

    def change_classes(self, out_size):
        num_ftrs = self.densenet121.classifier[0].in_features
        self.densenet121.classifier = nn.Sequential(
            nn.Linear(num_ftrs, out_size),
            nn.Sigmoid()
        )


ml_model = load_model()
