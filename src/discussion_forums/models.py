from django.db import models


class Forum(models.Model):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)  # type: ignore
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Thread(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)  # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    created_by = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)  # type: ignore
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
