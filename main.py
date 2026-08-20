import requests
from bs4 import BeautifulSoup
import customtkinter as ctk
from PIL import Image
from io import BytesIO
import webbrowser


headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

mainurl = "https://es.wikipedia.org"
respuesta = requests.get(mainurl,headers=headers)
soup = BeautifulSoup(respuesta.text, "lxml")
titulo = soup.find("h1", id="firstHeading").text




#pagina de busqueda
def newpage(solicitud):
    searchpage = ctk.CTk()
    searchpage.geometry("1000x615")
    soup = BeautifulSoup(solicitud.text, "lxml")
    title = soup.find("h1", id="firstHeading").text

    imagenes = []
    videos = []
    links = []

    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            if src.startswith("//"):
                src = "https:" + src
            imagenes.append(src)
    

    
    for video in soup.find_all("video"):
        source = video.find("source")
        if source:
            v_src = video.find("source")
            if v_src.startswith("//"):
                v_src = "https:" + v_src
            videos.append(src)


    for a in soup.find_all("a", href=True):
        href = a.get("href")
        if href.startswith("/wiki/"):
            if ":" not in href:
                link = "https://es.wikipedia.org" + href
                links.append(link)
               
        elif href.startswith("http://") or href.startswith("https://"):
            links.append(href)


   
    marco_abajo = ctk.CTkFrame(searchpage, fg_color="transparent")
    marco_abajo.pack(pady=0)

    marco_videos = ctk.CTkFrame(marco_abajo, fg_color="transparent")
    marco_videos.pack(pady=0, side="left")


    marco_imagenes = ctk.CTkFrame(marco_abajo, fg_color="transparent")
    marco_imagenes.pack(pady=0, side="right")






    marco_arriba = ctk.CTkFrame(searchpage, fg_color="transparent")
    marco_arriba.pack(pady=0)

    marco_links = ctk.CTkFrame(marco_arriba, fg_color="transparent")
    marco_links.pack(pady=0, side="right")


    marco_titulo = ctk.CTkFrame(marco_arriba, fg_color="transparent")
    marco_titulo.pack(pady=0, side="left")


    titulomp = ctk.CTkLabel(marco_titulo,text="WikiWrapTool ", font=("Segoe UI", 40, "bold"), anchor="e" )
    titulomp.pack(side="left",pady=0)
    titulomp = ctk.CTkLabel(marco_titulo,text=title, font=("Segoe UI", 35, "bold"), anchor="e" )
    titulomp.pack(side="left",pady=0)




    scroll_links = ctk.CTkScrollableFrame(marco_links, width=420, height=220)
    scroll_links.pack(fill="both", expand=True)

    def abrir(url_destino):
        webbrowser.open(url_destino)
        
    for link in links:
        btn_link = ctk.CTkButton(
            scroll_links, 
            text=link, 
            font=("Arial", 18),
            fg_color="transparent",
            text_color="#64B5F6",
            hover_color="#2B2B3D",
            anchor="w",
            command=lambda l=link: abrir(l)
        )
        btn_link.pack(fill="x", pady=2, padx=5)

    searchpage.mainloop()






#esto es para la pagina principal xdxdxd


if "Wikipedia" in titulo:
    titulo = "Connected with wikipedia"
else:
    titulo = "Error connecting"
mainpage = ctk.CTk()


marco_titulo = ctk.CTkFrame(mainpage, fg_color="transparent")
marco_titulo.pack(pady=60)

mainpage.title(titulo)
mainpage.geometry("1000x615")

titulomp = ctk.CTkLabel(marco_titulo,text="WikiWrapTool", font=("Segoe UI", 50, "bold"), anchor="e" )
titulomp.pack(side="left",pady=0)
logo_imagen = ctk.CTkLabel(marco_titulo, image=ctk.CTkImage(light_image=Image.open("wikitool/spider.png"), dark_image=Image.open("wikitool/spider.png"), size=(140,80)), text="")
logo_imagen.pack(side="right")

mainpage.configure(fg_color="#1F1F2E")



def boton_buscar():
    url = insertar_url.get().strip()
    try:    
        
        solicitud = requests.get(url,headers=headers)
        if solicitud.status_code == 200:
            newpage(solicitud)
    except:
        error = ctk.CTk()
        mte = ctk.CTkFrame(error, fg_color="transparent")
        mte.pack(pady=60)
        titulomp = ctk.CTkLabel(mte,text="ERROR searching or getting: ", font=("Segoe UI", 20, "bold"), anchor="e" )
        titulomp.pack(pady=0,side="left")
        titulomp = ctk.CTkLabel(mte,text=url, font=("Segoe UI", 23, "bold"), anchor="e" )
        titulomp.pack(pady=0,side="right")
        error.geometry("800x150")
        error.configure(fg_color="#FD6161")
        e = "Error searching: " + url
        error.title(e)
        error.mainloop()


textomp = ctk.CTkLabel(mainpage,text="""
wikiwraptool its a tool for wikipedia, put below your wikipedia url you want to scrap and you can get the images,videos,gifs,links etc...,
the finally of this tool its you can get easy acces to the files that wikipedia provides, also its a random button if you want to try!



""", font=("Arial", 15), anchor="e")
textomp.pack(pady=0)



marco_inferior = ctk.CTkFrame(mainpage, fg_color="transparent")
marco_inferior.pack(pady=100)


insertar_url = ctk.CTkEntry(marco_inferior, placeholder_text="insert wikipedia url here", width=275, height=45, font=("Arial", 15, "bold")) 
insertar_url.pack(pady=0)




boton = ctk.CTkButton(marco_inferior, text="start to scrap ou yeahh", command=boton_buscar, font=("Arial", 20, "bold"), width=350, height=50)
boton.pack(pady=0)







mainpage.mainloop()