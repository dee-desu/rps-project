from django.contrib import admin
from .models import Category, Project, ProjectImage, BannerImage

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectImage)
@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'created_at']