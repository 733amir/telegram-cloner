from json import load as json_load
from os.path import expanduser

class ConfigParser:

    template = """{
    "app": {
        "session": "telegram-cloner"
    },
    "telegram": {
        "api_id": "012345",
        "api_hash": "01234567890123456789012345678901"
    }
}
    """

    def __init__(self, config_path):
        self._config_path = config_path
    
    def parse(self):
        with open(expanduser(self._config_path), 'r') as config_file:
            config = json_load(config_file)
            return config