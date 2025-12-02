MAX_POSITION = 99
MIN_POSITION = 0

def ceildiv(a: int, b: int) -> int:
    """Ceiling division of a by b."""
    return -(a // -b)

def spin_right(current: int, distance: int) -> tuple[int, int]:
    """Spin right on a circular track of size 100."""
    """Returns new position and number of times passed position 0."""
    raw_position = current + distance
    new_position = raw_position % 100
    right_distance_to_zero = (MAX_POSITION - current + 1) + MIN_POSITION if current <= MAX_POSITION else 0
    passes_zero = 0

    #print(f"\t\traw_position: {raw_position}, new_position: {new_position}, right_distance_to_zero: {right_distance_to_zero}, passes_zero: {passes_zero}")
    if distance >= right_distance_to_zero:
        #passes_zero = 1 * ceildiv(distance, 100)
        passes_zero += 1 * (distance // 100)

    return new_position, passes_zero

def spin_right_basic(current: int, distance: int) -> tuple[int, int]:
    """Basic version of spin right on a circular track of size 100."""
    """Returns new position and number of times passed position 0."""
    
    passes_zero = 0
    for _ in range(distance):
        current += 1
        if current > MAX_POSITION:
            current = MIN_POSITION
            passes_zero += 1

    if current == MIN_POSITION:
        passes_zero -= 1  # Adjust since being at 0 is not a pass

    return current, passes_zero

def spin_left(current: int, distance: int) -> tuple[int, int]:
    """Spin left on a circular track of size 100."""
    """Returns new position and number of times passed position 0."""
    raw_position = current - distance
    new_position = raw_position % 100
    left_distance_to_zero = current - MIN_POSITION if current >= MIN_POSITION else 0
    passes_zero = 0

    #print(f"\t\traw_position: {raw_position}, new_position: {new_position}, left_distance_to_zero: {left_distance_to_zero}, passes_zero: {passes_zero}")
    if distance >= left_distance_to_zero and left_distance_to_zero != 0:
        passes_zero += 1 * ceildiv(distance, 100)

    return new_position, passes_zero

def spin_left_basic(current: int, distance: int) -> tuple[int, int]:
    """Basic version of spin left on a circular track of size 100."""
    """Returns new position and number of times passed position 0."""
    
    passes_zero = 0
    for _ in range(distance):
        current -= 1
        if current < MIN_POSITION:
            current = MAX_POSITION
            passes_zero += 1

    if current == MIN_POSITION:
        passes_zero -= 1  # Adjust since being at 0 is not a pass

    return current, passes_zero

def main():
    print("Hello from puzzle-2!")

    starting_position = 50
    current_position = starting_position
    times_at_zero = 0
    passes_zero = 0

    print(f"Before Spin: Current: {current_position}")

    with open('data/input.txt', 'r') as input_file:
        for line in input_file:
            direction = line[0]
            raw_distance = int(line[1:].strip())
            passes = 0

            if direction == 'R':
                current_position, passes = spin_right(current_position, raw_distance)
                passes_zero += passes
            elif direction == 'L':
                current_position, passes = spin_left(current_position, raw_distance)
                passes_zero += passes

            print(f"Direction: {direction}, Distance: {raw_distance} -> After Spin: Current: {current_position}")
            
            if current_position == 0:
                times_at_zero += 1
                passes -= 1
                passes_zero -= 1  # Adjust since being at 0 is not a pass
            
            if passes > 0:
                print(f"\tPassed 0 moving {'right' if direction == 'R' else 'left'} {passes} time(s).")
                print(f"\tCurrent passed 0 count: {passes_zero}")
                
    print(f"Number of times at position 0: {times_at_zero}")
    print(f"Number of times passed position 0: {passes_zero}")
    print(f"Total: {times_at_zero + passes_zero}")


if __name__ == "__main__":
    main()
