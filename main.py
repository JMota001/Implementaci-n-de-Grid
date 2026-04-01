import tkinter as tk
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
USER_ENV = os.getenv("APP_USER")
PASS_ENV = os.getenv("APP_PASSWORD")

def validar():
    if entry_user.get() == USER_ENV and entry_pass.get() == PASS_ENV:
        lbl_info.config(text="Acceso correcto", fg="green")
    else:
        lbl_info.config(text="Usuario o contraseña incorrectos", fg="red")

# --- Ventana Principal ---
ventana = tk.Tk()
color_fondo = "lightblue"
ventana.title("Mi primera app en tkinte")
ventana.geometry("300x500")
ventana.configure(bg=color_fondo)

# Etiquetas y campos
label_usuario=tk.Label(ventana,bg="white", text="Usuario",fg="black").grid(row=1, column=0, pady=25)
entry_user = tk.Entry(ventana)
entry_user.grid(row=2, column=0, pady=25)

label_password=tk.Label(ventana, bg="white", text="Contraseña",fg="black").grid(row=3, column=0, pady=25)
entry_pass = tk.Entry(ventana, show="*")
entry_pass.grid(row=4, column=0, pady=25)

# Botón Principal
tk.Button(ventana, text="ENTRAR", bg="blue", fg="white", command=validar).grid(row=5, column=0, pady=28)

# Mensaje de respuesta
lbl_info = tk.Label(ventana, text="")
lbl_info.grid(row=6, column=0, pady=10)

ventana.mainloop()