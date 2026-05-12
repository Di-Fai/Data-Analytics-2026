# Description: This script practices using lists, len(), sorted(), sort(), and append()
# Author: Dimitri Nji

favorite_movies = ["Black Panther", "Inception", "Avatar", "Creed", "The Batman"]

# Print the length of the list inside a descriptive sentence
print(f"The list favorite_movies includes my top {len(favorite_movies)} favorite movies")

# Print the complete list
print(favorite_movies)

# Use sorted() to print the list in alphabetical order
print(sorted(favorite_movies))

# Print the original list again
print(favorite_movies)

# Observation:
# sorted() displays the list in alphabetical order, but it does not permanently change the original list.

# Use .sort() to permanently sort the list
favorite_movies.sort()

# Print the list again
print(favorite_movies)

# Observation:
# .sort() permanently changes the order of the original list.

# Add another movie using .append()
favorite_movies.append("Spider-Man: No Way Home")

# Print updated description and updated list
print(f"The list favorite_movies now includes my top {len(favorite_movies)} favorite movies")
print(favorite_movies)

# Group comparison observation:
# My group members and I should get similar results if we use len(), sorted(), .sort(), and .append() correctly.
# The movie titles may be different, but the list behavior should be the same.

