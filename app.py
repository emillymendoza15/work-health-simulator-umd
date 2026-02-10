import streamlit as st

# --------------------------------------------------
# Page Setup
# --------------------------------------------------
st.set_page_config(page_title="Many Ways to Be Here", layout="centered")

# --------------------------------------------------
# Global Styling
# --------------------------------------------------
st.markdown("""
<style>
    :root {
        --nyu-purple: #57068c;
        --light-violet: #f6f2fb;
    }

    .stApp {
        background-color: var(--light-violet);
    }

    html, body, p, span, label, li, div {
        color: black !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    h1, h2, h3 {
        color: var(--nyu-purple) !important;
        font-weight: 700;
    }

    .section-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 14px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .quote {
        font-style: italic;
        background: white;
        border-left: 4px solid var(--nyu-purple);
        padding: 0.75rem 1rem;
        border-radius: 8px;
        margin-top: 0.75rem;
    }

    .mosaic-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 1.25rem;
        margin-top: 1.5rem;
    }

    .mosaic-card {
        background: white;
        border-left: 4px solid var(--nyu-purple);
        border-radius: 12px;
        padding: 1rem 1.25rem;
        font-style: italic;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .stButton > button {
        background-color: white !important;
        color: black !important;
        border: 2px solid var(--nyu-purple) !important;
        border-radius: 10px;
        padding: 0.4rem 1rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: var(--nyu-purple) !important;
        color: white !important;
    }

    .footer {
        text-align: center;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-bottom: 1rem;
        color: #444;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Session State
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = 0

if "selected_elements" not in st.session_state:
    st.session_state.selected_elements = []

# --------------------------------------------------
# Navigation Helpers
# --------------------------------------------------
def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

def reset_app():
    st.session_state.page = 0
    st.session_state.selected_elements = []

# --------------------------------------------------
# Data
# --------------------------------------------------
elements = {
    "🚇 Navigating the City Every Day": {
        "insights": [
            "Plans their day around one dependable train line and builds buffer time automatically.",
            "Uses commute time to mentally rese music, podcasts, zoning out."
        ],
        "quote": "Some days the train works, some days it doesn’t. You learn to stop fighting it."
    },
    "🕒 Balancing School With Work or Family": {
        "insights": [
            "Plans by the week, not the day flexibility matters more than perfection.",
            "Communicates early instead of apologizing after."
        ],
        "quote": "I don’t have perfect weeks I have manageable ones."
    },
    "🏙️ Living in Shared or Crowded Spaces": {
        "insights": [
            "Finds one reliable quiet place and treats it like home base.",
            "Accepts that focus looks different headphones become essential."
        ],
        "quote": "Privacy is a privilege, so you get creative about finding space."
    },
    "😴 Living With an Inconsistent Sleep Rhythm": {
        "insights": [
            "Focuses on recovery instead of chasing perfect routines.",
            "Listens to how rested they feel, not the clock."
        ],
        "quote": "I stopped fixing my sleep and started listening to my body."
    },
    "🥡 Eating Life On-the-Go": {
        "insights": [
            "Keeps a rotation of dependable meals and snacks.",
            "Treats food as fuel during busy weeks."
        ],
        "quote": "Some days food is fuel, not an experience and that’s okay."
    },
    "🌡️ Existing Through Every Season": {
        "insights": [
            "Over-prepares with layers, water, and backups.",
            "Slows expectations on extreme weather days."
        ],
        "quote": "You don’t cancel plans because of weather you adapt."
    }
}

# --------------------------------------------------
# Pages
# --------------------------------------------------
def page_welcome():
    st.title("Many Ways to Be Here")
    st.subheader("A reflection on student life, adaptation, and community.")
    st.caption("Step 1 of 4")

    st.markdown("""
    <div class="section-card">
    This project explores how students experience life differently 
    not through achievements, but through daily realities.

    In a city shaped by movement and diversity, no two paths look the same.
    Community forms when those differences are seen.
    </div>
    """, unsafe_allow_html=True)

    st.button("Begin", on_click=next_page)

def page_build():
    st.title("Build a Day in the City")
    st.caption("Step 2 of 4")
    st.write("Select everything that feels true to your experience.")

    selections = []
    for label in elements:
        checked = st.checkbox(label, value=(label in st.session_state.selected_elements))
        if checked:
            selections.append(label)

    st.session_state.selected_elements = selections

    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_page)
    with col2:
        if selections:
            st.button("Finish", on_click=next_page)

def page_shapes():
    st.title("What This Experience Shapes")
    st.caption("Step 3 of 4")

    for item in st.session_state.selected_elements:
        st.markdown(f"<div class='section-card'><h3>{item}</h3>", unsafe_allow_html=True)

        for insight in elements[item]["insights"]:
            st.write("• " + insight)

        st.markdown(
            f"<div class='quote'>“{elements[item]['quote']}”</div></div>",
            unsafe_allow_html=True
        )

    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_page)
    with col2:
        st.button("Next", on_click=next_page)

def page_why():
    st.title("Why This Matters")
    st.caption("Step 4 of 4")

    st.markdown("""
    <div class="section-card">
    Students arrive with different routines, responsibilities, and starting points 
    all shaped by environment and circumstance.

    Recognizing these differences is part of what turns a shared space
    into a real community.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Student Voices")

    st.markdown("""
    <div class="mosaic-grid">
        <div class="mosaic-card">“I don’t have one routine I adjust every week.”</div>
        <div class="mosaic-card">“My commute is the only time my thoughts slow down.”</div>
        <div class="mosaic-card">“Some weeks, surviving is success.”</div>
        <div class="mosaic-card">“I learned to stop comparing my pace to other people’s.”</div>
        <div class="mosaic-card">“Community doesn’t mean sameness — it means awareness.”</div>
        <div class="mosaic-card">“I found balance by letting go of perfection.”</div>
        <div class="mosaic-card">“You make space where you can.”</div>
        <div class="mosaic-card">“Belonging isn’t automatic — it’s built.”</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_page)
    with col2:
        st.button("Restart", on_click=reset_app)

    st.markdown("<div class='footer'>Created by Emily Mendoza Dominguez</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Router
# --------------------------------------------------
pages = [page_welcome, page_build, page_shapes, page_why]
pages[st.session_state.page]()
