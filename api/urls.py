from django.urls import path
from .views import CreatePoll

urlpatterns = [
    path('createPoll/', CreatePoll.as_view())
]