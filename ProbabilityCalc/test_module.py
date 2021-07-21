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
        #copy hat /// creat draw copy /// convert into dic for compare
        hat_copy = copy.deepcopy(hat)
        drawn_copy = hat_copy.draw(num_balls_drawn)
        drawn_copy_dict = {ball: drawn_copy.count(ball) for ball in set(drawn_copy)}

        #compare hat copy input to drawn copy
        matches = True
        for key, value in expected_balls.items():
            #check to see if type of ball is in copys
            if key not in drawn_copy_dict:
                matches = False
                break
            #check to see if # of balls == ball type
            if drawn_copy_dict[key] < expected_balls[key]:
                matches = False
                break
        if matches:
            count +=1
    return count/num_experiments
