from django.urls import path
from .views import CreatePoll, VotePoll, GetResult

urlpatterns = [
    path('createPoll/', CreatePoll.as_view()),
    path('poll/', VotePoll.as_view()),
    path('getResult/', GetResult.as_view()),
]