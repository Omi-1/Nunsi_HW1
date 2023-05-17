def compress_string(s):
    compressed = ''
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1

    # Add the last character and its count
    compressed += s[-1] + str(count)

    return compressed

# Read the input string
input_string = input("Enter the string to compress: ")

# Compress the string using the algorithm
compressed_string = compress_string(input_string)

# Output the compressed string
print(compressed_string)
