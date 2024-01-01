'''Module for Cinegy Air API wrapper'''

import requests


class CinegyAir:
    '''
    Class wrapper for Cinegy Air API.

    Attributes:
        host (str): The server name or IP address of the Cinegy Air Engine.
        port (str): Network port for Cinegy Air engine API access.
        device (str): The Cinegy Air engine device name.
    '''
    
    def __init__(self, host: str, port: str = '5521', device: str = 'video') -> None:
        '''
        Initialises an Cinegy Air API object.

        Parameters:
            host (str): The server name or IP address of the Cinegy Air engine.
            port (str): Network port for Cinegy Air engine API access. Port is 5521 plus the instance number.
            device (str): The Cinegy Air engine device name. Possible values are
                -video\n
                -titler_0\n
                -logo\n
                -cg_0 …​ cg_8\n
                -cg_logo\n
                -gfx_0 … gfx_8\n
                -gfx_logo\n
                -gfx_0 … gfx_8\n
                -gfx_logo\n
                -audio
        '''

        self.host = host
        self.port = port
        self.device = device
        self.base_url = f'http://{self.host}:{self.port}/{self.device}'

    def post_command(self, data: str) -> requests.Response:
        '''
        POST command to engine.

        Parameters:
            data(str): Request XML. Request Tags are:
                <Cue Id="{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}"/>\n
                <StartCued />\n
                <GPI Commercial="y" Preroll="10" />\n
                <GPI Commercial="n" Preroll="10" />\n
                <Event Device="" Cmd="" Op1="" Op2="" Op3=""\n
                        Name="" Description="" ThirdPartyId=""\n
                        Id="{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}">\n
                    <Op1></Op1>\n
                    <Op2></Op2>\n
                    <Op3></Op3>\n
                </Event>\n
                <SetOutput State="Normal|Black|Bypass|Clean"/>\n
                <ExitSceneLoop/>\n
                <SetVariables>\n
                    <Variable Name="Name1" Value="Val1"/>\n
                    <Variable Name="Name2" Value="Val2"/>\n
                    <!-- More like above -->\n
                </SetVariables>
        '''

        base_url = f'{self.base_url}/command'
        headers = {'Content-Type': 'text/xml'}

        response = requests.post(base_url, data=data, headers=headers)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def get_status(self, item: str | None = None) -> requests.Response:
        '''
        GET status of engine, active or cued item.

        Parameters:
            item (str): None, active or cued.
        '''

        if item is None:
            base_url = f'{self.base_url}/status'
        elif item == 'active':
            base_url = f'{self.base_url}/status/active'
        elif item == 'cued':
            base_url = f'{self.base_url}/status/cued'

        response = requests.get(base_url)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def get_list(self, id: str | None = None) -> requests.Response:
        '''
        GET list of scheduled playlist items or specified item.

        Parameters:
            id (str): ID of playlist item.
        '''

        if id is None:
            base_url = f'{self.base_url}/list'
        else:
            base_url = f'{self.base_url}/list/{id}'

        response = requests.get(base_url)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response
    
    def get_metrics(self) -> requests.Response:
        """
        GET Cinegy engine metrics
        """
        base_url = f'{self.base_url}/metrics'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response
    
    def get_metrics_srt(self) -> requests.Response:
        """
        GET Cinegy engine SRT metrics
        """
        base_url = f'{self.base_url}/metrics/srt'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response