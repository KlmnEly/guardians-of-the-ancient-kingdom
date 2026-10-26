from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre, vida, ataque, defensa):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")
        if not (0 <= vida <= 100):
            raise ValueError("La vida debe estar entre 0 y 100.")
        if ataque <= 0:
            raise ValueError("El ataque debe ser un entero positivo.")
        if defensa < 0:
            raise ValueError("La defensa no puede ser negativa.")
        
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa

    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_vida(self):
        return self.__vida
    
    def get_ataque(self):
        return self.__ataque
    
    def get_defensa(self):
        return self.__defensa

    # Setters
    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Nombre invalido.")
        self.__nombre = nombre

    def set_vida(self, vida):
        if not (0 <= vida <= 100):
            raise ValueError("Vida fuera de rango.")
        self.__vida = vida

    def set_ataque(self, ataque):
        if ataque <= 0:
            raise ValueError("Ataque debe ser positivo.")
        self.__ataque = ataque

    def set_defensa(self, defensa):
        if defensa < 0:
            raise ValueError("Defensa no puede ser negativa.")
        self.__defensa = defensa

    def recibir_danio(self, cantidad):
        if cantidad < 0:
            return 0
        danio_real = min(cantidad, self.__vida)
        self.__vida -= danio_real
        if self.__vida < 0:
            self.__vida = 0
        return danio_real

    def esta_vivo(self):
        return self.__vida > 0

    def mostrar_estado(self):
        print(f"[{self.__nombre}] Vida: {self.__vida} | Ataque: {self.__ataque} | Defensa: {self.__defensa}")

    @abstractmethod
    def atacar(self, objetivo):
        pass


class Guerrero(Personaje):
    def atacar(self, objetivo):
        if not self.esta_vivo():
            print(f"{self.get_nombre()} esta derrotado y no puede atacar.")
            return 0
        if not objetivo.esta_vivo():
            print("El objetivo ya esta derrotado.")
            return 0
        
        calculo = self.get_ataque() * 1.20 - objetivo.get_defensa()
        danio = max(0, int(calculo))
        danio_real = objetivo.recibir_danio(danio)
        print(f"-> {self.get_nombre()} (Guerrero) ataca a {objetivo.get_nombre()} causando {danio_real} de danio.")
        return danio_real


class Mago(Personaje):
    def atacar(self, objetivo):
        if not self.esta_vivo():
            print(f"{self.get_nombre()} esta derrotado y no puede atacar.")
            return 0
        if not objetivo.esta_vivo():
            print("El objetivo ya esta derrotado.")
            return 0
        
        danio = self.get_ataque()
        danio_real = objetivo.recibir_danio(danio)
        print(f"-> {self.get_nombre()} (Mago) usa hechizo contra {objetivo.get_nombre()} causando {danio_real} de danio (ignora defensa).")
        return danio_real


class Arquero(Personaje):
    def atacar(self, objetivo):
        if not self.esta_vivo():
            print(f"{self.get_nombre()} esta derrotado y no puede atacar.")
            return 0
        if not objetivo.esta_vivo():
            print("El objetivo ya esta derrotado.")
            return 0
        
        base = max(0, self.get_ataque() - objetivo.get_defensa())
        danio = base * 2 if self.get_ataque() > objetivo.get_defensa() else 0
        danio_real = objetivo.recibir_danio(danio)
        print(f"-> {self.get_nombre()} (Arquero) dispara a {objetivo.get_nombre()} causando {danio_real} de danio.")
        return danio_real


class Combate:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.ronda = 1

    def iniciar(self):
        print(f"\n=== INICIO DEL COMBATE: {self.p1.get_nombre()} vs {self.p2.get_nombre()} ===")
        self.p1.mostrar_estado()
        self.p2.mostrar_estado()
        print("=" * 55)

        while self.p1.esta_vivo() and self.p2.esta_vivo() and self.ronda <= 50:
            print(f"\n--- Ronda {self.ronda} ---")
            
            vida_p1_antes = self.p1.get_vida()
            vida_p2_antes = self.p2.get_vida()

            if self.p1.esta_vivo():
                self.p1.atacar(self.p2)

            if self.p2.esta_vivo():
                self.p2.atacar(self.p1)

            vida_p1_despues = self.p1.get_vida()
            vida_p2_despues = self.p2.get_vida()

            print("Estado:")
            self.p1.mostrar_estado()
            self.p2.mostrar_estado()

            if vida_p1_antes == vida_p1_despues and vida_p2_antes == vida_p2_despues:
                print("-> Empate tecnico: ningun personaje recibio danio en esta ronda.")
                break

            self.ronda += 1

        self.mostrar_resultado()

    def mostrar_resultado(self):
        print("\n" + "=" * 20 + " RESULTADO FINAL " + "=" * 20)
        if self.p1.esta_vivo() and not self.p2.esta_vivo():
            print(f"Ganador: {self.p1.get_nombre()}")
        elif self.p2.esta_vivo() and not self.p1.esta_vivo():
            print(f"Ganador: {self.p2.get_nombre()}")
        else:
            print("El combate termino en empate o limite de rondas.")