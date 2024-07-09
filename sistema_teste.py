# Testando o sistema
import classes as cl

sistema = cl.Sistema()

carro1 = cl.Carro('ABC1234', 2020, 'Preto', 'Civic', 10000, 100, 'Nenhum')
carro2 = cl.Esportivo('XYZ5678', 2021, 'Vermelho', 'Ferrari', 5000, 500, 'Nenhum', 5, ['Rodas de liga leve', 'Bancos de couro'])
carro3 = cl.Utilitario('DEF4321', 2019, 'Branco', 'HRV', 20000, 150, 'Nenhum', 5, 500, 10)

sistema.cadastrar_carro(carro1)
sistema.cadastrar_carro(carro2)
sistema.cadastrar_carro(carro3)

funcionario1 = cl.Funcionario('João', '12345678900', 30, 'Rua A, 123', '01/01/2020', 2000, 0, True, '999999999')
sistema.cadastrar_funcionario(funcionario1)

cliente1 = cl.Cliente('Maria', '98765432100', 25, '01/01/1995', '123456', 'foto', '01/01/2025', 'Rua B, 456', '888888888', 'maria@mymail.com')
sistema.cadastrar_cliente(cliente1)

reserva1 = cl.Reserva(cliente1, 1, 'Ativo', '01/01/2021', '10/01/2021')
sistema.cadastrar_reserva(reserva1, funcionario1, carro1)

promocao1 = cl.Promocao('Promoção de Natal', 'Desconto de 10% em todos os carros', '25/12/2020')
sistema.cadastrar_promocao(promocao1)

print('Listando carros, reservas, funcionários, clientes e promoções:')
print('====================')
sistema.listar_carros()
print('====================')
sistema.listar_reservas()
print('====================')
sistema.listar_funcionarios()
print('====================')
sistema.listar_clientes()
print('====================')
sistema.listar_promocoes()
print('====================\n')

print('Enviando promoção para cliente:')
sistema.enviar_promocao(promocao1, cliente1)
