import csv
import os

class Gestor_CSV:
    def __init__(self, archivo):
        self.archivo = archivo
        self.headers = [
            "fecha", "nombre", "apellido", "celular", "email", 
            "marca", "item", "modelo", "n/s", "precio s/iva usd",
            "precio c/iva usd", "cambio $", "precio s/iva $", "precioc/iva $",
            "forma pago", "factura tipo", "factura nro", "comisión usd", "comisión $"
        ]
        self.inicializar_archivo()

    def inicializar_archivo(self): # método de clase
        if not os.path.exists(self.archivo): # verifica si existe el archivo
            with open(self.archivo, "w", newline="") as f: # abre el archivo en modo escritura
                writer = csv.writer(f) # crea el archivo y escribe las columnas
                writer.writerow(self.headers) # escribe los encabezados en la fila 1 (0)
                