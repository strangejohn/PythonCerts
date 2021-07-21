import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **hats):
        self.contents = []
        for key, value in hats.items():
            for i in range(value):
                self.contents.append(key)


    def draw(self, pick):
        picked_balls = []
        #if bag is empty end func
        if len(self.contents) <= 0:
            return 'No balls.'
        #if draw == or exceeds return all balls
        if pick >= len(self.contents):
            return self.contents
        for i in range(pick):
            which_ball = random.choice(self.contents)
            picked_balls.append(which_ball)
            self.contents.pop(self.contents.index(which_ball))

        return picked_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
  
    for i in range(num_experiments):
      hat_copy = copy.deepcopy(hat)
  
      drawn_copy = hat_copy.draw(num_balls_drawn)
  
      # Convert result to dict:
      drawn_copy_dict = {ball: drawn_copy.count(ball) for ball in set(drawn_copy)}
  
      # Compare drawn balls to desired result:
      result = True
      for key, value in expected_balls.items():
        if key not in drawn_copy_dict or drawn_copy_dict[key] < expected_balls[key]:
          result = False
          break
  
      if result:
        count += 1
  
    return count/num_experiments
