from adapackage import *


def main():
	n: int = 10
	m: int = 7
	k: int = 3

	animals: set[Animal] = Animal.generate_random_animals(n)

	show: Show = Show.generate_random_show(m, k, animals)
	print(show)
	#show.merge_sort_show()
	show.counting_sort_show()
	show.problem_solver()

if __name__ == "__main__":
	main()