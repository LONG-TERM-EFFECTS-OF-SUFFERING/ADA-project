from adapackage import Show

def test1() -> bool:
	n = 6
	m = 3
	k = 2

	animals = ["gato", "libelula", "ciempies", "nutria", "perro", "tapir"]

	greatness = [3, 2, 1, 6, 4, 5]

	opening_act_input = [["tapir", "nutria", "perro"], ["tapir", "perro" "gato"], ["ciempies", "tapir", "gato"], ["gato", "ciempies", "libelula"]]

	acts_input = [
		[["tapir", "nutria", "perro"], ["ciempies", "tapir", "gato"]],
		[["gato", "ciempies", "libelula"], ["tapir", "perro" "gato"]]
	]

	show = Show(n, m, k, animals, greatness, opening_act_input, acts_input)

	opening_act = [
		["ciempies", "libelula", "gato"],
		["ciempies", "gato", "tapir"],
		["gato", "perro", "tapir"],
		["perro", "tapir", "nutria"]
	]

	acts = [
		[
			["ciempies", "libelula", "gato"],
			["gato", "perro", "tapir"]
		],
		[
			["ciempies", "gato", "tapir"],
			["perro", "tapir", "nutria"]
		]
	]

	most_participating_animals = ["gato", "tapir"]
	less_participating_animals = ["libelula"]

	greatness_min_scene = ["ciempies", "libelula", "gato"]
	greatness_max_scene = ["perro", "tapir", "gato"]

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
