# Step 1: Start Your Backpack
# Create a list with at least 5 items of different types (strings, numbers, booleans)
backpack = ["water bottle", "compass", "map", 2, True]

print("--- Initial Backpack ---")
# Step 2: Print Your Backpack Contents
print("Entire list:", backpack)
print("First item:", backpack[0])
print("Last item:", backpack[-1])
print("First three items:", backpack[:3])
print()

# Step 3: Check for Specific Items (Using If-Else)
print("--- Checking Items ---")
if "map" in backpack:
    print("Map is packed.")
else:
    print("You forgot your map!")

# Checking for an item that is not in the list
if "tent" in backpack:
    print("Tent is packed.")
else:
    print("You forgot your tent!")
print()

# Step 4: Modify the Backpack
print("--- Modifying Backpack ---")
# Replace the second item (index 1) with "first aid kit"
backpack[1] = "first aid kit"
print("After replacing second item:", backpack)

# Use .append() to add an item to the end
backpack.append("energy bars")
print("After appending 'energy bars':", backpack)

# Use .insert() to place an item at index 2
backpack.insert(2, "flashlight")
print("After inserting 'flashlight' at index 2:", backpack)
print()

# Step 5: Loop Through the Backpack
print("--- Looping Through Backpack ---")
for item in backpack:
    print("Packing:", item)
print()

# Step 6: Double the Quantity (Numeric Items)
print("--- Doubling Numeric Items ---")
for i in range(len(backpack)):
    if isinstance(backpack[i], (int, float)):
        backpack[i] *= 2

print("Backpack after doubling numbers:", backpack)
print()

# Step 7: Safe Access Check
print("--- Safe Access Check ---")
try:
    user_input = input("Enter an index number to check: ")
    index = int(user_input)
    
    # Check if index is within the valid range
    if 0 <= index < len(backpack):
        print(f"Item at slot {index}: {backpack[index]}")
    else:
        print("That slot doesn't exist in your backpack.")
except ValueError:
    print("Please enter a valid integer.")

print()

# Optional Extension: Search Function
print("--- Search Function Test ---")
def check_item(item_name):
    if item_name in backpack:
        return f"{item_name} is packed!"
    else:
        return f"{item_name} is missing!"

print(check_item("map"))
print(check_item("sunscreen"))