import turtle

# Configuración inicial
t = turtle.Turtle()
t.speed(0)  # Máxima velocidad
turtle.bgcolor("black")  # Fondo negro

# Función para dibujar un pétalo con curvas más suaves y alargadas
def dibujar_petalo():
    t.circle(120, 60)  # Curva más suave y alargada
    t.left(120)
    t.circle(120, 60)
    t.left(120)

# Función para dibujar una flor sin centro ni tallo, solo pétalos
def dibujar_flor(x, y, petalos, color_petalo):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color_petalo, color_petalo)  # Color de los pétalos
    t.begin_fill()
    for _ in range(petalos):
        dibujar_petalo()
        t.left(360 / petalos)  # Ajustamos el giro para la cantidad de pétalos
    t.end_fill()

# Dibuja varias flores en diferentes posiciones y con diferentes colores
dibujar_flor(0, 0, 12, "magenta")      # Flor central magenta
dibujar_flor(-200, 100, 10, "cyan")    # Flor a la izquierda color cian
dibujar_flor(200, -100, 8, "yellow")   # Flor a la derecha color amarillo
dibujar_flor(100, 150, 14, "orange")   # Flor arriba derecha color naranja
dibujar_flor(-100, -150, 16, "lightgreen")  # Flor abajo izquierda verde claro

# Oculta la tortuga y muestra el resultado
t.hideturtle()
turtle.done()
