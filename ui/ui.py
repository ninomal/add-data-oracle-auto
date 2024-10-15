import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pathlib import Path
from tkinter import filedialog
from products.products import Products


class Ui():
    def __init__(self):
        self.windows = Tk()
        self.windows.geometry("850x420")
        self.windows.title("Excel para o Banco")
        self.windows.config(background="#080121")
        self.caminhoEntry = ''
        self.conts = 0
        self.products = Products()
        self.canvasImage()
        self.frame1()
        self.buttonPainel()
        self.firma()
        self.clearLIstEntrys()
        self.ioMainLoop()
        self.bancoEntry = ''

        
    def firma(self):
        label_footer = tk.Label(self.windows, text="Radical dreamers aw rpg ltda", 
                        font=("Helvetica", 17), fg="#1b52a4", bg="#080121")
        label_footer.place(x=820, y=791, width=349, height=45)
           
    def frame1(self):
        self.anchorPane = tk.Frame(self.windows, width=400, height=276,
                                   background="#4A1985")
        self.anchorPane.place(x=15, y=135) 
        
        
        self.Labelcaminho = tk.Label(self.anchorPane, text="Procure o arquivo Excel",
                                     font=("Helvetica", 21), bg="#4A1985")
        self.Labelcaminho.place(x=12, y=120, width=350, height=31)

    def canvasImage(self): 
        image_frame = Canvas(self.windows, width=406, height=400, background="#080121")
        image_frame.place(x=430, y=8)
        self.logo_img = PhotoImage(file= self.randomImagem())
        image_frame.create_image(100, 100, image = self.logo_img)
        
    def randomImagem(self):
        path = self.products.randImage()
        return path
                                                   
    def buttonPainel(self):
        button_add = tk.Button(self.anchorPane, text="Procurar", font=("Helvetica", 18),
                               bg="#A580CA", command= self.popADD)
        button_add.place(x=200, y= 194, width=149)

    def popValueError(self):
        masterPoP = Tk()
        masterPoP.geometry("500x300")
        masterPoP.config(bg="#A580CA")
        messagebox = tk.Label(master= masterPoP,
                              text= "Valor invalido",
                              font=("Helvetica", 27))
        messagebox.pack(padx= 40, pady= 40)   
        self.listData = []
        self.contsAdd = 0
                  
    def popEraserError(self):
        messagebox.showwarning(title="Erro",
                message= "Error para Adicionar")
    
    def popPathError(self):
        messagebox.showwarning(title="Erro",
                message= "Erro de caminho")
        
    def popTabelaExist(self):
        messagebox.showwarning(title="Erro",
                message= "Tabela existe utilize outro nome")
                               
    def clearLIstEntrys(self):
        self.listData = []
             
    def popADD(self):
        self.clickSearch()
        try:
            self.listOfComboInfo = self.products.readSheetsOfXlsx(self.caminhoEntry)
            if self.listOfComboInfo:
                self.masterPoP = Tk()
                self.masterPoP.geometry("500x300")
                self.masterPoP.config(bg="#A580CA")  
                self.testes = ['notas', 'fios', 'consulta']

                self.comboTabelas = ttk.Combobox(self.masterPoP, 
                                            values= self.listOfComboInfo,
                                            font=("Helvetica", 14),
                                             state='normal')
                
                self.comboTabelas.place(x=198, y=150, width=180, height=25)
                self.comboTabelas.set(self.listOfComboInfo[0])  

                messagebox = tk.Label(master= self.masterPoP, text= "Selecione a aba:",
                                    font=("Helvetica", 14), bg="#A580CA")
                messagebox.place(x= 35, y= 150, width= 150) 

                messageboxBancoName = tk.Label(master= self.masterPoP, text= "Nome da Tabela:",
                                    font=("Helvetica", 14), bg="#A580CA")
                messageboxBancoName.place(x= 35, y= 200, width= 150) 

                self.bancoEntry = tk.Entry(self.masterPoP, font=("Helvetica", 14))
                self.bancoEntry.place(x=198, y=200, width=250, height=26)

                buttonADD = tk.Button(master= self.masterPoP, text="Adicionar Dados",
                                    font=("Helvetica", 18),
                                    bg="#A580CA",command= self.addOracle)
                buttonADD.place(x= 265 , y= 250, width= 195, height= 38)

                buttonCreate= tk.Button(master= self.masterPoP, text="Criar Tabela",
                                    font=("Helvetica", 18),
                                    bg="#A580CA",command= self.createTable)
                buttonCreate.place(x= 40 , y= 250, width= 180, height= 38)
        except:
            self.popPathError()
    
    # create table in oracle
    def createTable(self):
        if self.products.checkTables(self.bancoEntry.get().upper()):
            self.popTabelaExist()
            self.bancoEntry.delete(0, END)
        else:
            self.products.createAuto(self.bancoEntry.get(), self.caminhoEntry, self.comboTabelas.get())
    
    #HEREEEE add data 
    def addOracle(self):
        data = self.products.addOracle()
        #print(self.products.addOracleDataAuto(self.bancoEntry, data))
        

    #search for xlsx file with click
    def clickSearch(self):
        self.caminhoEntry = Path(filedialog.askopenfilename())
       
    
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    