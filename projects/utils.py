from .models import Project, Tag
from django.db.models import Q

def searchProjects(request):

    search_querys = ''
    if request.method=='POST' :
        search_querys = request.POST['search_query']

    tags = Tag.objects.filter(name__icontains=search_querys)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_querys) |
        Q(description__icontains=search_querys) |
        Q(owner__name__icontains=search_querys) |
        Q(tags__in=tags)
    )
    return projects, search_querys