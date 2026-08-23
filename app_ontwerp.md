# 📱 KrinSranan App-Schermen Architectuur

Dit document bevat de volledige, definitieve visuele en functionele indeling van de KrinSranan smartphone-app. De app maakt gebruik van een vertrouwde, nationale Surinaamse stijl (Groen, Wit en Goud/Geel).

## 🎨 Huisstijl & Kleuren
* **Hoofdkleur (Achtergrond):** Zuiver Wit (`#FFFFFF`) voor overzicht en rust.
* **Accentkleur 1 (Knoppen & Status):** Krachtig Groen (`#007A33`) - symbool voor een schoon milieu en hoop.
* **Accentkleur 2 (Beloningen & Ster):** Goudgeel (`#FCD116`) - symbool voor de rijkdom van het land en verdiende voordelen.

---

## 🖥️ Scherm 1: Het Hoofddashboard (Startscherm)
Dit is het eerste scherm dat de burger ziet bij het openen van de app.

* **Bovenbalk:**
  * **Anoniem ID:** Toont het gecodeerde DID-nummer van de burger (bijv. `did:krin:sr...`). 100% privacy-proof.
  * **Mijn Score:** Een grote, groene cirkel met de actuele sociale kredietscore (Schaal 0 tot 1000). Start op `500`.
  * **Mijn Wallet:** Een gouden vlak met het direct besteedbare saldo in Surinaamse Dollars (bijv. `SRD 1.250,00`).

* **Middenstuk (Actie-knoppen):**
  * 🟢 **KNOP: "Schoon Suriname" (Milieubijdrage)**
    * *Werking:* Opent de persoonlijke QR-code om te scannen bij een vuil-inleverstation, óf toont de digitale kaart met openstaande schoonmaaktaken in de wijk.
  * 🛒 **KNOP: "De Markt" (Verzilveren)**
    * *Werking:* Opent de digitale winkel waarmee het SRD-saldo direct kan worden omgezet in barcodes voor supermarktpakketten, of waarmee EBS/SWM-rekeningen direct worden voldaan.

* **Onderbalk (Rechtvaardigheid & Controle):**
  * 🛡️ **KNOP: "Meld Corruptie" (Klokkenluider)**
    * *Werking:* Activeert de camera en microfoon om anoniem bewijs van corruptie of zware milieuvervuiling te uploaden.
  * ⚖️ **KNOP: "Volksjury" (Mijn Burgerplicht)**
    * *Werking:* Toont of er een actieve zaak is waarin de burger anoniem mag meestemmen over de bezwaren van een mede-Surinamer.

---

## 🖥️ Scherm 2: Het Volksjury-Portaal (De Loophole)
Het scherm waar burgers naartoe gaan als ze een automatische straf willen aanvechten, of als ze als jurylid zijn gekozen.

* **Sectie A: Mijn Bezwaren**
  * Toont eventuele openstaande automatische straffen (bijv. *Foutief vuilstorten gedetecteerd op 24-08-2026*).
  * **Knop: "In beroep gaan"** -> Stuurt het dossier direct naar de anonieme digitale volksjury. De strafpunten worden 14 dagen bevroren.

* **Sectie B: Actieve Juryrechtspraak**
  * Toont een willekeurige, anonieme casus van een andere burger aan de geselecteerde juryleden.
  * *Tekst op het scherm:* "Bekijk het bewijsmateriaal en de uitleg van deze burger. Was er sprake van overmacht of een geldige reden?"
  * **Knop [JA] (Groen):** Wist de straf en herstelt de punten van de burger.
  * **Knop [NEE] (Rood):** Maakt de straf definitief.

---

## 🖥️ Scherm 3: Het Klokkenluidersportaal (Anoniem Melden)
Dit scherm is ontworpen om corruptie aan de top direct te filmen en te stoppen.

* **Upload-veld:** Sleep- en neerzetveld voor foto's, video's of documenten.
* **Beveiligingsstatus:** Een grote indicator die aangeeft: 🔒 *Cryptografische anonimisering ACTIEF. Uw apparaatgegevens en IP-adres zijn volledig gewist.*
* **Knop: "Verzend naar AI-Analyse"** -> Verwerkt de melding direct en start de automatische controleprocedure.

