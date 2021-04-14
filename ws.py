# Importamos y utilizamos la librerias pyautogui y webbrowser
import pyautogui, webbrowser
from time import sleep
#pones un banner facherito 
print("██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗ ██████╗     ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗")     
print("██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗    ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗")    
print("██║ █╗ ██║███████║███████║   ██║   ███████╗███████║██████╔╝██████╔╝    ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝")    
print("██║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██╔══██║██╔═══╝ ██╔═══╝     ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗")    
print("╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║██║  ██║██║     ██║         ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║")    
print(" ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝         ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝")

                                                                                                                             
#pedimos el numero a quien enviar el mensaje con el codigo de la pais 
print('A quien le vas a enviar el mensaje')
num = input()
# pedimos el mensaje que tiene que estar en un archivo .txt (hola.txt)
print('Que archivo va a enviar?')
msg = input()

# con web browser abrimos un ventana del navegador para enviar el mensaje con el numero a enviar 
webbrowser.open('https://web.whatsapp.com/send?phone='+num)

sleep(15)

# metodo que lee el mensaje linea por linea 
with open(msg, 'r') as file:
    for line in file:
        pyautogui.typewrite (line)
        pyautogui.press("enter")