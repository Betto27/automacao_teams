import tkinter as tk
from tkinter import ttk

root = tk.Tk()
label = tk.Label(root, text="DIGITE O NOME DO PROGRAMA QUE SERA FECHADO")
label.pack(side="left", fill="both", padx=10, pady=10, anchor="nw")

# Criar uma instância do Combobox
combo = ttk.Combobox(root, state="readonly", width=10)

# Definir as opções do combo de hora
horas = [str(i).zfill(2) for i in range(24)]
combo["values"] = horas

# Definir o valor padrão selecionado
combo.set(horas[0])

# Posicionar o Combobox na janela
combo.pack()

root.mainloop()