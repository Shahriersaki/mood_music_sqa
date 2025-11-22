# Fix for importing from parent folder
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your MusicRecommender class
from app.music_recommender import MusicRecommender

# ========================
# Test functions
# ========================

def test_detect_happy():
    bot = MusicRecommender()
    mood = bot.detect_mood("I am feeling very joyful today!")
    assert mood == "happy"

def test_detect_sad():
    bot = MusicRecommender()
    mood = bot.detect_mood("I feel down")
    assert mood == "sad"

def test_unknown_mood():
    bot = MusicRecommender()
    mood = bot.detect_mood("I feel like a dragon")
    assert mood == "unknown"

def test_valid_recommendation():
    bot = MusicRecommender()
    playlist = bot.recommend("happy")
    assert playlist in bot.playlists["happy"]

def test_invalid_mood_recommendation():
    bot = MusicRecommender()
    playlist = bot.recommend("confused")
    assert playlist == "Mood not recognized"
