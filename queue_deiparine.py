def run_queue():

    queue = []

    letters = ['D', 'E', 'I', 'P', 'A', 'R', 'I', 'N', 'E']
    for letter in letters:
        queue.append(letter)

    print("Initial Queue (Front is at index 0):")
    print(queue)
    print("-" * 30)

    while len(queue) > 0:
        dequeued_item = queue.pop(0)
        print(f"Dequeued '{dequeued_item}':")
        print(queue)

    print("-" * 30)
    print("Queue is now empty. Stop.")


if __name__ == "__main__":
    run_queue()