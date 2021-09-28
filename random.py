helyes_jelszo = "alma"
jelszo = input("Add meg a jelszót: ")
helyes_e = False
probalkozasok_szama = 3

while jelszo != helyes_jelszo:
    probalkozasok_szama -= 1
    helyes_e = False
    print("Helytelen jelszó!")
    jelszo = input("Add meg a jelszót: ")

    if probalkozasok_szama <= 1:
        print("Hát ezt bebuktad tesó!")
        exit()

if jelszo == helyes_jelszo:
    helyes_e = True
    print("szia")

    
