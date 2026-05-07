# Calculate how many boxes of tiles are needed

import math

length = float(input("Enter the room length in feet: "))
width = float(input("Enter the room width in feet: "))

room_area = length * width
tiles_needed = room_area
extra_tiles = tiles_needed * 1.10

boxes_needed = math.ceil(tiles_needed / 12)
total_boxes_with_extra = math.ceil(extra_tiles / 12)

print(f"Room area: {room_area:.2f} square feet")
print(f"Boxes needed without extra tiles: {boxes_needed}")
print(f"Total boxes needed with 10% extra: {total_boxes_with_extra}")