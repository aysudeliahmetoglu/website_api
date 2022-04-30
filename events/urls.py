from django.urls import include, path
from . import views

urlpatterns = [
    
    path('deneme/', views.deneme.as_view()),
    path('create-event/', views.CreateEvent.as_view()),
    path('list-event/', views.ListEvents.as_view()),
    path('delete-event/<int:id>', views.DeleteEvents.as_view()),





    
]