from rest_framework import serializers
from .models import Category, Project, ProjectImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # You can specify which fields to include if needed

class ProjectSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Use the CategorySerializer for the related field

    class Meta:
        model = Project
        fields = '__all__'

    def to_representation(self, instance):
        # Serialize locations as an array
        representation = super().to_representation(instance)
        representation['locations'] = instance.locations
        return representation    
        
class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('image',)