from adapackage.Animal import Animal
from adapackage.Scene import Scene
from adapackage.Act import Act
import random


class Show:
    """
    Class used to represent a show in the zoo
    A show is a set of m different acts

    Atributes
    ---------
    acts : set
        The set of different acts in the show

    Methods
    -------

    """

    def __init__(self, acts: list[Act]):
        """
        Parameters
        ----------
        acts : set
            The set of different acts in the show
        """
        self.acts = acts

    def __str__(self):
        return "{\n" + "\n".join(str(act) for act in self.acts) + "\n}"

    @staticmethod
    def generate_random_show(m: int, k: int, animals: list[Animal]) -> 'Show':
        """
        Generate a random show with m different acts
        The first act of the show is the opening act, that has (m - 1) * k different scenes
        In the other m-1 acts there are k different scenes and each scene comes from the opening act

        Parameters
        ----------
        m : int
            The number of acts in the show
        k : int
            The number of scenes in each act
        animals : list
            The list of animals that can be used in the show

        Returns
        -------
        show : Show
            The randomly generated show for the given values of m, k and animals
        """
        opening_act: Act = Act.generate_opening_act(m, k, animals)
        copy_of_scenes_in_opening_act: list[Scene] = list(opening_act.scenes.copy())

        acts: set[Act] = {opening_act}

        for i in range(1, m):
            scenes: set[Scene] = set()

            for j in range(k):
                left_scenes: int = len(copy_of_scenes_in_opening_act)
                random_scene = random.randint(0, left_scenes - 1)
                scenes.add(copy_of_scenes_in_opening_act.pop(random_scene))

            acts.add(Act(scenes))

        return Show(acts)
