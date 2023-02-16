import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
        print(self.contents)

    # def draw(self, number):
    #     total_removed = []
    #     if number > len(self.contents):
    #         return self.contents
    #     for i in range(number):
    #         removed = self.contents.pop(int(random.random() * len(self.contents)))
    #         total_removed.append(removed)
    #     return total_removed
    
    
    def draw(self, balls):
        draw_list = list()
        if balls > len(self.contents):
            return self.contents
        for i in range(balls):
            deleted = random.randrange(len(self.contents))
            draw_list.append(self.contents[deleted])
            self.contents.pop(deleted)
        return draw_list

    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    itterator = 0
    
    for i in range(num_experiments):
        copy_balls = copy.deepcopy(expected_balls)
        copy_hat = copy.deepcopy(hat)
        chosen_color = copy_hat.draw(num_balls_drawn)
        
        for color in chosen_color:
            if color in copy_balls:
                copy_balls[color]-=1
                
        if all (x <= 0 for x in copy_balls.values()):
            itterator += 1
            
    return itterator / num_experiments 
