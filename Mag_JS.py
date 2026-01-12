import streamlit as st

# 1. Ustawienie konfiguracji strony - profesjonalna ikona magazynu
st.set_page_config(
    page_title="System Magazynowy",
    page_icon="📦",
    layout="centered"
)

# --- NAGŁÓWEK ---
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Prosty Magazyn")
    st.write("System zarządzania asortymentem w czasie rzeczywistym.")

with col2:
    # Ikona paczki/logistyki (neutralna)
    image_url = "https://cdn-icons-png.flaticon.com/512/679/679720.png"
    st.image(image_url, width=100)

st.divider()

# --- LOGIKA BAZY DANYCH (Session State) ---
if 'produkty' not in st.session_state:
    st.session_state.produkty = []

# --- SEKCJA DODAWANIA ---
st.subheader("➕ Dodaj nowy produkt")
with st.form(key='add_form', clear_on_submit=True):
    nowy_produkt_input = st.text_input("Nazwa produktu:")
    submit_button = st.form_submit_button(label='Zatwierdź i dodaj')

    if submit_button:
        if nowy_produkt_input:
            # Normalizacja nazwy (brak duplikatów)
            if not any(p.lower() == nowy_produkt_input.lower() for p in st.session_state.produkty):
                st.session_state.produkty.append(nowy_produkt_input.strip())
                st.success(f"Pomyślnie dodano: {nowy_produkt_input}")
            else:
                st.warning("Ten produkt już figuruje w spisie.")
        else:
            st.error("Pole nazwy nie może być puste.")

# --- SEKCJA USUWANIA ---
st.subheader("🗑️ Zarządzanie stanem")

if st.session_state.produkty:
    col_del1, col_del2 = st.columns([3, 1])
    with col_del1:
        produkt_do_usuniecia = st.selectbox(
            "Wybierz produkt do usunięcia:", 
            st.session_state.produkty,
            label_visibility="collapsed"
        )
    with col_del2:
        if st.button("Usuń produkt", use_container_width=True):
            st.session_state.produkty.remove(produkt_do_usuniecia)
            st.rerun()
else:
    st.info("Magazyn jest obecnie pusty.")

st.divider()

# --- SEKCJA WYŚWIETLANIA ---
st.subheader(f"📋 Aktualna lista ({len(st.session_state.produkty)} pozycji)")

if st.session_state.produkty:
    # Wyświetlanie listy w sformatowanych kontenerach
    for i, produkt in enumerate(st.session_state.produkty, 1):
        st.info(f"**{i}.** {produkt}")
else:
    st.write("Brak zarejestrowanych produktów.")
