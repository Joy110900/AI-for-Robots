# Write code that makes the robot move twice and then prints 
# out the resulting distribution, starting with the initial 
# distribution p = [0, 1, 0, 0, 0]

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8 #Probability that it makes exact movement
pOvershoot = 0.1 #Probability that it overshoots
pUndershoot = 0.1 #Probability that ir undershoots

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]  #Movement contribution by exact movement
        s = s + pOvershoot * p[(i-U-1) % len(p)] #Movement contribution by inexact movement
        s = s + pUndershoot * p[(i-U+1) % len(p)] #Movement contribution by inexact movement; i-U+1 as i-(U-1),U-1 as underhoot
        q.append(s)
    return q
#
#ADD CODE HERE

def move_times(p,m):
    q = p
    for i in range(m):
        q = move(q,1)
    return q
#
print(move_times(p,2))
# Make sure to print out p!
