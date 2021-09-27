from django.db import models
from django.contrib.auth.models import User


# a simple user part in which it can
# see the training courses available with possibility of search and
# filter by category (web, mobile, Cloud) as well as their details.

# Create your models here.
class Categories(models.Model):
    category_choices = (
        ("web","web"),
        ("mobile","mobile"),
        ("cloud","cloud")
    )
    name = models.CharField(max_length=100,choices=category_choices,blank=True,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    course_details = models.TextField(max_length=500)
    logo = models.ImageField()
    cotegory = models.ForeignKey(Categories, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
