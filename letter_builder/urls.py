"""letter_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView, LetterView, CreateLetterView, UpdateLetterView, DeleteLetterView, \
UserProfileView, CreateUserProfileView, UpdateUserProfileView, DeleteUserProfileView, \
JobProfileView, CreateJobProfileView, UpdateJobProfileView, DeleteJobProfileView, \
LetterDetailView, IframeLetterView, EditLetterTemplateFileView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),

    path('letters/', LetterView.as_view(), name="letters"),
    path('letters/add/', CreateLetterView.as_view(), name="add-letter"),
    path('letters/edit/<int:pk>/', UpdateLetterView.as_view(), name="edit-letter"),
    path('letters/delete/<int:pk>/', DeleteLetterView.as_view(), name="delete-letter"),
    path('letters/view/<int:pk>/', LetterDetailView.as_view(), name="view-letter"),
    path('letters/iframe/<int:pk>/', IframeLetterView.as_view(), name='iframe-letter'),
    path('letters/template/edit/<int:pk>/', EditLetterTemplateFileView.as_view(), name='template-edit-letter'),

    path('user/profiles/', UserProfileView.as_view(), name="user-profiles"),
    path('user/profiles/add/', CreateUserProfileView.as_view(), name="add-user-profile"),
    path('user/profiles/edit/<int:pk>/', UpdateUserProfileView.as_view(), name="edit-user-profile"),
    path('user/profiles/delete/<int:pk>/', DeleteUserProfileView.as_view(), name="delete-user-profile"),

    path('job/profiles/', JobProfileView.as_view(), name="job-profiles"),
    path('job/profiles/add/', CreateJobProfileView.as_view(), name="add-job-profile"),
    path('job/profiles/edit/<int:pk>/', UpdateJobProfileView.as_view(), name="edit-job-profile"),
    path('job/profiles/delete/<int:pk>/', DeleteJobProfileView.as_view(), name="delete-job-profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
