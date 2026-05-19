# Velocity Rush

A fast-paced 2D endless runner game built with Python and Pygame. Jump over obstacles, collect coins, and beat your high score!

---

## Gameplay

- Run automatically and **jump over obstacles** to survive
- **Collect coins** for bonus points
- The game gets **faster over time** — how long can you last?
- Your **high score is saved** between sessions

---

## Controls

| Key | Action |
|-----|--------|
| `SPACE` | Jump |
| `SPACE` (on Game Over screen) | Restart |

---

## Structure

```
velocity-rush/
├── velocity_rush.py     # Main game file
├── highscore.json       # Saved high score
├── bg.png               # Scrolling background
├── player1.png          # Player run sprite
├── jump.png             # Player jump sprite
├── obstacle.png         # Obstacle sprite
├── coin.png             # Coin sprite
├── jump.wav             # Jump sound effect
├── coin.wav             # Coin collect sound effect
├── hit.wav              # Collision sound effect
└── README.md
```

---

## Scoring

| Action | Points |
|--------|--------|
| Surviving (per frame) | +1 |
| Collecting a coin | +50 |

The game speed increases gradually over time. Your high score is automatically saved to `highscore.json`.

---

## Obstacle Types

- **Normal** — moves at standard speed
- **Fast** — moves 1.5× faster, harder to react to

---

## Built With

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/)
