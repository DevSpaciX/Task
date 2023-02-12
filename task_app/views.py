from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from task_app.forms import CreateTaskForm
from task_app.models import Task, Tag


def home(request):
    return render(request,"home.html")

class TaskPage(generic.ListView):
    template_name = "home.html"
    queryset = Task.objects.order_by("is_done","created_at")
    context_object_name = "tasks"

class CreateTaskView(generic.CreateView):
    form_class = CreateTaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task:home-page")

def status(request,task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == "POST" and task.is_done is True:
        task.is_done = False
        task.save()
    else:
        task.is_done = True
        task.save()

    return HttpResponseRedirect(reverse("task:home-page"))

class TagsPage(generic.ListView):
    template_name = "tags.html"
    model = Tag
    context_object_name = "tags"


class UpdateTags(generic.UpdateView):
    fields = "__all__"
    template_name = "update_tags.html"
    model = Tag
    success_url = reverse_lazy("task:tags")

class DeleteTags(generic.DeleteView):
    template_name = "delete_tags.html"
    model = Tag
    success_url = reverse_lazy("task:tags")

class CreateTag(generic.CreateView):
    fields = "__all__"
    model = Tag
    template_name = "task_form.html"
    success_url = reverse_lazy("task:tags")

class UpdateTask(generic.UpdateView):
    form_class = CreateTaskForm
    template_name = "update_tags.html"
    model = Task
    success_url = reverse_lazy("task:home-page")

class DeleteTask(generic.DeleteView):
    fields = "__all__"
    template_name = "delete_task.html"
    model = Task
    success_url = reverse_lazy("task:tags")