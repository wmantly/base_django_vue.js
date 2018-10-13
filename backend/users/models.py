from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Team(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()
	# created_by = models.ForeignKey(User, related_name="+", on_delete=models.DO_NOTHING)
	created_at = models.DateTimeField(default=timezone.now, editable=False)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zip = models.IntegerField()
	street_name = models.CharField(max_length=20)
	email_confirm = models.BooleanField(default='False')
	teams = models.ManyToManyField(Team)
	bio = models.TextField()
