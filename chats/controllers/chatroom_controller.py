from rest_framework import viewsets
from chats.models import Chatroom
from chats.serializers import ChatroomSerializer

class ChatroomViewSet(viewsets.ModelViewSet):
    queryset = Chatroom.objects.all()
    serializer_class = ChatroomSerializer
