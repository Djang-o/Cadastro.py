from tkinter import *
from tkinter import ttk
import controller

 
def Cadastro():
   
   def clique():
      senha = inputSenha.get()
      nome = inputNome.get()
      print(nome,senha)
      controller.cadastroPessoa(nome,senha)
      labelConfirm = Message( janelaC, text = "Sucesso", width=100) 
      labelConfirm.place(x=150, y=160)
   
   janelaC = Toplevel()
   janelaC.title("Cadastro")
   janelaC. geometry("235x318")
   janelaC.transient(janela)
   janelaC.focus_force()
   janelaC.grab_set()
   janelaC.resizable(False,False)
   frame_corpo = Frame(janelaC,width=235, height=318, bg="#fff" )
   frame_corpo.grid(row =0, column=0)


   inputNome = Entry(janelaC, 
                  bg="#999")
   inputNome.place(x=70, y=30)



   labelNome = Label(janelaC, 
                    text="Nome: ", 
                    font=('Ivy 13 bold'),
                    bg="#fff", 
                    fg="#000")
   labelNome.place(x=0, y=30)

   inputSenha = Entry(janelaC,
                show="*",
                bg="#999")
   inputSenha.place(x=70, y=60)
   labelSenha = Label(janelaC, 
                text="Senha: ", 
                font=('Ivy 13 bold'),
                bg="#fff", 
                fg="#000")
   labelSenha.place(x=0, y=60)



   botao = Button(janelaC, text="Cadastrar", command=clique)
   botao.place(x=150, y=100) 
   botao1 = Button(janelaC, text="Cancelar", command=janelaC.destroy)
   botao1.place(x=25, y=100) 
 


   
janela = Tk()
janela.title("Inicio")
janela. geometry("235x318")
janela.resizable(False,False)
frame_corpo = Frame(janela,width=235, height=318, bg="#fff" )
frame_corpo.grid(row =0, column=0)
labelNome = Label(janela, 
                    text="Sistema Login/Cadastro \n Pseudo BD ", 
                    font=('Ivy 13 bold'),
                    bg="#fff", 
                    fg="#2c3ee6")
labelNome.place(x=25, y=0)
app_1_linha = Label(janela, text="",height=1, width=235, anchor=CENTER, font=('Ivy 1 bold'), bg="#3045ff", fg="#3045ff")
app_1_linha.place(x=0, y=40)

botaoC = Button(janela,width=10, text="Cadastrar", command=Cadastro)
botaoC.place(x=75, y=100)
botaoL = Button(janela,width=10, text="Login", command=Cadastro)
botaoL.place(x=75, y=130)


      


janela.mainloop()
   
   
      


