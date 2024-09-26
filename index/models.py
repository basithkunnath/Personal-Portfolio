from django.db import models

# Create your models here.


class About(models.Model):
    heading = models.CharField(max_length=200)  # Field for the heading
    image = models.ImageField(upload_to='about_images/')  # Field for the image
    description = models.TextField()  # Field for the description

    def __str__(self):
        return self.heading
    

class Services(models.Model):
    heading = models.CharField(max_length=200)  # Main heading for the services section
    service1_title = models.CharField(max_length=100)  # Title for the first service
    service1_icon = models.ImageField(upload_to='services_icons/')  # Icon for the first service
    service2_title = models.CharField(max_length=100)  # Title for the second service
    service2_icon = models.ImageField(upload_to='services_icons/')  # Icon for the second service
    service3_title = models.CharField(max_length=100)  # Title for the third service
    service3_icon = models.ImageField(upload_to='services_icons/')  # Icon for the third service

    def __str__(self):
        return self.heading


class Projects(models.Model):
    project_image = models.ImageField(upload_to='project_images/')  # Image for the project


class Contact(models.Model):
    heading = models.CharField(max_length=200)  # Field for the heading

    def __str__(self):
        return self.heading