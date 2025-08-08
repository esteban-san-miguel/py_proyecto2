import csv
import os

class Gestor_CSV: # clase
    def __init__(self, archivo): # constructor (propiedades y estado inicial del objeto)
        self.archivo = archivo # Permite acceder a los atributos del objeto como el archivo
        self.headers = [
            "fecha", "nombre", "apellido", "celular", "email", 
            "marca", "item", "modelo", "n/s", "precio s/iva usd",
            "precio c/iva usd", "cambio $", "precio s/iva $", "precioc/iva $",
            "forma pago", "factura tipo", "factura nro", "comisión usd", "comisión $"
        ]
        self.inicializar_archivo() # Llamada al método para inicializar el archivo

    def inicializar_archivo(self): # método de clase (acciones que realizará el objeto)
        if not os.path.exists(self.archivo): # verifica si existe el archivo sino lo crea
            with open(self.archivo, "w", newline="") as f: # abre el archivo en modo escritura
                writer = csv.writer(f) # instancía la clase, crea el objeto writer
                writer.writerow(self.headers) # escribe los encabezados en la fila 1 (0)
                
    def guardar(self, fila): # método de clase c/2 args (fila es un diccionario contenedor del archivo csv)
        archivo_vacio = not os.path.exists(self.archivo) or os.path.getsize(self.archivo) == 0
        with open(self.archivo, "a", newline="") as f: # abre, agrega y cierra el archivo csv
            writer = csv.DictWriter(f, fieldnames=self.headers) # escribe datos en el archivo desde diccionarios
            if archivo_vacio:
                writer.writeheader() # llamada al método que escribe los encabezados si el archivo está vacío
            writer.writerow(fila) # llamada al método que escribe la fila pasada como un diccionario
            
    def cargar(self): # método de clase
        if not os.path.exists(self.archivo): # verifica si existe el archivo sino lo crea
            return [] # si csv no existe, retorna una lista vacía para evitar errores
        with open(self.archivo, "r", newline="") as f: # abre el archivo en modo lectura
            reader = csv.DictReader(f) # Lee como diccionarios donde clave=header, valor=datos
            return list(reader) # Convierte al objeto reader (iterador) en una lista completa
        
    def eliminar(self, index): # método de clase donde index es un entero y representa índeice de posición
        datos = self.cargar() # datos recibe lista de diccionarios traídos por el método cargar
        if 0 <= index <= len(datos): # verifica que index esté dentro de los límites de la lista
            datos.pop(index) # elimina el elemento de la posición index y corre una fila hacia arriba
            with open(self.archivo, "w", newline="") as f: # abre, escribe y cierra el archivo
                writer = csv.DictWriter(f, fieldnames=self.headers) # crea el objeto reader y escribe filas como diccionarios según orden y columnas
                writer.writeheader() # escribe 1er fila con los encabezados
                writer.writerows(datos) # escribe filas como diccionarios, excepto la eliminada
                
    def eliminar_todo(self): # método de clase
        with open(self.archivo, "w", newline="") as f: # abre, escribe y cierra el csv y borra todo su contenido
            writer = csv.writer(f) # crea el objeto writer csv, escribe filas csv en el archivo f
            writer. writerow(self.headers) # llamada al método en la que self.headers es una lista con los encabezados y escribiéndola como única fila