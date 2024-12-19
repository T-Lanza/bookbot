# Bookbot Project

# Functions
def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_count(file_contents):
    count = len(file_contents.split())
    return count

def char_count(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else: 
            chars[lowered] = 1
    return chars

def sort_on(chars):
    return chars["Qty"]

# Main Loop
def main():
    path = "books/frankenstein.txt"
    file_contents = get_text(path)
    print(file_contents)

    print("======================================")
    print("")
    count = word_count(file_contents)
    print(f"Total words in file: {count}")
    chars = char_count(file_contents)
    list_of_dict = [{"key": key, "value": value} for key, value in chars.items()]
    sorted_list = []
    for item in list_of_dict:
        if list_of_dict[item].isalpha():
            print(f"The {item} as found {value} times")

main()