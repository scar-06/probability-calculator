import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents.extend([ball] * count)

    def draw(self, num_balls):
        # drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            # self.contents = []
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    favorable_outcomes = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {}
        for ball in drawn_balls:
            drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1

        success = True
        for ball, count in expected_balls.items():
            if drawn_balls_dict.get(ball, 0) < count:
                success = False
                break

        if success:
            favorable_outcomes += 1

    probability = favorable_outcomes / num_experiments
    return probability
