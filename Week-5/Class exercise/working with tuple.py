# U.S. States Tuple Exercise

states = ("New York", "California", "Texas", "Florida", "Illinois")

total_states = len(states)
first_state = states[0]
last_state = states[-1]
texas_check = "Texas" in states
alphabetical_states = sorted(states)
longest_state = max(states, key=len)
longest_length = len(longest_state)

print(f"Total number of states: {total_states}")
print(f"First state: {first_state}")
print(f"Last state: {last_state}")
print(f"Is Texas in the tuple? {texas_check}")
print(f"States in alphabetical order: {alphabetical_states}")
print(f"Longest state name length: {longest_length}")