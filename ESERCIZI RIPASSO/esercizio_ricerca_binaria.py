
# RICERCA BINARIA

def RicercaBinaria(lista:list,target:int)->bool:
    lista1 = sorted(lista)
    print(lista1)
    i = 0
    v = len(lista1)-1
    while i <= v:
        m = (i+v) //2
        if lista1[m] == target:
            return True
        elif lista1[m] < target:
            i = m +1
        else:
            v = m -1
    return False

# fatto in classe con il prof      j = UPPER BOUND        i = LOWER BOUND

def bin_search (x,y):

    i, j = 0, len(x)
    mid = len(x) // 2
    
    if x[mid] == y:

        print("numero trovato")
    
    elif x[mid] > y:

        j = mid - 1
        bin_search (x[i:j + 1], y)

    else:

        i = mid + 1
        bin_search (x[i:j], y)