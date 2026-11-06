
# ============================================================
# MAJI NDOGO — BUILDING THE DIGITAL TWIN
# Author: Cornelius-Snowhyt
# Standalone Python version (no Marimo required)
# ============================================================


# CHALLENGE 1: Read the fuel gauge
def fuel_status(fuel_level, fuel_capacity):
    if fuel_level == 0:
        return "Empty"

    fraction = fuel_level / fuel_capacity

    if fraction < 0.25:
        return "Low"
    elif fraction < 1.0:
        return "OK"
    else:
        return "Full"


# CHALLENGE 2: Count planted cells
def count_planted_cells(field):
    count = 0

    for row in field:
        for cell in row:
            if cell == 1:
                count += 1

    return count


# CHALLENGE 3: Drive the tractor down a row
def drive_and_plant(row):
    index = 0

    while index < len(row):
        if row[index] == -1:
            break

        row[index] = 1
        index += 1

    return row


# CHALLENGE 4: Calculate total fleet horsepower
def total_horsepower(fleet):
    total = 0

    for vehicle in fleet:
        total += vehicle["horsepower"]

    return total


# CHALLENGE 5: Identify low-fuel models
def low_fuel_models(fleet, threshold):
    return [
        vehicle["model"]
        for vehicle in fleet
        if vehicle["fuel_capacity"] < threshold
    ]


# CHALLENGE 6: Calculate revenue for each crop
def revenue_by_crop(harvest_kg, price_per_kg):
    return {
        crop: kg * price_per_kg[crop]
        for crop, kg in harvest_kg.items()
    }


# CHALLENGE 7: Compare two farms' crop plans
def compare_crop_plans(farm_a_crops, farm_b_crops):
    farm_a = set(farm_a_crops)
    farm_b = set(farm_b_crops)

    return {
        "shared": sorted(farm_a & farm_b),
        "only_in_a": sorted(farm_a - farm_b),
        "all_crops": sorted(farm_a | farm_b)
    }


# CHALLENGE 8: Maintain the regional harvest registry
def record_harvest(registry, farm_id, crop, kg):
    if farm_id not in registry:
        registry[farm_id] = {}

    if crop in registry[farm_id]:
        registry[farm_id][crop] += kg
    else:
        registry[farm_id][crop] = kg

    return registry


# ============================================================
# TESTING THE EIGHT CHALLENGES
# ============================================================

print("\n========== MAJI NDOGO DIGITAL TWIN ==========")

# Challenge 1
print("\n1. FUEL STATUS")
print("Fuel 10/60:", fuel_status(10, 60))
print("Fuel 60/60:", fuel_status(60, 60))

# Challenge 2
print("\n2. PLANTED CELLS")
field = [[1, 0, 1], [0, 1, 0]]
print("Planted cells:", count_planted_cells(field))

# Challenge 3
print("\n3. TRACTOR MOVEMENT")
print("With obstacle:", drive_and_plant([0, 1, 0, -1, 0]))
print("Without obstacle:", drive_and_plant([0, 0, 0, 0]))

# Fleet data used by Challenges 4 and 5
fleet = [
    {
        "model": "TX-1300",
        "colour": "Green",
        "horsepower": 150,
        "fuel_capacity": 60
    },
    {
        "model": "RX-850",
        "colour": "Red",
        "horsepower": 120,
        "fuel_capacity": 45
    },
    {
        "model": "SX-750",
        "colour": "White",
        "horsepower": 180,
        "fuel_capacity": 80
    }
]

# Challenge 4
print("\n4. TOTAL FLEET HORSEPOWER")
print("Combined horsepower:", total_horsepower(fleet))

# Challenge 5
print("\n5. LOW-FUEL MODELS")
print("Below 50:", low_fuel_models(fleet, 50))
print("Below 70:", low_fuel_models(fleet, 70))

# Challenge 6
print("\n6. REVENUE BY CROP")
harvest = {"wheat": 2050, "potato": 3600}
prices = {"wheat": 2, "potato": 1.4}
print("Crop revenue:", revenue_by_crop(harvest, prices))

# Challenge 7
print("\n7. COMPARE CROP PLANS")
farm_a = ["wheat", "potato", "maize", "wheat"]
farm_b = ["potato", "rice", "maize"]
print("Comparison:", compare_crop_plans(farm_a, farm_b))

# Challenge 8
print("\n8. REGIONAL HARVEST REGISTRY")
registry = {}

record_harvest(registry, 18442, "wheat", 2050)
print("First harvest:", registry)

record_harvest(registry, 18442, "wheat", 500)
print("Updated harvest:", registry)

print("\n========== DIGITAL TWIN TESTS COMPLETE ==========")

if __name__ == "__main__":

    print("BUILDING THE DIGITAL TWIN")
    print("=" * 40)

    # Challenge 1: Fuel status
    print("\n1. FUEL STATUS")
    print("Fuel at 10/60:", fuel_status(10, 60))
    print("Fuel at 60/60:", fuel_status(60, 60))

    # Challenge 2: Count planted cells
    print("\n2. COUNT PLANTED CELLS")
    field = [
        [1, 0, 1],
        [0, 1, 0]
    ]
    print("Planted cells:", count_planted_cells(field))

    # Challenge 3: Drive and plant
    print("\n3. DRIVE AND PLANT")
    row = [0, 1, 0, -1, 0]
    print("Field before:", row)
    print("Field after:", drive_and_plant(row))

    # Challenge 4: Total horsepower
    print("\n4. TOTAL HORSEPOWER")
    fleet = [
        {"model": "TX-1300", "horsepower": 300, "fuel_capacity": 60},
        {"model": "RX-850", "horsepower": 150, "fuel_capacity": 40}
    ]
    print("Total horsepower:", total_horsepower(fleet))

    # Challenge 5: Low-fuel models
    print("\n5. LOW-FUEL MODELS")
    print("Below 50:", low_fuel_models(fleet, 50))
    print("Below 70:", low_fuel_models(fleet, 70))

    # Challenge 6: Revenue by crop
    print("\n6. REVENUE BY CROP")
    harvest = {"wheat": 2050, "potato": 3600}
    prices = {"wheat": 2, "potato": 1.4}
    print("Revenue:", revenue_by_crop(harvest, prices))

    # Challenge 7: Compare crop plans
    print("\n7. COMPARE CROP PLANS")
    farm_a = {"maize", "potato", "wheat"}
    farm_b = {"maize", "potato", "rice"}
    print("Comparison:", compare_crop_plans(farm_a, farm_b))

    # Challenge 8: Record harvest
    print("\n8. RECORD HARVEST")
    registry = {}
    record_harvest(registry, "Farm A", "wheat", 2050)
    record_harvest(registry, "Farm A", "wheat", 500)
    print("Harvest registry:", registry)

    print("\n" + "=" * 40)
    print("DIGITAL TWIN TESTS COMPLETED")
