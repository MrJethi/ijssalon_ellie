from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    totaal_btw = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal_btw} euro btw betaald dient te worden."

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.9

def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro." 

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

def hoog_en_laag(invoer_lijst):
    hoog = max(invoer_lijst)
    laag = min(invoer_lijst)
    return hoog, laag

def meervoudig(invoer_lijst):
    hoog, laag = hoog_en_laag(invoer_lijst)
    return [hoog, laag]

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
invoer_lijst2 = [10, 5, 3, 2, 1, 2, 9]

def combinatie(invoer_lijst2):
    hoog, laag = hoog_en_laag(invoer_lijst2)
    return mijn_functie_2(hoog, laag)

print(aanbieding_1("aardbei", 4, 0.1))

print(inkomsten_totaal(week_inkomsten, btw_percentage))

print(gemiddelde(mijn_lijst))

print(meervoudig(invoer_lijst))

print(combinatie(invoer_lijst2))