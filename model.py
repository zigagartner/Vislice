import random

STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = 'Z'

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'


ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        self.crke = [] if crke is None else [crka.upper() for crka in crke]
    
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]
   
    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return set(self.geslo) == set(self.pravilne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        s = ''
        for crka in self.geslo:
            if crka in self.crke:
                s += crka
            else:
                s += '_'
        return s
        
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.upper()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(ugibana_crka)
            if ugibana_crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA


bazen_besed = []
for beseda in open('besede.txt', encoding='utf-8'):
    bazen_besed.append(beseda.strip().upper())

def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda)


class Vislice:
    def __init__(self):
        #Slovar, ki ID-ju priredi igro.
        self.igre = {}    # Int -> (Igra, stanje)
        
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        # dobimo svež ID, naredimo novo igro, vse to shranimo v self.igre
        nov_id = self.prost_id_igre()
        sveza_igra = nova_igra()
        self.igre[nov_id] = sveza_igra, ZACETEK
        #Vrnemo nov ID.
        return nov_id

    def ugibaj(self, id_igre, crka):
        #Dobimo staro igro ven
        trenutna_igra, _ = self.igre[id_igre]
        #Ugibamo_crko
        novo_stanje = trenutna_igra.ugibaj(crka)
        #Zapišemo posodobljeno stanje in igro nazaj v "BAZO"
        self.igre[id_igre] = (trenutna_igra, novo_stanje)



