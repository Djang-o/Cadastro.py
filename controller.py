from pessoa import Pessoa
import re

usuario = Pessoa("teste","teste")

def cadastroPessoa(nome, senha):
    usuario.set_Nome(nome)
    usuario.set_Senha(senha)
    Nnome = usuario.get_Nome()
    Nsenha = usuario.get_Senha()
    criarPessoaonBD(Nnome,Nsenha)

def retorneSucesso():
    return "Sucesso"

def loginPessoa(nome,senha):
    nome = nome
    senha = senha
    arquivo = open('bd.txt', 'r')
    dadosArquivo = (f"Nome: {nome} Senha: {senha}")
    print(dadosArquivo)
    for dados in arquivo:
        if dadosArquivo in dados :
            return "Login valido"
        else:
            return "Login invalido"
    
def existePessoa(nome,senha):
    regex_palavras = re.compile(r'\b(\w+)\b')
    Snome = nome
    Ssenha = senha
    with open('bd.txt', 'r', encoding = 'utf-8') as arquivo:
       texto = arquivo.readlines()
       print(texto)
       for nomes in texto:
           
           if Snome in nomes:
               return "Ja existe este nome"
           
           else:
                cadastroPessoa (Snome,Ssenha)
                break
        
                
        
        
     
            
    


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
    
    

existePessoa("Jorge","12345")

