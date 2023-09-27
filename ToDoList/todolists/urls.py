from django.urls import path

from . import views

app_name = "todolists"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.task_detail, name="detail"),
    path("<int:task_id>/update/", views.task_update, name="update"),
    path("<int:task_id>/delete/", views.task_delete, name="delete"),
]