import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Prosty Magazyn", page_icon="📦")

st.title("📦 Prosty Magazyn")
st.write("Aplikacja do zarządzania listą produktów (dane tymczasowe).")

# 2. Inicjalizacja stanu (bazy danych w pamięci)
# Sprawdzamy, czy lista produktów już istnieje w sesji. Jeśli nie, tworzymy pustą.
if 'produkty' not in st.session_state:
    st.session_state.produkty = []

# 3. Sekcja: Dodawanie produktu
st.header("1. Dodaj produkt")
col1, col2 = st.columns([3, 1])

with col1:
    # Pobieramy nazwę produktu
    nowy_produkt = st.text_input("Nazwa produktu", key="input_produkt")

with col2:
    # Przycisk dodawania jest obok pola tekstowego
    st.write("") # Pusty odstęp dla wyrównania
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
    # Wyświetlenie listy
    st.write("Aktualne produkty:")
    for i, produkt in enumerate(st.session_state.produkty, 1):
        st.text(f"{i}. {produkt}")
    
    st.divider()
    
    # Usuwanie
    st.subheader("Usuń produkt")
    produkt_do_usuniecia = st.selectbox(
        "Wybierz produkt do usunięcia", 
        st.session_state.produkty
    )
    
    if st.button("Usuń wybrany"):
        st.session_state.produkty.remove(produkt_do_usuniecia)
        st.rerun() # Odświeżamy aplikację, aby zaktualizować listę natychmiast
else:
    st.info("Magazyn jest pusty. Dodaj pierwszy produkt powyżej.")
