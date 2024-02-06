# Importar módulos necesarios
import requests
from tkinter import *
from tkinter import ttk

# Función para obtener información de un Pokémon a través de la API
def obtener_pokemon(numero):
    # Construir la URL de la API con el número del Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{numero}/"
    # Realizar una solicitud GET a la API
    respuesta = requests.get(url)
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Convertir la respuesta a formato JSON
        datos_pokemon = respuesta.json()
        # Extraer información relevante del Pokémon
        nombre = datos_pokemon["name"].capitalize()
        tipos = "/".join([tipo["type"]["name"].capitalize() for tipo in datos_pokemon["types"]])
        altura = str(datos_pokemon["height"] / 10) + " m"
        peso = str(datos_pokemon["weight"] / 10) + " kg"
        # Devolver los datos del Pokémon en una tupla
        return (numero, nombre, tipos, altura, peso)
    else:
        # Imprimir un mensaje de error si la solicitud no fue exitosa
        print(f"No se pudo obtener la información del Pokemon {numero}")
        return None

# Crear la ventana principal de la aplicación
Ventana_principal = Tk()
Ventana_principal.title("Tabla del doctor Oak")
Ventana_principal.minsize(width=1200, height=600)
Ventana_principal.config(padx=35, pady=35)
Ventana_principal['bg'] = '#fb0'

# Crear un Treeview (tabla) para mostrar la información de los Pokémon
tv = ttk.Treeview(Ventana_principal, columns=("col0", "col1", "col2", "col3", "col4"))

# Configurar las columnas de la tabla
tv.column("#0", width=0)
tv.column("col0", width=220, anchor=CENTER)
tv.column("col1", width=220, anchor=CENTER)
tv.column("col2", width=220, anchor=CENTER)
tv.column("col3", width=220, anchor=CENTER)
tv.column("col4", width=220, anchor=CENTER)

# Configurar las cabeceras de las columnas
tv.heading("col0", text="ID", anchor=CENTER)
tv.heading("col1", text="Nombre", anchor=CENTER)
tv.heading("col2", text="Tipo(s)", anchor=CENTER)
tv.heading("col3", text="Altura", anchor=CENTER)
tv.heading("col4", text="Peso", anchor=CENTER)

# Obtener información de los primeros 151 Pokémon y mostrar solo los de tipo "Grass"
for numero in range(1, 152):
    datos = obtener_pokemon(numero)
    if datos:
        tipos = datos[2]  # Extraer la cadena de tipos del Pokémon
        if "Grass" in tipos:  # Revisar si el tipo "Grass" está en la lista de tipos
            # Insertar una nueva fila en la tabla con los datos del Pokémon
            tv.insert("", "end", values=datos)

# Empaquetar y mostrar la tabla en la ventana principal
tv.pack(fill="both", expand=True)
Ventana_principal.mainloop()
