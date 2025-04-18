from rest_framework import generics, permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Task
from .serializers import RegisterSerializer, TaskSerializer
from .permissions import IsOwner
from .tasks import notify_user_task_created

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        notify_user_task_created.delay(task.id)
