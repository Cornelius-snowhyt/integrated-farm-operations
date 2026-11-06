"""
Tractor Traversal
Standalone Python version for running in VS Code.

Cornelius-Snowhyt
"""

def tractor_movement_standard(field):
    """Return every field position, moving left-to-right row by row."""
    positions = []

    for row_index, row in enumerate(field):
        for col_index in range(len(row)):
            positions.append((row_index, col_index))

    return positions


def reverse_list(input_list):
    """Return a new list with the items in reverse order."""
    return input_list[::-1]


def tractor_movement_realistic(field, start_direction="right"):
    """
    Return field positions in an alternating, back-and-forth pattern.

    With start_direction="right", the first row moves left-to-right.
    With start_direction="left", the first row moves right-to-left.
    """
    if start_direction not in ("right", "left"):
        raise ValueError("start_direction must be 'right' or 'left'")

    positions = []

    for row_index, row in enumerate(field):
        columns = list(range(len(row)))

        if start_direction == "right":
            if row_index % 2 == 1:
                columns = reverse_list(columns)
        else:
            if row_index % 2 == 0:
                columns = reverse_list(columns)

        for col_index in columns:
            positions.append((row_index, col_index))

    return positions


def field_summary(field):
    """Return the row count, total cell count, and rectangular-field status."""
    num_rows = len(field)
    total_cells = 0

    for row in field:
        total_cells += len(row)

    is_rectangular = len(set(len(row) for row in field)) <= 1

    return num_rows, total_cells, is_rectangular


def total_fuel_used(*segment_costs):
    """Return the total fuel used across all supplied segments."""
    return sum(segment_costs)


def log_trip(tractor_id, **details):
    """Return a dictionary containing the tractor ID and trip details."""
    trip_record = {"tractor_id": tractor_id}
    trip_record.update(details)

    return trip_record


def main():
    # Small example fields so the functions can be tested immediately.
    field_standard = [
        ["soil", "soil", "soil"],
        ["soil", "soil", "soil"],
    ]

    field_irregular = [
        ["soil", "soil", "soil"],
        ["soil", "soil"],
    ]

    print("1. Standard tractor movement:")
    print(tractor_movement_standard(field_standard))

    print("\n2. Reverse a list:")
    print(reverse_list([0, 1, 2, 3, 4]))

    print("\n3. Realistic tractor movement (starting left):")
    print(tractor_movement_realistic(field_standard, start_direction="left"))

    print("\n4. Standard field summary:")
    print(field_summary(field_standard))

    print("\n   Irregular field summary:")
    print(field_summary(field_irregular))

    print("\n5. Total fuel used:")
    print(total_fuel_used(2.5, 1.0, 0.5))

    print("\n6. Trip record:")
    print(log_trip("TX-1300", rows_covered=10, fuel_used=4.0))


if __name__ == "__main__":
    main()