from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def home(request):
    # return render(request,'trail.html')
    movies=Movie.objects.all()
    for movie in movies:
        print(movie.poster)
        print("**************")
        print(movie.name)
    return render(request,'home.html',{'movies':movies})

def movie(request):
    print("edoti edoti knaosdighakjngdcfghlasdfgjk;''asdfghjk;")
    nam=request.GET.get("mname")
    print(request.GET)
    print("djangodjangodjandodjangodjandogndjdnaog")
    return render(request,'index.html')
