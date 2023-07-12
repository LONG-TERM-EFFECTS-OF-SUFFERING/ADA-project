from adapackage import *


def main():
	n: int = 10
	m: int = 5
	k: int = 3

	animals: set[Animal] = Animal.generate_random_animals(n)

	# scene: Scene = Scene.generate_random_scene(animals)
	# print(scene)
	# scene.sort_scene()
	# print(scene)


	# opening: Act = Act.generate_opening_act(3, 2, animals)
	# opening.counting_sort_act()
	# print(opening.tranform_to_list())
	# print(opening)
	# opening.counting_sort_act()
	# print(opening)

	show: Show = Show.generate_random_show(m, k, animals)
	print(show)
	show.merge_sort_show()
	# show.counting_sort_show()
	show.problem_solver()


if __name__ == "__main__":
	main()