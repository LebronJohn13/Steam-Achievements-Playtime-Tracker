import React, { useState, useEffect } from 'react';
import { Container, Typography, Box, TextField, Button } from '@mui/material';
import PlaytimeChart from './components/PlaytimeChart';
import AchievementTable from './components/AchievementTable';

function App() {
  const [steamId, setSteamId] = useState('');
  const [games, setGames] = useState([]);
  const [selectedGame, setSelectedGame] = useState(null);
  const [achievements, setAchievements] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchGames = async () => {
    if (!steamId) return;
    
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`http://localhost:5000/api/games/${steamId}`);
      if (!response.ok) throw new Error('Failed to fetch games');
      const data = await response.json();
      setGames(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const fetchAchievements = async (appId) => {
    if (!steamId || !appId) return;
    
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`http://localhost:5000/api/achievements/${steamId}/${appId}`);
      if (!response.ok) throw new Error('Failed to fetch achievements');
      const data = await response.json();
      setAchievements(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGameSelect = (game) => {
    setSelectedGame(game);
    fetchAchievements(game.app_id);
  };

  return (
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Steam Achievements & Playtime Tracker
        </Typography>

        <Box sx={{ mb: 4 }}>
          <TextField
            label="Steam ID"
            value={steamId}
            onChange={(e) => setSteamId(e.target.value)}
            sx={{ mr: 2 }}
          />
          <Button
            variant="contained"
            onClick={fetchGames}
            disabled={!steamId || loading}
          >
            Load Games
          </Button>
        </Box>

        {error && (
          <Typography color="error" sx={{ mb: 2 }}>
            {error}
          </Typography>
        )}

        {games.length > 0 && (
          <>
            <PlaytimeChart games={games} onGameSelect={handleGameSelect} />
            {selectedGame && (
              <AchievementTable
                achievements={achievements}
                gameName={selectedGame.name}
              />
            )}
          </>
        )}
      </Box>
    </Container>
  );
}

export default App; 