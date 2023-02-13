import numpy as np
import math

p=0
zob = 0
c = 0
kz = 0
kb = 0
zb = 0

hoh = input(str("Bevat jou oplossing meer H+ atomen dan OH- atomen? (antwoord met 'ja', 'nee' of 'geen idee') "))
print("")

i = 0

if hoh == "ja":
    i = 1
    p=1    
elif hoh == "nee":
    i = 2
    p=2
elif hoh == "geen idee":
    
    v1 = input(str("Bekijk p.46 in de cursus en ga na als u stof een zuur of een base is. Is het een zuur of een base? " ))
    if "zuur" in v1:
        i=1 
        
    elif "base" in v1:
        i=2
        
    else: 
        print("")
        print("")
        print("")
        print("U hebt niet op de vraag geantwoord. Gebruik het woord 'base' of 'zuur' in uw antwoord.")
        i = 90
else:
    print("Je hebt niet op de vraag geantwoord.")
    i = 404
    
    
    
    
while i == 404:
    hoh = input(str("Bevat jou oplossing meer H+ atomen dan OH- atomen? (antwoord met 'ja', 'nee' of 'geen idee') "))
    print("")

    i = 0

    if hoh == "ja":
        i = 1
            
    elif hoh == "nee":
        i = 2
        
    elif hoh == "geen idee":
        
        v1 = input(str("Bekijk p.46 in de cursus en ga na als u stof een zuur of een base is. Is het een zuur of een base? " ))
        if "zuur" in v1:
            i=1 
            
        elif "base" in v1:
            i=2
            
        else: 
            print("")
            print("")
            print("")
            print("U hebt niet op de vraag geantwoord. Gebruik het woord 'base' of 'zuur' in uw antwoord.")
            i = 90
    else:
        print("")
        print("")
        print("")
        print("Je hebt niet op de vraag geantwoord.")
        i = 404



while i == 90:
    i=0
    
    print("")
    v1 = input(str("Bekijk p.46 in de cursus en ga na als u stof een zuur of een base is. Is het een zuur of een base? " ))
    if "zuur" in v1:
        i=1 
        p = 1
    elif "base" in v1:
        i=2
        p = 2
    else: 
        print("")
        print("")
        print("")
        print("U hebt niet op de vraag geantwoord. Gebruik het woord 'base' of 'zuur' in uw antwoord.")
        i = 90

while p == 1:
    p=0
    if i == 1:
        print("")
        expz = input("U hebt te maken met een zuur, wat is de exponent van 10 van de zuurconstante? De tabel kan geraadpleegd worden op p.46 in de cursus. ")
        mexpz = -1*expz
        
      
        
        
        if int(expz) > 1:
                    print("")
                    print("U hebt te maken met een sterk zuur. De pH van sterke zuren kan je berekenen met de formule: pH = -log(czuur) ")
                    
                    zb = 1
        elif int(expz) > -14:
                    print("")
                    print("U hebt te maken met een zwak zuur. De pH van zwakke zuren kan je berekenen met de formule: pH = ½(pKz - log(czuur)) ")
                    
                    zb = 2
        elif int(expz) < -14:
                    print("")
                    print("U hebt te maken met een uiterst zwak zuur, van uiterst zwakke zuren kunnen we geen pH berekenen.")
while p == 2:
    p=0   
    if i == 2:
        print("")
        expb = input("U hebt te maken met een base, wat is de exponent van 10 van de baseconstante? De tabel kan geraadpleegd worden op p.46 in de cursus. ")
        
        if expb.isnumeric() == False:
            
            print("")
            print("U hebt niet correct op de vraag geantwoord, gelieve nog eens te proberen. ")            
            p=2
        
        elif int(expb) > 1:
                    print("")
                    print("U hebt te maken met een sterke base. De pH van sterke basen kan je berekenen met de formule: pH = 14 + log(cbase) ")
                
                    zb = 3
        elif int(expb) > -14:
                    print("")
                    print("U hebt te maken met een zwakke base. De pH van zwakke basen kan je berekenen met de formule: pH = 14 - ½(pKb – log(cbase)) ")
                   
                    zb = 4
        elif int(expb) < -14:
                    print("")
                    print("U hebt te maken met een uiterst zwakke base, van uiterst zwakke basen kunnen we geen pH berekenen.")
        

p=8

while p== 8:
    
    print("")                
    ber = input(str("Wilt u dat ik de pH voor u bereken? (antwoord alleen met 'ja' of 'nee'.) "))
    
    p=0
    if ber == "ja":
        
        if zb == 1:
            c = input("Geef de concentratie van het sterk zuur in mol/L: ")
            phsz = -1 * np.log10(float(c))
            print("De pH is: " + str(phsz) + ".")
            
        if zb == 2:
            c = input("Geef de concentratie van het zwakke zuur in mol/L: ")
            kz = input("Geef de zuurconstante in zonder de 10 en de exponent van 10: ")
            pkz = -1 * np.log10(float(kz) * (10**int(expz)))
            phzz = 0.5 * (pkz - np.log10(float(c)))
            print("De pH is: " + str(phzz) + ".")
            
        if zb == 3:
            c = input("Geef de concentratie van de sterke base in mol/L: ")
            phsb = 14 + np.log10(float(c))
            print("De pH is: " + str(phsb) + ".")
            
        if zb == 4:
            c = input("Geef de concentratie van de zwakke base in mol/L: ")
            kb = input("Geef de basenconstante in zonder de 10 en de exponent van 10: ")
            pkb = -1 * np.log10(float(kb) * (10**int(expb)))
            phzb = 14 - (0.5*(pkb - np.log10(float(c))))
            print("De pH is: " + str(phzb) + ".")
            
    elif ber == "nee":  
        print("")
        print("Ok, bedankt om mij te gebruiken, om nog eens ;)")
        
    else:
        print("Gelieve te antwoorden met 'ja' of 'nee'.")
        p=8
        
    
    



                
                