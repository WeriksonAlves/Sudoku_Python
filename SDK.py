'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Werikson Alves
:Data de início: 19/02/2023 - Data de término: ?? :
:::::::::::::::::::::::::::::::::::::::::::::::::::

PLATAFORMA SUDOKU

Conjunto de janelas para se inicializar o jogo
Através de um conjunto de botões será possível acionar as ações do jogo.
'''
#..............................................................................................................
#Bibliotecas usadas:
from tkinter import*

import sys
import os

import tkinter as tk
import numpy as np
import random
#..............................................................................................................
class App_SUDOKU:
    def __init__(self):
        # Variaveis principais:
        self.Var_Game_Matrix = np.zeros((9,9))
        self.Var_Sol_Matrix = np.zeros((9,9))
        self.Var_Life = 3
        self.Var_Help = 3


        # Executa as funções
        self.Create_Window()
        self.Create_Checkbutton()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Create_Window(self):
        self.WindowMain = Tk()                       # Cria a janela
        self.WindowMain.title("SDKpy")               # Titulo da janela
        self.WindowMain.minsize(300, 500)            # Tamanho mínimo da janela
        self.WindowMain.maxsize(300, 500)            # Tamanho máximo da janela
        self.WindowMain.configure(bg='grey')      # Cor de fundo da janela

        self.Main_StatusBar = Label(self.WindowMain,
                               text="Instruções: \nEscolher o nível de dificuldade \nIniciar partida",
                               bd=1, relief=SUNKEN, anchor=CENTER)
        self.Main_StatusBar.pack(side=BOTTOM, fill=X)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Limpa a nota de rodapé
    def Clear_StatusBar(self): 
        self.Main_StatusBar.config(text="")
        self.Main_StatusBar.update_idletasks() 
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Atualiza a nota de rodapé
    def Set_StatusBar(self, texto): 
        self.Main_StatusBar.config(text=texto)
        self.Main_StatusBar.update_idletasks()       
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria as checkbutton de para cada nivel de dificuldade
    def Create_Checkbutton(self):
        self.Var_Easy = tk.IntVar()
        Chebut_Easy = Checkbutton(self.WindowMain, text="Fácil", bg="green", variable=self.Var_Easy, command=self.Command_EasyMod)
        Chebut_Easy.place(height=50, width=100, x=0, y=0)

        self.Var_Mean = tk.IntVar()
        Chebut_Mean = Checkbutton(self.WindowMain, text="Médio", bg="yellow", variable=self.Var_Mean)#, command=self.Command_MeanMod)
        Chebut_Mean.place(height=50, width=100, x=100, y=0)

        self.Var_Hard = tk.IntVar()
        Chebut_Hard = Checkbutton(self.WindowMain, text="Difícil", bg="red", variable=self.Var_Hard)#, command=self.Command_HardMod)
        Chebut_Hard.place(height=50, width=100, x=200, y=0)

        self.Btn_Start = Button(self.WindowMain, text= "Iniciar partida", state='disabled', command = self.Command_StartGame)
        self.Btn_Start.place(height=50, width=200, x=50, y=70)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_EasyMod(self):
        self.Btn_Start.configure(state='active')
        self.Var_Difficult = 1
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_StartGame(self):
        self.Var_Sol_Matrix = np.zeros((9,9))
        a = self.Command_CreateSolution()
        print(a)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_CreateSolution(self):
        L = 0
        while L < np.size(self.Var_Sol_Matrix,0):
            Var_Numbers = list(range(1,10))
            random.shuffle(Var_Numbers)
            Num = Var_Numbers        
            for C in range(0,np.size(self.Var_Sol_Matrix,1)):
                Id = 0
                self.Var_Sol_Matrix[L][C], Ok = self.Command_CheckNum(L,C,Num,Id)
                if (Ok == "R"):
                    break
            if (Ok == "R"):
                self.Var_Sol_Matrix[L, 0:] = np.zeros((1,9))
            elif (Ok == "Y"):
                L = L + 1
        return self.Var_Sol_Matrix
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_CheckNum(self,L,C,Num,Id):
        Ok = "N"
        if (Id >= len(Num)):
            Ok = "R"
            return 0, Ok 
        elif (Num[Id] in self.Var_Sol_Matrix[L, 0:]) or (Num[Id] in self.Var_Sol_Matrix[0:, C]):
            # print('Linha:', self.Var_Sol_Matrix[L, 0:])
            # print('Coluna:', self.Var_Sol_Matrix[0:, C])
            # print('Elemento:', Num[Id])
            Id = Id + 1
            N, Ok = self.Command_CheckNum(L,C,Num,Id)
            if (Ok=="Y") or (Ok=="R"):
                return N,Ok
        else:
            Ok = "Y"
            Item = Num[Id]
            del Num[Id]
            return Item,Ok




    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # # Cria o menu inicial do sistema
    # def Create_Button(self): 
    #     # Abre a janela de configurações da camera
    #     OpenWindowCamera = Button(self.WindowMain, text= "Câmera", command = self.Command_OpenWindowCamera)#lambda: threading.Thread(target=self.Command_OpenWindowCamera).start()) 
    #     OpenWindowCamera.place(height=50, width=200, x=50, y=10)

    #     # Abre a janela de configurações da camera
    #     LoadSettings = Button(self.WindowMain, text= "Carrega a última calibração", command = self.Command_LoadSettings)
    #     LoadSettings.place(height=50, width=200, x=50, y=70)
        
    #     # Abre a janela de configurações da partida
    #     OpenWindowGame = Button(self.WindowMain, text= "Habilitar Partida", command = self.Command_OpenGameWindow)
    #     OpenWindowGame.place(height=50, width=200, x=50, y=130)
        
    #     # Abre a janela de calibração de cores
    #     OpenWindowColors = Button(self.WindowMain, text= "Calibrar Cores", command = self.Command_OpenWindowColors)
    #     OpenWindowColors.place(height=50, width=200, x=50, y=190)

    #     # Abre a janela de calibração de campo
    #     OpenWindowField = Button(self.WindowMain, text= "Calibrar Campo", command = self.Command_OpenWindowField)
    #     OpenWindowField.place(height=50, width=200, x=50, y=250)       

    #     #Encerra o software
    #     CloseAll = Button(self.WindowMain, text= "Encerrar o programa", bg='grey', activebackground='red', command=self.Command_Stop)
    #     CloseAll.place(height=50, width=200, x=50, y=310)
    # # #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # def Command_LoadSettings(self):
    #     try:
    #         self.Var_MatrixColor = np.loadtxt(self.Current_Folder+'\Colors\MatrixHSV.txt')
    #         self.Var_PTM = np.loadtxt(self.Current_Folder+'\Field\MatrixTransformação.txt')
    #         self.Clear_StatusBar()
    #         self.Set_StatusBar("Calibragem carregada.")
    #     except:
    #         self.Clear_StatusBar()
    #         self.Set_StatusBar("Arquivo não encontrado, faça uma nova calibração.")
    # #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # # Cria a janela e as funções da camera
    # def Command_OpenWindowCamera(self):
    #     self.WindowCamera = CameraWindow(self.Var_CameraOn,self.Var_MedianBlur,self.Var_FPS)
    #     self.Clear_StatusBar()
    #     self.Set_StatusBar("Instruções: \nInicializar a câmera: Em progresso \nCalibrar as cores: Faltando \nCalibrar o campo: Faltando \nIniciar a partida: Faltando")
    #     self.WindowCamera.Command_Run()
    # #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # # Cria a janela e as funções de calibragem de cores
    # def Command_OpenWindowColors(self):
    #     try:
    #         self.Var_CameraOn = self.WindowCamera.Var_CameraOn
    #         self.Var_CamInfo = self.WindowCamera.Var_CameraInformation
            
    #         self.WindowColors = ColorsWindow(self.Var_Kernel,self.Var_MedianBlur,self.Var_MatrixColor,self.Var_CamInfo,self.Var_FPS)

    #         self.Clear_StatusBar()
    #         self.Set_StatusBar("Instruções: \nInicializar a câmera: Feito \nCalibrar as cores: Em progresso \nCalibrar o campo: Faltando \nIniciar a partida: Faltando")

    #         self.WindowColors.Command_Run()
    #     except:
    #         self.Clear_StatusBar()
    #         self.Set_StatusBar("Instruções: \nInicializar a câmera: Conecte uma câmera primeiro \nCalibrar as cores: Faltando \nCalibrar o campo: Faltando \nIniciar a partida: Faltando")
    # #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # # Cria a janela de calibragem do campo
    # def Command_OpenWindowField(self):
    #     try:
    #         self.Var_CameraOn = self.WindowCamera.Var_CameraOn
    #         self.Var_CamInfo = self.WindowCamera.Var_CameraInformation
        
    #         self.WindowField = FieldWindow(self.Var_CamInfo,self.Var_FPS)

    #         self.Clear_StatusBar()
    #         self.Set_StatusBar("Instruções: \nInicializar a câmera: Feito \nCalibrar as cores: Feito \nCalibrar o campo: Em progresso \nIniciar a partida: Faltando")

    #         self.WindowField.Command_Run()
    #     except:
    #         self.Clear_StatusBar()
    #         self.Set_StatusBar("Instruções: \nInicializar a câmera: Conecte uma câmera primeiro \nCalibrar as cores: Faltando \nCalibrar o campo: Faltando \nIniciar a partida: Faltando")
    # #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # def Command_OpenGameWindow(self):
    #     try:
    #         self.Var_CameraOn = self.WindowCamera.Var_CameraOn
    #         self.Var_CamInfo = self.WindowCamera.Var_CameraInformation

    #         self.WindowGame = GameWindow(self.Var_MatrixColor,self.Var_CamInfo,self.Var_FPS,self.Var_Kernel,self.Var_MedianBlur,self.Var_PTM)

    #         self.Clear_StatusBar()
    #         self.Set_StatusBar("Instruções: \nInicializar a câmera: Feito \nCalibrar as cores: Feito \nCalibrar o campo: Feito \nIniciar a partida: Em progresso")

    #         self.WindowGame.Command_Run()
    #     except:
    #         self.Clear_StatusBar()
    #         self.Set_StatusBar("Instruções: \nFaça ou carregue as calibrações \nda Câmera, Cores e/ou Campo")
    # #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Encerra o programa
    def Command_Stop(self):
        self.WindowMain.quit()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Faz o loop da janela ?    
    def Command_Run(self):
        self.WindowMain.mainloop()
#..............................................................................................................
#Bibliotecas usadas:

def main(args):
    app_proc = App_SUDOKU()
    app_proc.Command_Run()   

if __name__ == '__main__':
    sys.exit(main(sys.argv))