# 2D Flight Simulator Game

Welcome to the **2D Flight Simulator Game**! In this game, you pilot a plane, navigate the skies, and simulate real-world physics. Key features include smooth controls, HUD updates, and correct speed mechanics resembling the **B-2 Spirit Bomber** with a maximum speed of **628 mph**.

---

## Features

### 1. Dynamic Plane Physics
- **Throttle Control**: Adjust speed dynamically by increasing or decreasing throttle.
- **Landing Gear Mechanics**: Deploy and retract landing gear as needed during the flight.
- **Altitude and Movement**:
   - Use arrow keys to ascend and descend.
   - Accelerate and decelerate horizontally with realistic drag effects.
- **Maximum Speed Limit**: Aircraft tops out at **628 mph** (in game units).

### 2. Heads-Up Display (HUD)
- Displays real-time data:
  - **Speed**: Horizontal movement speed.
  - **Altitude**: Distance above ground level.
  - **Throttle Percentage**: Fuel thrust output.
  - **Landing Gear Status**: Shows whether landing gear is deployed or retracted.

### 3. Visual and Background Scrolling
- Infinite background tiling for horizontal and vertical scrolling.
- Seamless plane movement across a visually rich background.

---

## Controls

| Key          | Action                              |
|--------------|-------------------------------------|
| **Up Arrow** | Ascend / Increase Altitude          |
| **Down Arrow** | Descend / Decrease Altitude        |
| **Right Arrow** | Accelerate (Increase speed)       |
| **Left Arrow** | Decelerate (Reduce speed)          |
| **L**         | Toggle landing gear (Deployed/Retracted) |
| **Page Up**   | Increase throttle (boost thrust)   |
| **Page Down** | Decrease throttle                  |

---

## Installation

### Prerequisites
1. [Python 3.x](https://www.python.org/) must be installed.
2. Install `pygame` library:
   ```bash
   pip install pygame
   ```

---

## How to Run

1. Clone or download the repository.
2. Ensure the following files are in the **assets/** folder:
   - `plane.png`: The plane image.
   - `background.png`: The background image.
3. Run the game:
   ```bash
   python main.py
   ```

---

## Gameplay

1. Start the game, and the plane is idle on the runway (at the bottom of the screen).
2. Use **Page Up/Down** to control throttle.
3. Move the plane:
   - Use **Right/Left Arrow** to increase/decrease horizontal speed.
   - Use **Up/Down Arrow** to ascend/descend.
4. Toggle **Landing Gear**:
   - Press **L** to deploy or retract the landing gear.
   - HUD dynamically updates the landing gear status.

---

## File Overview

```
flight_simulator/
├── main.py            # Main game logic
├── README.md          # Documentation
└── assets/            # Game assets
    ├── plane.png      # Plane sprite
    ├── background.png # Background image
```

---

## Troubleshooting

1. **Assets Not Found**:
   Ensure you’ve placed `plane.png` and `background.png` in the `assets/` folder.
   
2. **Pygame Not Installed**:
   Install `pygame` with:
   ```bash
   pip install pygame
   ```

3. **Screen Freezes or Stutters**:
   - Reduce frame rendering logic.
   - Check system performance.

---

## Credits

- **Plane Sprite and Background**: Please ensure `plane.png` and `background.png` are royalty-free images or have proper attribution.
- Game developed using **Pygame**.

---

## License

This project is licensed under the **MIT License**. You’re free to use, modify, and distribute this project with proper attribution.

