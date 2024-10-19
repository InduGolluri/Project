# Snake-Gam

Hey there! I'm Hindhu, a third-year BTech student! 👩‍🎓 Welcome to my GitHub! I'm excited to share my projects, learn from each other, and explore the world of coding together. Let’s collaborate and create something amazing!
Let's play and learn together!

<br><br>
# Snake Game Overview

## Objective
The goal of the game is to control a snake on a grid, eat food items to grow in length, and avoid collisions with itself or the game boundaries. The game ends when such collisions occur.

## Setup
- **Game Screen**: A square grid with dimensions of 600x600 pixels.
- **Snake Start Position**: The snake begins in the center of the grid, facing a default direction (typically right).
- **Food Appearance**: Food items appear randomly on the grid for the snake to eat.

## Gameplay Mechanics

### Snake Movement
- The snake moves continuously in the direction it was last directed by the player using the arrow keys.
- Arrow keys (UP, DOWN, LEFT, RIGHT) control the direction of the snake's movement.
- The snake wraps around the screen edges, meaning if it moves off one edge, it reappears on the opposite edge (similar to classic snake games).

### Eating Food
- Food items are represented as small circles that appear randomly on the grid.
- When the snake’s head (the front segment) collides with a food item, it consumes the food.
- Upon eating food, the snake grows longer by adding a new segment to its tail.

### Growing and Scoring
- Each time the snake eats food, the player's score increases.
- The game speed may increase as the snake grows longer or based on specific game settings.

### Game Over Conditions
- The game ends if the snake collides with itself (when its head intersects with any part of its body).
- The game also ends if the snake collides with the screen boundaries (unless the wrap-around feature is enabled).

## Features

### Color Scheme
- The snake is light yellow in color.
- Food items are represented by dark blue circles.

### User Interaction
- Players control the snake's movement in real-time using the arrow keys.
- The game updates the snake's position and checks for collisions based on player input.

## Future Improvements
Possible enhancements could include:
- Increasing game difficulty over time.
- Adding obstacles or hazards on the grid.
- Implementing levels with different challenges or objectives.

# Installation Guide for Snake Game

## Requirements
Before running the game, ensure you have the following installed:
- **Python 3.x**
- **Pygame Library**: Install using the command:
  ```bash
  pip install pygame
  ```

## Installation Steps

1. **Clone the Repository**:
   Open your terminal and run:
   ```bash
   git clone https://github.com/InduGolluri/Snake-Game.git
   ```

2. **Install Pygame**:
   If Pygame is not already installed, install it by executing:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   Navigate to the game directory and start the game. 

You're all set to enjoy the Snake Game!

-----------------------------------------------------------******------------------------------------------------------

Run the script and have fun!

Thank you!

Developed by:Hindhu Golluri (Hindhu Golluri, GameHub)
