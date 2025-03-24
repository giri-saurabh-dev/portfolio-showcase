from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, help_text="Font Awesome class for icon")
    proficiency = models.IntegerField(help_text="Skill level from 1 to 100")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=300)

    def __str__(self):
        return self.title

