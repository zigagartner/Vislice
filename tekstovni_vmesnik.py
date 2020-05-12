import model


def izpis_igre(igra):
    return (
        f'Pravilni del gesla: {igra.pravilni_del_gesla()}\n' +
        f'Neuspeli poskusi: {igra.nepravilni_ugibi()}\n' + 
        f'Število preostalih poskusov:{model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}\n'
    )

def izpis_zmage(igra):
    return(
        'Čestitam, uganil si geslo\n' +
        f'Uspelo ti je v {len(igra.crke)} poskusih\n'
    )

def izpis_poraza(igra):
    return (
        'Porabil si vse poskuse\n' +
        f'Geslo je {igra.geslo}\n'
    )

def zahtevaj_vnos():
    return input('Vnesi črko: ')

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        stanje = igra.ugibaj(poskus)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

pozeni_vmesnik()