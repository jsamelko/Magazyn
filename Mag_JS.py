import streamlit as st

# 1. Konfiguracja strony (musi być zawsze pierwsza)
st.set_page_config(page_title="Prosty Magazyn", page_icon="📦")

# --- ZMIANA: UKŁAD Z MIKOŁAJEM ---
# Tworzymy dwie kolumny: lewa szersza (tekst), prawa węższa (obrazek)
col_header_L, col_header_R = st.columns([4, 1])

with col_header_L:
    st.title("📦 Prosty Magazyn")
    st.write("Aplikacja do zarządzania listą produktów (dane tymczasowe).")

with col_header_R:
    # Wyświetlamy obrazek Mikołaja z publicznego adresu URL
    st.image("https://cdn-icons-png.flaticon.com/512/3794/3794458.png", width=100)
    # Możesz też użyć st.write("🎅") dla dużej emotikony, jeśli nie chcesz obrazka
# ---------------------------------

# 2. Inicjalizacja stanu (bazy danych w pamięci)
if 'produkty' not in st.session_state:
    st.session_state.produkty = []

# 3. Sekcja: Dodawanie produktu
st.header("1. Dodaj produkt")
col1, col2 = st.columns([3, 1])

with col1:
    nowy_produkt = st.text_input("Nazwa produktu", key="input_produkt")

with col2:
    st.write("") # Pusty odstęp dla wyrównania w pionie
    st.write("")
    if st.button("Dodaj"):
        if nowy_produkt:
            if nowy_produkt not in st.session_state.produkty:
                st.session_state.produkty.append(nowy_produkt)
                st.success(f"Dodano: {nowy_produkt}")
            else:
                st.warning("Ten produkt już jest na liście!")
        else:
            st.error("Wpisz nazwę produktu.")

st.divider()

# 4. Sekcja: Lista produktów i Usuwanie
st.header("2. Stan magazynowy")

if len(st.session_state.produkty) > 0:
    st.write("Aktualne produkty:")
    for i, produkt in enumerate(st.session_state.produkty, 1):
        st.text(f"{i}. {produkt}")
    
    st.divider()
    
    st.subheader("Usuń produkt")
    produkt_do_usuniecia = st.selectbox(
        "Wybierz produkt do usunięcia", 
        st.session_state.produkty
    )
    
    if st.button("Usuń wybrany"):
        st.session_state.produkty.remove(produkt_do_usuniecia)
        st.rerun()
else:
    st.info("Magazyn jest pusty. Dodaj pierwszy produkt powyżej.")
