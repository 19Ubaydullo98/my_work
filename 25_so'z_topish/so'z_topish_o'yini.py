from uzwords import lotin_words
import random as r

def get_words():
    a = r.choice(lotin_words)
    return a 

def display(x,y):
    a =""
    for i in range(len(y)):
        if y[i] in x:
            a += y[i]
        else:
            a +="-"
    return a 
          
def play():
    word = get_words()
    
    print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi ?")
    for i in range(len(word)):
        print("-", end = "")
    harflar = ''
    sanoq = 0
    while True:
        sanoq += 1
        taxmin = input(f"\nHarf kriting: ")
        harflar +=taxmin
        funksiya =  display(harflar,word)
        print(funksiya)
        print(f"Siz kiritgan harflar: {harflar}")
        if word == funksiya:
            print(f"Tabriklayman! {word} so'zini {sanoq} ta urinishda topdiz")
            break
play()          

