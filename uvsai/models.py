from django.db import models


class XRayImage(models.Model):
    file = models.TextField()
    user = models.ForeignKey('Competitor', on_delete=models.CASCADE, default=None)


class Competitor(models.Model):
    email = models.TextField()
