from django.shortcuts import render
import requests
from django.http import  HttpResponse,JsonResponse

TMDB = "6b4b5e818acacabce4da0b82b84fad38"


def search(request):
    query = request.GET.get('q')

    result = []
    if query:
        data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={TMDB}&language=en-US&page=1&include_adult=false&query={query}")
        # temp = []
        # for a in data.json()["results"]:
        #     if len(temp)<3:
        #         temp.append({"name":a["name"],"poster": a["poster_path"],"overview": a["overview"]})
        #     else:
        #         result.append(temp)
        # result.append(temp) if len(temp)>0 else None

    else:
        return HttpResponse("please enter a search query")
    return render(request,'home/results.html',{
        'data':data.json(),
        'type':request.GET.get('type')
    })


def index(request):
    data = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB}&language=en-US")
    data1 = requests.get(f"https://api.themoviedb.org/3/trending/tv/day?api_key={TMDB}&language=en-US")

    
    return render(request, 'home/index.html',{
        'data':data.json(),
        'data1':data1.json(),
    })


def tv_detail(request,id):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{id}?api_key={TMDB}&language=en-US&page=1&include_adult=false")
    recommendations = requests.get(f"https://api.themoviedb.org/3/tv/{id}/recommendations?api_key={TMDB}&language=en-US")

    return render(request,'home/tv_detail.html',{
        'data':data.json(),
        'recommendations':recommendations.json(),
        'type':"tv"
        
    })

def movie_detail(request,id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key={TMDB}&language=en-US&page=1&include_adult=false")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{id}/recommendations?api_key={TMDB}&language=en-US")

    return render(request,'home/movie_details.html',{
        'data':data.json(),
        'recommendations':recommendations.json(),
        'type':"movie"
        
    })