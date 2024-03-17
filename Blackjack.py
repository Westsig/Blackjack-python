import random

def initialiser_kortstokk():
    return [
        "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠knekt", "♠dronning", "♠konge", "♠ess",
        "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥knekt", "♥dronning", "♥konge", "♥ess",
        "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦knekt", "♦dronning", "♦konge", "♦ess",
        "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣knekt", "♣dronning", "♣konge", "♣ess"
    ]

def få_kort(kortstokk):
    kort = random.choice(kortstokk)
    kortstokk.remove(kort)
    return kort

def beregn_poeng(hånd):
    poeng = 0
    ess_teller = hånd.count("♠ess") + hånd.count("♥ess") + hånd.count("♦ess") + hånd.count("♣ess")

    for kort in hånd:
        poeng += kortverdier[kort]

    while poeng > 21 and ess_teller:
        poeng -= 10
        ess_teller -= 1

    return poeng

def vis_hånd(hånd):
    return ", ".join(hånd)
  
def score(penger):
  if penger < 100:
    print("Din score er: BIG L")
  elif penger < 1000:
    print("Din score er: Avhengig")
  elif penger < 2000:
    print("Din score er: Normal")
  elif penger < 5000:
    print("Din score er: Nice")
  elif penger < 10000:
    print("Din score er: Wow")
  elif penger < 20000:
    print("Din score er: Lucky")
  elif penger < 50000:
    print("Din score er: Verdens mester")
  elif penger < 100000:
    print("Din score er: Gambler GOD")
  else:
    print("Din score er: Error, for mye ")
    
def spill():
    penger = 1000
    innsats = 0
    while penger > 0:
        kortstokk = initialiser_kortstokk()
        spiller_hånd = [få_kort(kortstokk), få_kort(kortstokk)]
        dealer_hånd = [få_kort(kortstokk), få_kort(kortstokk)]

        innsats = plasser_innsats(penger)
        print(f"Dine kort: {vis_hånd(spiller_hånd)}")
        print(f"Dealers synlige kort: {dealer_hånd[0]}")


        while True:
            valg = input("Vil du trekke et nytt kort? (ja/nei) eller (q) for å beholde pengene og få en score: ").lower()
            if valg == "q":
              print(f"Du har {penger} penger")

              score(penger)
              penger = 0
              break

            if valg == "ja":
                spiller_hånd.append(få_kort(kortstokk))
                print(f"Dine kort: {vis_hånd(spiller_hånd)}")

                if beregn_poeng(spiller_hånd) > 21:
                    print("Du har overskredet 21 poeng. Du har tapt.")
                    penger -= innsats
                    break
            elif valg == "nei":
                while beregn_poeng(dealer_hånd) < 17:
                    dealer_hånd.append(få_kort(kortstokk))

                print(f"Dealers kort: {vis_hånd(dealer_hånd)}")
                poeng_spiller = beregn_poeng(spiller_hånd)
                poeng_dealer = beregn_poeng(dealer_hånd)

                print(f"Dine poeng: {poeng_spiller}")
                print(f"Dealers poeng: {poeng_dealer}")

                if poeng_spiller > poeng_dealer or poeng_dealer > 21:
                    print("Du har vunnet!")
                    penger += innsats * 2
                elif poeng_spiller < poeng_dealer:
                    print("Du har tapt.")
                    penger -= innsats
                else:
                    print("Uavgjort.")
                    innsats = 0

                break
            else:
                print("Ugyldig valg. Skriv 'ja' eller 'nei'.")

        if penger == 0 and valg != "q":
            print("""
            -----------------------------------------------
            Du har ingen penger igjen. Din score er: BIG L
            -----------------------------------------------
                """)
            break
        elif valg != "q":
            fortsett = input("Vil du spille igjen? (ja/nei): ").lower()
            if fortsett != "ja":
                break
        else:
            print("Takk for at du spillte")
            score(penger)
def plasser_innsats(penger):
    while True:
        try:
            innsats = int(input(f"Dine penger: {penger}. Plasser innsats: "))
            if 1 <= innsats <= penger:
                return innsats
            else:
                print("Ugyldig innsats. Vennligst velg en innsats mellom 1 og dine tilgjengelige penger.")
        except ValueError:
            print("Ugyldig innsats. Skriv inn et gyldig tall.")

# Definer kortverdier her
kortverdier = {
    "♠2": 2, "♠3": 3, "♠4": 4, "♠5": 5, "♠6": 6, "♠7": 7, "♠8": 8, "♠9": 9, "♠10": 10, "♠knekt": 10, "♠dronning": 10, "♠konge": 10, "♠ess": 11,
    "♥2": 2, "♥3": 3, "♥4": 4, "♥5": 5, "♥6": 6, "♥7": 7, "♥8": 8, "♥9": 9, "♥10": 10, "♥knekt": 10, "♥dronning": 10, "♥konge": 10, "♥ess": 11,
    "♦2": 2, "♦3": 3, "♦4": 4, "♦5": 5, "♦6": 6, "♦7": 7, "♦8": 8, "♦9": 9, "♦10": 10, "♦knekt": 10, "♦dronning": 10, "♦konge": 10, "♦ess": 11,
    "♣2": 2, "♣3": 3, "♣4": 4, "♣5": 5, "♣6": 6, "♣7": 7, "♣8": 8, "♣9": 9, "♣10": 10, "♣knekt": 10, "♣dronning": 10, "♣konge": 10, "♣ess": 11
}

# Kjør spillet
spill()