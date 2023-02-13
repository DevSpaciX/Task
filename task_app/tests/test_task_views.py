from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_app.models import Task, Tag

TASK_URL = reverse("task:home-page")



class DataFromFixtureListTests(TestCase):
    def test_get_fixture_data(self):
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(
            list(response.context["tasks"]), [])
        self.assertNotEqual(
            len(list(response.context["tasks"])), 3)


class OwnTaskData(TestCase):
    def test_get_own_data(self):
        self.task = Task.objects.create(title="test", is_done=False,created_at=datetime.now())
        all_tasks = Task.objects.all()
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            (list(all_tasks)) , list(all_tasks))

class TaskTagsCheck(TestCase):
    def setUp(self) -> None:
        self.task_tag_1 = Tag.objects.create(title='test tag 1')
        self.task_tag_2 = Tag.objects.create(title='test tag 2')

    def test_get_tags(self):
        self.task = Task.objects.create(title="test", is_done=False,created_at=datetime.now())
        self.task.tags.add(self.task_tag_1,self.task_tag_2)
        response = self.client.get(TASK_URL)
        self.assertEqual(
            list(response.context["tasks"].filter(title="test").first().tags.all()), list(self.task.tags.all()))
