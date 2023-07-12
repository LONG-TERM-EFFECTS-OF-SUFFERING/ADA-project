from adapackage import Show, Animal, Scene, Act

def test1() -> bool:
	m = 3
	k = 2

	animals = [
		Animal("Gato", 3),
		Animal("Libelula", 2),
		Animal("Ciempies", 1),
		Animal("Nutria", 6),
		Animal("Perro", 4),
		Animal("Tapir", 5)
	]


	opening_act_input = Act(
		set([
			Scene({animals[5], animals[3], animals[4]}), # "Tapir", "Nutria", "Perro"
			Scene({animals[5], animals[4], animals[0]}), # "Tapir", "Perro", "Gato"
			Scene({animals[2], animals[5], animals[0]}), # "Ciempies", "Tapir", "Gato"
			Scene({animals[0], animals[2], animals[1]})  # "Gato", "Ciempies", "Libelula"
		])
	)

	acts_input = [
		opening_act_input,
		Act(
			set([
				Scene({animals[5], animals[3], animals[4]}), # "Tapir", "Nutria", "Perro"
				Scene({animals[2], animals[5], animals[0]})  # "Ciempies", "Tapir", "Gato"
			])
		),
		Act(
			set([
				Scene({animals[0], animals[2], animals[1]}), # "Gato", "Ciempies", "Libelula"
				Scene({animals[5], animals[4], animals[0]})  # "Tapir", "Perro", "Gato"
			])
		)
	]

	show = Show(acts_input, animals, m, k)

	opening_act = [
		["Ciempies", "Libelula", "Gato"],
		["Ciempies", "Gato", "Tapir"],
		["Gato", "Perro", "Tapir"],
		["Perro", "Tapir", "Nutria"]
	]

	acts = [
		[
			["Ciempies", "Libelula", "Gato"],
			["Gato", "Perro", "Tapir"]
		],
		[
			["Ciempies", "Gato", "Tapir"],
			["Perro", "Tapir", "Nutria"]
		],
		opening_act
	]

	most_participating_animals = ["Gato", "Tapir"]
	less_participating_animals = ["Libelula"]

	greatness_min_scene = ["Ciempies", "Libelula", "Gato"]
	greatness_max_scene = ["Perro", "Tapir", "Gato"]

	greatness_average = 10.5

	show.counting_sort_show()
	show.problem_solver()

def test2() -> bool:
	m = 4
	k = 3

	animals = [
		Animal("Leon", 9),
		Animal("Pantera negra", 7),
		Animal("Cebra", 6),
		Animal("Cocodrilo", 5),
		Animal("Boa", 4),
		Animal("Loro", 2),
		Animal("Caiman", 3),
		Animal("Tigre", 8),
		Animal("Capibara", 1)
	]

	opening_act_input = Act(
		set([
			Scene({animals[6], animals[8], animals[5]}), # "Caiman", "Capibara", "Loro"
			Scene({animals[4], animals[6], animals[8]}), # "Boa", "Caiman", "Capibara"
			Scene({animals[3], animals[8], animals[5]}), # "Cocodrilo", "Capibara", "Loro"
			Scene({animals[1], animals[3], animals[5]}), # "Pantera negra", "Cocodrilo", "Loro"
			Scene({animals[7], animals[5], animals[8]}), # "Tigre", "Loro", "Capibara"
			Scene({animals[0], animals[6], animals[5]}), # "Leon", "Caiman", "Loro"
			Scene({animals[0], animals[3], animals[4]}), # "Leon", "Cocodrilo", "Boa"
			Scene({animals[0], animals[1], animals[2]}), # "Leon", "Pantera negra", "Cebra"
			Scene({animals[7], animals[2], animals[1]}), # "Tigre", "Cebra", "Pantera negra"
		])
	)

	acts_input = [
		opening_act_input,
		Act(
			set([
				Scene({animals[6], animals[8], animals[5]}), # "Caiman", "Capibara", "Loro"
				Scene({animals[7], animals[5], animals[8]}), # "Tigre", "Loro", "Capibara"
				Scene({animals[7], animals[2], animals[1]}), # "Tigre", "Cebra", "Pantera negra"
			])
		),
		Act(
			set([
				Scene({animals[1], animals[3], animals[5]}), # "Pantera negra", "Cocodrilo", "Loro"
				Scene({animals[0], animals[1], animals[2]}), # "Leon", "Pantera negra", "Cebra"
				Scene({animals[3], animals[8], animals[5]}), # "Cocodrilo", "Capibara", "Loro"
			])
		),
		Act(
			set([
				Scene({animals[4], animals[6], animals[8]}), # "Boa", "Caiman", "Capibara"
				Scene({animals[0], animals[6], animals[5]}), # "Leon", "Caiman", "Loro"
				Scene({animals[0], animals[3], animals[4]}), # "Leon", "Cocodrilo", "Boa"
			])
		),
	]

	show = Show(acts_input, animals, m, k)

	opening_act = [
		["capibara", "loro", "caiman"],
		["capibara", "caiman", "boa"],
		["capibara", "loro", "cocodrilo"],
		["capibara", "loro", "trigre"],
		["loro", "cocodrilo", "pantera negra"],
		["loro", "caiman", "leon"],
		["boa", "cocodrilo", "leon"],
		["cebra", "pantera negra", "trigre"],
		["cebra", "pantera negra", "leon"]
	]

	acts = [
		[
			["capibara", "loro", "caiman"],
			["capibara", "loro", "trigre"],
			["cebra", "pantera negra", "trigre"]
		],
		[
			["capibara", "caiman", "boa"],
			["loro", "caiman", "leon"],
			["boa", "cocodrilo", "leon"]
		],
		[
			["capibara", "loro", "cocodrilo"],
			["loro", "cocodrilo", "pantera negra"],
			["cebra", "pantera negra", "leon"]
		],
		opening_act
	]

	most_participating_animals = ["loro"]
	less_participating_animals = ["tigre", "cebra", "boa"]

	greatness_min_scene = ["capibara", "loro", "caiman"]
	greatness_max_scene = ["cebra", "pantera negra", "leon"]

	greatness_average = 13.56

	show.merge_sort_show()
	show.problem_solver()

#test1()
test2()
