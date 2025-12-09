[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/8gopUgpp)
# HW03 — Drawing App Undo Stack

## Story

You are building the **undo system** for a simple drawing application.

Each user action is logged as a string:

- `"DRAW line"`
- `"DRAW circle"`
- `"FILL red"`
- `"UNDO"`

Your job is to process this list of actions and return the final list of actions that remain after all `"UNDO"` operations are applied, using a **stack**.

---

## Technical Description

Implement in `main.py`:

```python
simulate_history(actions) -> list[str]
```

### Inputs

- `actions`: a list of strings
  - Regular actions: any string that is **not exactly** `"UNDO"`
  - Special action: the string `"UNDO"`

### Behavior

- Use a stack to store actions that are still “active”.
- For each action in order:
  - If it is `"UNDO"`:
    - Remove (“pop”) the **most recent** action from the stack, if there is one.
    - If the stack is empty, `"UNDO"` does nothing (no error).
  - Otherwise:
    - Push the action onto the stack.
- At the end, return the stack as a list (from oldest to newest).

### Outputs

- A list of strings representing the final sequence of actions that remain

### Constraints

- Time complexity: **O(N)** where N = `len(actions)`
- Space complexity: **O(N)** in the worst case (if there are no `"UNDO"` actions)
- Do not mutate the input list in ways that break the logic (e.g., deleting items while iterating)

---

## 8 Steps of Coding (lighter scaffold)

For this homework, you still **use all 8 steps**, but the prompts are shorter.

1. **Read and understand the problem**
   - What does `"UNDO"` do? What does the final list represent?

2. **Re-phrase the problem**
   - Describe how you transform the input list into the output list

3. **Identify input, output, variables**
   - Input: `actions` (list of strings)
   - Output: final list of strings (the stack contents)
   - Variables: the stack, a loop variable, maybe a helper for results

4–8. **Student-driven (on your worksheet or scratch)**
   - 4: Break the problem into simple steps
   - 5: Write pseudocode for stack operations
   - 6: Translate pseudocode to Python
   - 7: Debug with small examples
   - 8: Check complexity and any unnecessary work

---

## Hints

1. In Python, a regular list can be used as a stack with `append()` and `pop()`
2. Remember that `"UNDO"` on an empty stack should **not** crash the program
3. Test a case with **many** `"UNDO"` commands in a row

---

## How to Run Tests Locally

From the project root:

```bash
python -m pytest -q
```

Pytest will discover `hw03/tests/test_hw03.py`.

---
## FAQ

**Q1: Do I need to worry about invalid actions?**

For this assignment, treat any string not equal to `"UNDO"` as a normal drawing action.

**Q2: What if there are more `"UNDO"` commands than normal actions?**

Extra `"UNDO"` commands should just do nothing when the stack is empty.

**Q3: What Big-O do you expect?**

O(N) time, O(N) space. One pass over the actions, using a stack.

**Q4: Can I use a deque instead of a list?**

You could, but a Python list is enough for push/pop at the end.

**Q5: Why are we using a stack here?**

Undo systems naturally use LIFO behavior ("last thing done is the first thing rolled back").

**Q6: Pytest says my result is different but I think it is the same.**

Check exact order and spaces in strings. `"DRAW circle"` is different from `"DRAW  circle"` (two spaces).

**Q7: Can I print inside the function?**

You can while debugging, but remove or comment out prints before final submission.
