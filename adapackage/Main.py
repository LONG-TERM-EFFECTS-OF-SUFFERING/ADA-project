from adapackage import *


def main():
    n: int = 6
    m: int = 3
    k: int = 2

    animals: set[Animal] = Animal.generate_random_animals(n)
    print(Animal.display_list(animals))

    # scene: Scene = Scene.generate_random_scene(animals)
    # print(scene)
    #
    # opening: Act = Act.generate_opening_act(3, 2, animals)
    # print(opening)

    show: Show = Show.generate_random_show(m, k, animals)
    print(show)


if __name__ == "__main__":
    main()