import streamlit as st
import json
import os

# Ayarlar
PASSWORD = "Mehmetefe2011"
DATA_FILE = "perryn_data.json"

# Veri Yükleme
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"mood": "Mutlu", "memory": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

# Arayüz
st.title("Perryn AI")
st.write("Geliştirici: Mehmet Efe Karakaya")

mood_icons = {"Mutlu": "😊", "Düşünceli": "🤔", "Heyecanlı": "🤩", "Üzgün": "😔"}
st.markdown(f"<h1 style='text-align: center;'>{mood_icons.get(data['mood'], '😐')}</h1>", unsafe_allow_html=True)

user_input = st.text_input("Bana bir şey öğret:")
if st.button("Öğret"):
    if user_input:
        st.session_state.temp = user_input
        st.warning("Onaylıyorsan şifreyi gir:")
    else:
        st.error("Bir bilgi girmelisin!")

if "temp" in st.session_state:
    sifre = st.text_input("Şifre:", type="password")
    if st.button("Doğrula"):
        if sifre == PASSWORD:
            data["memory"].append(st.session_state.temp)
            data["mood"] = "Heyecanlı"
            save_data(data)
            st.success("Yeni bir şey öğrendim!")
            del st.session_state.temp
            st.rerun()
        else:
            st.error("Hatalı şifre!")

st.subheader("Hafızam")
st.write(data["memory"])
      
