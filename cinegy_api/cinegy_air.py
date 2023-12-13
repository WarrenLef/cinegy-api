import requests


class CinegyAir:
    
    def __init__(self, host, port=None, device=None):
        
        self.host = host

        if port is None:
            self.port = '5521'
        else:
            self.port = port

        if device is None:
            self.device = 'video'
        else:
            self.device = device

        self.base_url = f'http://{self.host}:{self.port}/{self.device}'

    def command(self, data):
        base_url_command = f'{self.base_url}/command'
        headers = {'Content-Type': 'text/xml'}

        command_response = requests.post(base_url_command, data=data, headers=headers)
        if command_response.status_code != requests.codes.ok:
            command_response.raise_for_status()


    def status(self, item=None):
        if item is None:
            base_url_status = f'{self.base_url}/status'
        elif item == 'active':
            base_url_status = f'{self.base_url}/status/active'
        elif item == 'cued':
            base_url_status = f'{self.base_url}/status/cued'

        status_response = requests.get(base_url_status)
        if status_response.status_code != requests.codes.ok:
            status_response.raise_for_status()
        return status_response.text


    def list(self, id=None):
        if id is None:
            base_url_list = f'{self.base_url}/list'
        else:
            base_url_list = f'{self.base_url}/list/{id}'

        list_response = requests.get(base_url_list)
        if list_response.status_code != requests.codes.ok:
            list_response.raise_for_status()
        return list_response.text