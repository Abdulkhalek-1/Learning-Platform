from django.db import models


class Review(models.Model):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)  # type: ignore
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)  # type: ignore
    rating = models.IntegerField(
        default=0,
        choices=[
            (1, "1 Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ],
    )
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
