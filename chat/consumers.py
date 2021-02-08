from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import *
# from accounts.models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatRoomConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        messages = Message.last_10_messages()
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        author = data['username']
        author_profile = User.objects.filter(username=author)[0].profile  # ***********
        message = Message.objects.create(author=author_profile, content=data['message'])
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'author': message.author.fname,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        # self.room_name = 'basic_room'
        self.room_group_name = 'basic_group'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
