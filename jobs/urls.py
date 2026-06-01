from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('jobs/', views.job_list, name='jobs'),
    path('joblist/', views.job_list, name='joblist'),
    path('job_list/', views.job_list, name='job_list_alias'),
    path('add/', views.add_job, name='add_job'),
    path('add_job/', views.add_job, name='add_job_alias'),
    path('add_jobs/', views.add_job, name='add_jobs_alias'),
    path('edit/<int:id>/', views.edit_job, name='edit_job'),
    path('delete/<int:id>/', views.delete_job, name='delete_job'),
]
