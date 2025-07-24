import streamlit as st

# Mood-to-Spotify and Netflix mapping
mood_map = {
    "Happy": {
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "netflix": ["Friends", "Brooklyn Nine-Nine", "Enola Holmes", "Intern", "Gilmore Girls"]
    },
    "Sad": {
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro",
        "netflix": ["The Pursuit of Happyness", "Your Name", "A Silent Voice", "Five Feet Apart", "The Notebook"]
    },
    "Angry": {
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWTtTyjgd08yp",
        "netflix": ["Breaking Bad", "Peaky Blinders", "Vikings", "Squid Game", "All of us are dead"]
    },
    "Bored": {
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6",
        "netflix": ["Stranger Things", "The Office", "Emily in Paris", "Gossip Girl", "Mean Girls"]
    },
    "Excited": {
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX1g0iEXLFycr",
        "netflix": ["Money Heist", "The Witcher", "Extraction", "Shawshank Redemption", "Shutter Island"]
    }
}

# Streamlit UI
st.set_page_config(page_title="MoodMate", page_icon="🎧", layout="centered")

st.title("🎭 MoodMate: Your Entertainment Companion")
st.write("Tell us how you feel, and we'll recommend what to watch and listen to!")

# Mood input
mood = st.selectbox("How are you feeling today?", list(mood_map.keys()))

if mood:
    st.subheader("🎵 Spotify Playlist")
    st.markdown(f"[Click here to listen on Spotify]({mood_map[mood]['spotify']})")

    st.subheader("📺 Netflix Recommendations")
    for item in mood_map[mood]['netflix']:
        st.write(f"- {item}")

#streamlit run app.py always run this in the terminal in order to run this code 
