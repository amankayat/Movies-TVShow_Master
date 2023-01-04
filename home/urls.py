from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name  = 'index'),
    path('search/',views.search,name = 'search'),
    path('tv/<int:id>/',views.tv_detail,name = 'tvdetail'),
    path('movie/<int:id>/',views.movie_detail,name = 'moviedetail')
]
