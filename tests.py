from adapackage import Show, Animal, Scene, Act

def test1() -> bool:
	n = 6
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


	opening_act_input = [
		Scene({animals[5], animals[3], animals[4]}), # "Tapir", "Nutria", "Perro"
		Scene({animals[5], animals[4], animals[0]}), # "Tapir", "Perro", "Gato"
		Scene({animals[2], animals[5], animals[0]}), # "Ciempies", "Tapir", "Gato"
		Scene({animals[0], animals[2], animals[1]})  # "Gato", "Ciempies", "Libelula"
	]

	acts_input = [
		[
			opening_act_input[0], # "Tapir", "Nutria", "Perro"
			opening_act_input[2]  # "Ciempies", "Tapir", "Gato"
		],
		[
			opening_act_input[3], # "Gato", "Ciempies", "Libelula"
			opening_act_input[1]  # "Tapir", "Perro", "Gato"
		]
	]

	show = Show(n, m, k, animals, greatness, opening_act_input, acts_input)

	opening_act = [
		[animals[2], animals[1], animals[0]], # "Ciempies", "Libelula", "Gato"
		[animals[2], animals[0], animals[5]], # "Ciempies", "Gato", "Tapir"
		[animals[0], animals[4], animals[5]], # "Gato", "Perro", "Tapir"
		[animals[4], animals[5], animals[3]]  # "Perro", "Tapir", "Nutria"
	]

	acts = [
		[
			[animals[2], animals[1], animals[0]], # "Ciempies", "Libelula", "Gato"
			[animals[0], animals[4], animals[5]]   # "Gato", "Perro", "Tapir"
		],
		[
			[animals[2], animals[0], animals[5]], # "Ciempies", "Gato", "Tapir"
			[animals[4], animals[5], animals[3]] # "Perro", "Tapir", "Nutria"
		]
	]

	most_participating_animals = [animals[0], animals[5]] # "Gato", "Tapir"
	less_participating_animals = [animals[1]] # "Libelula"

	greatness_min_scene = [animals[2], animals[1], animals[0]] # "Ciempies", "Libelula", "Gato"
	greatness_max_scene = [animals[4], animals[5], animals[0]] # "Perro", "Tapir", "Gato"

	greatness_average = 10.5

	return (
			opening_act == show.opening_act and
			acts == show.acts and
			most_participating_animals == show.most_participating_animals and
			less_participating_animals == show.less_participating_animals and
			greatness_min_scene == show.greatness_min_scene and
			greatness_max_scene == show.greatness_max_scene and
			greatness_average == show.greatness_average
		)


def test2() -> bool:
	n = 9
	m = 4
	k = 3

	animals = ["leon", "pantera negra", "cebra", "cocodrilo", "boa", "loro", "caiman", "tigre", "capibara"]

	greatness = [9, 7, 6, 5, 4, 2, 3, 8, 1]

	opening_act_input = [["caiman", "capibara", "loro"], ["boa", "caiman", "capibara"], ["cocodrilo", "capibara", "loro"], ["pantera negra", "cocodrilo", "loro"], ["tigre", "loro", "capibara"], ["leon", "caiman", "loro"], ["leon", "cocodrilo", "boa"], ["leon", "pantera negra", "cebra"], ["tigre", "cebra", "pantera negra"]]

	acts_input = [
		[["caiman", "capibara", "loro"], ["tigre", "loro", "capibara"], ["tigre", "cebra", "pantera negra"]],
		[["pantera negra", "cocodrilo", "loro"], ["leon", "pantera negra", "cebra"], ["cocodrilo", "capibara", "loro"]],
		[["boa", "caiman", "capibara"], ["leon", "caiman", "loro"], ["leon", "cocodrilo", "boa"]]
	]

	show = Show(n, m, k, animals, greatness, opening_act_input, acts_input)

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
		]
	]

	most_participating_animals = ["loro"]
	less_participating_animals = ["tigre", "cebra", "boa"]

	greatness_min_scene = ["capibara", "loro", "caiman"]
	greatness_max_scene = ["cebra", "pantera negra", "leon"]

	greatness_average = 13.56

	return (
			opening_act == show.opening_act and
			acts == show.acts and
			most_participating_animals == show.most_participating_animals and
			less_participating_animals == show.less_participating_animals and
			greatness_min_scene == show.greatness_min_scene and
			greatness_max_scene == show.greatness_max_scene and
			greatness_average == show.greatness_average
		)
