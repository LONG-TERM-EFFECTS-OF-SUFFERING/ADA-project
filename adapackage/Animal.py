import random


class Animal:
	"""
	Class used to represent an Animal in the show


	Attributes
	----------

	name : str
	greatness : int

	Methods
	-------
	sort(animals)
		Returns the list of animals in ascending order

	print(animals)
		Print the animals in an understandable way
	"""

	POSSIBLE_ANIMALS: list[str] = ["Dog", "Cat", "Tapir", "Otter", "Centipede", "Dragonfly", "Capybara", "Parrot", "Alligator",
								   "Boa", "Crocodile", "Zebra", "Black panther", "Tiger", "Lion", "Elephant", "Giraffe", "Hippopotamus", "Rhinoceros",
								   "Turtle", "Lizard", "Bear", "Koala", "Penguin", "Camel", "Sheep", "Pig", "Eagle", "Owl", "Duck", "Goose", "Swan",
								   "Flamingo", "Pigeon", "Raven", "Jellyfish", "Octopus", "Shark", "Whale", "Dolphin", "Seal", "Starfish", "Butterfly",
								   "Ant", "Bee", "Spider", "Puma", "Wolf", "Fox", "Horse", "Rabbit", "Turkey", "Panda", "Kangaroo", "Squirrel", "Deer",
								   "Salmon", "Bat", "Lynx", "Mouse", "Chimpanzee", "Gorilla", "Monkey", "Cheetah", "Condor", "Crab", "Lobster", "Scorpion",
								   "Ostrich", "Sloth", "Frog", "Hamster", "Iguana", "Chameleon", "Caterpillar", "Ladybug", "Jaguar", "Dove", "Goat",
								   "Cow", "Chicken", "Goldfish", "Seahorse", "Piranha", "Squid", "Gazelle", "Hyeana", "Racoon", "Beetle", "Worm", "Donkey",
								   "Grasshopper", "Mantis", "Fly", "Beaver", "Mole", "Moth", "Termite", "Cicada", "Armadillo", "Buffalo", "Bull", "Coyote"]

	def __init__(self, name: str, greatness: int):
		"""
		Parameters
		----------
		name : str
			The name of the animal
		greatness : int
			The greatness associated with an animal
		"""

		self.name = name
		self.gretness = greatness

	def __str__(self):
		return f"{self.name}, {self.gretness}"

	def display_list(animals: list) -> str:
		return '[ ' + ' '.join(str(animal) for animal in animals) + " ]"

	def __eq__(self, other_animal: 'Animal'):
		return self.gretness == other_animal.gretness

	def __ne__(self, other_animal: 'Animal'):
		return self.gretness != other_animal.gretness

	def __lt__(self, other_animal: 'Animal'):
		return self.gretness < other_animal.gretness

	def __le__(self, other_animal: 'Animal'):
		return self.gretness <= other_animal.gretness

	def __gt__(self, other_animal: 'Animal'):
		return self.gretness > other_animal.gretness

	def __ge__(self, other_animal: 'Animal'):
		return self.gretness >= other_animal.gretness

	@staticmethod
	def generate_random_animals(n: int) -> list['Animal']:
		""" Generate a list of n random different animals

		Parameters
		----------
		n : int
			The number of animals to generate

		Returns
		-------
		list
			List of n random non-repeated animals already sorted in ascending order by greatness
		"""

		animals: list['Animal'] = []
		i = 1

		while len(animals) < n:
			animal = Animal(random.choice(Animal.POSSIBLE_ANIMALS), i)

			if animal not in animals:
				animals.append(animal)
				i += 1

		return animals
