from django.urls import path, include
from . import views
from .api import ProjectListAPIView, ProjectListByCategoryAPIView

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create, name='project_create'),
    path('<int:project_id>/edit/', views.project_edit, name='project_edit'),
    path('<int:project_id>/delete/', views.project_delete, name='project_delete'),
    path('projects/', views.project_list, name='project_list'),
    path('api/projects/', ProjectListAPIView.as_view(), name='project-list'),
    # path('api/projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('api/projects/', ProjectListAPIView.as_view(), name='project-list'),
    # path('api/projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('api/projects/category/', ProjectListByCategoryAPIView.as_view(), name='project-list-by-category'),
    ]
