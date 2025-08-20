import streamlit as st
import requests
import feedparser

# === CONFIGURATION ===
CITY = "Nottingham,GB"
WEATHER_API_KEY = "ecb7c83816ba638dca5f1f8f3af9c5a4"
HOROSCOPE_SIGN = "cancer"
HOROSCOPE_API_KEY = "3IXWgTnP8MEVf0FN+aQx7g==4TsfTxxPnYxgjQyp"
CHIME_FILE = "ding.mp3"  # Add your chime file in the same folder

# === PAGE TITLE ===
st.title("🌅 Morning Briefing")

# === PLAY CHIME ===
st.audio(CHIME_FILE)

# === WEATHER ===
try:
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric"
    weather_res = requests.get(weather_url).json()
    weather_desc = weather_res["weather"][0]["description"].capitalize()
    temp = weather_res["main"]["temp"]
    st.subheader("Weather")
    st.write(f"The weather in {CITY} today is {weather_desc}, with a temperature of {temp}°C.")
except Exception as e:
    st.write("Weather info not available.")

# === NEWS ===
try:
    rss_url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(rss_url)
    headlines = [entry.title for entry in feed.entries[:5]]
    st.subheader("Top 5 News Headlines")
    for headline in headlines:
        st.write(f"- {headline}")
except Exception as e:
    st.write("News info not available.")

# === HOROSCOPE ===
try:
    horo_res = requests.get(
        f"https://api.api-ninjas.com/v1/horoscope?zodiac={HOROSCOPE_SIGN}",
        headers={"X-Api-Key": HOROSCOPE_API_KEY}
    ).json()
    st.subheader(f"{HOROSCOPE_SIGN.capitalize()} Horoscope")
    st.write(horo_res.get("horoscope", "Not available"))
except Exception as e:
    st.write("Horoscope info not available.")

# === CLOSING NOTE ===
st.write("Have a great day ahead! 🌞")
