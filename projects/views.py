from django.shortcuts import render, redirect
from .models import Project, Tag
from .forms import ProjectForm 
from django.contrib.auth.decorators import login_required


def projects(request):
    projects = Project.objects.all()
    # projects = searchProjects(request)
    # custom_range, projects = paginateProjects(request, projects, 6)

    context = {'projects': projects,
            }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
#     form = ReviewForm()

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         review = form.save(commit=False)
#         review.project = projectObj
#         review.owner = request.user.profile
#         review.save()

#         projectObj.getVoteCount

#         messages.success(request, 'Your review was successfully submitted!')
#         return redirect('project', pk=projectObj.id)

    return render(request, 'projects/single-project.html', {'project': projectObj,})

@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

#@login_required(login_url="login")
# def updateProject(request, pk):
    
#     project = Project.objects.get(id=pk)
#     form = ProjectForm(instance=project)
#     if request.method == 'POST':
#         form = ProjectForm(request.POST , request.FILES, instance=project)
#         if form.is_valid():
#             form.save()
#             return redirect('projects')

#     context = {'form': form}
#     return render(request, "projects/project_form.html", context)


#@login_required(login_url="login")
# def deleteProject(request, pk):
#     project = Project.objects.get(id=pk)
#     if request.method == 'POST':
#         project.delete()
#         return redirect('projects')
    
#     context = {'object': project}
#     return render(request, 'delete_template.html', context)



# Create your views here.
