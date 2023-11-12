import json

class Servico:
  def __init__(self, id, descricao, valor, duracao):
    if valor < 0: raise ValueError("Valor inválido")
    if duracao <= 0: raise ValueError("Duração inválida")
    self.__id = id
    self.__descricao = descricao
    self.__valor = valor
    self.__duracao = duracao

  def get_id(self): return self.__id
  def get_descricao(self): return self.__descricao
  def get_valor(self): return self.__valor
  def get_duracao(self): return self.__duracao

  def set_id(self, id): self.__id = id
  def set_descricao(self, descricao): self.__descricao = descricao
  def set_valor(self, valor): 
    if valor < 0: raise ValueError("Valor inválido")
    self.__valor = valor
  def set_duracao(self, duracao):
    if duracao <= 0: raise ValueError("Duração inválida")
    self.__duracao = duracao

  def __eq__(self, x):
    if self.__id == x.__id and self.__descricao == x.__descricao and self.__valor == x.__valor and self.__duracao == x.__duracao:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__descricao} - {self.__valor:.2f} - {self.__duracao} min"


class NServico:
  __servicos = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__servicos:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__servicos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__servicos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__servicos:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_descricao(obj.get_descricao())
      aux.set_valor(obj.get_valor())
      aux.set_duracao(obj.get_duracao())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__servicos.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__servicos = []
    try:
      with open("servicos.json", mode="r") as arquivo:
        servicos_json = json.load(arquivo)
        for obj in servicos_json:
          aux = Servico(obj["_Servico__id"], obj["_Servico__descricao"], obj["_Servico__valor"], obj["_Servico__duracao"])
          cls.__servicos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("servicos.json", mode="w") as arquivo:
      json.dump(cls.__servicos, arquivo, default=vars)
