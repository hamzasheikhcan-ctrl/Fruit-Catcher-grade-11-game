# Fruit Catcher Game
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/65d549ee-716c-4680-bc3d-cd53ec6265bb" />
A fast-paced, fullscreen arcade game built with Python and Pygame where players control a bowl to catch falling fruits while avoiding dangerous bombs. 
Get 700 points under 60 seconds, and the victory is yours!

### 🌟 Features

* **Dynamic Difficulty:** The falling speed of the objects gradually increases as your score gets higher.
* **Dynamic Player Avatar:** The catcher bowl grows wider as you lose lives, making it easier to catch items when you are in danger of losing
* **Power-ups:** Catching a banana triggers a 5-second slow-motion mode, allowing you to catch more fruit before they fall below the scree
* **Combos:** Catching 3 apples within 3 seconds grants a +10 point combo bonus and displays a "COMBO!" notification.

### 🎮 Controls

* **Left Arrow Key:** Move the catching bowl to the left.
* **Right Arrow Key:** Move the catching bowl to the right.
* **Mouse Click:** Use your mouse to interact with the Start, Quit, and Restart menu buttons


### 📋 Rules & Scoring

You start the game with 3 lives and have a maximum time limit of 60 seconds.

| Object / Action | Consequence |
| :--- | :--- |
| **Standard Fruits** (Pear, Apple, Watermelon, Coconut) | +10 points |
| **Banana** | +30 points and activates Slow-Mo mode |
| **Bomb** | -20 points and lose 1 life |
| **Missed Fruit** (Letting it fall off-screen) | -5 points |
| **Missed Bomb** | No penalty |


*❌*Game Over Conditions:❌

* **Win:** Reach a score of 700 or more within the 60-second time limit while having at least 1 life.
  
* **Lose:** Run out of time before reaching the 700-point win score, or lose all 3 of your lives by catching bombs.




### 🛠️ Requirements & Installation

* Python 3.13 is required to run the script.

* The `pygame` library must be installed.

* The game runs in a 1920x1080 fullscreen resolution.

* Ensure your working directory has the following folder structure and image assets in place for the game to load correctly:

* **Images folder (`pics/`):** `bowl_transparent.png`, `pear.png`, `apple.png`, `banana.png`, `watermelon.png`, `coconut.png`, `bomb.png`.
* **Backgrounds folder (`backgrounds/`):** `fruit_ninja.png`, `fruit_ninja2.png`.

