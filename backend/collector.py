import json
import os
from datetime import datetime
from pathlib import Path
from steam_client import SteamClient

class DataCollector:
    def __init__(self):
        self.steam_client = SteamClient()
        self.data_dir = Path("../data")
        self.data_dir.mkdir(exist_ok=True)

    def collect_user_data(self, steam_id: str):
        """Collect all data for a given Steam user."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Get owned games
        games = self.steam_client.get_owned_games(steam_id)
        
        # Collect achievements and stats for each game
        game_data = []
        for game in games:
            app_id = game['appid']
            try:
                achievements = self.steam_client.get_achievements(steam_id, app_id)
                stats = self.steam_client.get_game_stats(steam_id, app_id)
                
                game_data.append({
                    'app_id': app_id,
                    'name': game['name'],
                    'playtime_forever': game['playtime_forever'],
                    'achievements': achievements,
                    'stats': stats
                })
            except Exception as e:
                print(f"Error collecting data for game {game['name']}: {str(e)}")
                continue

        # Save data
        output_file = self.data_dir / f"steam_data_{steam_id}_{timestamp}.json"
        with open(output_file, 'w') as f:
            json.dump({
                'steam_id': steam_id,
                'timestamp': timestamp,
                'games': game_data
            }, f, indent=2)
        
        print(f"Data collected and saved to {output_file}")

def main():
    steam_id = os.getenv('STEAM_ID')
    if not steam_id:
        raise ValueError("STEAM_ID environment variable is not set")
    
    collector = DataCollector()
    collector.collect_user_data(steam_id)

if __name__ == "__main__":
    main() 