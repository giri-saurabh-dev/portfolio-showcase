from django.db import models

class Skill():
    title = models.CharField(max_length=200)
    description = models.TextField()
        
    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=300)

    def __str__(self):
        return self.title

