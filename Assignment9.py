import simpy
import random

def customer(env, name, server):
    print(f"{name} arrives at {env.now}")

    with server.request() as req:
        yield req

        print(f"{name} starts service at {env.now}")
        yield env.timeout(3)

        print(f"{name} leaves at {env.now}")

def setup(env):
    server = simpy.Resource(env, capacity=1)

    for i in range(5):
        env.process(customer(env, f"Customer-{i+1}", server))
        yield env.timeout(2)

env = simpy.Environment()
env.process(setup(env))
env.run()

import simpy

def customer(env, name, server):
    with server.request() as req:
        yield req
        print(name, "served at", env.now)
        yield env.timeout(3)

def setup(env):
    server = simpy.Resource(env, capacity=2)

    for i in range(5):
        env.process(customer(env, f"Customer-{i+1}", server))
        yield env.timeout(1)

env = simpy.Environment()
env.process(setup(env))
env.run()

import simpy

INTERARRIVAL = 1
SERVICE = 2

def customer(env, name, server):
    with server.request() as req:
        yield req
        yield env.timeout(SERVICE)

def setup(env):
    server = simpy.Resource(env, capacity=1)

    for i in range(10):
        env.process(customer(env, f"C{i+1}", server))
        yield env.timeout(INTERARRIVAL)

env = simpy.Environment()
env.process(setup(env))
env.run()

import simpy

waiting_times = []

def customer(env, name, server):
    arrival = env.now

    with server.request() as req:
        yield req

        wait = env.now - arrival
        waiting_times.append(wait)

        yield env.timeout(3)

def setup(env):
    server = simpy.Resource(env, capacity=1)

    for i in range(5):
        env.process(customer(env, f"C{i+1}", server))
        yield env.timeout(1)

env = simpy.Environment()
env.process(setup(env))
env.run()

avg_wait = sum(waiting_times) / len(waiting_times)
print("Average Waiting Time:", avg_wait)