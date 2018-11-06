# import operator
import random
import matplotlib.pyplot

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
   

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
            


matplotlib.pyplot.ylim(0, 99)  
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
 matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()


distance = distance_between(agents[0], agents[9])
print(distance)

max_distance = 0
'''
for i in range(num_of_agents):
    for j in range(num_of_agents):
        if (i > j):
            print (i, j)
            distance = distance_between(agents[i], agents[j])
            print("distance",distance)
            if (distance > max_distance):
                max_distance = distance
                print("max_distance", max_distance)
'''
for i in range(0, num_of_agents):
    for j in range(i, num_of_agents):
        #if (i > j):
        print (i, j)
            #distance = distance_between(agents[i], agents[j])
            #print("distance",distance)
            #if (distance > max_distance):
            #    max_distance = distance
            #    print("max_distance", max_distance)

print("max_distance", max_distance)