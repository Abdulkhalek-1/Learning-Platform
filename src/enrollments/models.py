from django.db import models


class Enrollment(models.Model):
    user = models.ForeignKey("accounts.CustomUser", verbose_name="", on_delete=models.CASCADE) #type: ignore
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)  # type: ignore
    enrollment_date = models.DateTimeField(auto_now_add=True)
    completion_status = models.BooleanField(default=False)
