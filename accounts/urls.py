from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name="login"),
    path('post/', views.post, name='post'),
    path('activate/<uid>/<token>', views.verification, name='activate'),
    path('post2/', views.post2, name='post2'),
    path('form/', views.form, name='form'),
    path('info/', views.info, name='info'),
]
