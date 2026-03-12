# Open 'poems.txt' in read mode and read all lines into a list
with open('poem.txt', 'r') as f:
    lines = f.readlines()  # Each element in 'lines' is one line from the file

# The word we want to search for (lowercase for consistent comparison)
word = 'twinkle'

# Flag to track whether the word was found at least once
found = False

# Loop through each line with its line number (starting from 1)
for line_num, line in enumerate(lines, start=1):
    
    # Check if the word exists in the current line (case-insensitive)
    if word in line.lower():
        
        # Print the line number and the line content (stripped of extra whitespace)
        print(f"Found '{word}' on line {line_num}: {line.strip()}")
        #print(f"Found '{word}' on line {line_num}: {line}")  # Without Line Strip
        # Set flag to True since the word was found
        found = True

# After checking all lines, print result based on the flag
if not found:
    print(f"The word '{word}' was NOT found in poem.txt")