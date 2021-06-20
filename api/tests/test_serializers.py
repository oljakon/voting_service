from django.test import TestCase
from unittest.mock import MagicMock

from api.models import Poll, PollChoice
from api.serializers import PollSerializer, PollChoiceSerializer


class PollSerializerTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_poll = Poll.objects.create(name='test_poll')
        cls.test_poll_serializer = PollSerializer(cls.test_poll, context={'request': MagicMock()})

    def test_poll_included_fields(self):
        data = self.test_poll_serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name'})

    def test_poll_field_content(self):
        data = self.test_poll_serializer.data
        self.assertEqual(data['name'], 'test_poll')


class PollChoiceSerializerTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_poll = Poll.objects.create(name='test_poll')
        cls.test_poll_choice = PollChoice.objects.create(name='test_poll_choice', poll=cls.test_poll)
        cls.test_poll_choice_serializer = PollChoiceSerializer(cls.test_poll_choice, context={'request': MagicMock()})

    def test_poll_choice_included_fields(self):
        data = self.test_poll_choice_serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name', 'vote_count', 'poll'})

    def test_poll_choice_field_content(self):
        data = self.test_poll_choice_serializer.data
        self.assertEqual(data['name'], 'test_poll_choice')
        self.assertEqual(data['poll'], self.test_poll.id)