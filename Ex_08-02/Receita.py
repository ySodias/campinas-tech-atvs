class Receita:

  def __init__(self, nome, rendimento, hora_cadastro):
    self.nome = nome
    self.rendimento = rendimento
    self.hora_cadastro = hora_cadastro
    
  def set_Receita(self, nome, rendimento, hora_cadastro):
    self.nome = nome
    self.rendimento = rendimento
    self.hora_cadastro = hora_cadastro
  
  def __del__(self):
    class_name = self.__class__.__name__
    print(f'{class_name} - detroyed')