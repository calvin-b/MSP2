from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:sinput>/', views.detailPost, name='detail'),
    path('category/<slug:cinput>/', views.categoryPost, name='category'),
]
