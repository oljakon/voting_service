from rest_framework.test import APITestCase
from rest_framework.utils import json
from rest_framework import status

from api.models import Poll, PollChoice


class CreatePollTest(APITestCase):
    def test_create_poll_successfully(self):
        data = {
            'poll': {'name': 'Test poll'},
            'choices': ['Test choice 1', 'Test choice 2']
        }
        response = self.client.post('/api/createPoll/',  json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Poll.objects.count(), 1)
        self.assertEqual(Poll.objects.get().name, 'Test poll')
        self.assertEqual(PollChoice.objects.count(), 2)
        self.assertTrue(PollChoice.objects.filter(name='Test choice 1').exists())
        self.assertTrue(PollChoice.objects.filter(name='Test choice 2').exists())

    def test_no_choices_provided(self):
        data = {
            'poll': {'name': 'Test poll'},
            'choices': []
        }
        response = self.client.post('/api/createPoll/',  json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_poll_without_poll_data(self):
        data = {
            'choices': ['Test choice 1', 'Test choice 2']
        }
        response = self.client.post('/api/createPoll/',  json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_poll_with_incorrect_poll_data(self):
        data = {
            'poll': {'not_name': 'Test poll'},
            'choices': ['Test choice 1', 'Test choice 2']
        }
        response = self.client.post('/api/createPoll/',  json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_poll_without_choices(self):
        data = {
            'poll': {'name': 'Test poll'}
        }
        response = self.client.post('/api/createPoll/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_poll_empty_request_data(self):
        data = {}
        response = self.client.post('/api/createPoll/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class VotePollTest(APITestCase):
    def setUp(cls):
        cls.test_poll = Poll.objects.create(id=1, name='test_poll')
        cls.test_poll_choice_01 = PollChoice.objects.create(id=1, name='test_poll_choice01', poll=cls.test_poll)
        cls.test_poll_choice_02 = PollChoice.objects.create(id=2, name='test_poll_choice02', poll=cls.test_poll)

    def test_vote_poll_successfully(self):
        self.assertEqual(PollChoice.objects.get(id=1).vote_count, 0)
        self.assertEqual(PollChoice.objects.get(id=2).vote_count, 0)

        data = {
            'poll_id': 1,
            'choice_id': 1
        }
        response = self.client.post('/api/poll/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PollChoice.objects.get(id=1).vote_count, 1)
        self.assertEqual(PollChoice.objects.get(id=2).vote_count, 0)

    def test_vote_in_non_existent_poll(self):
        data = {
            'poll_id': 100,
            'choice_id': 1
        }
        response = self.client.post('/api/poll/',  json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_vote_for_non_existent_choice(self):
        data = {
            'poll_id': 1,
            'choice_id': 100
        }
        response = self.client.post('/api/poll/',  json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_vote_without_poll_id(self):
        data = {
            'choice_id': 1
        }
        response = self.client.post('/api/poll/',  json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vote_without_choice_id(self):
        data = {
            'poll_id': 1
        }
        response = self.client.post('/api/poll/',  json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vote_empty_request_data(self):
        data = {}
        response = self.client.post('/api/poll/',  json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetResultTest(APITestCase):
    def setUp(cls):
        cls.test_poll = Poll.objects.create(id=1, name='test_poll')
        cls.test_poll_choice_01 = PollChoice.objects.create(
            id=1,
            name='test_poll_choice01',
            vote_count=5,
            poll=cls.test_poll
        )
        cls.test_poll_choice_02 = PollChoice.objects.create(
            id=2,
            name='test_poll_choice02',
            vote_count=10,
            poll=cls.test_poll
        )

    def test_get_poll_result_successfully(self):
        data = {
            'poll_id': 1,
        }
        expected_response = b'{"test_poll_choice01":5,"test_poll_choice02":10}'
        response = self.client.post('/api/getResult/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, expected_response)

    def test_get_result_of_non_existent_poll(self):
        data = {
            'poll_id': 100,
        }
        response = self.client.post('/api/getResult/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_empty_request_data(self):
        data = {}
        response = self.client.post('/api/getResult/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
