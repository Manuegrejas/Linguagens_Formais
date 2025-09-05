class AFD:
	def __init__(self):
		# Estados
		self.states = {'q1', 'q2', 'q3'}
		
		# Alfabeto
		self.alphabet = {'0', '1'}

		# Função de transição: (estado atual, simbolo da palavra) -> proximo estado
		self.transitions = {
			'q1': {'0': 'q1', '1': 'q2'},
			'q2': {'0': 'q3', '1': 'q2'},
			'q3': {'0': 'q2', '1': 'q2'},
		}
    
		# Estado inicial
		self.initial_state = 'q1' 
		# Estados finais
		self.final_states = {'q2'}
  
	def process(self, input_string):
		estado_atual = self.initial_state
		for simbolo in input_string:
			if simbolo not in self.alphabet:
				return False
			if simbolo in self.transitions[estado_atual]:
				estado_atual = self.transitions[estado_atual][simbolo]
		return estado_atual in self.final_states

def main():
	afd = AFD()
	palavras = input().strip().split()
	for palavra in palavras:
		resultado = afd.process(palavra)
		if resultado:
			print("aceita")
		else:
			print("rejeita")

if __name__ == "__main__":
	main()