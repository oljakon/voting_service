from django.urls import path
from .views import CreatePoll, VotePoll

urlpatterns = [
    path('createPoll/', CreatePoll.as_view()),
    path('poll/', VotePoll.as_view())
]