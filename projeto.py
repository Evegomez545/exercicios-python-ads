import tkinter as tk
from tkinter import ttk, messagebox
import json

ARQUIVO = "tarefas.json"

# Funções para salvar e carregar
def carregar_tarefas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_tarefas():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

# Funções principais
def atualizar_lista():
    lista_tarefas.delete(0, tk.END)
    dia = dia_var.get()
    if dia in tarefas:
        for t in tarefas[dia]:
            lista_tarefas.insert(tk.END, t)

def adicionar_tarefa():
    dia = dia_var.get()
    tarefa = entrada_tarefa.get().strip()
    if not tarefa:
        messagebox.showwarning("Aviso", "Digite uma tarefa antes de adicionar.")
        return
    tarefas.setdefault(dia, []).append(tarefa)
    salvar_tarefas()
    entrada_tarefa.delete(0, tk.END)
    atualizar_lista()

def remover_tarefa():
    dia = dia_var.get()
    selecionado = lista_tarefas.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")
        return
    indice = selecionado[0]
    tarefas[dia].pop(indice)
    salvar_tarefas()
    atualizar_lista()

# Interface
janela = tk.Tk()
janela.title("Organizador Diário - Evelyn")
janela.geometry("400x450")
janela.config(bg="#f4f4f4")

tarefas = carregar_tarefas()

# Dia da semana
tk.Label(janela, text="Selecione o dia da semana:", bg="#f4f4f4", font=("Arial", 11, "bold")).pack(pady=5)
dia_var = tk.StringVar(value="Segunda")
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
combo = ttk.Combobox(janela, textvariable=dia_var, values=dias, state="readonly")
combo.pack(pady=5)
combo.bind("<<ComboboxSelected>>", lambda e: atualizar_lista())

# Lista de tarefas
lista_tarefas = tk.Listbox(janela, width=45, height=12, font=("Arial", 10))
lista_tarefas.pack(pady=10)

# Entrada de tarefa
entrada_tarefa = tk.Entry(janela, width=40, font=("Arial", 10))
entrada_tarefa.pack(pady=5)

# Botões
frame_botoes = tk.Frame(janela, bg="#f4f4f4")
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Adicionar", bg="#4CAF50", fg="white", width=10, command=adicionar_tarefa).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Remover", bg="#F44336", fg="white", width=10, command=remover_tarefa).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="Atualizar", bg="#2196F3", fg="white", width=10, command=atualizar_lista).grid(row=0, column=2, padx=5)

atualizar_lista()

janela.mainloop()
