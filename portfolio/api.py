from rest_framework import generics
from rest_framework.response import Response
from .models import Project, BannerImage, ProjectImage
from .serializers import ProjectSerializer, ProjectImageSerializer, BannerImageSerializer

class ProjectListAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BannerImageListAPIView(generics.ListAPIView):
    queryset = BannerImage.objects.all()
    serializer_class = BannerImageSerializer

class ProjectListByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        category_name = self.request.data.get('category_name')
        if category_name:
            return Project.objects.filter(category__name=category_name)
        else:
            return Project.objects.all()

    def get_serializer(self, *args, **kwargs):
        # Customize the serializer to include project images
        kwargs['context'] = self.get_serializer_context()
        return ProjectSerializer(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        # Deserialize locations as an array
        locations = request.data.get('locations', [])
        request.data['locations'] = locations
        return super().create(request, *args, **kwargs)
