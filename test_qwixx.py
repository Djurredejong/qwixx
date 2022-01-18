from qwixx import deze_is_nog_vrij, kaartje_maken

def test_begin():
    kaart = kaartje_maken()
    print(deze_is_nog_vrij('rood', 5, kaart) == True)

def test_vakje_al_bezet():
    kaart = kaartje_maken()
    kaart['rood'][5] = 'doorgestreept'
    try:
        deze_is_nog_vrij('rood', 5, kaart)
        print(False)
    except ValueError as error:
        if type(error) == ValueError:# and error.__str__() == ('In deze kleur heb je al dit (of een later) getal doorgestreept:', 'rood', 5):
            print(True)
        else:
            print(False)

def test_vakje_verderop_al_bezet():
    kaart = kaartje_maken()
    kaart['rood'][7] = 'doorgestreept'
    try:
        deze_is_nog_vrij('rood', 5, kaart)
        print(False)
    except ValueError as error:
        if type(error) == ValueError:# and error.__str__() == ('In deze kleur heb je al dit (of een later) getal doorgestreept:', 'rood', 5):
            print(True)
        else:
            print(False)

def test_begin_blauw():
    kaart = kaartje_maken()
    print(deze_is_nog_vrij('rood', 5, kaart) == True)

def test_vakje_al_bezet_blauw():
    kaart = kaartje_maken()
    kaart['blauw'][5] = 'doorgestreept'
    try:
        deze_is_nog_vrij('blauw', 5, kaart)
        print(False)
    except ValueError as error:
        if type(error) == ValueError:# and error.__str__() == ('In deze kleur heb je al dit (of een later) getal doorgestreept:', 'rood', 5):
            print(True)
        else:
            print(False)

def test_vakje_verderop_al_bezet_blauw():
    kaart = kaartje_maken()
    kaart['blauw'][5] = 'doorgestreept'
    try:
        deze_is_nog_vrij('blauw', 5, kaart)
        print(False)
    except ValueError as error:
        if type(error) == ValueError:# and error.__str__() == ('In deze kleur heb je al dit (of een later) getal doorgestreept:', 'rood', 5):
            print(True)
        else:
            print(False)

def test_dobbelsteen_weghalen():

if __name__ in "__main__":
    test_begin()
    test_vakje_al_bezet()
    test_vakje_verderop_al_bezet()
    test_begin_blauw()
    test_vakje_al_bezet_blauw()
    test_vakje_verderop_al_bezet_blauw()

