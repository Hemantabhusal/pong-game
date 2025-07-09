# 🏓 Pong Game

A classic Pong game built using **Python** and **Pygame**, offering **single-player** (keyboard or mouse) and **two-player** modes. Players control paddles to hit a moving ball, scoring points when their opponent misses. Features include sound effects, start and end screens, increasing difficulty, and polished visuals.

---

## 🎮 Features

### Game Modes

- **Single-player (Keyboard):** Control one paddle using arrow keys; control switches based on ball direction.
- **Single-player (Mouse):** Control one paddle using mouse movement.
- **Two-player:** 
  - Left paddle: `W` (up), `S` (down)  
  - Right paddle: `↑` (up), `↓` (down)

### Gameplay

- Dynamic ball bounce angles based on paddle hit position.
- Score when the ball passes the opponent's paddle.
- Game ends when a player scores 5 points.
- Increasing ball and paddle speed for added challenge.
- Start screen, end screen with options to replay, return to home, or exit.

### Audio & Visuals

- Paddle and wall hit sound effects.
- Clean UI with a dotted center line and real-time score display.

---

## 📦 Prerequisites

- Python **3.6+**
- Pygame

Install Pygame using:

```bash
pip install pygame
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Hemantabhusal/pong-game.git
```

Navigate to the project directory:

```bash
cd pong-game
```

Install dependencies:

```bash
pip install pygame
```

---

## 🕹️ Usage

Ensure the sound files (`paddle_hit_sound.wav`, `wall_hit_sound.wav`) are located inside the `sounds/` directory.

Run the game:

```bash
python main.py
```

Select your preferred mode from the start screen:
- Single-player (keyboard or mouse)
- Two-player

Play continues until one side reaches 5 points, followed by end screen options:
- Replay  
- Return to Home  
- Exit

---

## ⌨️ Controls

### Single-player

- **Keyboard:** `↑` / `↓` to move the active paddle.
- **Mouse:** Move the mouse vertically to control the active paddle.

### Two-player

- **Left Paddle:** `W` (up), `S` (down)
- **Right Paddle:** `↑` (up), `↓` (down)

---

## 📁 File Structure

```text
pong-game/
├── game_objects/
│   ├── ball.py               # Ball logic (movement, collisions, reset)
│   └── paddle.py             # Paddle behavior and speed control
├── screens/
│   ├── start_screen.py       # Handles start menu UI
│   └── end_screen.py         # Handles end game screen and replay logic
├── sounds/
│   ├── paddle_hit_sound.wav  # Sound for paddle hits
│   └── wall_hit_sound.wav    # Sound for wall collisions
├── utils/
│   ├── constants.py          # Game constants (size, speed, colors)
│   └── helper.py             # Helper functions (e.g., draw_dotted_line)
├── main.py                   # Main game loop
└── README.md                 # Project documentation
```

---

## 📝 Notes

- Ensure sound files are present in the `sounds/` directory.
- Check and fix potential issue in `ball.py`:  
  Replace `SCREEN_HEIGHT * 3 // 3` with `SCREEN_HEIGHT // 2` if necessary for correct vertical reset position.

---

## 📄 License

Licensed under the **MIT License** — feel free to modify and distribute as needed.
