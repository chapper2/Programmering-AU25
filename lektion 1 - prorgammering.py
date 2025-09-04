#Hej Thomas

def hejThomas():
    i = 0
    while i < 100000:
        print('Hej Thomas')
        i+=1
    
    
hejThomas()


def gætThomasAlder():
    print('Du skal gætte Thomas alder i dette spil')
    alderen = '42'
    gæt = input('skriv dit første gæt')
    while(gæt != alderen):
        if(gæt < alderen):
            print('Dit gæt er for lavt, prøv igen')
            gæt = input('skriv dit næste gæt')
        elif(gæt > alderen):
            print('Dit gæt er for højt, prøv igen')
            gæt = input('skriv dit næste gæt')
    else:
        print('Tillykke du har gættet Thomas alder!')