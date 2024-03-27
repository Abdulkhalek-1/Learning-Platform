from django.db import models


class Quiz(models.Model):
    lesson = models.ForeignKey("lessons.Lesson", on_delete=models.CASCADE)  # type: ignore
    title = models.CharField(max_length=75)
    description = models.TextField()
    time_limit = models.PositiveIntegerField(
        default=0, help_text="Time limit for the quiz in minutes (0 for no limit)"
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    # Define choices for question_type
    MULTIPLE_CHOICE = "MCQ"
    TRUE_FALSE = "TF"
    SHORT_ANSWER = "SA"

    QUESTION_TYPE_CHOICES = [
        (MULTIPLE_CHOICE, "Multiple Choice"),
        (TRUE_FALSE, "True/False"),
        (SHORT_ANSWER, "Short Answer"),
    ]
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.TextField()
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPE_CHOICES)
    explanation = models.TextField(blank=True, null=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    is_correct = models.BooleanField(default=False)


class Submission(models.Model):
    user = models.ForeignKey("accounts.CustomUser", verbose_name="", on_delete=models.CASCADE)  #type: ignore
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    answers = models.ManyToManyField(Answer, related_name="quiz_submissions")  # type: ignore
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
