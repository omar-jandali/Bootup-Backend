from rest_framework.generics import ListAPIView, RetrieveAPIView

from chat.models import Chat
from .serializers import ChatSerializer

class ChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetailsView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
