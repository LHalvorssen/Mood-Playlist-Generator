import random
import json
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from rich.console import Console
from rich.prompt import Prompt

# Console setup for enhanced CLI
console = Console()

# Spotify API credentials
SPOTIFY_CLIENT_ID = "your_client_id"  # Replace with your actual Client ID
SPOTIFY_CLIENT_SECRET = "your_client_secret"  # Replace with your actual Client Secret
REDIRECT_URI = "http://localhost:8888/callback"  # Ensure this matches your Spotify app setup

# Initialize Spotify client with required permissions
spotify = Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-read-private",
    )
)

# Test Spotify API connection
console.print("[yellow]Testing Spotify API connection...[/yellow]")
current_user = spotify.me()
console.print(f"[green]Authenticated as: {current_user['display_name']}[/green]")

# Define mood keywords
MOOD_KEYWORDS = {
    "Happy": ["feel-good", "happy", "party"],
    "Calm": ["chill", "acoustic", "lo-fi"],
    "Focused": ["focus", "study", "instrumental"],
    "Energetic": ["workout", "dance", "upbeat"],
    "Sad": ["sad", "melancholy", "slow"],
    "Romantic": ["romantic", "love", "slow jams"],
    "Angry": ["rock", "metal", "hardcore"],
    "Motivated": ["inspirational", "uplifting", "success"],
    "Nostalgic": ["oldies", "retro", "throwback"],
    "Relaxed": ["relax", "ambient", "meditation"],
}

# Define random genre twist options
GENRES = ["Jazz", "Lo-Fi", "EDM", "Classical", "Pop", "Rock", "Hip-Hop", "Reggae", "Country", "Indie"]

def fetch_playlist(mood):
    """Fetch a playlist based on the user's mood."""
    keywords = MOOD_KEYWORDS.get(mood, [])
    if not keywords:
        console.print(f"[red]No keywords defined for mood: {mood}[/red]")
        return None

    # Pick a random keyword and add a genre twist
    keyword = random.choice(keywords)
    genre = random.choice(GENRES)
    search_query = f"{keyword} {genre}"

    try:
        # Search for playlists with the mood keyword and genre twist
        console.print(f"Searching for playlists with keyword: [cyan]{keyword}[/cyan] and genre twist: [magenta]{genre}[/magenta]")
        results = spotify.search(q=search_query, type="playlist", limit=5)
    except Exception as e:
        console.print(f"[red]Error fetching playlists: {e}[/red]")
        return None

    # Filter out None values in the items list
    playlists = [item for item in results["playlists"]["items"] if item is not None]

    # Check if there are any valid playlists
    if not playlists:
        console.print(f"[yellow]No playlists found for mood: {mood}[/yellow]")
        return None

    # Randomly select a playlist
    playlist = random.choice(playlists)
    return {
        "name": playlist["name"],
        "url": playlist["external_urls"]["spotify"],
    }

def save_playlist(mood, playlist):
    """Save the playlist to a JSON file."""
    data = {}
    try:
        # Load existing playlists if the file exists
        with open("playlists.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        pass

    # Append the new playlist under the mood
    if mood not in data:
        data[mood] = []
    data[mood].append(playlist)

    # Write back to the JSON file
    with open("playlists.json", "w") as file:
        json.dump(data, file, indent=4)
    console.print("[green]Playlist saved successfully![/green]")

def view_saved_playlists():
    """View playlists saved in the JSON file."""
    try:
        with open("playlists.json", "r") as file:
            data = json.load(file)
            console.print("[bold blue]Previously Saved Playlists:[/bold blue]")
            for mood, playlists in data.items():
                console.print(f"\n[bold]{mood}[/bold]:")
                for idx, playlist in enumerate(playlists, 1):
                    console.print(f"  {idx}. [cyan]{playlist['name']}[/cyan] - [link={playlist['url']}]{playlist['url']}[/link]")
    except FileNotFoundError:
        console.print("[yellow]No saved playlists found![/yellow]")

def main():
    """Main script execution."""
    console.print("[bold blue]Welcome to the Mood-Based Playlist Generator![/bold blue]")
    option = Prompt.ask(
        "What would you like to do?",
        choices=["Generate Playlist", "View Saved Playlists"]
    )

    if option == "Generate Playlist":
        mood = Prompt.ask("How are you feeling?", choices=list(MOOD_KEYWORDS.keys()))
        console.print(f"Fetching playlists for mood: [green]{mood}[/green]...")
        playlist = fetch_playlist(mood)
        if playlist:
            console.print(f"\n🎶 [bold]Here's a playlist for your mood:[/bold]")
            console.print(f"📜 [cyan]{playlist['name']}[/cyan]")
            console.print(f"🔗 [link={playlist['url']}]{playlist['url']}[/link]")
            save_playlist(mood, playlist)
        else:
            console.print("[red]Sorry, we couldn't find a playlist for your mood.[/red]")

    elif option == "View Saved Playlists":
        view_saved_playlists()

if __name__ == "__main__":
    main()
