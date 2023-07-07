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
		The list of scenes in the act order by greatness using merge sort as the sorting algorithm.

	counting_sorted_scenes : list
		The list of scenes in the act order by greatness using counting sort as the sorting algorithm.

	gratness : int
		The greatness associated with the act (sum of greatness of all scenes).

	Methods
	-------
	"""

	def __init__(self, scenes: set[Scene]):
		"""
		Constructor for an act.
		Uses a set as the unsorted data structure for the scenes.
		Uses lists as the sorted data structure for the scenes.

		Parameters
		----------
		scenes : set
			The set of different scenes in the act.
		"""
		self.scenes: set[Scene] = scenes
		self.merge_sorted_scenes: list[Scene] = None
		self.counting_sorted_scenes: list[Scene] = None
		self.greatness: int = sum(scene.greatness for scene in scenes)

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
		return self.greatness <= other_act.greatness

	def __gt__(self, other_act):
		return self.greatness > other_act.greatness

	def __ge__(self, other_act):
		return self.greatness >= other_act.greatness

	@staticmethod
	def generate_opening_act(m: int, k: int, animals: list[Animal]) -> 'Act':
		"""
		Generate the opening act of the show.

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
		The merge sort algorithms follows a divide and conquer technique, so the total cost of this part is O(k * log(k)).
		"""
		for scene in self.scenes: scene.sort_scene() # O(k)

		self.merge_sorted_scenes = list(self.scenes)

		left: int = 0
		right: int = len(self.merge_sorted_scenes) - 1

		return Algorithms.merge_sort(self.merge_sorted_scenes, left, right) # O(k * log(k))

	def counting_sort_act(self) -> None:
		"""Sorts the scenes in the act using counting sort.

		First, each of the k scenes in the act sorts its own animals.
		The process of sorting animals in a scene takes O(1) and there are k scenes, so the total cost of this part is O(k).

		Then, the k scenes of the act are sorted using merge sort.
		The merge sort algorithms follows a divide and conquer technique, so the total cost of this part is O(k * log(k)).
		"""

		for scene in self.scenes: scene.sort_scene() # O(k)

		scenes = list(self.scenes)

		return Algorithms.counting_sort(scenes, Methods.max(scenes).greatness) # O(k)

