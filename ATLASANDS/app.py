import streamlit as st

st.set_page_config(
    page_title="ATLASANDS",
    page_icon="🌍",
    layout="wide"
)

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown("""

<div style='
height:500px;
border-radius:30px;
background:linear-gradient(
135deg,
#007CF0,
#00DFD8
);
display:flex;
justify-content:center;
align-items:center;
flex-direction:column;
color:white;
'>

<h1 style='font-size:70px;'>

ATLASANDS

</h1>

<h3>

Explore India Beyond Maps

</h3>

</div>

""",
unsafe_allow_html=True)
from data.destinations import DESTINATIONS

st.markdown("## Featured Destinations")

cols = st.columns(4)

for i,d in enumerate(DESTINATIONS):

    with cols[i % 4]:

        st.image(
            d["image"],
            use_container_width=True
        )

        st.markdown(f"""
        <div class='destination-card'>

        <h3>{d['name']}</h3>

        <p>{d['state']}</p>

        <p>{d['category']}</p>

        <p>{d['budget']}</p>

        </div>
        """,
        unsafe_allow_html=True)
        st.sidebar.title("Trip Preferences")

category = st.sidebar.selectbox(
    "Category",
    [
        "All",
        "Beach",
        "Hill Station",
        "Adventure",
        "Nature"
    ]
)

budget = st.sidebar.slider(
    "Budget",
    10000,
    100000,
    30000
)

days = st.sidebar.slider(
    "Days",
    1,
    20,
    5
)