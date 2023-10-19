from django.db import models

# Create your models here.

class Course(models.Model):
    course_id =models.CharField(
        unique = True,
        null = False,
        blank=False,
        max_length=20
    ) 

    name = models.CharField(
        unique = True,
        null = False,
        blank=False,
        max_length=30
    )

    description = models.TextField(
        unique = True,
        null=False,
        blank=False,
        max_length=2000
    )

    def __str__(self) -> str:
        return self.name

class Person(models.Model):
    first_name =models.CharField(
        unique = False,
        null = False,
        blank=False,
        max_length=30
    ) 

    middle_name =models.CharField(
        unique = False,
        null = True,
        blank=True,
        max_length=30
    ) 

    last_name =models.CharField(
        unique = False,
        null = False,
        blank=False,
        max_length=30
    ) 

    courses = models.ManyToManyField(
    Course
    )
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
 