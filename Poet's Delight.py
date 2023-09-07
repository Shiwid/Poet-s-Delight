import customtkinter as tk
from tkinter import messagebox

import nltk
from nltk.corpus import machado, mac_morpho, floresta

dicionario_portugues = set(
    word.lower()
    for word in machado.words() + mac_morpho.words() + floresta.words()
    if ' ' and '_' not in word  
)

def encontrar_rimas(palavra_digitada, dicionario):
    rimas = []
    palavra_digitada = palavra_digitada.lower()  
    for palavra in dicionario:
        if palavra.endswith(palavra_digitada[-3:]):
            rimas.append(palavra)
    return rimas

def buscar_rimas():
    palavra_digitada = entrada_palavra.get()
    rimas_encontradas = encontrar_rimas(palavra_digitada, dicionario_portugues)

    if rimas_encontradas:
        resultado_text.configure(state=tk.NORMAL)
        resultado_text.delete("2.0", tk.END)
        for rima in rimas_encontradas:
            resultado_text.insert(tk.END, rima + "\n")
        resultado_text.configure(state=tk.DISABLED)
    else:
        messagebox.showinfo("Nenhuma rima encontrada", f"Nenhuma rima encontrada para '{palavra_digitada}'")


tk.set_appearance_mode("dark")

janela = tk.CTk()
janela.title("Poet's Delight")
janela.geometry("300x300")
janela.resizable(False, False)

label_palavra = tk.CTkLabel(janela, text="Digite uma palavra:")
label_palavra.pack()

entrada_palavra = tk.CTkEntry(janela)
entrada_palavra.pack()

botao_buscar = tk.CTkButton(janela, text="Buscar Rimas", command=buscar_rimas)
botao_buscar.pack()

resultado_text = tk.CTkTextbox(janela, wrap=tk.WORD)
resultado_text.configure(state=tk.DISABLED)
resultado_text.pack()

janela.mainloop()