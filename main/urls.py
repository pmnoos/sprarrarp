from django.urls import path
from . import views
    
  
   
urlpatterns = [
    path('home1', views.home1, name='home1'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update', views.post_update, name='post_update'),
    path('about', views.about, name='about'),
    path('contact' , views.contact, name='contact'),
    path('booking' , views.booking, name='booking'),
    path('group' , views.group, name='group'),
    path('turriding' , views.turriding, name='turriding'),
    path('riders' , views.member, name='booking/riders'),
    path('individual' , views.Individual, name='bookings/individual'),
    path('member' , views.member, name='member'),
    path('horses' , views.horses, name='horses'),
    path('about' , views.about, name='about'),
    path('gallery' , views.gallery, name='gallery'),
    path('ridschool' , views.ridschool, name='ridschool'),
    path('calendar' , views.calendar, name='calendar'),
    path('register_user' , views.sign_up, name='sign_up'),
    path('login', views.login_user , name = 'registration/login'), 
    path('logout',views.logout_user , name = 'registration/logout'), 
    path('footer', views.footer, name='footer'),
    path('nav', views.nav, name='nav'),
]
