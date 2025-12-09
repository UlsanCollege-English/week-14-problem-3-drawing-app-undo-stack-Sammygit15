def simulate_history(actions):

    stack = []

    for action in actions:
        if action == "UNDO":
            # Remove the most recent action if any
            if stack:
                stack.pop()
        else:
            # Regular action: push onto the stack
            stack.append(action)

    return stack


if __name__ == "__main__":
    sample = ["DRAW line", "DRAW circle", "UNDO", "FILL blue", "UNDO", "UNDO"]
    print(simulate_history(sample))
