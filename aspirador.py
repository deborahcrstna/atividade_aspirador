class Ambiente:
    def __init__(self):
        self.locais = [['Sujo' if i % 2 == 0 and j % 2 == 0 else 'Limpo' for j in range(4)] for i in range(4)]

    def esta_sujo(self, x, y):
        return self.locais[x][y] == 'Sujo'

    def limpar_local(self, x, y):
        self.locais[x][y] = 'Limpo'

class AgenteAspirador:
    def __init__(self, ambiente):
        self.x, self.y = 0, 0  
        self.energia = 100
        self.bolsa_sujeira = 0
        self.ambiente = ambiente

    def perceber(self):
        return self.ambiente.esta_sujo(self.x, self.y)

    def mover(self, direcao):
        if direcao == 'Norte' and self.x > 0:
            self.x -= 1
        elif direcao == 'Sul' and self.x < 3:
            self.x += 1
        elif direcao == 'Leste' and self.y < 3:
            self.y += 1
        elif direcao == 'Oeste' and self.y > 0:
            self.y -= 1
        self.energia -= 1  

    def aspirar_sujeira(self):
        if self.perceber():
            self.ambiente.limpar_local(self.x, self.y)
            self.bolsa_sujeira += 1
            self.energia -= 1  

    def verificar_bolsa_sujeira(self):
        return self.bolsa_sujeira >= 10

    def esta_em_casa(self):
        return self.x == 0 and self.y == 0

    def voltar_para_casa(self):
        
        while not self.esta_em_casa():
            print("Posição atual antes do movimento:", (self.x, self.y))
            if self.x > 0:
                self.mover('Norte')
            elif self.y > 0:
                self.mover('Oeste')
        self.bolsa_sujeira = 0  
        print("Agente retornou para casa. Posição atual:", (self.x, self.y))

    def limpar(self):
        direcoes = ['Leste', 'Sul', 'Oeste', 'Norte']
        while self.energia > 0:
            if self.verificar_bolsa_sujeira():
                self.voltar_para_casa()

            if self.perceber():
                self.aspirar_sujeira()
            else:
                if self.y == 3:
                    self.mover('Sul')
                else:
                    self.mover('Leste')

        print("Agente retornou para casa. Posição atual:", (self.x, self.y))

ambiente = Ambiente()
agente = AgenteAspirador(ambiente)
agente.limpar()

for linha in ambiente.locais:
    print(linha)



