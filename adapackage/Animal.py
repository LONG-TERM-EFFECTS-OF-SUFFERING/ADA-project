import random


class Animal:
	"""
	Class used to represent an Animal in the show.

	- An animal is a pair (name, greatness).

	Attributes
	----------

	name : str
	greatness : int

	Methods
	-------
	generate_random_animals(n: int) -> set[Animal]
	"""

	POSSIBLE_ANIMALS_NAMES: list[str] = [
		"Dog", "Cat", "Tapir", "Otter", "Centipede", "Dragonfly", "Capybara", "Parrot",  "Alligator",
		"Boa", "Crocodile", "Zebra", "Black panther", "Tiger", "Lion", "Elephant", "Giraffe", "Hippopotamus", "Rhinoceros",
		"Turtle", "Lizard", "Bear", "Koala", "Penguin", "Camel", "Sheep", "Pig", "Eagle", "Owl", "Duck", "Goose", "Swan",
		"Flamingo", "Pigeon", "Raven", "Jellyfish", "Octopus", "Shark", "Whale", "Dolphin", "Seal", "Starfish", "Butterfly",
		"Ant", "Bee", "Spider", "Puma", "Wolf", "Fox", "Horse", "Rabbit", "Turkey", "Panda", "Kangaroo", "Squirrel", "Deer",
		"Salmon", "Bat", "Lynx", "Mouse", "Chimpanzee", "Gorilla", "Monkey", "Cheetah", "Condor", "Crab", "Lobster", "Scorpion",
		"Ostrich", "Sloth", "Frog", "Hamster", "Iguana", "Chameleon", "Caterpillar", "Ladybug", "Jaguar", "Dove", "Goat",
		"Cow", "Chicken", "Goldfish", "Seahorse", "Piranha", "Squid", "Gazelle", "Hyeana", "Racoon", "Beetle", "Worm", "Donkey",
		"Grasshopper", "Mantis", "Fly", "Beaver", "Mole", "Moth", "Termite", "Cicada", "Armadillo", "Buffalo", "Bull", "Coyote"
		]

	def __init__(self, name: str, greatness: int):
		"""
		Parameters
		----------
		name : str
			The name of the animal.
		greatness : int
			The greatness associated with an animal.
		"""

		self.name = name
		self.greatness = greatness

	def __str__(self):
		return f"({self.name} {self.greatness})"

	def __eq__(self, other_animal: 'Animal'):
		return self.greatness == other_animal.greatness

	def __ne__(self, other_animal: 'Animal'):
		return self.greatness != other_animal.greatness

	def __hash__(self):
		return hash(self.name) + hash(self.greatness)

	def __lt__(self, other_animal: 'Animal'):
		return self.greatness < other_animal.greatness

	def __le__(self, other_animal: 'Animal'):
		return self.greatness <= other_animal.greatness

	def __gt__(self, other_animal: 'Animal'):
		return self.greatness > other_animal.greatness

	def __ge__(self, other_animal: 'Animal'):
		return self.greatness >= other_animal.greatness

	@staticmethod
	def generate_random_animals(a: int) -> list['Animal']:
		""" Generate a list of "a" random different animals.

		Parameters
		----------
		a : int
			The number of animals to generate.

		Returns
		-------
		animals : list
			list of "a" random non-repeated animals already sorted in ascending order by greatness.
		"""

		animals: list[Animal] = []
		i = 1

		if a <= len(Animal.POSSIBLE_ANIMALS_NAMES):
			while len(animals) < a:
				animal = Animal(random.choice(Animal.POSSIBLE_ANIMALS_NAMES), i)

				if animal.name not in [element.name for element in animals]:
					animals.append(animal)
					i += 1

		else:
			while len(animals) < a:
				animal: Animal = Animal("Animal" + str(i), i)
				animals.append(animal)
				i += 1

		return animals
