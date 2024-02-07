import pyautogui
import schedule
import time

def realizar_click():

    # Localizar a posição do botão na tela (x, y) usando pyautogui.locateOnScreen()
    botao_pos = pyautogui.locateOnScreen('imagens/botao_sair.png')

    if botao_pos is not None:
        # Obter as coordenadas do centro do botão
        centro_x = botao_pos.left + botao_pos.width / 2
        centro_y = botao_pos.top + botao_pos.height / 2

        # Movimentar o cursor para o centro do botão e realizar o clique
        pyautogui.moveTo(centro_x, centro_y)
        pyautogui.click()
    else:
        print("Botão não encontrado.")

# Agendando o clique para ser executado em um horário específico
schedule.every().day.at("18:31").do(realizar_click)

# Execução contínua do agendador
while True:
    schedule.run_pending()
    time.sleep(1)