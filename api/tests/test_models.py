from django.test import TestCase

from api.models import Poll, PollChoice


class PollTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_poll_01 = Poll.objects.create(name='test_poll01')
        cls.test_poll_02 = Poll.objects.create(name='test_poll02')

    def test_get_poll_by_name(self):
        test_poll_01 = Poll.objects.get(name='test_poll01')
        self.assertEqual(test_poll_01.name, 'test_poll01')

    def test_get_not_existing_poll(self):
        throw_exception = False

        try:
            Poll.objects.get(name='test_poll03')
        except Poll.DoesNotExist:
            throw_exception = True

        self.assertTrue(throw_exception)


class PollChoiceTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_poll_01 = Poll.objects.create(name='test_poll01')
        cls.test_poll_choice_01 = PollChoice.objects.create(name='test_poll_choice01', poll=cls.test_poll_01)
        cls.test_poll_choice_02 = PollChoice.objects.create(name='test_poll_choice02', poll=cls.test_poll_01)

    def test_get_poll_by_name(self):
        test_poll_choice_01 = PollChoice.objects.get(name='test_poll_choice01')
        self.assertEqual(test_poll_choice_01.name, 'test_poll_choice01')

    def test_get_not_existing_poll(self):
        throw_exception = False

        try:
            PollChoice.objects.get(name='test_poll_choice03')
        except PollChoice.DoesNotExist:
            throw_exception = True

        self.assertTrue(throw_exception)
