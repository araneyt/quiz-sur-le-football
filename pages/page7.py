import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Dimensionen des Spielfelds
FIELD_HEIGHT = 200
FIELD_WIDTH = 300
GOAL_HEIGHT = 50
GOAL_WIDTH = 20
NET_LINES = 5  # Anzahl der Linien im Netz

# Initialisierung der Ballposition
ball_x = FIELD_WIDTH // 2
ball_y = FIELD_HEIGHT // 2

# Funktion zum Zeichnen des Spielfelds und des Balls
def draw_field():
    fig, ax = plt.subplots()
    ax.set_xlim(0, FIELD_WIDTH)
    ax.set_ylim(0, FIELD_HEIGHT)

    # Spielfeld
    ax.fill_between([0, FIELD_WIDTH], GOAL_HEIGHT, FIELD_HEIGHT - GOAL_HEIGHT, color='green')

    # Tore mit Netz
    goal1 = Rectangle((-GOAL_WIDTH, (FIELD_HEIGHT - GOAL_HEIGHT) / 2), GOAL_WIDTH, GOAL_HEIGHT, color='black')
    ax.add_patch(goal1)
    goal2 = Rectangle((FIELD_WIDTH - GOAL_WIDTH, (FIELD_HEIGHT - GOAL_HEIGHT) / 2), GOAL_WIDTH, GOAL_HEIGHT, color='black')
    ax.add_patch(goal2)

    # Netzlinien
    for i in range(1, NET_LINES):
        ax.plot([-GOAL_WIDTH, 0], [(i / NET_LINES) * GOAL_HEIGHT, (i / NET_LINES) * GOAL_HEIGHT], 'w-', lw=2)
        ax.plot([FIELD_WIDTH - GOAL_WIDTH, FIELD_WIDTH], [(i / NET_LINES) * GOAL_HEIGHT, (i / NET_LINES) * GOAL_HEIGHT], 'w-', lw=2)

    # Fußball
    draw_football(ax, ball_x, ball_y)

    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    st.pyplot(fig)

# Funktion zum Zeichnen eines Fußballs
def draw_football(ax, x, y):
    ball_radius = 10
    circle = plt.Circle((x, y), ball_radius, color='black')
    ax.add_artist(circle)
    patches = []
    for angle in range(0, 360, 36):
        angle_rad = np.radians(angle)
        x1 = x + ball_radius * np.cos(angle_rad)
        y1 = y + ball_radius * np.sin(angle_rad)
        patches.append([x1, y1])

    vertices = np.array(patches)
    path = plt.Polygon(vertices, closed=True, fill=None, edgecolor='black')
    ax.add_patch(path)

# Hauptprogramm
def main():
    st.title("Wandtafelfußball")

    st.write("Willkommen beim Wandtafelfußball!")
    st.write("Bewege den Ball mit den Pfeiltasten.")

    # Tastatureingabe abfangen
    key = st.radio("Richtung wählen:", options=["↑", "↓", "←", "→"])

    # Bewegung des Balls basierend auf der Tastatureingabe
    global ball_x, ball_y
    if key == "↑":
        ball_y -= 10
    elif key == "↓":
        ball_y += 10
    elif key == "←":
        ball_x -= 10
    elif key == "→":
        ball_x += 10

    # Ball innerhalb des Spielfelds halten
    ball_x = np.clip(ball_x, 0, FIELD_WIDTH)
    ball_y = np.clip(ball_y, 0, FIELD_HEIGHT - GOAL_HEIGHT)

    # Spielfeld zeichnen
    draw_field()

if __name__ == "__main__":
    main()

