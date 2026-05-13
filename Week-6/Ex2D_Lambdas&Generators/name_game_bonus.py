# Description: This script demonstrates functions, string logic, and a generator function
# Author: Dimitri Nji

# Prompt the user for a name
user_name = input("Enter a name: ")


def trunc_name(name):
    name = name.lower().strip()

    vowels = "aeiou"

    # If the name starts with a vowel, keep the whole name
    if name[0] in vowels:
        return name

    # If the first two letters are consonants, remove both
    elif len(name) > 1 and name[0] not in vowels and name[1] not in vowels:
        return name[2:]

    # Otherwise, remove only the first consonant
    else:
        return name[1:]


# Test the function first
# print(trunc_name(user_name))


def name_game(name):
    lower_name = name.lower().strip()
    display_name = name.strip().title()

    blocked_names = ["bart", "buck"]

    if lower_name in blocked_names:
        yield f"Warning: {display_name} may create an inappropriate rhyme, so this name will not be used."
        return

    short_name = trunc_name(name)

    # Special rule for names that start with b, f, or m
    if lower_name.startswith("b"):
        b_part = short_name
    else:
        b_part = "b" + short_name

    if lower_name.startswith("f"):
        f_part = short_name
    else:
        f_part = "f" + short_name

    if lower_name.startswith("m"):
        m_part = short_name
    else:
        m_part = "m" + short_name

    yield f"{display_name}, {display_name}, bo-{b_part}"
    yield f"banana fana fo-{f_part}"
    yield f"me my mo-{m_part}"
    yield f"{display_name}!"


# Print the user name version
print()
print("User name example:")
for line in name_game(user_name):
    print(line)


# Print the required test examples
print()
print("Required examples:")

test_names = ["Dimitri", "carly", "CHARLIE", "Aidan", "Braden", "Billy Bob"]

for name in test_names:
    print()
    for line in name_game(name):
        print(line)


# Observation:
# Names with different capitalization still work because the function converts the name to lowercase.
# Names that start with a vowel keep the full name.
# Names that start with one consonant remove the first letter.
# Names that start with two consonants remove the first two letters.
# Names starting with b, f, or m use the special rule so the same sound is not repeated.