class AFD:
  def __init__(self):
    self.states = []
    self.alphabet = []
    self.initial_state = None
    self.final_states = set()
    self.transition_function = {}
  
  def startup(self):
    # Ler estados
    self.states = [s.strip() for s in input().strip().split()]
    # Ler estado inicial
    self.initial_state = input().strip()
    # Ler estados finais
    self.final_states = set(s.strip() for s in input().strip().split())
    # Ler alfabeto
    self.alphabet = [a.strip() for a in input().strip().split()]
    # Ler função de transição
    for estado in self.states:
      transicoes = input().split()
      self.transition_function[estado] = {}
      for simbolo in self.alphabet:
        proximo_estado = transicoes[self.alphabet.index(simbolo)+1]
        self.transition_function[estado][simbolo] = proximo_estado
  
  def process(self, palavra):
    estado_atual = self.initial_state
    for simbolo in palavra:
      if simbolo not in self.alphabet:
        return False
      if simbolo in self.transition_function[estado_atual]:
        estado_atual = self.transition_function[estado_atual][simbolo]
    return estado_atual.strip() in self.final_states

def main():
  afd = AFD()
  afd.startup()
  palavras = input().strip().split()
  for palavra in palavras:
    resultado = afd.process(palavra)
    if resultado:
      print("aceita")
    else:
      print("rejeita")

if __name__ == "__main__":
  main()