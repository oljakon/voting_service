from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import F

from .models import PollChoice
from .serializers import PollSerializer, PollChoiceSerializer


class CreatePoll(APIView):
    def post(self, request):
        poll_data = request.data.get('poll')
        poll_choices = request.data.get('choices')

        if not poll_choices:
            return Response(data='Bad request: no poll choices provided', status=status.HTTP_400_BAD_REQUEST)

        poll_serializer = PollSerializer(data=poll_data)

        if poll_serializer.is_valid():
            poll_serializer.save()

            for poll_choice in poll_choices:
                choice_serializer = PollChoiceSerializer(
                    data={'name': poll_choice, 'poll': poll_serializer['id'].value}
                )

                if choice_serializer.is_valid():
                    choice_serializer.save()

            return Response(data=poll_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=poll_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VotePoll(APIView):
    def post(self, request):
        poll_id = request.data.get('poll_id')
        choice_id = request.data.get('choice_id')

        if poll_id and choice_id:
            poll_choice = PollChoice.objects.filter(id=choice_id, poll=poll_id)

            if poll_choice.exists():
                poll_choice.update(vote_count=F('vote_count') + 1)
                return Response(data='Vote taken', status=status.HTTP_200_OK)

            return Response(data='Poll with given choice not found', status=status.HTTP_404_NOT_FOUND)

        return Response(
            data='Bad request: poll_id and choice_id should be provided',
            status=status.HTTP_400_BAD_REQUEST
        )


class GetResult(APIView):
    def post(self, request):
        poll_id = request.data.get('poll_id')

        if poll_id:
            poll_choices = PollChoice.objects.filter(poll=poll_id)

            if poll_choices:
                poll_result = {choice.name: choice.vote_count for choice in poll_choices}
                return Response(data=poll_result, status=status.HTTP_200_OK)

            return Response(data='Poll not found', status=status.HTTP_404_NOT_FOUND)

        return Response(data='Bad request: poll_id should be provided', status=status.HTTP_400_BAD_REQUEST)
