from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)  # type: ignore
    order = models.IntegerField()


class Video(models.Model):
    lesson = models.OneToOneField(
        Lesson, on_delete=models.CASCADE, related_name="video"
    )
    title = models.CharField(max_length=255)
    video_file = models.FileField(
        upload_to="lesson_videos/"
    )  # Upload videos to media/lesson_videos/


class Document(models.Model):
    lesson = models.OneToOneField(
        Lesson, on_delete=models.CASCADE, related_name="document"
    )
    title = models.CharField(max_length=255)
    file = models.FileField(
        upload_to="lesson_documents/"
    )  # Upload documents to media/lesson_documents/
