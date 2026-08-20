import requests
from bs4 import BeautifulSoup
import customtkinter as ctk


mainurl = "https://es.wikipedia.org"

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

respuesta = requests.get(mainurl,headers=headers)
soup = BeautifulSoup(respuesta.text, "lxml")
titulo = soup.find("h1", id="firstHeading").text




#esto es para la pagina principal xdxdxd


mainpage = ctk.CTk()
mainpage.title(titulo)
mainpage.geometry("1000x600")
titulomp = ctk.CTkLabel(mainpage,text="WikiWrapTool", font=("Arial", 50), anchor="e")
titulomp.pack(pady=40)
mainpage.configure(fg_color="#1F1F2E")



def boton_buscar():
    pass


boton = ctk.CTkButton(mainpage, text="start to scrap ou yeahh", command=boton_buscar, font=("Arial", 20, "bold"))
boton.pack(pady=80)


insert





mainpage.mainloop()