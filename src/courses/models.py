from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    instructor = models.ForeignKey("accounts.CustomUser", verbose_name=(""), on_delete=models.CASCADE) #type: ignore
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)