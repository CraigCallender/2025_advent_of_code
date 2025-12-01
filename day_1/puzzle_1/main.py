def main():
    print("Hello from puzzle-1!")

    max_position = 99
    min_position = 0
    starting_position = 50
    current_position = starting_position
    times_at_zero = 0

    with open('data/input.txt', 'r') as input_file:
        for line in input_file:
            direction = line[0]
            raw_distance = int(line[1:].strip())
            distance = raw_distance % 100
            print(f"Current: {current_position} -> Direction: {direction}, Distance: {distance}")

            if direction == 'R':
                current_position += distance
                if current_position > max_position:
                    current_position -= 100
            elif direction == 'L':
                current_position -= distance
                if current_position < min_position:
                    current_position += 100
            
            if current_position == 0:
                times_at_zero += 1
    
    print(f"Number of times at position 0: {times_at_zero}")


if __name__ == "__main__":
    main()
