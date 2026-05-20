# We would like to read the raw file
def read_raw_file():
    file_path = "data/raw_classes.txt" #original path for raw data

    #easier to close fine, open file as read mode (exists, so no problem)
    with open(file_path, 'r') as file:
        raw_text = file.read() # read the entire file, text file is small

    return raw_text #send raw text back to caller

def split_course_blocks(raw_text):
    # Remove extra spaces or blank lines from the beginning and end of the file.
    # This helps avoid creating an empty course block by accident.
    cleaned_text = raw_text.strip()

    # Split the big string into smaller strings.
    # Each course block is separated by one blank line, which is "\n\n".
    course_blocks = cleaned_text.split("\n\n")

    # Return the list of course blocks.
    return course_blocks

def main(): 
        # Read the full contents of raw_classes.txt.
    course_text = read_raw_file()

    # Split the raw text into individual course blocks.
    course_blocks = split_course_blocks(course_text)

    # Print the number of course blocks found.
    # len(course_blocks) counts how many items are in the list.
    print("Number of course blocks found:", len(course_blocks))

    # Print a blank line to make the output easier to read.
    print()

    # Loop through each course block in the list.
    for block in course_blocks:

        # Print a divider so we can clearly see where each block starts.
        print("----- COURSE BLOCK -----")

        # Print the current course block.
        print(block)

        # Print a blank line after each block for readability.
        print()


#calls main and the read_raw_file function when the script is executed
main()

