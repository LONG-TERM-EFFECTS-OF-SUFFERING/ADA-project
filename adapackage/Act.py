from adapackage.Animal import Animal
from adapackage.Scene import Scene
from adapackage.Algorithms import Algorithms, Methods


class Act:
	"""
	Class used to represent an act in the show.

	- An act is a group of k different scenes.

	Attributes
	---------
	scenes : set
		The set of different scenes in the act.

	merge_sorted_scenes : list
		The list of scenes in the act ordered by greatness using merge sort as the sorting algorithm.

	counting_sorted_scenes : list
		The list of scenes in the act ordered by greatness using counting sort as the sorting algorithm.

	greatness : int
		The greatness associated with the act (sum of greatness of all scenes).

	Methods
	-------
	generate_opening_act(m: int, k: int, animals: list[Animal]) -> Act

	transform_to_list() -> list[Scene]

	merge_sort_act()

	counting_sort_act()
	"""

	def __init__(self, scenes: set[Scene]):
		"""
		Constructor for an act.
		- Uses a set as the unsorted data structure for the scenes.
		- Uses lists as the sorted data structure for the scenes.

		Parameters
		----------
		scenes : set
			The set of different scenes in the act.
		"""
		self.scenes: set[Scene] = scenes
		self.merge_sorted_scenes: list[Scene] = None
		self.counting_sorted_scenes: list[Scene] = None
		self.greatness: int = Methods.sum([scene.greatness for scene in scenes])

	def __str__(self):
		# When scenes have not been sorted yet
		if self.merge_sorted_scenes is None and self.counting_sorted_scenes is None:
			return self.display_unsorted_scenes()

		# When scenes were sorted using merge sort
		elif self.merge_sorted_scenes is not None:
			return self.display_merge_sorted_scenes()

		# When scenes were sorted using counting sort
		else:
			return self.display_couting_sorted_scenes()

	def display_unsorted_scenes(self) -> str:
		string: str = (
			"\t { \n\t\t" +
			"\n\t\t".join(str(scene) for scene in self.scenes) +
			"\n\t\t" + str(self.greatness) +
			"\n\t }" )
		return string

	def display_merge_sorted_scenes(self) -> str:
		string: str = (
			"\t [ \n\t\t" +
			"\n\t\t".join(str(scene) for scene in self.merge_sorted_scenes) +
			"\n\t\t" + str(self.greatness) +
			"\n\t ]" )
		return string

	def display_couting_sorted_scenes(self) -> str:
		string: str = (
			"\t [ \n\t\t" +
			"\n\t\t".join(str(scene) for scene in self.counting_sorted_scenes) +
			"\n\t\t" + str(self.greatness) +
			"\n\t ]" )
		return string

	def __eq__(self, other_act):
		return self.scenes == other_act.scenes

	def __ne__(self, other_act):
		return self.scenes != other_act.scenes

	def __hash__(self):
		return hash(frozenset(self.scenes))

	def __iter__(self):
		return iter(self.scenes)

	def __lt__(self, other_act):
		return self.greatness < other_act.greatness

	def __le__(self, other_act):
		"""
		If both acts have the same greatness,
		then make pairs of acts based on the sorted list of scenes in descending order
		and look for the first pair of scenes that are different.

		Returns
		-------
		bool
			The result of the comparison between the first pair of scenes that are different.
		"""
		# If both acts have the same greatness then check for the tiebreaker
		if self.greatness == other_act.greatness:

			# Reverse the list of scenes to make pairs in descending order of greatness
			for this_scene, other_scene in Methods.zip(Methods.reverse(self.merge_sorted_scenes), Methods.reverse(other_act.merge_sorted_scenes)):
				if this_scene != other_scene and this_scene < other_scene:
					return True

				elif this_scene != other_scene and this_scene > other_scene:
					return False

		else:
			return self.greatness < other_act.greatness

	def __gt__(self, other_act):
		return self.greatness > other_act.greatness

	def __ge__(self, other_act):
		"""
		If both acts have the same greatness,
		then make pairs of acts based on the sorted list of scenes in descending order
		and look for the first pair of scenes that are different.

		Returns
		-------
		bool
			The result of the comparison between the first pair of scenes that are different.
		"""
		# If both acts have the same greatness then check for the tiebreaker
		if self.greatness == other_act.greatness:

			# Reverse the list of scenes to make pairs in descending order of greatness
			for this_scene, other_scene in Methods.zip(Methods.reverse(self.merge_sorted_scenes), Methods.reverse(other_act.merge_sorted_scenes)):

				if this_scene != other_scene and this_scene > other_scene:
					return True

				elif this_scene != other_scene and this_scene < other_scene:
					return False

		else:
			return self.greatness > other_act.greatness

	def transform_to_list(self):
		act_list = []
		for escene in self.counting_sorted_scenes: # Bounded by k
			act_list.append(escene.greatness)
		act_list.append(self.greatness)

		return act_list

	@staticmethod
	def generate_opening_act(m: int, k: int, animals: list[Animal]) -> 'Act':
		"""Generate the opening act of the show.

		- The opening act has (m - 1) * k different scenes.

		Parameters
		----------
		m : int
			The number of acts in the show.

		k : int
			The number of scenes in each act.

		animals : list
			The list of possbile animals in the show.

		Returns
		-------
		Act
			The opening act of the show with (m - 1) * k different randomly generated scenes.

			- The scenes in the opening act will be part (not necessarily all) of the other (m - 1) acts of the show.
		"""

		act: set[Scene] = set()

		while len(act) < (m - 1) * k:
			scene: Scene = Scene.generate_random_scene(animals)

			if scene not in act:
				act.add(scene)

		return Act(act)

	def merge_sort_act(self) -> None:
		"""Sorts the scenes in the act using merge sort.

		First, each of the k scenes in the act sorts its own animals.
		The process of sorting animals in a scene takes O(1) and there are k scenes, so the total cost of this part is O(k).

		Then, the k scenes of the act are sorted using merge sort.
		The merge sort algorithm follows a divide and conquer technique, so the time complexity of this part is O(k * log(k)).
		"""
		self.merge_sorted_scenes = list(self.scenes) # The animals in each scene are already sorted in O(k)

		left: int = 0
		right: int = Methods.len(self.merge_sorted_scenes) - 1

		Algorithms.merge_sort(self.merge_sorted_scenes, left, right) # O(k * log(k))

	def counting_sort_act(self) -> None:
		"""Sorts the scenes in the act using counting sort.

		First, each of the k scenes in the act sorts its own animals.
		The process of sorting animals in a scene takes O(1) and there are k scenes, so the total cost of this part is O(k).

		Then, the k scenes of the act are sorted using counting sort.
		The total cost of this part is O(k).
		"""
		scenes = list(self.scenes) # The scenes are already sorted O(k)

		scenes_aux = []
		index = 0

		for scene in scenes:
			scene_list = scene.transform_to_list()
			scene_list.append(index)
			scenes_aux.append(scene_list)
			index += 1
		# [animal 1 greatness, animal 2 greatness, animal 3 greatness, scene greatness, scene object index]

		n = Methods.len(scenes)
		def max_values(scenes_aux, n):
			max_values = []

			for i in range(4):
				column_numbers = []
				for j in range(n):
					column_numbers.append(scenes_aux[j][i])
				max_values.append(Methods.max(column_numbers))

			return max_values

		max_list = max_values(scenes_aux, n)

		sorted_act = None

		for j in range(4):
			sorted_act = Algorithms.counting_sort(n, scenes_aux, j, max_list[j])
			scenes_aux = sorted_act

		# Assigning original objects
		for i in range(n):
			sorted_act[i] = scenes[sorted_act[i][4]]

		self.counting_sorted_scenes = sorted_act # O(n)

