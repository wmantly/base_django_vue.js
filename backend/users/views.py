from .models import Team
from rest_framework import viewsets
from .serializers import TeamSerializer


class TeamSet(viewsets.ModelViewSet):
	# def perform_create(self, serializer):
	# 	serializer.save(created_by=self.request.user)
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
