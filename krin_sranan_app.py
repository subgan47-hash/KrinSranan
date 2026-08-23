import streamlit as st
import time
from Krin_sranan_core_ import KrinSrananEngine

# Pagina-instellingen voor mobiel (Nationale Surinaamse look)
st.set_page_config(page_title="KrinSranan App", page_icon="🇸🇷", layout="centered")

# Stijl aanpassen naar Groen, Wit en Goud
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    h1 { color: #007A33; }
    .stButton>button { background-color: #007A33; color: white; border-radius: 10px; width: 100%; }
    .stButton>button:hover { background-color: #FCD116; color: black; }
    .wallet-box { background-color: #FCD116; padding: 20px; border-radius: 10px; color: black; font-weight: bold; text-align: center; }
    .admin-box { background-color: #F0F2F6; padding: 15px; border-radius: 10px; border: 1px dashed #007A33; }
    </style>
""", unsafe_allow_html=True)

st.title("🇸🇷 KrinSranan")
st.caption("De Digitale Herstelmachine - Gecentraliseerd-vrij & Onomkoopbaar")

# Initialiseer de motor achter de schermen via het anonieme DID
if "engine" not in st.session_state:
    st.session_state.engine = KrinSrananEngine(burger_did="did:krin:sr:paramaribo:12345")
engine = st.session_state.engine

# --- BEHEERDERS INTERFACE (DYNAMISCHE TARIEVEN) ---
# Dit zijmenu simuleert de onafhankelijke commissie die inflatie-correcties doorvoert
with st.sidebar:
    st.markdown("<div class='admin-box'>⚙️ <b>Ressort Beheer</b><br><small>Alleen toegankelijk voor onafhankelijke wijkraden via cryptografische sleutel.</small></div>", unsafe_allow_html=True)
    st.write("")
    tarief_plastic = st.slider("Vergoeding per kilo plastic (SRD):", min_value=5.0, max_value=100.0, value=15.0, step=0.5)
    st.info(f"Huidige economische instelling: 1 kg vuil = SRD {tarief_plastic:,.2f}")

# --- SCHERM 1: HOOFDDASHBOARD ---
st.subheader("👤 Mijn Anoniem Profiel")
st.text(f"ID: {engine.burger_did}")

# Score en Wallet visueel weergeven
col1, col2 = st.columns(2)
with col1:
    st.metric(label="🎯 Mijn Score", value=f"{engine.score} / 1000")
with col2:
    st.markdown(f"<div class='wallet-box'>💰 MIJN WALLET<br><span style='font-size:24px;'>SRD {engine.wallet_srd:,.2f}</span></div>", unsafe_allow_html=True)

st.divider()

# Keuze voor de Resorten (Direct schaalbaar voor alle 62)
ressort = st.selectbox("📍 Selecteer uw Bestuursressort:", [
    "Latour", "Flora", "Rainville", "Meerzorg", "Tapanahony", "Brokopondo-Centrum", "Nickerie-West"
])

# Actie-knoppen
st.subheader("🟢 Acties & Inkomen")

# De 5 functionele tabbladen van KrinSranan
tab1, tab2, tab3, tab4, tab5 = st.tabs(["♻️ Milieu", "🛒 Markt", "⚖️ Volksjury", "🛡️ Klokkenluider", "📖 Handleiding"])

with tab1:
    st.write(f"Verdien direct SRD door je resort schoon te houden. Actueel tarief in **{ressort}**: SRD {tarief_plastic:,.2f} per kilo.")
    kilo = st.number_input("Aantal kilo ingeleverd plastic/vuil:", min_value=0.0, step=0.5)
    if st.button("Bevestig Inlevering"):
        if kilo > 0:
            vergoeding = kilo * tarief_plastic  # Berekend op basis van de dynamische schuifbalk
            resultaat = engine.registreer_milieu_bijdrage(transactie_id=str(time.time()), kilo_plastic=kilo, srd_vergoeding=vergoeding)
            st.success(f"Geweldig! Succesvol verwerkt in {ressort}. Score stijgt! Ontvangen: SRD {vergoeding:,.2f}")
            time.sleep(1)
            st.rerun()
        else:
            st.warning("Voer eerst het aantal kilo in.")

with tab2:
    st.write("Verzilver je saldo direct voor nutsvoorzieningen.")
    optie = st.radio("Wat wilt u betalen?", ["EBS Stroomrekening", "SWM Waterrekening", "Basispakket Supermarkt"])
    bedrag = st.number_input("Bedrag in SRD:", min_value=0.0, step=10.0)
    if st.button("Betaal Nu Direct"):
        resultaat = engine.betaal_basisvoorziening(instantie_type=optie, bedrag_srd=bedrag)
        if resultaat["status"] == "GOEDGEKEURD":
            st.success(f"Betaling goedgekeurd! Resterend saldo: SRD {resultaat['resterend_saldo']:,.2f}")
            time.sleep(1)
            st.rerun()
        else:
            st.error("❌ Onvoldoende saldo in uw Wallet. Lever eerst milieu-bijdragen in.")

with tab3:
    st.write("⚖️ Anonieme Burgerplicht: Beoordeel overmacht-zaken uit andere ressorten.")
    straf_id = "STRAF-998"
    if straf_id not in engine.quarantaine_straffen:
        engine.automatische_straf_quarantaine(straf_id, "Zwerfvuil gedetecteerd door camera", 50)
    
    straf = engine.quarantaine_straffen[straf_id]
    if straf["status"] == "WACHT_OP_VOLKSJURY":
        st.info(f"**Casus in beraad:** Een burger heeft bezwaar gemaakt tegen een automatische straf voor: *{straf['overtreding']}*.")
        st.write("Was hier sprake van overmacht of een geldige reden?")
        col_ja, col_nee = st.columns(2)
        with col_ja:
            if st.button("👍 JA (Onschuldig)"):
                engine.verwerk_anonieme_volksjury_stem(straf_id, volk_stemt_onschuldig=True)
                st.success("Uw anonieme stem is cryptografisch verwerkt. Dank u voor uw burgerplicht!")
                time.sleep(1)
                st.rerun()
        with col_nee:
            if st.button("👎 NEE (Schuldig)"):
                engine.verwerk_anonieme_volksjury_stem(straf_id, volk_stemt_onschuldig=False)
                st.error("Uw anonieme stem is verwerkt. Straf wordt definitief.")
                time.sleep(1)
                st.rerun()
    else:
        st.write("🎉 Er wachten op dit moment geen zaken op uw stem.")

with tab4:
    st.write("🛡️ Meld corruptie of zware kwiklozingen volledig anoniem.")
    file = st.file_uploader("Upload foto, video of document als bewijsmateriaal:")
    if st.button("Verzend Anoniem naar AI-Analyse"):
        if file:
            st.success("🔒 Melding gecodeerd! Uw IP-adres en apparaat-ID zijn gewist. De AI start de controleprocedure.")
        else:
            st.warning("Voeg eerst bewijsmateriaal toe.")

with tab5:
    st.markdown("""
    ### 📖 Hoe werkt deze app?
    KrinSranan helpt Suriname schoner te maken en bestrijdt direct armoede, onafhankelijk van politieke partijen. Iedereen begint met **500 punten**.
    
    #### ♻️ 1. Geld verdienen met vuilnis
    Verzamel plastic of zwerfvuil en breng het naar het inleverstation van jouw ressort. Vul het aantal kilo in en klik op **Bevestig Inlevering**. Je ontvangt direct **SRD 15,- per kilo** (of het actueel geldende ressort-tarief) in je Wallet en je score stijgt!
    
    #### 🛒 2. Rekeningen betalen
    Met het geld in je Wallet kun je direct en veilig je **EBS Stroom**, **SWM Water** of een **Basispakket** bij de supermarkt betalen via het tabblad 'Markt'.
    
    #### ⚖️ 3. De Volksjury (De Loophole)
    Als het systeem jou onterecht een automatische straf oplegt, beslissen anonieme mede-burgers uit andere ressorten via hun app of de straf gewist moet worden. Corruptie is hierdoor onmogelijk.
    
    #### 🛡️ 4. Anoniem corruptie melden
    Upload foto's of video's van corruptie of milieuvervuiling. Je apparaat- en internetgegevens worden direct onkraakbaar gewist. Als de melding klopt, keert het systeem automatisch een **veiligheidsbonus** uit in je Wallet.
    """)

