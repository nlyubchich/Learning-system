from django.core.validators import RegexValidator
from django.db import models


class Course(models.Model):
    title = models.TextField(unique=True)
    img = models.ImageField(upload_to="courses", default="/media/courses/default.png")
    short_description = models.TextField(default="")
    full_description = models.TextField(default="")


class News(models.Model):
    course = models.ForeignKey("Course")
    title = models.TextField()
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)


class Week(models.Model):
    course = models.ForeignKey("Course")
    number = models.IntegerField("Number of week")

    class Meta:
        unique_together = ('course', 'number',)


class Lecture(models.Model):
    order_id = models.IntegerField()
    title = models.CharField(max_length=80)
    video_url = models.URLField(
        validators=[RegexValidator(r"^https?:\/\/(www\.)?youtube\.com\/watch\?v\=\S{11}$", "It is not from Youtube")])
    embed_video_url = models.URLField(
        validators=[RegexValidator(r"^https?:\/\/(www\.)?youtube\.com\/embed\/\S{11}$", "Something bad with URL")])

    week = models.ForeignKey("Week")

    class Meta:
        unique_together = ('order_id', 'week',)
        ordering = ('order_id',)


class LectureMaterials(models.Model):
    lecture = models.ForeignKey("Lecture")
    title = models.TextField()
    link = models.URLField()