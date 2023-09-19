from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

class Category(models.Model):
    catname = models.CharField(max_length=100)

    def __str__(self):
        return self.catname

class Project(models.Model):
    name = models.CharField(max_length=200)
    date = models.IntegerField(choices=[(year, year) for year in range(1940, 2201)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='project_thumbnails/', null=True, blank=True)
    locations = ArrayField(models.CharField(max_length=100), blank=True)

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return str(self.image)
    
class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner_images/')
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.image)   
