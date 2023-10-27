from models.cliente import Cliente, NCliente
from models.servico import Servico, NServico
from models.agenda import Agenda, NAgenda
import datetime

class View:
  def cliente_inserir(nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)

  def cliente_listar():
    return NCliente.listar()
  
  def cliente_listar_id(id):
    return NCliente.listar_id(id)

  def cliente_atualizar(id, nome, email, fone):
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)
    
  def cliente_excluir(id):
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)    

  def servico_listar():
    return NServico.listar()

  def servico_listar_id(id):
    return NServico.listar_id(id)

  def servico_inserir(descricao, valor, duracao):
    NServico.inserir(Servico(0, descricao, valor, duracao))

  def servico_atualizar(id, descricao, valor, duracao):
    NServico.atualizar(Servico(id, descricao, valor, duracao))

  def servico_excluir(id):
    NServico.excluir(Servico(id, "", "", ""))

  def agenda_listar():
    return NAgenda.listar()

  def agenda_inserir(data, confirmado, id_cliente, id_servico):
    NAgenda.inserir(Agenda(0, data, confirmado, id_cliente, id_servico))

  def agenda_atualizar(id, data, confirmado, id_cliente, id_servico):
    NAgenda.atualizar(Agenda(id, data, confirmado, id_cliente, id_servico))

  def agenda_excluir(id):
    NAgenda.excluir(Agenda(id, "", "", 0, 0))

  def agenda_abrir_agenda(data, hinicio, hfim, intervalo):
    data_inicio = datetime.datetime.strptime(f"{data} {hinicio}", "%d/%m/%Y %H:%M")
    data_fim = datetime.datetime.strptime(f"{data} {hfim}", "%d/%m/%Y %H:%M")
    delta = datetime.timedelta(minutes = intervalo) 
    aux = data_inicio
    while aux <= data_fim :
      NAgenda.inserir(Agenda(0, aux, False, 0, 0))
      aux = aux + delta
