#First we define the superclass that's named PokemonClass
class PokemonClass:
	#This function name tells python to use this funtion as the INITIAL state of the object
	#If you have played pokemon you know that every pokemon has a name, a lvl, movements and exp
	#They also have stats but for keeping it simple i won't include them
	def __init__(self, hp, movement, name, lvl, exp):
		self.hp=hp
		self.movement=movement
		self.name=name
		self.lvl=lvl
		self.exp=exp
	#Additionally i added a PokemonState function, this tells us the hp, exp, movements, etc of our pokemon
	#By the way, \n it's used for skipping the line on the text, kinda like pressing enter on wordpad
	def PokemonState(self):
		print("Your pokemon has ", self.hp, "HP" "\nYour pokemon has ", self.movement, "\nYour pokemon is called ", self.name, "\nYour pokemon is level ", self.lvl,
			"\nYour pokemon has ", self.exp, " exp")


#Now i can use this class for making pokemons
#In this case I created pikachu and almacenating the class and the values on a variable
#You need to define the variables from the PokemonClass, hp, movement, name, lvl and exp
#First you need to define the hp because it's the first on the function, second define the movement, third define the name an so on
#If you don't define this it will give an error saying that PokemonClass takes at least 5 arguments (hp, movement, lvl, etc)
Pikachu=PokemonClass(100, "Thunderbolt", "Pikachu", 10, 50)
#Here i call PokemonState function with my pokemon pikachu, it will print the hp, exp, name, etc of pikachu or any pokemon that i say
Pikachu.PokemonState()