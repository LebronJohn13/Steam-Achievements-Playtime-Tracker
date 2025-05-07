from flask import Flask, jsonify
from flask_cors import CORS
import json
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_DIR = Path("../data")

def get_latest_data(steam_id: str):
    """Get the most recent data file for a given Steam ID."""
    files = list(DATA_DIR.glob(f"steam_data_{steam_id}_*.json"))
    if not files:
        return None
    
    latest_file = max(files, key=lambda x: x.stat().st_mtime)
    with open(latest_file, 'r') as f:
        return json.load(f)

@app.route('/api/games/<steam_id>')
def get_games(steam_id):
    """Get list of games with basic info."""
    data = get_latest_data(steam_id)
    if not data:
        return jsonify({'error': 'No data found'}), 404
    
    games = [{
        'app_id': game['app_id'],
        'name': game['name'],
        'playtime_forever': game['playtime_forever']
    } for game in data['games']]
    
    return jsonify(games)

@app.route('/api/achievements/<steam_id>/<int:app_id>')
def get_achievements(steam_id, app_id):
    """Get achievements for a specific game."""
    data = get_latest_data(steam_id)
    if not data:
        return jsonify({'error': 'No data found'}), 404
    
    game = next((g for g in data['games'] if g['app_id'] == app_id), None)
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    
    return jsonify(game['achievements'])

@app.route('/api/stats/<steam_id>/<int:app_id>')
def get_stats(steam_id, app_id):
    """Get detailed stats for a specific game."""
    data = get_latest_data(steam_id)
    if not data:
        return jsonify({'error': 'No data found'}), 404
    
    game = next((g for g in data['games'] if g['app_id'] == app_id), None)
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    
    return jsonify(game['stats'])

if __name__ == '__main__':
    app.run(debug=True, port=5000) 