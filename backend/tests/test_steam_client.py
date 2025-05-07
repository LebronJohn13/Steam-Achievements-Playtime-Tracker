import pytest
from unittest.mock import patch, MagicMock
from steam_client import SteamClient

@pytest.fixture
def steam_client():
    with patch.dict('os.environ', {'STEAM_API_KEY': 'test_key'}):
        return SteamClient()

def test_init_without_api_key():
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(ValueError, match="STEAM_API_KEY environment variable is not set"):
            SteamClient()

def test_get_owned_games(steam_client):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'response': {
            'games': [
                {'appid': 1, 'name': 'Test Game', 'playtime_forever': 100}
            ]
        }
    }
    mock_response.raise_for_status = MagicMock()

    with patch('requests.get', return_value=mock_response) as mock_get:
        games = steam_client.get_owned_games('12345')
        
        mock_get.assert_called_once()
        assert len(games) == 1
        assert games[0]['appid'] == 1
        assert games[0]['name'] == 'Test Game'

def test_get_achievements(steam_client):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'playerstats': {
            'achievements': [
                {'name': 'Test Achievement', 'achieved': 1}
            ]
        }
    }
    mock_response.raise_for_status = MagicMock()

    with patch('requests.get', return_value=mock_response) as mock_get:
        achievements = steam_client.get_achievements('12345', 1)
        
        mock_get.assert_called_once()
        assert len(achievements) == 1
        assert achievements[0]['name'] == 'Test Achievement'
        assert achievements[0]['achieved'] == 1

def test_get_game_stats(steam_client):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'playerstats': {
            'stats': [
                {'name': 'Test Stat', 'value': 100}
            ]
        }
    }
    mock_response.raise_for_status = MagicMock()

    with patch('requests.get', return_value=mock_response) as mock_get:
        stats = steam_client.get_game_stats('12345', 1)
        
        mock_get.assert_called_once()
        assert 'stats' in stats
        assert len(stats['stats']) == 1
        assert stats['stats'][0]['name'] == 'Test Stat'
        assert stats['stats'][0]['value'] == 100 