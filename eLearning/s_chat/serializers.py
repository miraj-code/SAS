from s_chat.models import ChatGroup, ChatGroupMessage
from rest_framework import serializers

class ChatGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatGroup
        fields = '__all__'

        