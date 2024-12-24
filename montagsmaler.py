import streamlit as st
import random

# Define categories and words
normal_words = [
    "Apfel", "Banane", "Katze", "Hund", "Elefant", "Blume", "Gitarre", "Haus", "Insel", "Affe",
    "Drachen", "Löwe", "Berg", "Stift", "Ozean", "Klavier", "Königin", "Regenbogen", "Sonne", "Baum",
    "Regenschirm", "Geige", "Wal", "Xylophon", "Yacht", "Zebra", "Auto", "Fahrrad", "Tisch", "Stuhl",
    "Lampe", "Buch", "Radio", "Hut", "Schuhe", "Brot", "Milch", "Kamera", "Brille", "Kissen",
    "Teppich", "Fenster", "Tür", "Kerze", "Tasse", "Glocke", "Papier", "Koffer", "Ball"
]

christmas_words = [
    "Weihnachtsbaum", "Schlitten", "Rentier", "Geschenk", "Weihnachtsmann", "Plätzchen", "Schneemann", "Adventskalender", "Kerze", "Krippe",
    "Glühwein", "Weihnachtsstern", "Schnee", "Lametta", "Weihnachtslied", "Nikolaus", "Mistelzweig", "Kamin", "Schlittenfahrt", "Eiskristall",
    "Tannenbaum", "Christkind", "Zimtstern", "Lebkuchen", "Kugeln", "Engel", "Rudolph", "Heiligabend", "Stern", "Wichtel",
    "Punsch", "Kranz", "Schokoladenfigur", "Festessen", "Geschenkpapier", "Weihnachtsmarkt", "Socken", "Weihnachtsdeko", "Lichterkette", "Christbaumkugel",
    "Eislaufen", "Eiszapfen", "Schneeflocke", "Brief", "Sternsinger", "Schneeballschlacht", "Winterjacke", "Pullover", "Stiefel", "Zuckerstange"
]


# Initialize session state for used words
if "used_words" not in st.session_state:
    st.session_state.used_words = {"normal": set(), "christmas": set()}

# Streamlit app title
st.markdown("<h1 style='text-align: center;'>Montagsmaler</h1>", unsafe_allow_html=True)

# Add a description
st.write("Wählen Sie eine Kategorie und drücken Sie den Knopf unten, um ein Wort zum Zeichnen zu generieren!")

# Select category
category = st.selectbox("Wählen Sie eine Kategorie:", ("Normal", "Weihnachten"))

# Center layout with larger button and word display
st.markdown("""
<style>
    .stButton > button {
        display: block;
        margin: 0 auto;
        font-size: 48px;
        padding: 15px 30px;
        color: white;
        border: none;
        border-radius: 10px;
        cursor: pointer;
    }
    .stText {
        text-align: center;
        font-size: 100px;
        margin-top: 20px;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Button to generate a random word
if st.button("Wort generieren"):
    if category == "Normal":
        word_list = normal_words
        used_category = "normal"
    else:
        word_list = christmas_words
        used_category = "christmas"

    # Filter out already used words
    available_words = [word for word in word_list if word not in st.session_state.used_words[used_category]]

    if available_words:
        # Choose a random word from the available list
        random_word = random.choice(available_words)
        st.session_state.used_words[used_category].add(random_word)
        # Display the word in the center and large
        st.markdown(f"<div class='stText'>{random_word}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='stText'>Keine weiteren Wörter in der Kategorie \"{category}\" verfügbar!</div>", unsafe_allow_html=True)
