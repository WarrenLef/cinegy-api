'''Module for Cinegy Multiviewer API wrapper'''

import requests


class CinegyMultiviewer:
    '''
    Class wrapper for Cinegy Multiviewer API.

    Attributes:
        host (str): The server name or IP address of the Cinegy Multiviewer.
        port (str): Network port for Cinegy Multiviewer API access.
    '''
    
    def __init__(self, host: str, port: str = '8090') -> None:
        '''
        Initialises an Cinegy Multiviewer API object.

        Parameters:
            host (str): The server name or IP address of the Cinegy Multiviewer.
            port (str): Network port for Cinegy Multiviewer API access. Default port is 8090.
            '''
        self.host = host
        self.port = port
        self.base_url = f'http://{self.host}:{self.port}/Multiviewer/Rest'

    def get_status(self) -> requests.Response:
        '''Returns status of Cinegy Multiviewer'''
        base_url = f'{self.base_url}/GetStatus'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response
    
    def get_srt_stats(self) -> requests.Response:
        '''Returns SRT connection statistics'''
        base_url = f'{self.base_url}/GetSRTStats'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def get_players_number(self) -> requests.Response:
        '''Returns the number of players loaded into the current layout'''
        base_url = f'{self.base_url}/GetPlayersNumber'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def get_active_player(self) -> requests.Response:
        '''Returns the zero-based index of the active / selected player'''
        base_url = f'{self.base_url}/GetActivePlayer'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response
    
    def set_active_player(self, id: str) -> requests.Response:
        '''Changes the currently active / selected player
        
        Parameters:
            id (str): The Index of the player to activate. Index range is 0 to "count-1" of players.
        '''
        base_url = f'{self.base_url}/SetActivePlayer?ID={id}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response
    
    def get_layouts_number(self) -> requests.Response:
        '''Returns the number of layouts loaded into Cinegy Multiviewer'''
        base_url = f'{self.base_url}/GetLayoutsNumber'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def get_layout_title(self, id: str) -> requests.Response:
        '''Returns the current title of the specified layout
        
        Parameters:
            id (str): The ID of the target Cinegy Multiviewer layout.
        '''
        base_url = f'{self.base_url}/GetLayoutTitle?ID={id}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def set_layout_title(self, id: str, title: str) -> requests.Response:
        '''Changes the title of the specified layout
        
        Parameters:
            id (str): The ID of the target Cinegy Multiviewer layout.
            title (str): The new layout name.
        '''
        base_url = f'{self.base_url}/SetLayoutTitle?ID={id}&Title={title}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response
    
    def set_player_title(self, player_id: str, title: str) -> requests.Response:
        '''Changes the title of the specified player
        
        Parameters:
            player_id (str): The ID of the Cinegy Multiviewer player.
            title (str): The new player title.
        '''
        base_url = f'{self.base_url}/SetPlayerTitle?PlayerID={player_id}&Title={title}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def get_active_layout(self) -> requests.Response:
        '''Returns the zero-based index of the active layout'''
        base_url = f'{self.base_url}/GetActiveLayout'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def set_active_layout(self, id: str) -> requests.Response:
        '''Changes the currently active layout
        
        Parameters:
            id (str): The Index of the layout to activate. Index range is 0 to "count-1" of layouts.
        '''
        base_url = f'{self.base_url}/SetActiveLayout?ID={id}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response
    
    def get_audio_channels_number(self, player_id: str) -> requests.Response:
        '''Returns the number of audio channels for the specified player
        
        Parameters:
            player_id (str): The Index of the player to query. Index range is 0 to "count-1" of players.
        '''
        base_url = f'{self.base_url}/GetAudioChannelsNumber?PlayerID={player_id}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def set_active_audio_channel(self, player_id: str, id: str) -> requests.Response:
        '''Sets the selected / active audio channel in the specified player
        
        Parameters:
            player_id (str): The Index of the player to set. Index range is 0 to "count-1" of players.
            id (str): The index of the audio channel.
        '''
        base_url = f'{self.base_url}/SetActiveAudioChannel?PlayerID={player_id}&ID={id}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response
    
    def get_active_audio_channel(self, player_id: str) -> requests.Response:
        '''Returns the selected / active audio channel in the specified player
        
        Parameters:
            player_id (str): The Index of the player to query. Index range is 0 to "count-1" of players.
        '''
        base_url = f'{self.base_url}/GetActiveAudioChannel?PlayerID={player_id}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def restart(self) -> requests.Response:
        '''Causes a soft-restart of Cinegy Multiviewer, reloading settings and layouts'''
        base_url = f'{self.base_url}/Restart'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def play_alert(self, file: str) -> requests.Response:
        '''Allows a user-specified WAV file to be played via the alarm audio channel
        
        Parameters:
            file (str): Path to an accessible WAV file.
        '''
        base_url = f'{self.base_url}/PlayAlarm?FileName={file}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def set_player_border_color(self, player_id: str, color: str) -> requests.Response:
        '''Specifies a colored border to be rendered around the specified player
        
        Parameters:
            player_id (str): The Index of the player to query. Index range is 0 to "count-1" of players.
            color (str): Specify color to set players border. ARGB hex format.
        '''
        base_url = f'{self.base_url}/SetPlayerBorderColor?PlayerID={player_id}&Color={color}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def get_player_border_color(self, player_id: str) -> requests.Response:
        '''Returns the current border color for the specified player

        Parameters:
            player_id (str): The Index of the player to query. Index range is 0 to "count-1" of players.
        '''
        base_url = f'{self.base_url}/GetPlayerBorderColor?PlayerID={player_id}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response

    def get_player_title(self, player_id: str) -> requests.Response:
        '''Returns the current title of the specified player
        
        Parameters:
            player_id (str): The Index of the player to query. Index range is 0 to "count-1" of players.
        '''
        base_url = f'{self.base_url}/GetPlayerTitle?PlayerID={player_id}'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response
    
    def get_web_socket_preview_info(self) -> requests.Response:
        '''Returns the parameters of WEB stream for the corresponding WEB socket.'''

        base_url = f'{self.base_url}/GetWebSocketPreviewInfo'
        response = requests.get(base_url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        return response