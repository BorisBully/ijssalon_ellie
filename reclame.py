from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    korting_prijs = prijs - (prijs * korting)
    return f"Vaandag in de aanbieding: emmertje ijs 1 (liter) in de smaak {smaak}, van {prijs} euro voor {korting_prijs} euro."
     


print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * btw
    return f"Het totaal voor alle inkomst van deze week is {totaal_inkomsten} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
     
    
inkomsten_list = [220, 430, 125, 160, 205, 90, 345]
btw_tarief = 0.09
resultaat = inkomsten_totaal(inkomsten_list, btw_tarief)

print(resultaat)

def laag_hoog(mijn_list):
    laagtse = min(mijn_list)
    hoogtse = max(mijn_list)
    return [laagtse, hoogtse]
inkomsten_list = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_hoog(inkomsten_list)

print(resultaat)

def gemiddelde(mijn_list):
    totaal = sum(mijn_list)
    gemiddelde = totaal / len(mijn_list)
    return  f"De gemiddelde inkomsten in deze week {totaal} euro."
    
inkomsten_list = [220, 430, 125, 160, 205, 90, 345]
resultaat = gemiddelde(inkomsten_list)

print(resultaat)

def laag_en_hoog(invoer_lijst):
    hoogste = max(invoer_lijst)
    laagste = min(invoer_lijst)
    return [hoogste, laagste]

def meervoedig(invoer_lijst):
    if len(invoer_lijst) < 5 or len(invoer_lijst) > 10:
         raise ValueError("Input list must have between 5 and 10 elements.")
    return laag_en_hoog(invoer_lijst)

nums = [10,5,3,2,1,2,9]
resultaat = meervoedig(nums)

print(resultaat)


def combinatie(invoer_list_2):
    korte_list = laag_en_hoog(invoer_list_2)
    uitvoer = mijn_functie_2(korte_list[0], korte_list[1])
    return uitvoer

print(combinatie)