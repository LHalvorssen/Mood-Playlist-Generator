# Mood-Based Playlist Generator 🎵

## Overview
The **Mood-Based Playlist Generator** is a Python script that creates Spotify playlists based on your current mood. It includes a fun twist of adding a random genre for variety and saves playlists for future reference.

## Features
- Select a mood (e.g., Happy, Calm, Energetic) to get curated playlists.
- Adds a random genre twist to the playlist search.
- Saves generated playlists to a local JSON file (`playlists.json`).
- View previously saved playlists.

## Requirements
- Python 3.7 or higher
- A Spotify Developer account to obtain API credentials

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/LHalvorssen/Mood-Playlist-Generator.git
cd Mood-Playlist-Generator
```

### 2. Create a Virtual Environment (Optional)
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Spotify API Credentials
- Create a new Spotify Developer account and obtain API credentials.
- Replace `your_client_id` and `your_client_secret` in `mood_playlist_generator.py` with your actual credentials.
- Create a `.env` file in the root directory with the following variables:
   - `SPOTIFY_CLIENT_ID`=your_client_id
   - `SPOTIFY_CLIENT_SECRET`=your_client_secret
   - `SPOTIFY_REDIRECT_URI`=http://localhost:8080/callback
- Load these values in your script:
```python
from dotenv import load_dotenv
import os

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
```

### 5. Run the Script
```bash
python3 mood_playlist_generator.py
```
### Usage
1. Choose between generating a playlist or viewing saved ones.
2. If generating a playlist, select a mood and optionally add a random genre.
   - The script will display the playlist name and URL.
   - Playlists are saved to `playlists.json` for future reference.
3. If viewing saved playlists, the script will display a list of saved playlists.

### Example Workflow
Welcome to the Mood-Based Playlist Generator!
What would you like to do? [Generate Playlist/View Saved Playlists]: Generate Playlist
How are you feeling? [Happy/Calm/Focused/Energetic/Sad]: Happy
Fetching playlists for mood: Happy...
Here's a playlist for your mood:
📜 Happy Vibes
🔗 https://open.spotify.com/playlist/7GhawGpb43Ctkq3PRP1fOL
Playlist saved successfully!

### License
This project is licensed under the MIT License.