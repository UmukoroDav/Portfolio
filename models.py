from django.db import models

# Create your models here.
class About(models.Model):
    details = models.TextField()
    image = models.ImageField(upload_to='image/')

class Expertise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.title


class Educations(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.title
    
class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, default='Recital')
    composer = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    project_link = models.URLField(blank=True, null=True)
    description = models.TextField()
    date = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"{self.title} by {self.composer}"


class Contact(models.Model):
    email = models.EmailField(unique=True)
    telephone = models.IntegerField()

    def __str__(self):
        return self.email


class Social(models.Model):
    name = models.CharField(max_length=100)
    urlfiled = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='certificates/')
    description = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
