import schedule
import time
import sys
import pyautogui
import os
import tkinter as tk

#Criar uma janela raiz
root = tk.Tk()
root.title("ENCERRADOR DE PROGRAMA COM HORA MARCADA !!!")
root.geometry("500x300")

label = tk.Label(root, text="DEFINA UM HORARIO PARA O PROGRAMA SER EXECUTADO NO FORMATO (00:00)")
label.pack(pady=10)

entry_hr = tk.Entry(root)
entry_hr.pack()

label = tk.Label(root, text="DIGITE O NOME DO PROGRAMA QUE SERA FECHADO")
label.pack(pady=10)

entry_pro = tk.Entry(root)
entry_pro.pack(pady=10)

label = tk.Label(root, text="DIGITE A FRASE PARA O ENVIO")
label.pack(pady=10)

entry_msg = tk.Entry(root)
entry_msg.pack(pady=10)

def callback():

    hora = entry_hr.get()
    programa = entry_pro.get()
    msg = entry_msg.get()

    label_hr = tk.Label(root, text="EXECUÇÃO DO PROGRAMA AGENDADA ")
    label_hr.pack()
    print("As ", hora, "hrs o programa", programa, "será encerrado e a frase ", msg, "será enviada")

    def tarefa():

        try:
            # Move o cursor até o campo de digitar mensagem e clica
            pyautogui.moveTo(1100, 650)
            pyautogui.click()
            pyautogui.click()
            # Escreve a mensagem e clica no enter para enviar
            pyautogui.write(msg)
            pyautogui.press('enter')
        except pyautogui.FailSafeException:
            print("Primeira ação falhou. Executando segunda ação...")
            # Move o cursor até a segunda posição e executa a ação alternativa
            pyautogui.moveTo(1200, 500)
            pyautogui.click()

        # Move o cursor até o botão de sair e dá um duplo clique
        pyautogui.moveTo(1290, 70)
        pyautogui.doubleClick()

        def fechar_programa(nome_programa):
            # Executa o comando taskkill para encerrar o programa pelo nome
            os.system(f"taskkill /F /IM {nome_programa}")

        time.sleep(5)
        # Exemplo de uso: fechar o programa "teams.exe"
        fechar_programa(programa)

        print("Tarefa executada!")

        # Encerra o programa
        sys.exit(0)

    # Agendar a tarefa para ser executada às 14:35
    schedule.every().day.at(hora).do(tarefa)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)

button = tk.Button(root, text="Clique Aqui", command=callback)
button.pack()

root.mainloop()