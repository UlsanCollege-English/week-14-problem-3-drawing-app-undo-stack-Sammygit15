
## main.py
```python
"""
HW03 — Drawing App Undo Stack

Implement simulate_history(actions) that applies "UNDO" commands using a stack
and returns the final list of actions.
"""


def simulate_history(actions):
    """
    Process a list of actions for a drawing app and apply UNDO behavior.

    :param actions: list of strings; "UNDO" means remove the most recent action
    :return: list of strings representing the remaining actions
    """
    # TODO (8 Steps of Coding, short version):
    # 1. Make sure you understand what UNDO does to the stack.
    # 2. Re-phrase the task in your own words.
    # 3. Identify inputs, outputs, and the stack variable.
    # 4. Break the algorithm into small steps on paper.
    # 5. Write pseudocode (loop over actions, push or pop).
    # 6. Translate to Python using a list as a stack.
    # 7. Debug with small examples (including extra UNDOs).
    # 8. Check that you only loop once (O(N)).
    raise NotImplementedError("Implement simulate_history in main.py")


if __name__ == "__main__":
    sample = ["DRAW line", "DRAW circle", "UNDO", "FILL blue", "UNDO", "UNDO"]
    print(simulate_history(sample))
