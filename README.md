# **PRD: RoboPet Web Game**

## **1. Project Overview**
RoboPet is an **interactive virtual pet simulation game**, where users **adopt, feed, play with, and take care of a digital pet** through a web-based interface. The game dynamically updates the pet's **energy, hunger, and happiness** levels, and the pet evolves based on how well it is cared for. If neglected, RoboPet may **run away** or become sick.  

The game is designed to be **simple yet engaging**, incorporating real-time interactions, **progress bars**, and **cute animations** to enhance the user experience.  

---

## **2. Target Audience**
- **Casual web users** looking for a fun, low-maintenance virtual pet experience.  
- **Children & students** who enjoy pet simulations like Tamagotchi or Nintendogs.  
- **Time management & productivity users** who want a lighthearted, interactive break.  
- **Gamification enthusiasts** interested in AI-driven pet evolution mechanics.  

---

## **3. Core Features & Functionality**
### **3.1 Pet Adoption & Customization**
- Users **start by adopting a pet**:
  - Choose a **pet type** (cat, dog, dragon, alien, etc.).
  - Choose a **pet name** (text input).
- Each pet type has **unique animations and behaviors**.

### **3.2 Pet Stats & Status**
- The pet has three core stats that continuously change:
  1. **Energy** ⚡ (decreases over time, restored by sleeping)
  2. **Hunger** 🍖 (increases over time, reduced when fed)
  3. **Happiness** 🎾 (increases with play, decreases if ignored)
- **Real-time stat tracking**:
  - A **progress bar UI** shows the pet’s current stats.
  - Stats gradually change over time.
  - Users must interact to keep their pet happy and healthy.

### **3.3 Interactive Actions**
- Users can **click buttons** to interact with RoboPet:
  1. **Feed it** 🍖 (Restores hunger)
  2. **Play with it** 🎾 (Boosts happiness but reduces energy)
  3. **Put it to sleep** 💤 (Restores energy)
- **Each action has an animation** (e.g., the pet eats food, jumps happily, or sleeps).

### **3.4 Real-Time Stat Changes & Evolution**
- Stats change **automatically every few seconds**.
- If the pet is well taken care of:
  - It **levels up** and evolves into a new form.
  - Gains **special abilities** or changes appearance.
- If neglected:
  - The pet **gets sick** (UI turns gray, sad animation).
  - The pet **runs away** (game over screen).

### **3.5 Game Over Conditions**
- If Hunger = 100% → **Pet Starves & Runs Away**
- If Happiness = 0% → **Pet Becomes Depressed & Leaves**
- If Energy = 0% → **Pet Falls into Deep Sleep & Becomes Inactive**
- Users get a **Game Over screen** with an option to adopt a new pet.

---

## **4. User Interface (UI) Design**
### **4.1 Main Game Screen**
- **Background:** A colorful pet room or outdoor environment.
- **Pet Display:** The animated RoboPet in the center.
- **Stat Bars:** Progress bars showing Energy, Hunger, and Happiness.
- **Action Buttons:** Large, clear buttons for **Feed, Play, Sleep**.
- **Time Tracker:** Optional feature to show how long the pet has been alive.

### **4.2 Game Over Screen**
- Shows **reason for game over** (starvation, sadness, exhaustion).
- Displays a **farewell message from the pet**.
- **Restart button** to adopt a new pet.

---

## **5. Game Logic & Mechanics**
### **5.1 Time-Based Stat Reduction**
- Every **5 seconds**, the pet’s stats decrease:
  - Hunger +5%
  - Energy -3%
  - Happiness -4%
- **If a stat reaches a danger zone (e.g., Hunger > 80%)**, the pet gives a warning.

### **5.2 User Interactions**
- **Feeding:** Increases Hunger by -30% (but caps at 0%).
- **Playing:** Increases Happiness by +20% (but decreases Energy by -10%).
- **Sleeping:** Restores Energy by +30% (but increases Hunger by +10%).

### **5.3 Pet Evolution System**
- Every **2 minutes**, if the pet is healthy, it evolves into a **stronger, happier version**.
- Evolution stages:
  1. **Baby** → Default form (basic animations).
  2. **Teen** → Gains new animations & facial expressions.
  3. **Adult** → Becomes more independent (less stat decay).
  4. **Legendary Form** → Ultimate version with a golden glow.

---

## **6. Technical Requirements**
### **6.1 Frontend (User Interface)**
- **HTML**: Structure of the game.
- **CSS**: Styling & animations.
- **JavaScript**: Real-time updates & user interactions.

### **6.2 Backend (Game Logic & Data Storage)**
- **Flask (Python)**: Handles pet status updates.
- **JSON / SQLite**: Saves pet progress across sessions.

### **6.3 API Endpoints**
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/pet/stats` | GET | Returns pet stats (Energy, Hunger, Happiness) |
| `/api/pet/feed` | POST | Feeds pet (reduces hunger) |
| `/api/pet/play` | POST | Plays with pet (boosts happiness, reduces energy) |
| `/api/pet/sleep` | POST | Puts pet to sleep (restores energy) |
| `/api/pet/evolve` | GET | Checks if the pet should evolve |



---

## **7. Summary**
RoboPet is a **fun, interactive virtual pet game** that combines **real-time stat tracking, animations, and pet evolution mechanics** into a simple **web-based game**. The goal is to **engage users through meaningful interactions** and **gamify pet care**.

