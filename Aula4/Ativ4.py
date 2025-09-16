class AFN:
    def __init__(self):
        self.states = []
        self.orig_alphabet = []
        self.alphabet = []
        self.initial_state = None
        self.final_states = []
        self.transition_function = {}
        self.empty_tokens = {'vazio', '_', '-', 'eps', 'epsilon', 'ε', ''}

    def startup(self):
        self.states = [s.strip() for s in input().strip().split()]
        self.orig_alphabet = [a.strip() for a in input().strip().split()]
        self.alphabet = list(self.orig_alphabet) + ['vazio']
        self.initial_state = input().strip()
        finals_line = input().strip()
        self.final_states = finals_line.split() if finals_line else []
        needed = len(self.alphabet)
        for estado in self.states:
            line = input().strip()
            parts = line.split() if line else []
            if parts and parts[0] in self.states:
                parts = parts[1:]
            if len(parts) < needed:
                parts += ['vazio'] * (needed - len(parts))
            self.transition_function[estado] = {}
            for i, simbolo in enumerate(self.alphabet):
                token = parts[i].strip()
                if token in self.empty_tokens:
                    destinos = []
                else:
                    destinos = [t.strip() for t in token.split(',') if t.strip()]
    
self.transition_function[estado][simbolo] = destinos

    def epsilon_closure(self, estados):
        closure = list(estados)
        i = 0
        while i < len(closure):
            s = closure[i]
            for dest in self.transition_function.get(s, {}).get('vazio', []):
                closure.append(dest)
            i += 1
        return closure

    def _print_states_in_order(self, states_list):
        ordered = []
        for s in self.states:
            for st in states_list:
                if s == st:
                    ordered.append(s)
        print("[" + ", ".join("'" + s + "'" for s in ordered) + "]")

    def process_word(self, palavra):
        current_states = self.epsilon_closure([self.initial_state])
        self._print_states_in_order(current_states)
        for simbolo in palavra:
            print(simbolo)
            if simbolo not in self.orig_alphabet:
                current_states = []
                self._print_states_in_order(current_states)
                continue
                next_states = []
                for estado in current_states:
                    destinos = self.transition_function.get(estado, {}).get(simbolo, [])
                    for d in destinos:
                        next_states.extend(self.epsilon_closure([d]))
                current_states = next_states
        self._print_states_in_order(current_states)
        if any(s in self.final_states for s in current_states):
            print("aceita")
        else:
            print("rejeita")

def main():
    afn = AFN()
    afn.startup()
    line = input().strip()
    if not line:
        return
    palavras = line.split()
    for palavra in palavras:
        afn.process_word(palavra)

if __name__ == "__main__":
    main()