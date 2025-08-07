import csv
import os

class Gestor_CSV: # clase
    def __init__(self, archivo): # constructor (propiedades y estado inicial del objeto)
        self.archivo = archivo
        self.headers = [
            "fecha", "nombre", "apellido", "celular", "email", 
            "marca", "item", "modelo", "n/s", "precio s/iva usd",
            "precio c/iva usd", "cambio $", "precio s/iva $", "precioc/iva $",
            "forma pago", "factura tipo", "factura nro", "comisión usd", "comisión $"
        ]
        self.inicializar_archivo()

    def inicializar_archivo(self): # método de clase (acciones que realizará el objeto)
        if not os.path.exists(self.archivo): # verifica si existe el archivo
            with open(self.archivo, "w", newline="") as f: # abre el archivo en modo escritura
                writer = csv.writer(f) # crea el archivo y escribe las columnas
                writer.writerow(self.headers) # escribe los encabezados en la fila 1 (0)
                
    def guardar(self, fila): # método de clase c/2 args (fila es un diccionario contenedor del archivo csv)
        with open(self.archivo, "a", newline="") as f: # abre, agrega y cierra el archivo csv
            writer = csv.DictWriter(f, fieldnames=self.headers) # escribe datos en el archivo desde diccionarios
            writer.writerow(self.headers) # escribe una fila nueva según el orden de fieldnames
            
    