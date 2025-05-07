# Steam Achievements and Playtime Tracker

A web application that tracks Steam achievements and playtime for games in your library. The application collects data periodically and presents it through an interactive dashboard.

## Features

- Track Steam achievements progress
- Monitor game playtime
- Visualize gaming statistics
- Automated data collection

## Project Structure

```
steam-tracker/
├── backend/          # Python backend for Steam API integration
├── data/            # Data storage for game statistics
├── frontend/        # React frontend application
└── .github/         # GitHub Actions workflows
```

## Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Steam API key in the environment variables:
   ```bash
   export STEAM_API_KEY=your_api_key_here
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## Development

- Backend API runs on port 5000
- Frontend development server runs on port 3000
- Data collection runs nightly via GitHub Actions

## License

MIT 