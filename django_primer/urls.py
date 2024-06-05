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

from .views import ReportView, ScoreListView, SubjectListView, \
StudentListView, IndexView, ScoreCreateView, SubjectCreateView, StudentCreateView, \
StudentUpdateView, StudentDeleteView, SubjectDeleteView, SubjectUpdateView, ScoreDeleteView, \
ScoreUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('score/list/', ScoreListView.  as_view(), name='score_list'),
    path('score/form/', ScoreCreateView.as_view(), name='score_create'),
    path('score/<int:pk>/update/', ScoreUpdateView.as_view(), name='score_update'),
    path('score/<int:pk>/delete/', ScoreDeleteView.as_view(), name='score_delete'),

    path('student/list/', StudentListView.as_view(), name='student_list'),
    path('student/form/', StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    path('subject/list/', SubjectListView.as_view(), name='subject_list'),
    path('subject/form/', SubjectCreateView.as_view(), name='subject_create'),
    path('subject/<int:pk>/update/', SubjectUpdateView.as_view(), name='subject_update'),
    path('subject/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),

    path('report/', ReportView.as_view(), name='report')
]
