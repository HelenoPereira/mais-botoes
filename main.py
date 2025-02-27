from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

from tkinter import filedialog as fd

from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando views
from view import *
# cores

co0 = "#2e2d2b"
co1 = "#feffff"      # preta
co2 = "#4fa882"      # branca
co3 = "#38576b"      # verde
co4 = "#403d3d"      # valor
co5 = "#e06636"      # letra
co6 = "#038cfc"      # - profit
co7 = "#3fbfb9"      # verde
co8 = "#263238"      # + verde
co9 = "#e9edf5"      # + verde

# criando janela

janela = Tk()
janela.title('')
janela.geometry('1100x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# criando frames

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# criando funcoes -------------------------------------------------------------
global tree

# funcao inserir
def inserir():
    global imagem, imagem_string, l_imagem
    
    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    marca = e_marca.get()
    data_empr = e_data_empr.get_date()
    data_devo = e_data_devo.get_date()
    nomecolab = e_nomecolab.get()
    setor = e_setor.get()
    imagem = imagem_string
    
    lista_inserir = [nome, local, descricao, marca, data_empr, data_devo, nomecolab, setor, imagem]
    
    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    inserir_form(lista_inserir)
    
    messagebox.showinfo('Sucesso', 'Os dados foram inserido com sucesso!')
    
    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_marca.delete(0, 'end')
    e_data_empr.delete(0, 'end')
    e_data_devo.delete(0, 'end')
    e_nomecolab.delete(0, 'end')
    e_setor.delete(0, 'end')
    imagem_string.delete(0, 'end')
    
    for widget in frameMeio.winfo_children():
        widget.destroy()
        
    mostrar()
    
    
# funcao para escolher imagem -----------------------------------------------------    
global imagem, imagem_string, l_imagem  

def escolher_imagem():
    global imagem, imagem_string, l_imagem  
    
    imagem = fd.askopenfilename()
    imagem_string = imagem
    
    # abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)
    
    
  

# trabalhando no frame de cima -------------------------------------------------

# abrindo imagem
app_img = Image.open('iconcaixaferramentas.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Caixa de Ferramentas', width=1100, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)


# trabalhando no frame meio -----------------------------------------------------------

# criando entradas 
#------------------------------------NOME------------------------------------------------------------
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)

e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

#---------------------------------LOCAL---------------------------------------------------------------

l_local = Label(frameMeio, text='Local', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)

e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

#---------------------------------DESCRIÇÃO-------------------------------------------------------------

l_descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)

e_descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

#----------------------------------MARCA--------------------------------------------------------

l_marca = Label(frameMeio, text='Marca/Modelo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_marca.place(x=10, y=100)

e_marca = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_marca.place(x=130, y=101) 


#----------------------------Data de emprestimo----------------------------------------------------------

l_data_empr = Label(frameMeio, text='Data Empréstimo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_data_empr.place(x=10, y=130)

e_data_empr  = DateEntry(frameMeio, width=12, Background='darkblue', bordewidth=2, year=2024)
e_data_empr.place(x=130, y=131)

#----------------------------Data de devolucao-----------------------------------------------------------

l_data_devo = Label(frameMeio, text='Data Devolução', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_data_devo.place(x=10, y=160)

e_data_devo  = DateEntry(frameMeio, width=12, Background='darkblue', bordewidth=2, year=2024)
e_data_devo.place(x=130, y=161)

#----------------------------Nome do Colaborador-----------------------------------------------------------

l_nomecolab = Label(frameMeio, text='Colaborador', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nomecolab.place(x=10, y=190)

e_nomecolab = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nomecolab.place(x=130, y=191) 

#----------------------------Setor de Trabalho-----------------------------------------------------------

l_setor = Label(frameMeio, text='Setor', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_setor.place(x=10, y=220)

e_setor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_setor.place(x=130, y=221) 

#----------------------------Carregamento da Imagem-----------------------------------------------------------

l_carregar = Label(frameMeio, text='Ferramenta', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=250)

#botão carregar
b_carregar = Button(frameMeio, command=escolher_imagem, width=29, text='carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief= RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=251)

#----------------------------Botão Inserir--------------------------------------------------------
img_add = Image.open('iconadd.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

#botão Inserir -- Faz o insert na nossa tabela
b_inserir = Button(frameMeio,command=inserir, image=img_add, width=95, text='  ADICIONAR'.upper(), compound=LEFT, anchor=NW, overrelief= RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)

#----------------------------Botão Atualizar--------------------------------------------------------
img_update = Image.open('iconUpdate.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)

#botão ATUALIZAR -- Faz o update na nossa tabela
b_update = Button(frameMeio, image=img_update, width=95, text='  ATUALIZAR'.upper(), compound=LEFT, anchor=NW, overrelief= RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_update.place(x=330, y=50)

#----------------------------Botão Deletar--------------------------------------------------------
img_delete = Image.open('iconDelete.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

#botão DELETAR -- Faz o delete na nossa tabela
b_delete = Button(frameMeio, image=img_delete, width=95, text='  DELETAR'.upper(), compound=LEFT, anchor=NW, overrelief= RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_delete.place(x=330, y=90)

#----------------------------Botão Deletar--------------------------------------------------------
img_ferramenta = Image.open('iconFolder.png')
img_ferramenta = img_ferramenta.resize((20,20))
img_ferramenta = ImageTk.PhotoImage(img_ferramenta)

#botão DELETAR -- Faz o delete na nossa tabela
b_ferramenta = Button(frameMeio, image=img_ferramenta, width=95, text='  VER IMAGEM'.upper(), compound=LEFT, anchor=NW, overrelief= RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_ferramenta.place(x=330, y=250)

# Labels Quantidade total e Valores

l_total = Label(frameMeio, text='', width=14, height=2, anchor=CENTER, font=('Ivy 18 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=17)
l_total_ = Label(frameMeio, text='            Total de Empréstimos      ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total_.place(x=450, y=12)

l_qtd = Label(frameMeio, text='', width=14, height=2, anchor=CENTER, font=('Ivy 18 bold'), bg=co7, fg=co1)
l_qtd.place(x=450, y=90)
l_qtd_ = Label(frameMeio, text='  Quantidade total de itens  ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_.place(x=450, y=92)

# tabela 
def mostrar():
    #creating a treeview with dual scrollbars
    tabela_head = ['#Item','Nome',  'Local','Descrição', 'Marca/Modelo', 'Data de Empréstimo','Data de Devolução', 'Nome Funcionário', 'Setor/Area', 'Imagem']

    lista_itens = ver_form()


    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center","center","center",'center']
    h=[40,50,50,100,130,150,150,150,150,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = [8888,88]

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

mostrar()





janela.mainloop()