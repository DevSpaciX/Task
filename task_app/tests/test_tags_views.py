from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_app.models import Task, Tag

TASK_URL = reverse("task:tags")



class DataFromFixtureListTests(TestCase):
    def test_get_fixture_data(self):
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(
            list(response.context["tags"]), [])
        self.assertEqual(
            len(list(response.context["tags"])), 3)

class OwnTagsData(TestCase):
    def test_get_fixture_data(self):
        Tag.objects.create(title="test")
        all_tags = Tag.objects.all()
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            (list(response.context["tags"])), list(all_tags))