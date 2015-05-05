from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class QuestionSet(models.Model):
    title = models.TextField(unique=True)
    description = models.TextField(unique=True)
    number = models.IntegerField()
    max_questions = models.PositiveIntegerField()
    course = models.ForeignKey("courses.Course")
    week = models.ForeignKey("courses.Week")


class Question(models.Model):
    POSSIBLE_TYPES = (
        ("multiset", "Multiple checkboxes"),
        ("singleset", "Radiobuttons"),
        ("multiset_custom", "Multiple checkboxes with student's own answer"),
        ("singleset_custom", "Radiobuttons with student's own answer")
    )

    questionset = models.ForeignKey(QuestionSet)
    question = models.TextField()
    explanation = models.TextField(blank=True, default="")
    value = models.PositiveIntegerField()
    type = models.TextField(choices=POSSIBLE_TYPES)


class PossibleAnswer(models.Model):
    text = models.TextField()
    correct_value = models.TextField(null=True, default=None)
    is_correct = models.BooleanField(default=False)
    explanation = models.TextField(blank=True, default="")


class StudentAnswerSet(models.Model):
    user = models.ForeignKey(User)
    questionset = models.ForeignKey(QuestionSet)
    mark = models.PositiveIntegerField()
    is_finished = models.BooleanField(default=False)


class StudentAnswer(models.Model):
    answerset = models.ForeignKey(StudentAnswerSet)
    question = models.ForeignKey(Question)
    chosed_answer = models.ForeignKey(PossibleAnswer)