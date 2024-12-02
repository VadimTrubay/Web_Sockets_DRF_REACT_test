import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from dialogs.models import Dialog
from dialogs.serializers import DialogListSerializer


class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "chat_room"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        await self.send_dialogs_list()

    @database_sync_to_async
    def get_dialogs_from_db(self):
        return DialogListSerializer(Dialog.objects.all()).data

    async def send_dialogs_list(self):
        await self.send(text_data=json.dumps({
            "action": "list_dialogs",
            "dialogs": await self.get_dialogs_from_db(),
        }))

    async def receive(self, text_data=None, bytes_data=None):
        if text_data is not None:
            data = json.loads(text_data)
            await self.create_message(data)
            await self.channel_layer.group_send(
                self.room_name,
                {
                    "type": "broadcast_dialogs"
                }
            )

    async def create_message(self, text):
        user = self.scope["user"]

        if user.is_authenticated:
            await database_sync_to_async(Dialog.objects.create)(
                user=user,
                text=text,
            )

    async def broadcast_dialogs(self, event):
        await self.send_dialogs_list()
