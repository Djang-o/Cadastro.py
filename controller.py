from pessoa import Pessoa

usuario = Pessoa("teste","teste")

def cadastroPessoa(nome, senha):
    usuario.set_Nome(nome)
    usuario.set_Senha(senha)
    Nnome = usuario.get_Nome()
    Nsenha = usuario.get_Senha()
    criarPessoaonBD(Nnome,Nsenha)
    
    
def loginPessoa(nome,senha):
    nome = nome
    senha = senha
    arquivo = open('bd.txt', 'r')
    for dados in arquivo:
        if nome in dados :
            return "Login valido"
        else:
            return "Login invalido"
    

def criarPessoaonBD(nome, senha):
    # Abra o arquivo (leitura)
    arquivo = open('bd.txt', 'r')
    conteudo = arquivo.readlines()
    print(conteudo)
# insira seu conteúdo
# obs: o método append() é proveniente de uma lista
    conteudo.append(f"Nome: {nome} Senha: {senha}\n")

# Abre novamente o arquivo (escrita)
# e escreva o conteúdo criado anteriormente nele.
    arquivo = open('bd.txt', 'w')
    arquivo.writelines(conteudo)

    arquivo.close()
    
    
def procurarPessoaonBd():
    pass

