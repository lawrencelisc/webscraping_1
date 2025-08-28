import requests


class TGBot:
    def __init__(self, token: str, chat_id: str):
        """
        :param token: Telegram bot token from BotFather
        :param chat_id: ID of the target chat (can be a group, channel, or user)
        """
        self.base_url = 'https://api.telegram.org'
        self.token = token
        self.chat_id = chat_id

    def send_message(self, text: str, disable_notification=False, thread_id: int = None):
        """
        Send a message to a chat or a thread (topic) in a forum group.

        :param text: Message text
        :param disable_notification: If True, message will be sent silently
        :param thread_id: Optional. ID of the message thread (topic) in a forum group
        """
        params = {
            'chat_id': self.chat_id,
            'text': text,
            'disable_notification': disable_notification
        }

        if thread_id is not None:
            params['message_thread_id'] = thread_id

        response = requests.post(f"{self.base_url}/bot{self.token}/sendMessage", data=params)

        return response