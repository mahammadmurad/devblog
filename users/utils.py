from django.db.models import Q
from .models import Profile, Skill

def searchProfiles(request):
    search_querys = ''
    if request.method=='POST' :
        search_querys = request.POST['search_query']
    
    skills = Skill.objects.filter(name__contains=search_querys)
    profiles= Profile.objects.distinct().filter(Q(name__contains=search_querys)|
                                     Q(short_intro__contains=search_querys) | 
                                     Q(skill__in=skills))

    return profiles , search_querys