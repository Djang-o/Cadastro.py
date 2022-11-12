from pessoa import Pessoa

usuario = Pessoa("teste","teste")

def cadastroPessoa(nome, senha):
    usuario.set_Nome(nome)
    usuario.set_Senha(senha)
    Nnome = usuario.get_Nome()
    Nsenha = usuario.get_Senha()
    PessoaonBD(Nnome,Nsenha)

def PessoaonBD(nome, senha):
    # Abra o arquivo (leitura)
    arquivo = open('./Cadastro/bd.txt', 'r')
    conteudo = arquivo.readlines()
    print(conteudo)
# insira seu conteúdo
# obs: o método append() é proveniente de uma lista
    conteudo.append(f"Nome: {nome} Senha: {senha}\n")

# Abre novamente o arquivo (escrita)
# e escreva o conteúdo criado anteriormente nele.
    arquivo = open('./Cadastro/bd.txt', 'w')
    arquivo.writelines(conteudo)

    arquivo.close()
    

