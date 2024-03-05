import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=706, y=372)
pyautogui.write("allanfelipe@gmail.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

table = pd.read_csv("produtos.csv")

for line in table.index:
    pyautogui.click(x=714, y=258)
    codigo = table.loc[line, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "custo"]))
    pyautogui.press("tab")
    obs = table.loc(line, "obs")
    if not pd.isna(obs):
        pyautogui.write(str(table.loc(line, "obs")))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(300)
