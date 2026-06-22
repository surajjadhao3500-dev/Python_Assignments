#1.Single Server Queue

import simpy
def customer(env, name, server):
    with server.request() as req:
        yield req
        print(name, "is being served at", env.now)
        yield env.timeout(2)

env = simpy.Environment()
server = simpy.Resource(env, capacity=1)

for i in range(3):
    env.process(customer(env, "Customer"+str(i+1), server))

env.run()

#2.Double Server Queue

import simpy

def customer(env, name, server):
    with server.request() as req:
        yield req
        print(name, "is being served at", env.now)
        yield env.timeout(2)

env = simpy.Environment()
server = simpy.Resource(env, capacity=2)

for i in range(3):
    env.process(customer(env, "Customer"+str(i+1), server))

env.run()

#3.Change service time

import simpy

def customer(env, server):
    with server.request() as req:
        yield req
        print("Service starts at", env.now)
        yield env.timeout(5)

env = simpy.Environment()
server = simpy.Resource(env, capacity=1)

env.process(customer(env, server))
env.run()

#4.Average Waiting Time

waiting = [1, 2, 3, 4]

avg = sum(waiting) / len(waiting)

print("Average Waiting Time =", avg)
