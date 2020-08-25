from django.urls import path

from . import views

urlpatterns = [
	path('update/(?P<update_id>[0-9]+)$', views.update, name='update'),
	path('delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    path('create/', views.create, name='create_contact'),
    path('', views.index, name='index'),
]
