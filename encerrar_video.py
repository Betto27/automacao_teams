import pyautogui as bot
import time
import pyperclip
import os
import keyboard
import schedule



def inicirar():

    bot.alert("====== INICIANDO BOT DE  ENCERRAMENTO DE CHAMADA  ======")

    def minha_acao():

        bot.doubleClick('imagens/botao_sairo.png')
        print("Ação executada!")

    # Agendando a ação para ser executada em um horário específico
    schedule.every().day.at("14:23").do(minha_acao)



    bot.alert("====== Finalizando BOT  ======")

inicirar()
# Execução contínua do agendador
while True:
    schedule.run_pending()
    time.sleep(1)



