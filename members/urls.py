from django.urls import path
from . models import Individual, Member, EventInfo
from . import views  

urlpatterns = [
 path('individual' , views.Individual, name='bookings/individual'),

]