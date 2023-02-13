from django import forms

from task_app.models import Task, Tag


class CreateTaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = ["title", "tags"]
