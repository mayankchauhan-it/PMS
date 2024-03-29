from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    # People URL
    path('add_people', views.add_people, name='add_people'), 
    path('list_people', views.people_list, name='people_list'), 
    # Building URL
    path('add_building', views.add_building, name='add_building'), 
    path('building_list', views.building_list, name='building_list'), 

    # Customer URL
    path('add_customer', views.add_customer, name='add_customer'),  
    path('customer_list', views.customer_list, name='customer_list'), 
    
    
    
    
    # Udita's Development
    
    path('udita_customer_list', views.udita_customer_list, name='udita_customer_list'), 
    path('udita_building_list', views.udita_building_list, name='udita_building_list'), 
    path('udita_people_list', views.udita_people_list, name='udita_people_list'), 
     
]
