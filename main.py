import base64
import streamlit as st

st.title("Scrapegraph-ai")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("scrapegraphai_logo.png")


key = st.text_input("API key")

link = st.text_input("Link to scrape")

genre = st.radio(
    "What operation you want do?",
    ["a", "b", "c"],
    index=1,
)

if st.button("Run th program", type="primary"):
    st.write('DO something')
else:
    st.write('')

left_co2,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,cent_co2,last_co2 = st.columns([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

with cent_co2:
    discord_link = "https://discord.gg/DujC7HG8"
    discord_logo = base64.b64encode(open("discord.png", "rb").read()).decode()
    st.markdown(
        f"""<a href="{discord_link}" target="_blank">
        <img src="data:image/png;base64,{discord_logo}" width="25">
        </a>""",
        unsafe_allow_html=True,
    )

with last_co2:
    discord_link = "https://github.com/VinciGit00/Scrapegraph-ai"
    discord_logo = base64.b64encode(open("github.png", "rb").read()).decode()
    st.markdown(
        f"""<a href="{discord_link}" target="_blank">
        <img src="data:image/png;base64,{discord_logo}" width="25">
        </a>""",
        unsafe_allow_html=True,
    )
