from telethon import TelegramClient
from config_parser import ConfigParser


class CommandlineInterface:
    def __init__(self, config='~/.telegram-cloner.json'):
        self._config = ConfigParser(config).parse()

        self._tg_client = TelegramClient(
            self._config['app']['session'],
            self._config['telegram']['api_id'],
            self._config['telegram']['api_hash']
        )
        self._tg_client.start()
    
    def recent_media(self, username, limit=10):
        for m in self._tg_client.iter_messages(username, limit):
            filename = self._tg_client.download_media(m)
            if filename:
                print('Filename:', filename)