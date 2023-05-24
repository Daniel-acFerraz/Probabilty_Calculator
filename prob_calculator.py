import random
import copy
class Hat:
    def __init__(self,**balls):
        self.contents = list()
        for k, v in balls.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, draws):
        drawnBalls = list()
        if draws >= len(self.contents): drawnBalls = self.contents
        else:
            for i in range(draws):
                randomBall = random.randint(0, len(self.contents)-1)
                drawnBalls.append(str(self.contents[randomBall]))
                self.contents.remove(self.contents[randomBall])

        return drawnBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0  

    for i in range(num_experiments):
        hat2 = copy.deepcopy(hat)
        subCounter = 0
        ballsRetrieved = hat2.draw(num_balls_drawn)
        for k, v in expected_balls.items():
            if ballsRetrieved.count(k) >= expected_balls[k]:
                subCounter += 1

        if subCounter >= len(expected_balls):
            counter += 1
    

    chance = counter/num_experiments

    return chance

myHat = Hat(black=6, red=5, green=9)
probability = experiment(hat=myHat, expected_balls={"red":1, "black": 1}, num_balls_drawn=2, num_experiments=500)
print(probability)
