import os
import uuid
from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

def get_image_upload_path(instance, filename):
    gallery_title = instance.gallery.title
    gallery_slug = slugify(gallery_title)
    print("Путь" + gallery_slug)
    return os.path.join('galleries/' + gallery_title, gallery_slug, filename)

class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete = models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=get_image_upload_path)

    def __str__(self):
        return self.title if self.title else f"Image {self.pk}"

class Service(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='servises/')
    text = HTMLField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    review = models.CharField(max_length=3000, blank=True)
    value = models.IntegerField(blank=True)

    def __str__(self):
        return self.title
    
class Information(models.Model):
    title = models.CharField(max_length=200, blank=True)
    main_text =  HTMLField()
    text = HTMLField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title