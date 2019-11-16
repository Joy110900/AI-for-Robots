# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up

def localize(colours,measurement,motion,sr,pm): # sr is sensor right which is the error in sensor,; pm is the error in movement
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colours)) / float(len(colours[0]))
    p = [[pinit for row in range(len(colours[0]))] for col in range(len(colours))]
    # >>> Insert your code here <<<
    
    for i in range(len(measurement)):
       p = move(p, motion[i], pm)
       p = sense(p, colours, measurement[i], sr)

    return p

def sense(p, color, Z, st):
    aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    sw = 1 - st
    t = 0.0
    for i in range(len(p)):
        for j in range(len(p[0])):
            hit = (Z == color[i][j])
            aux[i][j] = p[i][j] * (hit * st + (1 - hit) * sw)
            t += aux[i][j]
            
    for i in range(len(aux)):
        for j in range(len(aux[i])):
            aux[i][j] /= t
    return aux

def move(p, U, pm):
    aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    ps = 1 - pm
    for i in range(len(aux)):
        for j in range(len(aux[i])):
            aux[i][j] = ((pm * p[(i - U[0] % len(p))][(j - U[1]) % len(p)] + (ps * p[i][j]))) 
    return aux

def show(s):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in s]
    print('[' + ',\n '.join(rows) + ']')
    
#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)
colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]

measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

s = localize(colors,measurements,motions, sr = 0.7, pm = 0.8)
show(s) # displays your answer