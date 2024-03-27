from django.db import models
from django.contrib.auth.models import Permission


class Role(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    permissions = models.ManyToManyField(Permission)  # type: ignore
