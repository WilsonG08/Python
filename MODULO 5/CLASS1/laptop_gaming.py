from laptop import Laptop

class Laptop_gaming(Laptop):
    def __init__(self, marca, procesador, memoria, tarjeta_graf, costo=500, impuesto=10):
        # Super para acceder a el metodo de la clase padre
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarjeta_graf = tarjeta_graf

    # EL mismo nombre porque es hijo
    def realizar_diagnostico_sistema(self):
        # ME devuelve un valor y lo almaceno
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juegos = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultado juegos"] = resultado_juegos
        return resultado_diagnostico
    
    def __str__(self):
        return f"Marca: {self.marca}, \n Procesador: {self.procesador}, \n Memoria: {self.memoria}, \n Tarjeta Grafica: {self.tarjeta_graf}, \n Costo: {self.costo},\n Impuesto: {self.impuesto}\n"

    def realizar_diagnostico_juegos(self):
        juegos = ["FORNITE", "COD", "GTA"]
        resultados = {}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarjeta_graf:
                fps = fps_base * 3
            elif "GTX" in self.tarjeta_graf:
                fps = fps_base *2 
            else:
                fps = fps_base

            resultados [juego] = f"{fps} FPS" 
        return resultados
    
    def realizar_informe_uso(self):
        informe = super().realizar_informe_uso()
        informe.update({
            "Tipo" : "Gaming",
            "Uso Recomendado" : "Juegos de video",
            "Horas de uso" : 10,
            "Recomendaciones de Software" : ["Antivirus", "VPN"]
        })
        return informe

    pass