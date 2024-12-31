#Sistema de gerenciamento de locação e devolução de carros

class Carro:
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diaria, obs):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valor_diaria = valor_diaria
        self.obs = obs
        self.reserva = None

class Esportivo(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diaria, obs, tempo_100, melhorias):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diaria, obs)
        self.tempo_100 = tempo_100
        self.melhorias = melhorias

class Utilitario(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diaria, obs, passageiros, bagageiro, km_litro):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diaria, obs)
        self.passageiros = passageiros
        self.bagageiro = bagageiro
        self.km_litro = km_litro

class Reserva:
    def __init__(self, cliente, id, status, data_inicio, data_fim):
        self.cliente = cliente
        self.id = id
        self.status = status
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.ativo = True

class Pessoa:
    def __init__(self, nome, cpf, idade, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade, endereco, data_contratacao, salario, alugueis_realizados, status, telefone):
        super().__init__(nome, cpf, idade, endereco, telefone)
        self.data_contratacao = data_contratacao
        self.salario = salario
        self.alugueis_realizados = alugueis_realizados
        self.status = status

class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade, data_nascimento, cnh, foto_cnh, vencimento_cnh, endereco, telefone, email):
        super().__init__(nome, cpf, idade, endereco, telefone)
        self.data_nascimento = data_nascimento
        self.cnh = cnh
        self.foto_cnh = foto_cnh
        self.vencimento_cnh = vencimento_cnh
        self.email = email

class Promocao:
    def __init__(self, titulo, descricao, data_validade):
        self.titulo = titulo
        self.descricao = descricao
        self.data_validade = data_validade

class Sistema:
    def __init__(self):
        self.carros = []
        self.reservas = []
        self.funcionarios = []
        self.clientes = []
        self.promocoes = []
        self.qtd_alugueis = 0

    def cadastrar_carro(self, carro):
        if self.buscar_carro(carro.placa) is None:
            self.carros.append(carro)
        else:
            print('Carro já cadastrado')

    def cadastrar_reserva(self, reserva, funcionario, carro):
        if self.buscar_funcionario(funcionario.cpf) is not None:
            if self.buscar_carro(carro.placa) is not None:
                if carro.reserva is None:
                    self.qtd_alugueis += 1
                    reserva.qtd_alugueis = self.qtd_alugueis
                    carro.reserva = reserva
                    self.reservas.append(reserva)
                else:
                    print('Carro já reservado')
            else:
                print('Carro não cadastrado')
        else:
            print('Funcionário não cadastrado')

    def cadastrar_funcionario(self, funcionario):
        if self.buscar_funcionario(funcionario.cpf) is None:
            self.funcionarios.append(funcionario)
        else:
            print('Funcionário já cadastrado')

    def cadastrar_cliente(self, cliente):
        if self.buscar_cliente(cliente.cpf) is None:
            self.clientes.append(cliente)
        else:
            print('Cliente já cadastrado')

    def cadastrar_promocao(self, promocao):
        self.promocoes.append(promocao)

    def listar_carros(self):
        for carro in self.carros:
            print(carro.modelo)

    def listar_reservas(self):
        for reserva in self.reservas:
            print(reserva.id)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario.nome)

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente.nome)

    def listar_promocoes(self):
        for promocao in self.promocoes:
            print(promocao.titulo)

    def buscar_carro(self, placa):
        for carro in self.carros:
            if carro.placa == placa:
                return carro
        return None

    def buscar_reserva(self, id):
        for reserva in self.reservas:
            if reserva.id == id:
                return reserva
        return None

    def buscar_funcionario(self, cpf):
        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                return funcionario
        return None

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def remover_carro(self, placa):
        carro = self.buscar_carro(placa)
        if carro is not None:
            self.carros.remove(carro)
            self.remover_reserva(carro.reserva.id)

    def remover_reserva(self, id):
        reserva = self.buscar_reserva(id)
        if reserva is not None:
            self.reservas.remove(reserva)
            for carro in self.carros:
                if carro.reserva == reserva:
                    carro.reserva = None

    def enviar_promocao(self, promocao, cliente):
        print(f'Enviando promoção {promocao.titulo} para o cliente: {cliente.email}')