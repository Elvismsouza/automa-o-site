import webbrowser
import pyautogui
import pyperclip

webbrowser.open('https://cursoautomacao.netlify.app/')

pyautogui.moveTo(879,261,duration=2)
pyautogui.scroll(-2200)
pyautogui.click()

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')
pyautogui.click()
escrever_frase('ELVIS MARTINS DE SOUZA')

pyautogui.moveTo(884,301,duration=1)
pyautogui.click()

pyautogui.moveTo(1274,292,duration=1)
pyautogui.moveTo(1272,213,duration=1)
pyautogui.click()

pyautogui.moveTo(858,308,duration=2)
pyautogui.scroll(2200)
pyautogui.click()

pyautogui.moveTo(929,301,duration=2)
pyautogui.scroll(-3450)
pyautogui.click()

pyautogui.moveTo(928,415,duration=2)
pyautogui.click()

pyautogui.alert(text='VOCÊ TERMINOU!', title='Alerta', button='OK')
