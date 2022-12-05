import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from a_user.models import Student
from django.shortcuts import get_object_or_404

from s_chat.models import ChatGroup, ChatGroupMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['roomName']
        self.room_group_name = 'chat_%s' % self.room_name
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message, 
                'sender': self.scope["user"].username
            }
        )

        room = await database_sync_to_async(ChatGroup.objects.get)(name=self.room_name)
        new_msg = await self.save_message(self.scope["user"].username, message, self.room_name)

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        # Send message to WebSocket
        
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))

    #Save chat messages to the database
    @database_sync_to_async
    def save_message(self, sender, message, room): 
        msender = get_object_or_404(Student, username=sender)
        group = get_object_or_404(ChatGroup, name=self.room_name)

        new_msg = ChatGroupMessage.objects.create(sender=msender, message=message, group=group)
        
        return new_msg

    