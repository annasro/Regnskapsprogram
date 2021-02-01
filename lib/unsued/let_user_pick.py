
def LetUserPick(options):
    print("Velg: ")
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,element))
    print("{}) Annet/Ny elev".format(idx+2))
    i = input("Skriv tall: ")

    try:
        if i >= idx + 2:
            i = input("Navn: ")
        if 0 < int(i) <= len(options):
            return options[i]
    except:
        pass
    return None
