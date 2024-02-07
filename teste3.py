import schedule
import time
import sys
import pyautogui

def tarefa():
    print("Tarefa executada!")

    #Move o cursor até o campo de digitar mensagem e clica
    pyautogui.moveTo(1100, 650)
    pyautogui.click()
    pyautogui.click()
    #Escreve a mensagem e clica no enter para enviar
    pyautogui.write(" . ")
    pyautogui.press('enter')

    #Move o cursor ate o botão de sair e da um duplo click
    pyautogui.moveTo(1290, 70)
    pyautogui.doubleClick()

    # Encerra o programa
    sys.exit(0)

# Agendar a tarefa para ser executada às 8:00
schedule.every().day.at("14:35").do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(1)
