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

	def __init__(self, name : str, greatness : int):
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

	def sort(animals : list, n : int):
		"""Sort the animals in ascending order.


		Parameters
		----------
		animals : list
			The list of all animals in the show

		n: int
			The number of animals in the animals list

		Returns
		-------
		list
			The list of animals in ascending order
		"""

		# Resulting list inicialization
		A = [None for index in range(n)]

		for index in range(n):
			A[animals[index].gretness - 1] = animals[index]

		return A

	def display_list(animals : list):
		print('\n'.join(str(animal) for animal in animals))

	def __str__(self):
		return f"{self.name}, {self.gretness}"



animals = [
	Animal("Ciempies", 1),
	Animal("Libelula", 2),
	Animal("Gato", 3),
	Animal("Perro", 4),
	Animal("Tapir", 5),
	Animal("Nutria", 6)
]


def problem_solver(animals : list, m : int, k : int):
	n = len(animals)
	sorted_list = Animal.sort(animals, n)
	open_scenes = (m - 1) * k

	return sorted_list


if __name__ == "__main__":
	Animal.display_list(problem_solver(animals, 1, 2))
