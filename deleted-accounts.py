from telethon.sync import TelegramClient
from telethon.tl.types import UserStatusRecently

# Your credentials
api_id = ''
api_hash = ''

# Create a client session
with TelegramClient('session_name', api_id, api_hash) as client:
    # Get all dialogs (conversations)
    dialogs = client.get_dialogs()

    # Loop through each dialog and check if the user is a Deleted Account
    for dialog in dialogs:
        if dialog.is_user and dialog.entity.deleted:
            print(f'Deleting chat with Deleted Account: {dialog.entity.id}')
            client.delete_dialog(dialog.id)

