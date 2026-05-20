# We would like to read the raw file
def read_raw_file():
    file_path = "data/raw_data.txt" #original path for raw data

    #easier to close fine, open file as read mode (exists, so no problem)
    with open(file_path, 'r') as file:
        raw_text = file.read() # read the entire file, text file is small

    return raw_text #send raw text back to caller

def main(): 
    courses_text = read_raw_file() 