#Modify the code so that it updates the probability twice
#and gives the posterior distribution after both 
#measurements are incorporated. Make sure that your code 
#allows for any sequence of measurement of any length.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i]) #hit is a boolean
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss)) #if Z == world then hit = 1 and 1-hit = 0 sp pHit gets multiplies vis a vis
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s #Normalising whole probability
    return q
#
#ADD YOUR CODE HERE

for i in range(len(measurements)):
    p = sense(p,measurements[i])

#
print(p)
