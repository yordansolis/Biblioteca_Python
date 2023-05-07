from rest_framework import viewsets
from .serializer import TaskSeralizer
from .models import Task

# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSeralizer
    queryset = Task.objects.all()