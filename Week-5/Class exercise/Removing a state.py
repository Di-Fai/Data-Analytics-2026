
# Create a set with at least 5 U.S. states
states = {"Texas", "Florida", "Delaware", "New Jersey", "California"}
print(f"Total number of states: {len(states)}")
print(f"Is Texas in the set? {'Texas' in states}")
print(f"States in alphabetical order: {sorted(states)}")
longest_state = max(states, key=len)
print(f"The longest state name is {longest_state} with {len(longest_state)} characters.")
states.add("Georgia")
print(f"Updated set after adding Georgia: {states}")
states.discard("Florida")
print(f"Updated set after removing Florida: {states}")  