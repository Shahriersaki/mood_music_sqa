import random

class MusicRecommender:

    mood_keywords = {
        "happy": ["happy", "joy", "cheerful", "excited"],
        "sad": ["sad", "down", "upset", "depressed"],
        "angry": ["angry", "mad", "furious", "irritated"],
        "focus": ["focus", "study", "work", "concentrate"],
        "romantic": ["love", "romantic", "heart", "date"]
    }

    playlists = {
        "happy": ["Happy Vibes", "Sunny Beats", "Positive Energy"],
        "sad": ["Sad Hour", "Deep Emotions", "Calm & Cry"],
        "angry": ["Rock Rage", "Heavy Shots", "Boost Mode"],
        "focus": ["LoFi Beats", "Deep Focus", "Coding Mix"],
        "romantic": ["Love Hits", "Soft Romance", "Date Night"]
    }

    def detect_mood(self, text):
        text = text.lower()
        for mood, keywords in self.mood_keywords.items():
            if any(k in text for k in keywords):
                return mood
        return "unknown"

    def recommend(self, mood):
        if mood not in self.playlists:
            return "Mood not recognized"
        return random.choice(self.playlists[mood])
