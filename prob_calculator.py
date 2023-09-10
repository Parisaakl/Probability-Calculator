import random

class Hat:

    def __init__(self, **kwargs):
        # Initialize the Hat with different colored balls based on input counts
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)

    def draw(self, number):
        # Draw a specified number of random balls from the Hat
        if number >= len(self.contents):
            return self.contents
        return [self.contents.pop(random.randint(0, len(self.contents) - 1)) for _ in range(number)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for _ in range(num_experiments):
        # Create a new Hat for each experiment to maintain the original Hat's state
        new_hat = Hat(**hat.contents)
        balls = new_hat.draw(num_balls_drawn)

        # Count the occurrences of each ball in the drawn list
        ball_counts = {ball: balls.count(ball) for ball in set(balls)}

        # Check if all expected balls have been drawn as many times as expected
        success = all(expected_balls.get(ball, 0) <= count for ball, count in ball_counts.items())

        if success:
            successes += 1

    # Calculate the probability of success
    probability = successes / num_experiments
    return probability
