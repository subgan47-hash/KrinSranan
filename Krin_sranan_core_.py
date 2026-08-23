import hashlib
import time
import json

class KrinSrananEngine:
    def __init__(self, burger_did):
        self.burger_did = burger_did
        self.score = 500  
        self.wallet_srd = 0.0
        self.quarantaine_straffen = {}  
        self.blockchain_ledger = []    

    def _bereken_beveiligings_hash(self, data_pakket):
        return hashlib.sha256(json.dumps(data_pakket, sort_keys=True).encode('utf-8')).hexdigest()

    def _schrijf_naar_ledger(self, actie_type, score_mutatie, srd_mutatie, details=""):
        vorig_hash = self.blockchain_ledger[-1]['huidige_hash'] if self.blockchain_ledger else "KRIN_SRANAN_GENESIS"
        transactie = {
            "timestamp": time.time(),
            "actie_type": actie_type,
            "score_mutatie": score_mutatie,
            "srd_mutatie": srd_mutatie,
            "details": details,
            "vorig_hash": vorig_hash
        }
        transactie['huidige_hash'] = self._bereken_beveiligings_hash(transactie)
        self.blockchain_ledger.append(transactie)

    def registreer_milieu_bijdrage(self, transactie_id, kilo_plastic, srd_vergoeding, score_bonus=20):
        self.score = min(1000, self.score + score_bonus)
        self.wallet_srd += srd_vergoeding
        self._schrijf_naar_ledger("MILIEU_INLEVERING", score_bonus, srd_vergoeding, f"ID: {transactie_id} | {kilo_plastic}kg")
        return {"status": "SUCCES", "nieuwe_score": self.score, "wallet_srd": self.wallet_srd}

    def betaal_basisvoorziening(self, instantie_type, bedrag_srd):
        if self.wallet_srd >= bedrag_srd:
            self.wallet_srd -= bedrag_srd
            self._schrijf_naar_ledger(f"BETALING_{instantie_type.upper()}", 0, -bedrag_srd)
            return {"status": "GOEDGEKEURD", "resterend_saldo": self.wallet_srd}
        return {"status": "SALDO_TE_LAAG"}

    def automatische_straf_quarantaine(self, straf_id, type_overtreding, punten_aftrek):
        deadline = time.time() + (14 * 24 * 60 * 60)
        self.quarantaine_straffen[straf_id] = {"overtreding": type_overtreding, "punten": punten_aftrek, "deadline": deadline, "status": "WACHT_OP_VOLKSJURY"}
        self._schrijf_naar_ledger("STRAF_QUARANTAINE", 0, 0, f"Straf {straf_id} in beraad.")
        return {"status": "IN_BERAAD", "uiterste_datum_jury": deadline}

    def verwerk_anonieme_volksjury_stem(self, straf_id, volk_stemt_onschuldig):
        if straf_id not in self.quarantaine_straffen: return {"status": "STRAF_NIET_GEVONDEN"}
        straf = self.quarantaine_straffen[straf_id]
        if volk_stemt_onschuldig:
            straf["status"] = "VRIJGESPROKEN_DOOR_VOLK"
            self._schrijf_naar_ledger("VOLKSJURY_VRIJSPRAAK", 0, 0, f"Straf {straf_id} gewist.")
        else:
            straf["status"] = "DEFINITIEF_SCHULDIG"
            self.score = max(0, self.score - straf["punten"])
            self._schrijf_naar_ledger("STRAF_DEFINITIEF", -straf["punten"], 0, f"Straf {straf_id} toegepast.")
        return {"status": straf["status"], "actuele_score": self.score}

