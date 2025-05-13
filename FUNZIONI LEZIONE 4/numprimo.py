
def primo(n:int) -> bool:

    for i in range (n-1, 1, -1):

        if n% i == 0:
            return False
    
    return True 

print(primo(7))