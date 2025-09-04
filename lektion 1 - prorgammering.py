#Hej Thomas

def hejThomas():
    i = 0
    while i < 100000:
        print('Hej Thomas')
        i+=1
    
    
#hejThomas()


def gætThomasAlder():
    print('Du skal gætte Thomas alder i dette spil')
    alderen = '42'
    gæt = input('skriv dit første gæt')
    while(gæt != alderen):
        if(gæt < alderen):
            print('Dit gæt er for lavt, prøv igen')
            print('')
            gæt = input('skriv dit næste gæt')
        elif(gæt > alderen):
            print('Dit gæt er for højt, prøv igen')
            print('')
            gæt = input('skriv dit næste gæt')
    else:
        print('Tillykke du har gættet Thomas alder!')
        

#gætThomasAlder()



def antalOrd(tekst):
    antal = 0
    for tegn in tekst:
        if tegn == '':
            antal += 1
        antal += 1
    print('Der var: ' + str(antal) + ' bogstaver')
    
    
#antalOrd('Professionelt')


def eksempel():
    print('indtast antal km: ')
    antalKm = int(input())
    
    pris = antalKm*20+50
    
    print(pris)

#eksempel()

#Eksempel på at printe en liste sorteret
print(sorted([7,1,0]))
print(sorted(['Benny','Anders', 'Abe']))