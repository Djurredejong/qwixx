import random
import colorama
import os

def echte_kleur(kleur, getal):
    kleuren = ['rood','geel','groen','blauw']
    getallen = ['2','3','4','5','6','7','8','9','10','11','12',]
    if kleur not in kleuren or getal not in getallen:
        raise ValueError("Je hebt een niet bestaande kleur of getal gekozen:", kleur, getal)

def deze_is_nog_vrij(kleur, getal, kaartje):
    if kleur in ['rood', 'geel']:
        if all([kaartje[kleur][i] == 'leeg' for i in range(getal,13)]):
            return True
    elif kleur in ['blauw', 'groen']:
        if all([kaartje[kleur][i] == 'leeg' for i in range(getal,1, -1)]):
            return True
    raise ValueError("In deze kleur heb je al dit (of een later) getal doorgestreept:", kleur, getal)

def dit_is_gegooid(kleur, getal, dobbelstenen):
    # dobbelstenen = {'rood': 3, 'blauw': 6, 'geel': 1, 'groen': 4, 'wit1': 4, 'wit2': 5}
    # kleur: rood, getal: 8
    # ro: 3, bl: 6, ge: 1, gr: 4, w1: 4, w2: 5
    if (dobbelstenen['wit1'] + dobbelstenen['wit2'] == getal or
      dobbelstenen[kleur] + dobbelstenen['wit1'] == getal or
      dobbelstenen[kleur] + dobbelstenen['wit2'] == getal):
        pass
    else:
        raise ValueError("Je kunt niet " + kleur + '-' + str(getal) + " maken met de dobbelstenen.")

def kleur_afsluiten(kleur, getal):
    print('KLEUR AFSLUITEN FUNCTIE', kleur, getal, type(getal))
    print((kleur in ['rood', 'geel'] and getal == 12))
    print((kleur in ['blauw', 'groen'] and getal == 2))
    if (kleur in ['rood', 'geel'] and getal == 12) or (kleur in ['blauw', 'groen'] and getal == 2):
        return True
    return False

def kaartje_printen(kaartje, afgesloten, passen):
    print("Dit staat op je kaartje:")
    print(colorama.Fore.RED)
    kleuren ={'rood': '', 'geel': '', 'groen': '', 'blauw': ''}
    kleur_afgesloten ={'rood': '', 'geel': '', 'groen': '', 'blauw': ''}
    for kleur in kleuren.keys():
        for getal in kaartje[kleur]:
            if kaartje[kleur][getal] == 'leeg':
                kleuren[kleur] += ' ' + str(getal)
            else:
                if getal in [10,11,12]:
                    kleuren[kleur] += ' ' + '\u0336' + str(getal)[0] + '\u0336' + str(getal)[1]
                else:
                    kleuren[kleur] += ' ' + '\u0336' + str(getal)
        if kleur in afgesloten:
            kleur_afgesloten[kleur] = ' X '

    print(colorama.Fore.RED + kleuren['rood'] + kleur_afgesloten['rood'])
    print(colorama.Fore.YELLOW + kleuren['geel'] + kleur_afgesloten['geel'])
    print(colorama.Fore.GREEN + kleuren['groen'] + kleur_afgesloten['groen'])
    print(colorama.Fore.BLUE + kleuren['blauw'] + kleur_afgesloten['blauw'])
    print(colorama.Fore.LIGHTBLACK_EX + "Je hebt " + str(passen) + " keer gepast.")
    print(colorama.Style.RESET_ALL)

def dobbelen():
    dobbelstenen = {'rood': 0, 'blauw': 0, 'geel': 0, 'groen': 0, 'wit1': 0, 'wit2': 0}
    for kleur in dobbelstenen.keys():
        dobbelstenen[kleur] = random.randint(1,6)

    print('Dit heb je gedobbeld:')
    print(colorama.Fore.WHITE + "Wit 1:", dobbelstenen['wit1'])
    print(colorama.Fore.WHITE + "Wit 2:", dobbelstenen['wit2'])
    print(colorama.Fore.RED + "Rood:", dobbelstenen['rood'])
    print(colorama.Fore.YELLOW + "Geel:", dobbelstenen['geel'])
    print(colorama.Fore.GREEN + "Groen:", dobbelstenen['groen'])
    print(colorama.Fore.BLUE + "Blauw:", dobbelstenen['blauw'])
    print(colorama.Style.RESET_ALL)

    return dobbelstenen

def einde_spel(kaart, afgesloten, passen):
    print('Het spel is afgelopen. Goed gespeeld!')
    score_lijst = {0:0,1:1,2:3,3:6,4:10,5:15,6:21,7:28,8:36,9:45,10:55,11:66,12:78}
    score = {}
    for kleur in kaart.keys():
        kruisjes = list(kaart[kleur].values()).count('doorgestreept')
        if kleur in afgesloten:
            kruisjes += 1
        score[kleur] = score_lijst[kruisjes]

    rood = colorama.Fore.RED + str(score['rood'])
    geel = colorama.Fore.YELLOW + str(score['geel'])
    groen = colorama.Fore.GREEN + str(score['groen'])
    blauw = colorama.Fore.BLUE + str(score['blauw'])
    straf = colorama.Fore.LIGHTBLACK_EX + str(passen * 5)
    totaal = colorama.Fore.WHITE + str(sum(score.values()) - passen * 5)
    plus = colorama.Fore.WHITE + ' + '
    minus = colorama.Fore.WHITE + ' - '
    isje = colorama.Fore.WHITE + ' = '

    print('Je score is: ' + rood + plus + geel + plus + groen + plus + blauw + minus + straf + isje + totaal )

def kaartje_maken():
    kaartje = {}
    for kleur in ['rood','geel', 'groen','blauw']:
        kaartje[kleur] = {}
        getallen = [2,3,4,5,6,7,8,9,10,11,12]
        if kleur in ['groen', 'blauw']:
            getallen.reverse()
        for getal in getallen:
            kaartje[kleur][getal] = 'leeg'
    return kaartje

if __name__ in "__main__":
    # Hier begint het echte spel
    # Eerst gaan we een welkomst boodschap printen
    os.system('clear')
    print('-' * 43)
    print('---   W E L K O M   B I J   Q W I X X  ---')
    print('---      gemaakt door Emma & Djurre    ---')
    print('-' * 43)

    # Hier gaan we het kaartje maken
    kaart = kaartje_maken()
    afgesloten = []
    passen = 0

    # Nu beginnen we met spelen
    spelen = 'ja'
    while spelen == 'ja':
        kaartje_printen(kaart, afgesloten, passen)
        if len(afgesloten) == 2 or passen == 4:
            spelen == 'nee'
            einde_spel(kaart, afgesloten, passen)
            break

        dobbelstenen = dobbelen()

        print('Om een getal door te strepen, type <kleur>-<getal> (bijvoorbeeld: "rood-9")')
        print('Om te passen, type "Pas" (dit geeft strafpunten!)')
        print('Om te stoppen, type "Stop".')
        print('Type een opdracht, gevolgd door Enter:')
        wacht_op_opdracht = True
        while wacht_op_opdracht:
            getypt = input()
            if getypt.lower() == 'stop' or getypt.lower() == 's':
                spelen = 'stop'
                break
            if getypt.lower() == 'pas' or getypt.lower() == 'p':
                passen = passen + 1
                break
            try:
                kleur_getypt,getal_getypt = getypt.lower().split('-')
                echte_kleur(kleur_getypt, getal_getypt)
                dit_is_gegooid(kleur_getypt, int(getal_getypt), dobbelstenen)
                deze_is_nog_vrij(kleur_getypt, int(getal_getypt), kaart)
                for kleur in kaart:
                    for getal in kaart[kleur]:
                        if kleur == kleur_getypt and str(getal) == getal_getypt:
                            kaart[kleur][getal] = 'doorgestreept'
                            if kleur_afsluiten(kleur, getal):
                                afgesloten.append(kleur)
                            wacht_op_opdracht = False
            except ValueError as fout:
                print("Er ging iets niet goed:", fout)
                print('Type een nieuwe opdracht, gevolgd door Enter:')
            except:
                print('fout!')
                print('Type een nieuwe opdracht, gevolgd door Enter:')

        os.system('clear')
