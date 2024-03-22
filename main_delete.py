#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.db_storage import DBStorage
from models.state import State

db_storage = DBStorage()

# All States
all_states = db_storage.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
db_storage.new(new_state)
db_storage.save()
print("New State: {}".format(new_state))

# All States
all_states = db_storage.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = State()
another_state.name = "Nevada"
db_storage.new(another_state)
db_storage.save()
print("Another State: {}".format(another_state))

# All States
all_states = db_storage.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Delete the new State
db_storage.delete(new_state)

# All States
all_states = db_storage.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
