from adapackage.Animal import Animal
from adapackage.Scene import Scene
from adapackage.Act import Act
import random


class Show:
    """
    Class used to represent a show in the zoo
    A show is a list of m different acts

    Atributes
    ---------
    acts : list
        The list of different acts in the show

    Methods
    -------

    """

    def __init__(self, acts: list[Act]):
        """
        Parameters
        ----------
        acts : list
            The list of different acts in the show
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
        copy_of_opening_act: Act = Act(opening_act.scenes.copy())

        acts: list[Act] = [opening_act]

        for i in range(1, m):
            scenes: list[Scene] = []

            for j in range(k):
                left_scenes: int = len(copy_of_opening_act.scenes)
                random_scene = random.randint(0, left_scenes - 1)
                scenes.append(copy_of_opening_act.scenes.pop(random_scene))

            acts.append(Act(scenes))

        return Show(acts)
