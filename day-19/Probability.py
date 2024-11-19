import random
from copy import deepcopy

class Hat:
    def __init__(self, **kwargs):
        """Initialize the hat with balls based on input arguments."""
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        """Draw balls from the hat randomly without replacement."""
        if num_balls >= len(self.contents):
            # Return all balls and clear the contents of the hat
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_balls)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Estimate the probability of getting the expected balls in a number of experiments."""
    success_count = 0
    
    for _ in range(num_experiments):
        # Create a copy of the hat to preserve the original contents
        test_hat = deepcopy(hat)
        # Draw balls from the copied hat
        drawn_balls = test_hat.draw(num_balls_drawn)
        # Count occurrences of each ball color
        drawn_count = {color: drawn_balls.count(color) for color in drawn_balls}
        # Check if all expected balls are present in sufficient quantity
        success = all(drawn_count.get(color, 0) >= count for color, count in expected_balls.items())
        if success:
            success_count += 1
    
    # Calculate and return the probability
    return success_count / num_experiments

# Example usage
hat = Hat(blue=5, red=4, green=2)
probability = experiment(
    hat=hat,
    expected_balls={'red': 1, 'green': 2},
    num_balls_drawn=4,
    num_experiments=1000
)
print("Probability:", probability)