from adapackage.Animal import Animal
from adapackage.Algorithms import Methods
import random


class Scene:
	"""
	Class used to represent a Scene in the show.

	- A scene is a group of 3 different animals.


	Attributes
	---------
	animals : set
		The set of animals in the scene.

	sorted_animals : list
		The list of animals in the scene ordered by greatness.

	greatness : int
		The greatness associated with the scene (sum of greatness of all animals).

	Methods
	-------
	generate_random_scene(animals: list[Animal]) -> Scene

	sort_scene() -> None
	"""

	def __init__(self, animals: set[Animal]):
		"""
		Constructor for a scene.
		- Uses a set as the unsorted data structure for the animals.
		- Uses a list as the sorted data structure for the animals.

		Parameters
		----------
		animals : set[Animal]
			The set of animals in the scene.
		"""
		self.animals: set[Animal] = animals
		self.sorted_animals: list[Animal] = None
		self.sort_scene()
		self.greatness: int = Methods.sum([animal.greatness for animal in animals])

	def __str__(self):
		string: str = ""

		# When animals have not been sorted yet
		if self.sorted_animals is None:
			string += (
				"{ " + ", ".join(str(animal) for animal in self.animals) +
				", " + str(self.greatness) + " }" )

		# When animals were sorted
		else:
			string += (
				"[ " + ", ".join(str(animal) for animal in self.sorted_animals) +
				", " + str(self.greatness) + " ]" )

		return string

	def __eq__(self, other_scene: 'Scene'):
		return self.animals == other_scene.animals

	def __ne__(self, other_scene: 'Scene'):
		return self.animals != other_scene.animals

	def __hash__(self):
		return hash(frozenset(self.animals))

	def __iter__(self):
		return iter(self.animals)

	def __lt__(self, other_scene: 'Scene'):
		return self.greatness < other_scene.greatness

	def __le__(self, other_scene: 'Scene'):
		""""
		If both scenes have the same greatness,
		then make pairs of animals based on the sorted list of animals in descending order
		and look for the first pair of animals that is different.

		Returns
		-------
		bool
			The result of the comparison of the first different pair of animals.
		"""
		# If both scenes have the same greatness, then check for the tiebreaker
		if self.greatness == other_scene.greatness:

			# Reverse the list of animals to make pairs in descending order of greatness
			for this_animal, other_animal in Methods.zip(Methods.reverse(self.sorted_animals), Methods.reverse(other_scene.sorted_animals)):

				if this_animal != other_animal and this_animal < other_animal:
					return True

				elif this_animal != other_animal and this_animal > other_animal:
					return False

		else:
			return self.greatness < other_scene.greatness

	def __gt__(self, other_scene: 'Scene'):
		return self.greatness > other_scene.greatness

	def __ge__(self, other_scene: 'Scene'):
		"""
		If both scenes have the same greatness,
		then make pairs of animals based on the sorted list of animals in descending order
		and look for the first pair that is different.

		Returns
		-------
		bool
			The result of the comparison of the first different pair of animals.
		"""
		# If both scenes have the same greatness then check for the tiebreaker
		if self.greatness == other_scene.greatness:

			# Reverse the list of animals to make pairs in descending order of greatness
			for this_animal, other_animal in Methods.zip(Methods.reverse(self.sorted_animals), Methods.reverse(other_scene.sorted_animals)):
				if this_animal != other_animal and this_animal > other_animal:
					return True

				elif this_animal != other_animal and this_animal < other_animal:
					return False

		else:
			return self.greatness > other_scene.greatness

	def transform_to_list(self):
		[animal1, animal2, animal3] = self.sorted_animals

		return [animal1.greatness, animal2.greatness, animal3.greatness, self.greatness]

	@staticmethod
	def generate_random_scene(animals: list[Animal]) -> 'Scene':
		"""
		Generate a random scene with 3 different animals.

		Parameters
		----------
		animals : list[Animal]
			The list of possible animals in the show.

		Returns
		-------
		Scene
			A scene with 3 different randomly selected animals.
		"""

		scene: set[Animal] = set()

		while len(scene) < 3:
			animal: Animal = random.choice(animals)

			if animal not in scene:
				scene.add(animal)

		return Scene(scene)

	def sort_scene(self) -> None:
		"""
		Updates the list sorted_animals with the animals in the scene sorted in ascending order by greatness.
		Performs 6 comparisons at most, so its complexity is O(1).

		Returns
		-------
		None
			It only updates the sorted_animals attribute.
		"""

		(animal1, animal2, animal3) = self.animals

		if (
			animal1 < animal2 and
			animal2 < animal3
		):
			self.sorted_animals = [animal1, animal2, animal3]

		elif(
			animal1 < animal2 and
			animal2 > animal3 and
			animal1 < animal3
		):
			self.sorted_animals = [animal1, animal3, animal2]

		elif (
			animal1 < animal2 and
			animal2 > animal3 and
			animal1 > animal3
		):
			self.sorted_animals = [animal3, animal1, animal2]

		elif (
			animal1 > animal2 and
			animal1 < animal3
		):
			self.sorted_animals = [animal2, animal1, animal3]

		elif (
			animal1 > animal2 and
			animal1 > animal3 and
			animal2 < animal3
		):
			self.sorted_animals = [animal2, animal3, animal1]

		else:
			self.sorted_animals = [animal3, animal2, animal1]
