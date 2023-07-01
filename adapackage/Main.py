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

    # lion: Animal = Animal("Lion", 6)
    # tiger: Animal = Animal("Tiger", 5)
    # bear: Animal = Animal("Bear", 4)
    #
    # lion1: Animal = Animal("Lion", 6)
    # tiger1: Animal = Animal("Tiger", 5)
    # bear1: Animal = Animal("Bear", 4)
    #
    # butterfly: Animal = Animal("Butterfly", 10)
    # dog: Animal = Animal("Dog", 4)
    # cat: Animal = Animal("Cat", 1)
    #
    # scene1: Scene = Scene({lion, tiger, bear})
    # scene2: Scene = Scene({lion1, tiger1, bear1})
    # scene3: Scene = Scene({butterfly, dog, cat})
    #
    # print(lion in scene1)
    # print(lion1 in scene1)
    #
    # print(scene1 == scene2)
    # print(scene1 == scene3)




if __name__ == "__main__":
    main()