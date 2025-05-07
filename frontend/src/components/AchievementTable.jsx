import React from 'react';
import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
  LinearProgress,
  Box
} from '@mui/material';

const AchievementTable = ({ achievements, gameName }) => {
  const totalAchievements = achievements.length;
  const unlockedAchievements = achievements.filter(a => a.achieved === 1).length;
  const completionPercentage = (unlockedAchievements / totalAchievements) * 100;

  return (
    <Paper sx={{ p: 2 }}>
      <Typography variant="h6" gutterBottom>
        Achievements for {gameName}
      </Typography>
      
      <Box sx={{ mb: 2 }}>
        <Typography variant="body2" color="text.secondary" gutterBottom>
          Progress: {unlockedAchievements} / {totalAchievements} achievements
        </Typography>
        <LinearProgress
          variant="determinate"
          value={completionPercentage}
          sx={{ height: 10, borderRadius: 5 }}
        />
      </Box>

      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Description</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {achievements.map((achievement) => (
              <TableRow
                key={achievement.name}
                sx={{
                  backgroundColor: achievement.achieved ? 'action.hover' : 'inherit'
                }}
              >
                <TableCell>{achievement.name}</TableCell>
                <TableCell>{achievement.description}</TableCell>
                <TableCell>
                  {achievement.achieved ? 'Unlocked' : 'Locked'}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Paper>
  );
};

export default AchievementTable; 