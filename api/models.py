from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PollChoice(models.Model):
    name = models.CharField(max_length=50)
    vote_count = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

