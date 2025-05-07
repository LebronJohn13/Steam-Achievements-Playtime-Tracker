import os
import requests
from typing import Dict, List, Optional
from dotenv import load_dotenv

load_dotenv()

class SteamClient:
    def __init__(self):
        self.api_key = os.getenv('STEAM_API_KEY')
        if not self.api_key:
            raise ValueError("STEAM_API_KEY environment variable is not set")
        self.base_url = "https://api.steampowered.com"

    def get_owned_games(self, steam_id: str) -> List[Dict]:
        """Get list of games owned by the user."""
        url = f"{self.base_url}/IPlayerService/GetOwnedGames/v1/"
        params = {
            'key': self.api_key,
            'steamid': steam_id,
            'include_appinfo': True,
            'include_played_free_games': True
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()['response']['games']

    def get_achievements(self, steam_id: str, app_id: int) -> List[Dict]:
        """Get achievements for a specific game."""
        url = f"{self.base_url}/ISteamUserStats/GetPlayerAchievements/v1/"
        params = {
            'key': self.api_key,
            'steamid': steam_id,
            'appid': app_id
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()['playerstats']['achievements']

    def get_game_stats(self, steam_id: str, app_id: int) -> Dict:
        """Get detailed stats for a specific game."""
        url = f"{self.base_url}/ISteamUserStats/GetUserStatsForGame/v2/"
        params = {
            'key': self.api_key,
            'steamid': steam_id,
            'appid': app_id
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()['playerstats'] 