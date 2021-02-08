from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name="login"),
    path('activate/<uid>/<token>', views.verification, name='activate'),
    path('post2/', views.post2, name='post2'),
    path('info/', views.info, name='info'),
    path('home/', views.home, name="home"),
	path('profile/', views.profile, name="profile"),
]
