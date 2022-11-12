class Pessoa():
    def __init__(self, nome, senha) :
        self.nome = nome
        self.senha = senha

    
    def get_Nome (self):
        return self.nome
    
    def set_Nome (self, name):
        self.nome = name

    def get_Senha (self):
        return self.senha

    def set_Senha(self, passw):
        self.senha = passw

