from adapackage import *


def main():
	n: int = 6
	m: int = 3
	k: int = 2

	animals: set[Animal] = Animal.generate_random_animals(n)
	escena1 = Scene({Animal("A", 4), Animal("B", 5), Animal("C", 5)})
	escena2 = Scene({Animal("A", 4), Animal("B", 5), Animal("C", 6)})
	print(escena1 <= escena2)
	# print(Animal.display_list(animals))

	# scene: Scene = Scene.generate_random_scene(animals)
	# print(scene)
	# scene.sort_scene()
	# print(scene)
	
	opening: Act = Act.generate_opening_act(3, 2, animals)
	# print(opening)
	opening.counting_sort_act()
	# print(opening)

	# show: Show = Show.generate_random_show(m, k, animals)
	# print(show)
	# show.problem_solver()


if __name__ == "__main__":
	main()