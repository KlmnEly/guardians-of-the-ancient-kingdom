# Guardians of the Ancient Kingdom

## 1. Descripcion
Sistema de combate por turnos orientado a objetos desarrollado en Python que enfrenta a distintos guardianes (Guerreros, Magos y Arqueros) aplicando reglas de combate, validaciones estrictas y habilidades especiales únicas para cada orden.

## 2. Estructura del proyecto
El repositorio se encuentra organizado en los siguientes archivos principales:
- `personajes.py`: Contiene la clase abstracta `Personaje`, las subclases (`Guerrero`, `Mago`, `Arquero`) y la clase `Combate` encargada de administrar las rondas y turnos.
- `main.py`: Archivo principal dedicado a ejecutar las pruebas unitarias de validación, la creación de objetos y la simulación del combate.
- `.gitignore`: Archivo de configuración para ignorar carpetas temporales de caché (`__pycache__`).

## 3. Clases, Metodos y Funciones Principales

### Clase Abstracta `Personaje`
- **`__init__`**: Constructor que valida que el nombre no esté vacío, la vida esté entre 0 y 100, el ataque sea positivo y la defensa no sea negativa. Lanza excepciones de tipo `ValueError` si algún dato es incorrecto.
- **Getters y Setters**: Permiten consultar y modificar de forma segura los atributos encapsulados (`__nombre`, `__vida`, `__ataque`, `__defensa`).
- **`recibir_danio(cantidad)`**: Actualiza la vida del personaje asegurando que nunca baje de cero y calcula el daño efectivo recibido.
- **`esta_vivo()`**: Retorna `True` si la vida es mayor a cero, o `False` en caso contrario.
- **`atacar(objetivo)`**: Método abstracto que obliga a las clases hijas a definir su propia lógica de ataque.

### Habilidades Especiales (Subclases)
- **`Guerrero`**: Su ataque especial incrementa un 20% su fuerza antes de descontar la defensa del enemigo ($ataque \times 1.20 - defensa$), redondeando el resultado hacia abajo.
- **`Mago`**: Sus hechizos ignoran por completo la defensa del objetivo, aplicando un daño directo igual a su valor de ataque.
- **`Arquero`**: Evalúa si su ataque supera la defensa del rival. Si es mayor, duplica el daño base convencional; si no lo supera, el daño es cero.

### Clase `Combate`
- **`iniciar()`**: Controla el ciclo de turnos (hasta un máximo de 50 rondas). En cada iteración permite atacar alternadamente si los combatientes siguen con vida.
- **`verificar_ganador()`**: Comprueba el estado de ambos personajes al finalizar los turnos. Si ambos pierden la vida simultáneamente o se agotan las rondas sin un claro vencedor, maneja y declara el **empate técnico**.
- **`mostrar_resultado()`**: Imprime en consola el desenlace final del enfrentamiento.

## 4. Relaciones entre Clases
- **Herencia**: `Guerrero`, `Mago` y `Arquero` heredan los atributos y métodos comunes de la clase base `Personaje`.
- **Asociación**: Los personajes interactúan entre sí llamando a los métodos de daño y ataque de manera directa.
- **Agregación**: La clase `Combate` agrupa y administra a dos participantes que fueron creados de forma independiente.

## 5. Conceptos de POO aplicados
- **Abstracción**: Uso de `ABC` y `@abstractmethod` para definir una estructura genérica obligatoria para los guardianes.
- **Encapsulamiento**: Protección de los datos internos mediante el uso de atributos privados (`__`) y validaciones en los métodos de acceso.
- **Polimorfismo**: El sistema de combate ejecuta la función `atacar()` de forma genérica, permitiendo que cada objeto responda de manera distinta según su tipo específico.

## 6. Pruebas Iniciales y Validaciones
El proyecto incluye pruebas automatizadas en `main.py` que comprueban:
- El rechazo de nombres vacíos o nulos.
- El control de rangos de vida válidos (0 a 100).
- La validación de estadísticas de ataque y defensa correctas.
- El correcto funcionamiento de las habilidades de daño de cada clase y la imposibilidad de tener valores de vida negativos.

## 7. Instrucciones de Clonacion y Ejecucion

Para descargar y ejecutar el proyecto, sigue estos pasos desde tu terminal o consola:

1. Abrir tu **consola o terminal** en la computadora.
2. Clonar el repositorio escribiendo el siguiente comando:
   ```bash
   git clone https://github.com/KlmnEly/guardians-of-the-ancient-kingdom.git
   ```
3. Entrar en la carpeta del repositorio escribiendo el siguiente comando:
   ```bash
   cd guardians-of-the-ancient-kingdom
   ```
4. Ejecutar el archivo principal para correr las pruebas y la simulación del combate:
   ```bash
   python main.py
   ```