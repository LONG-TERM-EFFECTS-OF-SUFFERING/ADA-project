from adapackage.Animal import Animal
from adapackage.Scene import Scene


class Act:
	"""
	Class used to represent an act in the show.

	- An act is a set of k different scenes.

	Atributes
	---------
	scenes : set
		The set of different scenes in the act.
	gratness : int
		The greatness associated with the act (sum of greatness of all scenes).

	Methods
	-------

	"""

	def __init__(self, scenes: set[Scene]):
		"""
		Parameters
		----------
		scenes : set
			The set of different scenes in the act.
		"""
		self.scenes = scenes
		self.greatness = sum(scene.greatness for scene in scenes)

	def __str__(self):
		return "\t{\n\t\t" + "\n\t\t".join(str(scene) for scene in self.scenes) + "\n\t\t" + str(self.greatness) + "\n\t}"

	def __eq__(self, other_act):
		return self.scenes == other_act.scenes

	def __hash__(self):
		return hash(frozenset(self.scenes))

	def __lt__(self, other_act):
		return self.greatness < other_act.greatness

	def __le__(self, other_act):
		return self.greatness <= other_act.greatness

	def __gt__(self, other_act):
		return self.greatness > other_act.greatness

	def __ge__(self, other_act):
		return self.greatness >= other_act.greatness

	def __iter__(self):
		return iter(self.scenes)

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
