import random


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, n=10_000):
        """Initialize attributes of a walk."""
        self.n = n
        self.X = [0]
        self.Y = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        while len(self.X) < self.n:
            x_step = self._get_step()
            y_step = self._get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.X[-1] + x_step
            next_y = self.Y[-1] + y_step

            self.X.append(next_x)
            self.Y.append(next_y)

    def _get_step(self):
        """Determine the direction and distance for each step."""
        direction = random.choice([1, -1])
        distance = random.choice([0, 1, 2])

        return direction * distance
