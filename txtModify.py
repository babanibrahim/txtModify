import sys

# Get the input and output filenames from the command line
input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Open the input file for reading
with open(input_filename, 'r', encoding='utf-8') as input_file:
    # Create a set to store unique words
    unique_words = set()

    # Read each line from the input file and split into words
    for line in input_file:
        words = line.split()

        # Add each word to the set
        for word in words:
            unique_words.add(word)

# Open the output file for writing
with open(output_filename, 'w', encoding='utf-8') as output_file:
    # Write the unique words to the output file
    for word in unique_words:
        output_file.write(word + '\n')
