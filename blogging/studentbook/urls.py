from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('register_user/',views.register_user,name='register_user'),
    path('logout/',views.logout,name='logout'),
    path('create_post/',views.create_post,name='create_post'),
    path('readmore/<int:id>',views.readmore,name='readmore'),
    path('developer/',views.developer,name='developer'),
]