from adapackage.Animal import Animal
import random


class Scene:
	"""
	Class used to represent a Scene in the show
	A scene is a list of 3 different animals
	

	Atributes
	---------
	animals : list
		The list of animals in the scene
	gratness : int
		The greatness associated with the scene (sum of greatness of all animals)

	Methods
	-------
	
	"""

	def __init__(self, animals: list[Animal]):
		"""
		Parameters
		----------
		animals : list[Animal]
			The list of animals in the scene
		"""
		self.animals = animals
		self.greatness = sum(animal.gretness for animal in animals)

	def __str__(self):
		return f"[({self.animals[0]}), ({self.animals[1]}), ({self.animals[2]}), {self.greatness}]"

	def __eq__(self, other_scene: 'Scene'):
		return self.animals == other_scene.animals

	def __ne__(self, other_scene: 'Scene'):
		return self.animals != other_scene.animals

	def __lt__(self, other_scene: 'Scene'):
		return self.greatness < other_scene.greatness

	def __le__(self, other_scene: 'Scene'):
		return self.greatness <= other_scene.greatness

	def __gt__(self, other_scene: 'Scene'):
		return self.greatness > other_scene.greatness

	def __ge__(self, other_scene: 'Scene'):
		return self.greatness >= other_scene.greatness

	def __iter__(self):
		return iter(self.animals)

	@staticmethod
	def generate_random_scene(animals: list[Animal]) -> 'Scene':
		"""
		Generate a random scene with 3 different animals

		Parameters
		----------
		animals : list[Animal]
			The list of possible animals in the show

		Returns
		-------
		Scene
			A scene with 3 different randomly selected animals
		"""

		scene: list[Animal] = []

		while len(scene) < 3:
			animal: Animal = random.choice(animals)

			if animal not in scene:
				scene.append(animal)

		return Scene(scene)
