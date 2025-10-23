class TuringMachine:

    def __init__(self, states, input_alphabet, tape_alphabet, blank_symbol,
                 initial_state, accept_states, transitions):
        # --- Formal Definition Components ---
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.blank_symbol = blank_symbol
        self.initial_state = initial_state
        self.accept_states = accept_states
        self.transitions = transitions
        # --- Simulation Components ---
        self.tape = {}
        self.head_position = 0
        self.current_state = self.initial_state
        self.step_count = 0

    def _initialize_tape(self, input_string):
        """Loads the initial string onto the tape."""
        for i, char in enumerate(input_string):
            if char not in self.tape_alphabet:
                raise ValueError(f"Symbol '{char}' not in tape alphabet.")
            self.tape[i] = char
        self.head_position = 0
        self.current_state = self.initial_state
        self.step_count = 0

    def _print_status(self):
        """Prints the current configuration of the machine."""
        print(f"\n--- Step: {self.step_count} ---")
        print(f"State: {self.current_state}")
        
        # Determine the range of the tape to print
        if not self.tape:
            min_pos, max_pos = 0, 0
        else:
            min_pos = min(self.tape.keys())
            max_pos = max(self.tape.keys())
        
        # Adjust range to include the head if it's outside current tape bounds
        print_min = min(min_pos, self.head_position)
        print_max = max(max_pos, self.head_position)

        # Build tape string
        tape_str = ""
        for i in range(print_min -1, print_max + 2):
            tape_str += self.tape.get(i, self.blank_symbol)

        # Build head indicator string
        head_indicator = " " * (self.head_position - print_min + 1) + "^"

        print(f"Tape: ...{tape_str}...")
        print(f"Head:   {head_indicator}")


    def run(self, input_string):
        """Runs the simulation on a given input string."""
        self._initialize_tape(input_string)
        self._print_status()

        while self.current_state not in self.accept_states:
            # Get the symbol under the head, defaulting to the blank symbol
            current_symbol = self.tape.get(self.head_position, self.blank_symbol)

            # Find the transition rule for the current state and symbol
            action_key = (self.current_state, current_symbol)
            if action_key not in self.transitions:
                print(f"\nHALT: No transition rule found for state '{self.current_state}' and symbol '{current_symbol}'.")
                break
            
            new_symbol, move_direction, new_state = self.transitions[action_key]

            # 1. Write the new symbol to the tape
            self.tape[self.head_position] = new_symbol

            # 2. Move the head
            if move_direction.upper() == 'R':
                self.head_position += 1
            elif move_direction.upper() == 'L':
                self.head_position -= 1
            
            # 3. Transition to the new state
            self.current_state = new_state
            self.step_count += 1
            
            self._print_status()
            
            # Safety break to prevent very long or infinite loops in testing
            if self.step_count > 1000:
                print("\nHALT: Exceeded maximum steps (1000).")
                break

        if self.current_state in self.accept_states:
            print(f"\nACCEPT: Halted in accepting state '{self.current_state}'.")
        
        # Display final tape content
        sorted_keys = sorted(self.tape.keys())
        final_tape = "".join(self.tape.get(i, self.blank_symbol) for i in range(sorted_keys[0], sorted_keys[-1] + 1))
        print(f"Final tape content: {final_tape.strip(self.blank_symbol)}")


def get_user_definitions():
    """Interactively gets all Turing machine definitions from the user."""
    print("--- Definizione della Macchina di Turing ---")
    
    # Simple parsing by splitting on commas
    states = set(s.strip() for s in input("Inserisci gli stati, separati da virgola (es. q0,q1,qf): ").split(','))
    input_alphabet = set(s.strip() for s in input("Inserisci l'alfabeto di input, separato da virgola (es. 0,1): ").split(','))
    tape_alphabet = set(s.strip() for s in input("Inserisci l'alfabeto del nastro (deve includere quello di input, es. 0,1,X,_): ").split(','))
    initial_state = input("Inserisci lo stato iniziale (es. q0): ").strip()
    accept_states = set(s.strip() for s in input("Inserisci gli stati di accettazione, separati da virgola (es. qf): ").split(','))
    blank_symbol = input("Inserisci il simbolo di blank (es. _): ").strip()

    # --- Input Validation ---
    if initial_state not in states:
        raise ValueError("Lo stato iniziale non è nel set di stati.")
    if not accept_states.issubset(states):
        raise ValueError("Gli stati di accettazione non sono un sottoinsieme del set di stati.")
    if not input_alphabet.issubset(tape_alphabet):
        raise ValueError("L'alfabeto di input non è un sottoinsieme dell'alfabeto del nastro.")
    if blank_symbol not in tape_alphabet:
        raise ValueError("Il simbolo di blank deve essere nell'alfabeto del nastro.")

    transitions = {}
    print("\n--- Definizione delle Funzioni di Transizione ---")
    print("Inserisci le regole nel formato: stato_corrente,simbolo_letto,nuovo_simbolo,movimento (R o L),nuovo_stato")
    print("Esempio: q0,1,X,R,q1")
    print("Scrivi 'fine' quando hai terminato.")
    
    while True:
        rule_str = input("> ")
        if rule_str.lower() == 'fine':
            break
        try:
            current_s, read_sym, write_sym, move, next_s = (s.strip() for s in rule_str.split(','))
            
            # More validation
            if current_s not in states or next_s not in states:
                print("ERRORE: Uno degli stati non è valido. Riprova.")
                continue
            if read_sym not in tape_alphabet or write_sym not in tape_alphabet:
                print("ERRORE: Uno dei simboli non è nell'alfabeto del nastro. Riprova.")
                continue
            if move.upper() not in ['L', 'R']:
                print("ERRORE: Il movimento deve essere 'L' o 'R'. Riprova.")
                continue
            
            transitions[(current_s, read_sym)] = (write_sym, move.upper(), next_s)
            print(f"Regola aggiunta: ({current_s}, {read_sym}) -> ({write_sym}, {move.upper()}, {next_s})")
        except ValueError:
            print("Formato non valido. Assicurati di usare 5 elementi separati da virgola. Riprova.")

    return {
        "states": states,
        "input_alphabet": input_alphabet,
        "tape_alphabet": tape_alphabet,
        "blank_symbol": blank_symbol,
        "initial_state": initial_state,
        "accept_states": accept_states,
        "transitions": transitions
    }

if __name__ == "__main__":
    try:
        definitions = get_user_definitions()
        tm = TuringMachine(**definitions)
        
        initial_tape = input("\nInserisci la stringa iniziale sul nastro: ")
        tm.run(initial_tape)
        
    except (ValueError, KeyError) as e:
        print(f"\nErrore di configurazione: {e}")