import React from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from 'recharts';
import { Paper, Typography, Box } from '@mui/material';

const PlaytimeChart = ({ games, onGameSelect }) => {
  // Sort games by playtime and take top 10
  const topGames = [...games]
    .sort((a, b) => b.playtime_forever - a.playtime_forever)
    .slice(0, 10)
    .map(game => ({
      ...game,
      // Convert minutes to hours
      playtime_hours: (game.playtime_forever / 60).toFixed(1)
    }));

  return (
    <Paper sx={{ p: 2, mb: 4 }}>
      <Typography variant="h6" gutterBottom>
        Top 10 Games by Playtime
      </Typography>
      <Box sx={{ height: 400 }}>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            data={topGames}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
            onClick={(data) => {
              if (data && data.activePayload) {
                onGameSelect(data.activePayload[0].payload);
              }
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis
              dataKey="name"
              angle={-45}
              textAnchor="end"
              height={100}
              interval={0}
            />
            <YAxis label={{ value: 'Hours', angle: -90, position: 'insideLeft' }} />
            <Tooltip
              formatter={(value) => [`${value} hours`, 'Playtime']}
              labelFormatter={(label) => `Game: ${label}`}
            />
            <Bar
              dataKey="playtime_hours"
              fill="#8884d8"
              cursor="pointer"
            />
          </BarChart>
        </ResponsiveContainer>
      </Box>
    </Paper>
  );
};

export default PlaytimeChart; 