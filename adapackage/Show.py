from adapackage.Animal import Animal
from adapackage.Scene import Scene
from adapackage.Act import Act
from adapackage.Algorithms import Algorithms, Methods
import random


class Show:
	"""
	Class used to represent a show in the zoo.

	- A show is a group of m different acts.

	Attributes
	---------
	acts : set
		The set of different acts in the show.

	merge_sorted_acts : list
		The list of acts in the show ordered by greatness using merge sort as the sorting algorithm.

	counting_sorted_acts : list
		The list of acts in the show ordered by greatness using counting sort as the sorting algorithm.

	Methods
	-------

	"""

	def __init__(self, acts: list[Act]):
		"""
		Constructor for a show.
		- Uses a set as the unsorted data structure for the acts.
		- Uses lists as the sorted data structure for the acts.

		Parameters
		----------
		acts : set
			The set of different acts in the show.
		"""
		self.acts: set[Act] = acts
		self.merge_sorted_acts: list[Act] = None
		self.counting_sorted_acts: list[Act] = None
		self.m = Methods.len(acts)

	def __str__(self):
		# When acts have not been sorted yet
		if self.merge_sorted_acts is None and self.counting_sorted_acts is None:
			print(True)
			return "{ \n" + "\n".join(str(act) for act in self.acts) + "\n }"

		# When acts were sorted using merge sort
		if self.merge_sorted_acts is not None:
			return "[ \n" + "\n".join(str(act) for act in self.merge_sorted_acts) + "\n ]"

		# When acts were sorted using counting sort
		else:
			return "[ \n" + "\n".join(str(act) for act in self.counting_sorted_acts) + "\n ]"

	@staticmethod
	def generate_random_show(m: int, k: int, animals: list[Animal]) -> 'Show':
		"""
		Generate a random show with m different acts.

		- The first act of the show is the opening act, that has (m - 1) * k different scenes.
		- The other (m - 1) acts there are k different scenes and each scene comes from the opening act.

		Parameters
		----------
		m : int
			The number of acts in the show.
		k : int
			The number of scenes in each act.
		animals : list
			The list of animals that can be used in the show.

		Returns
		-------
		show : Show
			The randomly generated show for the given values of m, k and animals.
		"""
		opening_act: Act = Act.generate_opening_act(m, k, animals)
		copy_of_scenes_in_opening_act: list[Scene] = list(opening_act.scenes)

		acts: set[Act] = {opening_act}

		for i in range(1, m):
			scenes: set[Scene] = set()

			for j in range(k):
				left_scenes: int = len(copy_of_scenes_in_opening_act)
				random_scene = random.randint(0, left_scenes - 1)
				scenes.add(copy_of_scenes_in_opening_act.pop(random_scene))

			acts.add(Act(scenes))

		return Show(acts)

	def merge_sort_show(self) -> None:
		"""Sort the acts in the show using merge sort.

		First, each of the m acts in the show sorts its own scenes using merge sort.
		The process of sorting scenes in an act takes O(k * log(k)), and there are m acts, so the total time is O(m * k * log(k)).

		Then, the m acts are sorted using merge sort.
		The merge sort algorithm follows a divide and conquer technique, so the time complexity of this part is O(m * log(m)).
		"""

		for act in self.acts:
			act.merge_sort_act() # Sort the scenes in each act using merge sort O(m * k * log(k))

		self.merge_sorted_acts = list(self.acts)

		left: int = 0
		right: int = len(self.merge_sorted_acts) - 1

		Algorithms.merge_sort(self.merge_sorted_acts, left, right) # Sort the acts using merge sort O(m * log(m))

	def counting_sort_show(self, k: int) -> None:
		"""Sort the acts in the show using couting sort.

		First, each of the m acts in the show sorts its own scenes using couting sort.
		The process of sorting scenes in an act takes O(k), and there are m acts, so the total time is O(m * k).

		Then, the m acts are sorted using couting sort.

		Parameters
		----------
		k : int
			The number of scenes in each (m - 1) act .

		Returns
		-------
			NONE
		"""

		for act in self.acts:
			act.counting_sort_act() # Sort the scenes in each act using counting sort O(m * k)

		acts = list(self.acts)
		n = Methods.len(acts)
		# Remove opening act (it always be in the first position)
		opening_act = Methods.max(acts)

		for i in range(n):
			if acts[i].greatness == opening_act.greatness:
				acts.pop(i)
				break

		acts_aux = []
		index = 0

		for act in acts:
			act_list = act.transform_to_list()
			act_list.append(index)
			acts_aux.append(act_list)
			index += 1
		# [scene 1 greatness, scene 2 greatness, ... , scene k greatness, act greatness, act object index]

		n -= 1
		def max_values(acts_aux, n):
			max_values = []

			for i in range(k + 1): # + 1 because of the greatness
				column_numbers = []
				for j in range(n):
					column_numbers.append(acts_aux[j][i])
				max_values.append(max(column_numbers))

			return max_values

		max_list = max_values(acts_aux, n)
		sorted_show = None

		for j in range(k):
			sorted_show = Algorithms.counting_sort(n, acts_aux , j, max_list[j])
			acts_aux  = sorted_show

		# Assigning original objects
		for i in range(n):
			sorted_show[i] = acts[sorted_show[i][k + 1]]

		self.counting_sorted_scenes = [opening_act].append(sorted_show)

	def problem_solver(self):
		"""
		Still to be implemented.....
		"""
		self.merge_sort_show()

		print("The order of the show should be: ")

		print("Opening act: ")
		print(self.merge_sorted_acts[self.m - 1])

		for i in range(0, self.m - 1):
			print("Act " + str(i + 1) + ": ")
			print(self.merge_sorted_acts[i])

		print("Animals that acted in the most scenes: " )

		print("Animals that acted in the least scenes: ")

		print("Scene with the smallest greatness: ")

		print("Scene with the largest greatness: ")

		print("The average greatness of the show is: ")


