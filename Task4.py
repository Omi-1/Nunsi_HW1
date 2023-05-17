def generate_sequence(n):
    sequence = []
    current_num = 1
    count = 0

    while len(sequence) < n:
        count += 1
        sequence.append(current_num)

        if count == current_num:
            current_num += 1
            count = 0

    return sequence

# Read the input number
n = int(input("Enter the number of elements: "))

# Generate the sequence
result = generate_sequence(n)

# Output the sequence
print(*result)
