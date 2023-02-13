from django.contrib import admin
from django.urls import path, include
from task_app.views import *

urlpatterns = [
    path("", TaskPage.as_view(), name="home-page"),
    path("crate_task", CreateTaskView.as_view(), name="create-task"),
    path("update_task/<int:pk>/", UpdateTask.as_view(), name="update-task"),
    path("delete_task/<int:pk>/", DeleteTask.as_view(), name="delete-task"),
    path("update_status/<int:task_id>/", status, name="update-status"),
    path("tags", TagsPage.as_view(), name="tags"),
    path("tags_update/<int:pk>/", UpdateTags.as_view(), name="tags-update"),
    path("tags_delete/<int:pk>/", DeleteTags.as_view(), name="tags-delete"),
    path("tags_create/", CreateTag.as_view(), name="tags-create"),
]

app_name = "task_app"
