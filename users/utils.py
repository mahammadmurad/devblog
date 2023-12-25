from django.db.models import Q
from .models import Profile, Skill

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page=1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
    
    leftIndex = (int(page)-4)
    if leftIndex<1:
        leftIndex =1

    rightIndex = (int(page)+5)
    if rightIndex> paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, profiles


def searchProfiles(request):
    search_querys = ''
    if request.method=='POST' :
        search_querys = request.POST['search_query']
    
    skills = Skill.objects.filter(name__contains=search_querys)
    profiles= Profile.objects.distinct().filter(Q(name__contains=search_querys)|
                                     Q(short_intro__contains=search_querys) | 
                                     Q(skill__in=skills))

    return profiles , search_querys 