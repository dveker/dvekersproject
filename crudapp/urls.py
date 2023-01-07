from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('crudapps/', views.crudapps, name='crudapps'),
    path('ids/<int:id>', views.ids, name='ids'),
]