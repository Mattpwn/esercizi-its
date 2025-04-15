
# ESERCIZIO NUMERO 8

# Se la stringa è vuota non ci sono vocali nella stringa quindi --> 0

# Se la stringa non è vuota ed ad esempio è una stringa "Ciao"     N.B devo calcolare il primo carattere della stringa e poi andare avanti

# Considero il primo caratterre C = vocale --> NO ----- quindi ho zero vocali + quanteVocaliNellaStringa ("iao")

# Considero il primo carattere della stringa "iao"  i = vocale ---> SI ----- quindi ho una vocale + quanteVocaliNellaStringa ("ao")

# Considero il rpimo carattere della stringa "ao"  a = vocale ---> SI ----- quindi ho una vocale + quanteVocaliNellaStringa ("o")

# Considero il primo carattere della stringa "o"  o = vocale ---> SI ------ quindi ho una vocale + quanteVocaliNellaStringa ("")

def vowelsCounter( s:str) -> str:

# if s is an empty string return 0
    
    if not s:
        return 0
    
    # if the first char of the string is a vowel, we count a vowel, so we add 1 to the vowelCounter

    if s[0].lower() in ["a", "e", "i", "o", "u"]:

        return 1 + vowelsCounter(s[1:])
    
    # if the first char is not a vowel chech out for teh next char in the string

    else:

        return 0 + vowelsCounter(s[1:])
    
print(f"La stringa \"\" contiene {vowelsCounter("")} vocali")

print(f"La stringa \"CIAO\" contiene {vowelsCounter("CIAO")} vocali")
    
print(f"La stringa \"Pappagallo\" contiene {vowelsCounter("Pappagallo")} vocali")

print(f"La stringa \"Ho visto lei che bacia lui\" contiene {vowelsCounter("Ho visto lei che bacia lui")} vocali")