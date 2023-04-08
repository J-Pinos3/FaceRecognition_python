from tkinter import *
from tkinter import messagebox as msg
import os
import cv2
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN

path = "C:/Users/Usuario/Desktop/ReconocimientoFacial"
txt_login = "Iniciar Sesión"
txt_register = "Registrarse"

color_white = "#f4f5f4"
color_black = "#101010"

color_black_btn = "#202020"
color_background = "#151515"

font_label = "Century Gothic"
size_screen = "500x300"


#COLORS

color_succes = "\033[1;32;40m"
color_error = "\033[1;31;40m"
color_normal = "\033[0;37;40m"

res_bd = {"id":0, "affected":0}

#GENERAL
def getEnter(screen):
    Label(screen, text="", bg=color_background).pack()


def printAndShow(screen, text, flag):
    if flag:
        print(color_succes + text + color_normal)
        screen.destroy()
        msg.showinfo(message=text, title="Éxito")
    else:
        print(color_error + text + color_normal)
        Label(screen, text=text, fg="red", bg=color_background, font=(font_label,12)).pack()
        