from rest_framework import serializers

from .models import Poll, PollChoice


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class PollChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollChoice
        fields = '__all__'
