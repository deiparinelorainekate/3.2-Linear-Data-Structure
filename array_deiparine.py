def run_array():

    my_array = []

    letters = ['D', 'E', 'I', 'P', 'A', 'R', 'I', 'N', 'E']
    for letter in letters:
        my_array.append(letter)

    print("Initial Array:")

    print(my_array)
    print("-" * 30)

    while len(my_array) > 0:
        removed_item = my_array.pop(0)
        print(f"Removed '{removed_item}':")
        print(my_array)

    print("-" * 30)
    print("Array is now empty. Stop.")


if __name__ == "__main__":
    run_array()