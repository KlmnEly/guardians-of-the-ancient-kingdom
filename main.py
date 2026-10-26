from personajes import Guerrero, Mago, Arquero, Combate

def ejecutar_casos_de_prueba():
    print("=== CASOS DE PRUEBA ===")
    
    try:
        g = Guerrero("Arthas", 100, 30, 20)
        m = Mago("Gandalf", 80, 40, 10)
        a = Arquero("Legolas", 90, 35, 15)
        print("[OK] Creacion correcta de personajes.")
    except Exception as e:
        print(f"[ERROR] {e}")

    print("\nPruebas de validacion de errores:")
    try:
        Guerrero("", 100, 30, 20)
    except ValueError as e:
        print(f"[OK] Nombre vacio: {e}")

    try:
        Guerrero("Arthas", 120, 30, 20)
    except ValueError as e:
        print(f"[OK] Vida superior a 100: {e}")

    try:
        Guerrero("Arthas", -5, 30, 20)
    except ValueError as e:
        print(f"[OK] Vida negativa: {e}")

    try:
        Guerrero("Arthas", 50, -10, 20)
    except ValueError as e:
        print(f"[OK] Ataque negativo: {e}")

    try:
        Guerrero("Arthas", 50, 30, -5)
    except ValueError as e:
        print(f"[OK] Defensa negativa: {e}")

    print("\n" + "=" * 40 + "\n")

if __name__ == "__main__":
    ejecutar_casos_de_prueba()

    arthas = Guerrero("Arthas", 100, 30, 20)
    gandalf = Mago("Gandalf", 80, 40, 10)

    combate = Combate(arthas, gandalf)
    combate.iniciar()