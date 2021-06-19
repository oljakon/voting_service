from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import F

from .models import PollChoice
from .serializers import PollSerializer, PollChoiceSerializer


class CreatePoll(APIView):
    def post(self, request):
        poll_data = request.data.get('Poll')
        serializer = PollSerializer(data=poll_data)
        if serializer.is_valid():
            serializer.save()
            for poll_choice in request.data.get('choices'):
                choice = PollChoiceSerializer(data={'name': poll_choice, 'poll': serializer['id'].value})
                if choice.is_valid():
                    choice.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VotePoll(APIView):
    def post(self, request):
        poll_id = request.data.get('poll_id')
        choice_id = request.data.get('choice_id')

        if poll_id and choice_id:
            poll_choice = PollChoice.objects.filter(id=choice_id, poll=poll_id)

            if poll_choice.exists():
                poll_choice.update(vote_count=F('vote_count') + 1)
                return Response(status.HTTP_200_OK)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)