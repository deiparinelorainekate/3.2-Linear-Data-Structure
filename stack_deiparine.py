def run_stack():

    stack = []

    letters = ['D', 'E', 'I', 'P', 'A', 'R', 'I', 'N', 'E']
    for letter in letters:
        stack.append(letter)

    print("Initial Stack (Top is at the right end):")

    print(stack)
    print("-" * 30)

    while len(stack) > 0:
        popped_item = stack.pop()
        print(f"Popped '{popped_item}':")
        print(stack)

    print("-" * 30)
    print("Stack is now empty. Stop.")


if __name__ == "__main__":
    run_stack()