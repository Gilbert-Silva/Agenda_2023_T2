from models.cliente import Cliente, NCliente

class View:

  def cliente_inserir(nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)

  def cliente_listar():
    return NCliente.listar()

  def cliente_atualizar(id, nome, email, fone):
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)

  def cliente_excluir(id):
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)
