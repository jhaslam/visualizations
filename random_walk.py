from random import choice


class RandomWalk():
    """Produces a set of (x,y) coordinates representing a random walk"""

    def __init__(self, num_points: int = 5000) -> None:
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self) -> None:
        while len(self.x_values) < self.num_points:
            x_step = RandomWalk._get_step()
            y_step = RandomWalk._get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def _get_step() -> int:
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance
