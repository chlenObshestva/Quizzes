from rest_framework import mixins, viewsets

from .serializers import *
from .models import *


class QuizViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()