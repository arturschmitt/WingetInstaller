import tkinter as tk
from tkinter import ttk

import os

#funções para instalar os programas
def instalarVim():
    os.system("winget install vim.vim")

def instalarVLC():
    os.system("winget install VideoLAN.VLC")

def instalarFirefoxEsr():
    os.system("winget install Mozilla.Firefox.ESR")

def instalarLibreOffice():
    os.system("winget install TheDocumentFoundation.LibreOffice")

def instalarGIMP():
    os.system("winget install GIMP.GIMP")

def instalarKdenlive():
    os.system("winget install KDE.Kdenlive")

def instalarAudacity():
    os.system("winget install Audacity.Audacity")

def instalarqBittorrent():
    os.system("winget install qBittorrent.qBittorrent")

def instalarInkscape():
    os.system("winget install Inkscape.Inkscape")

def instalarBlender():
    os.system("winget install BlenderFoundation.Blender")

def instalarVirtualbox():
    os.system("winget install Oracle.VirtualBox")
    
def instalarPython3():
    os.system("winget install Python.Python.3")
    
def instalar4kVideoDownloader():
    os.system("winget install OpenMedia.4KVideoDownloader")

def instalarNotepad():
    os.system("winget install Notepad++.Notepad++")

def instalarTorBrowser():
    os.system("winget install TorProject.TorBrowser")

def instalarEmacs():
    os.system("winget install GNU.Emacs")
    
root = tk.Tk()

#titulo da janela
root.title("Winget Installer")

#tamanho da janela
root.geometry('620x400')

#fixar tamanho da janela
root.resizable(False, False)

#titulo
ttk.Label(
    root,
    text='Winget Installer',
    font=("Comic Sans MS", 14)
).place(x=240, y=0)


#Botão Vim
ttk.Button(root, text="Vim", command=instalarVim).place(x=200, y=50)

#Botão VLC
ttk.Button(root, text="VLC", command=instalarVLC).place(x=200, y=90)

#Botão Firefox ESR
ttk.Button(root, text="Firefox ESR", command=instalarFirefoxEsr).place(x=200, y=130)

#Botão LibreOffice
ttk.Button(root, text="LibreOffice", command=instalarLibreOffice).place(x=200, y=170)

#Botão GIMP
ttk.Button(root, text="GIMP", command=instalarLibreOffice).place(x=200, y=210)

#Botão Kdenlive
ttk.Button(root, text="Kdenlive", command=instalarKdenlive).place(x=200, y=250)

#Botão Audacity
ttk.Button(root, text="Audacity", command=instalarAudacity).place(x=200, y=290)

#Botão qBittorrent
ttk.Button(root, text="qBittorrent", command=instalarqBittorrent).place(x=200, y=330)

#Botão Inkscape
ttk.Button(root, text="Inkscape", command=instalarInkscape).place(x=340, y=50)

#Botão Blender
ttk.Button(root, text="Blender", command=instalarBlender).place(x=340, y=90)

#Botão Virtualbox
ttk.Button(root, text="Virtualbox", command=instalarVirtualbox).place(x=340, y=130)

#Botão Python3
ttk.Button(root, text="Python3", command=instalarPython3).place(x=340, y=170)

#Botão Chromium
ttk.Button(root, text="4kVD", command=instalar4kVideoDownloader).place(x=340, y=210)

#Botão Notepad++
ttk.Button(root, text="Notepad++", command=instalarNotepad).place(x=340, y=250)

#Botão VSCodium
ttk.Button(root, text="Tor Browser", command=instalarTorBrowser).place(x=340, y=290)

#Botão Emacs
ttk.Button(root, text="Emacs", command=instalarEmacs).place(x=340, y=330)


ttk.Label(root, text="Criado por Artur Brenner Schmitt sob a licença GPLv3").place(x=145, y=380)

root.mainloop()


