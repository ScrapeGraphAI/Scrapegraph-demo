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