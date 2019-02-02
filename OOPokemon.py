#Python OOP for Pokemon Battle
from random import *

n=0

class Pokemon:

    def __init__(self, name, pokemontype, hp, move1, move2, move3, move4):
        self.name = name
        self.pokemontype = pokemontype
        self.hp = hp
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

    def usemove1(self):
        if pokemonlist[n] == pokemon1:
            print(pokemon2.move1)
        else:
            print(pokemon1.move1)
        pokemonlist[n].hp = pokemonlist[n].hp -20
        print(pokemonlist[n].name, "hp is:",pokemonlist[n].hp)
        #pokemon2.hp = pokemon2.hp - 20
        #print(self.move1)
        #print(pokemon2.hp)

    def usemove2(self):
        if pokemonlist[n] == pokemon1:
            print(pokemon2.move2)
        else:
            print(pokemon1.move2)
        pokemonlist[n].hp = pokemonlist[n].hp -20
        print(pokemonlist[n].name, "hp is:",pokemonlist[n].hp)

    def usemove3(self):
        if pokemonlist[n] == pokemon1:
            print(pokemon2.move2)
        else:
            print(pokemon1.move2)
        pokemonlist[n].hp = pokemonlist[n].hp -20
        print(pokemonlist[n].name, "hp is:",pokemonlist[n].hp)

    def usemove4(self):
        if pokemonlist[n] == pokemon1:
            print(pokemon2.move2)
        else:
            print(pokemon1.move2)
        pokemonlist[n].hp = pokemonlist[n].hp -20
        print(pokemonlist[n].name, "hp is:",pokemonlist[n].hp)

    def battle(self):
        pass
        
pokemon1 = Pokemon('Pikachu', 'Electric', 100, 'Thunderbolt', 'Agility', 'Thunder', 'Leer')
pokemon2 = Pokemon('Charmander', 'Fire', 100, 'Flamethrower', 'Ember', 'Tackle', 'Smokescreen')

pokemonlist = []
pokemonlist.append(pokemon1)
pokemonlist.append(pokemon2)

pokemon1.usemove1()



        

    
        
