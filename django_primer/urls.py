"""django_primer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('student/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('subject/create/', views.SubjectCreateView.as_view(), name='subject_create'),
    path('subject/<int:pk>/update/', views.SubjectUpdateView.as_view(), name='subject_update'),
    path('subject/<int:pk>/delete/', views.SubjectDeleteView.as_view(), name='subject_delete'),
    path('score/create/', views.ScoreCreateView.as_view(), name='score_create'),
    path('score/<int:pk>/update/', views.ScoreUpdateView.as_view(), name='score_update'),
    path('score/<int:pk>/delete/', views.ScoreDeleteView.as_view(), name='score_delete'),
]
