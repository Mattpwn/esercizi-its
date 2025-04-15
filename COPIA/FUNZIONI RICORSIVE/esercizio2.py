
# ESERCIZIO NUMERO 2

# Supponiamo m = 1000.00 euro ---- t = 3 mesi

'''
 t = 3, significa che sono passati tre mesi, la somma disponibile sul conto sarà 1.005 * somma dopo due mesi

 t = 2, significa che sono passati due mesi, la somma disponibile sul conto sarà 1.005 * somma dopo un mese

 t = 1, significa che è passato un mese, la somma disponibile sul conto sarà 1.005 * la somma depositata all'inizio

 t = 0, siginifica che non è ancora passato un mese, la somma disponibile sarà quella depositata all'inizio ----> m = 1000.00 euro
'''

def compoundInterest(m: float, t: int) -> int:

    # if m is negative
    if m < 0.00:

        print("Computing compound interest on a negative\ null balance is not possible ")
        return 0.00
    
    #if m is 0, the compound interest is 0
    elif m == 0.00:
        return 0.00
    
    # m must be > 0
    else:
        # if t is negative or 0 that means that no month has passed yet and the balance is still m

        if t <= 0:

            return round(m,2)
        # otherwise compute the compound interest recursively

        else:

            return round(1.005 * compoundInterest(m, t-1), 2)
        
print(f"After 3 months balance is : {compoundInterest(1000.00, 3)}")
