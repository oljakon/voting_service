from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

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