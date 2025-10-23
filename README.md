
# ⚙️ Simple Turing Machine Simulator

A general-purpose, interactive Turing Machine simulator written in Python. This tool was created for **educational purposes** to help visualize and understand the inner workings of a Turing Machine, one of the foundational models of theoretical computer science.

Unlike other simulators with hardcoded rules, this script allows you to define the entire machine at runtime: its states, alphabets, and transition functions.

---

## 🚀 Features

* **Interactive Setup**: Define every component of the machine (states, alphabet, etc.) through simple command-line prompts.
* **General-Purpose**: Not tied to a specific problem. You can use it to simulate any algorithm that can be run on a Turing Machine.
* **Step-by-Step Simulation**: Displays the tape's status, head position, and current state at every single step of the computation.
* **Infinite Tape**: Efficiently simulates an infinite tape in both directions using a Python dictionary.
* **Input Validation**: Includes basic checks to ensure the user-provided definitions are consistent (e.g., the initial state must be in the set of states).

---

## 📚 Prerequisites

To run this script, you only need:

* **Python 3.6** or newer.

No external libraries are required.

---

## ▶️ How to Run

1.  **Download the file**: Make sure you have the `turing_simulator.py` file on your computer.
2.  **Open a terminal**: Open a terminal window (or Command Prompt on Windows).
3.  **Navigate to the folder**: Use the `cd` command to move to the directory where you saved the file.
    ```bash
    cd /path/to/your/folder
    ```
4.  **Run the script**: Execute the following command:
    ```bash
    python turing_simulator.py
    ```
5.  **Define the Machine**: Follow the on-screen prompts to define:
    * The states (`q0, q1, qf, ...`)
    * The input alphabet (`0, 1, ...`)
    * The tape alphabet (`0, 1, X, _, ...`)
    * The initial state, accept states, and the blank symbol.
    * The transition rules, one by one.
6.  **Enter the Input**: Provide the initial string to be written on the tape.
7.  **Watch the Simulation**: The program will show each step of the execution until it halts.

---

## ✨ Example: Incrementing a Binary Number

Let's see how to use the simulator for a machine that adds 1 to a binary number (e.g., `1011` → `1100`).

1.  Start the script with `python turing_simulator.py`.
2.  Enter the following definitions when prompted:

    * **States**: `q0, q1, qf`
    * **Input alphabet**: `0, 1`
    * **Tape alphabet**: `0, 1, _`
    * **Initial state**: `q0`
    * **Accept states**: `qf`
    * **Blank symbol**: `_`
    * **Transition Functions** (enter them one by one, then type `done`):
        ```
        q0,0,0,R,q0
        q0,1,1,R,q0
        q0,_,_,L,q1
        q1,1,0,L,q1
        q1,0,1,R,qf
        q1,_,1,R,qf
        ```
    * **Initial tape string**: `1011`

#### Expected Output

The simulator will show the intermediate steps and halt with an accept message, displaying the final tape:

```
[...]
--- Step: 8 ---
State: qf
Tape: ..._1100_...
Head:      ^

ACCEPT: Halted in accepting state 'qf'.
Final tape content: 1100
```

---

## 🔧 Customization

### Adding a Neutral ('N') Move

If you want the head to have the option to stay in place, you can easily modify the `run` method in the `TuringMachine` class to support a neutral `'N'` move.

Replace this block:
```python
# 2. Move the head
if move_direction.upper() == 'R':
    self.head_position += 1
elif move_direction.upper() == 'L':
    self.head_position -= 1
```
with this:
```python
# 2. Move the head
if move_direction.upper() == 'R':
    self.head_position += 1
elif move_direction.upper() == 'L':
    self.head_position -= 1
elif move_direction.upper() == 'N':
    pass # Do nothing if the move is Neutral
```
Remember to also update the input validation logic to accept `'N'` as a valid move.

---

## 👤 Author

Created with the assistance of Gemini.

## 📄 License

This project is released under the MIT License.
