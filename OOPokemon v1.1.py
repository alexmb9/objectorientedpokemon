###Python OOP for Pokemon Battle

###Imported modules

from random import *
import time

###Variable for turn counter

n=0

class Pokemon:

###Blueprint for a pokemon

    def __init__(self, name, pokemontype, hp, move1, move2, move3, move4):
        self.name = name
        self.pokemontype = pokemontype
        self.hp = hp
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

###Movesets, move1, move2, move3, move4

    def usemove1(self):
        if pokemonlist[n] == pokemon1:
            print(pokemon2.name,'uses',pokemon2.move1)
            time.sleep(3)
            pokemonlist[n].hp = pokemonlist[n].hp -20
            print(pokemonlist[n].name+"'s hp is:",pokemonlist[n].hp,"/ 100")
            time.sleep(1)
        else:
            print(pokemon1.name,'uses',pokemon1.move1)
            time.sleep(3)
            pokemonlist[n].hp = pokemonlist[n].hp -20
            print(pokemonlist[n].name+"'s hp is:",pokemonlist[n].hp,"/ 100")
            time.sleep(1)

    def usemove2(self):
        if pokemonlist[n] == pokemon1:
            print(pokemon2.name,'uses',pokemon2.move2)
            time.sleep(3)
            pokemonlist[n].hp = pokemonlist[n].hp -20
            print(pokemonlist[n].name+"'s hp is:",pokemonlist[n].hp,"/ 100")
            time.sleep(1)
        else:
            print(pokemon1.name,'uses',pokemon1.move2)
            time.sleep(3)
            pokemonlist[n].hp = pokemonlist[n].hp -20
            print(pokemonlist[n].name+"'s hp is:",pokemonlist[n].hp,"/ 100")
            time.sleep(1)

    def usemove3(self):
        if pokemonlist[n] == pokemon1:
            print(pokemon2.name,'uses',pokemon2.move3)
            time.sleep(3)
            pokemonlist[n].hp = pokemonlist[n].hp -20
            print(pokemonlist[n].name+"'s hp is:",pokemonlist[n].hp,"/ 100")
            time.sleep(1)
        else:
            print(pokemon1.name,'uses',pokemon1.move3)
            time.sleep(3)
            pokemonlist[n].hp = pokemonlist[n].hp -20
            print(pokemonlist[n].name+"'s hp is:",pokemonlist[n].hp,"/ 100")
            time.sleep(1)

    def usemove4(self):
        if pokemonlist[n] == pokemon1:
            print(pokemon2.name,'uses',pokemon2.move4)
            time.sleep(3)
            pokemonlist[n].hp = pokemonlist[n].hp -20
            print(pokemonlist[n].name+"'s hp is:",pokemonlist[n].hp,"/ 100")
            time.sleep(1)
        else:
            print(pokemon1.name,'uses',pokemon1.move4)
            time.sleep(3)
            pokemonlist[n].hp = pokemonlist[n].hp -20
            print(pokemonlist[n].name+"'s hp is:",pokemonlist[n].hp,"/ 100")
            time.sleep(1)

    def miss(self):
        if pokemonlist[n] == pokemon1:
            print(pokemon2.name,'missed!')
            time.sleep(3)
        else:
            print(pokemon1.name,'missed!')
            time.sleep(1)

### Battle algorithm

    def randombattle(self):
        while ((pokemon1.hp and pokemon2.hp) > 0):
            global n
            x = randint(0, 4)
            if x==0:
                pokemonlist[n].usemove1()
            elif x==1:
                pokemonlist[n].usemove2()
            elif x==2:
                pokemonlist[n].usemove3()
            elif x==3:
                pokemonlist[n].usemove4()
            else:
                pokemonlist[n].miss()
            n=n+1
            n=n%2

            if pokemon1.hp == 0:
                print(pokemon1.name,"has fainted.")
                time.sleep(2)
                print(pokemon2.name, "wins!")
            if pokemon2.hp == 0:
                print(pokemon2.name,"has fainted.")
                time.sleep(2)
                print(pokemon1.name,"wins.")
            
        
          

###Pokemon and list definitions

pokemon1 = Pokemon('Pikachu', 'Electric', 100, 'Thunderbolt', 'Agility', 'Thunder', 'Leer')
pokemon2 = Pokemon('Charmander', 'Fire', 100, 'Flamethrower', 'Ember', 'Tackle', 'Smokescreen')

pokemonlist = []
pokemonlist.append(pokemon1)
pokemonlist.append(pokemon2)

pokemon1.randombattle()



        

    
        
