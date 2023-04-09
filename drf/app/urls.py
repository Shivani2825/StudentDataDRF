
from django.urls import path  
from .views import StudentView  

urlpatterns = [  
    path('app',StudentView.as_view()),
    path('app/<int:id>/', StudentView.as_view()) ,  
    path('app/<int:id>/update/', StudentView.as_view())    
]  
