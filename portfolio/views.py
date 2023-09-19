from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, ProjectImage
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new project instance and populate it with form data
            project = form.save(commit=False)

            # Process the location data (assuming locations are comma-separated)
            location_data = request.POST.getlist('locations')
            project.locations = ', '.join(location_data)

            project.save()

            # Process and save the uploaded images
            for image in request.FILES.getlist('images'):
                project_image = ProjectImage(project=project, image=image)
                project_image.save()

            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/project_form.html', {'form': form})

def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            # Update the project instance and populate it with form data
            project = form.save(commit=False)

            # Process the location data (assuming locations are comma-separated)
            location_data = request.POST.getlist('locations')
            project.locations = ', '.join(location_data)

            project.save()

            # Clear existing project images and re-save the uploaded images
            ProjectImage.objects.filter(project=project).delete()
            for image in request.FILES.getlist('images'):
                project_image = ProjectImage(project=project, image=image)
                project_image.save()

            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/project_form.html', {'form': form})

def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'portfolio/project_confirm_delete.html', {'project': project})
