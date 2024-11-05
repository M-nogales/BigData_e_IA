# 10. **Clase Reloj**
# Define una clase Reloj con atributos como hora, minuto y segundo actual.
# Métodos que permitan ajustar la hora, avanzar un minuto o segundo, 
# y mostrar la hora actual en formato hh:mm:ss.

class Reloj:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def ajustar_hora(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def avanzar_minuto(self):
        if self.minuto == 59:
            self.minuto = 0
            if self.hora == 23:
                self.hora = 0
            else:
                self.hora += 1
        else:
            self.minuto += 1
    
    def avanzar_segundo(self):
        if self.segundo == 59:
            self.segundo = 0
            self.avanzar_minuto()
        else:
            self.segundo += 1
    
    def mostrar_hora(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
    
reloj1 = Reloj(12, 30, 45)
print('reloj1.mostrar_hora(): ', reloj1.mostrar_hora())
reloj1.avanzar_minuto()
print('reloj1.avanzar_minuto(): ')
print('reloj1.mostrar_hora(): ', reloj1.mostrar_hora())
reloj1.avanzar_segundo()
print('reloj1.avanzar_segundo(): ')
print('reloj1.mostrar_hora(): ', reloj1.mostrar_hora())
reloj1.ajustar_hora(23, 59, 59)
print('reloj1.ajustar_hora(23, 59, 59): ')
print('reloj1.mostrar_hora(): ', reloj1.mostrar_hora())
reloj1.avanzar_minuto()
print('reloj1.avanzar_minuto(): ')
print('reloj1.mostrar_hora(): ', reloj1.mostrar_hora())