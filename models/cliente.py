import json

class Cliente:
  def __init__(self, id, nome, email, fone, senha):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
    self.__senha = senha

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_fone(self): return self.__fone
  def get_senha(self): return self.__senha

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_email(self, email): self.__email = email
  def set_fone(self, fone): self.__fone = fone
  def set_senha(self, senha): self.__senha = senha

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__email == x.__email and self.__fone == x.__fone and self.__senha == x.__senha:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"


class NCliente:
  __clientes = []  # lista de clientes inicia vazia

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0  # encontrar o maior id já usado
    for aux in cls.__clientes:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)  # insere um cliente (obj) na lista
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__clientes  # retorna a lista de clientes

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__clientes:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_nome(obj.get_nome())
      aux.set_email(obj.get_email())
      aux.set_fone(obj.get_fone())
      aux.set_senha(obj.get_senha())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__clientes.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__clientes = []
    try:
      with open("clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
          aux = Cliente(obj["_Cliente__id"], 
                        obj["_Cliente__nome"], 
                        obj["_Cliente__email"],
                        obj["_Cliente__fone"],
                        obj["_Cliente__senha"])
          cls.__clientes.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
      json.dump(cls.__clientes, arquivo, default=vars)
