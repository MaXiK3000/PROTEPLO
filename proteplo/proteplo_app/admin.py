from django.contrib import admin
from .models import Image, Service, Gallery, Information, Review

# Register your models here.
admin.site.register(Gallery)
# admin.site.register(Image)
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'gallery')
admin.site.register(Service)
admin.site.register(Information)
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')