Based on the PRD, here are the code-ready tasks for the RoboPet Web Game:

**Frontend Development:**

1. Design and develop the main game screen:
   - Create a colorful background for the pet's environment.
   - Develop an animated display for the RoboPet.
   - Implement progress bars for Energy, Hunger, and Happiness stats.
   - Create action buttons for Feed, Play, and Sleep.
   - Optionally, develop a time tracker to show the pet's age.

2. Design and develop the Game Over screen:
   - Display the reason for the game over (starvation, sadness, exhaustion).
   - Show a farewell message from the pet.
   - Implement a restart button to adopt a new pet.

**Backend Development:**

3. Develop the game logic and mechanics:
   - Implement time-based stat reduction every 5 seconds.
   - Develop user interactions for feeding, playing, and sleeping.
   - Create a pet evolution system that triggers every 2 minutes if the pet is healthy.

4. Implement data storage:
   - Save pet progress across sessions using JSON or SQLite.

**API Development:**

5. Develop API endpoints:
   - `/api/pet/stats` (GET): Returns pet stats (Energy, Hunger, Happiness).
   - `/api/pet/feed` (POST): Feeds pet (reduces hunger).
   - `/api/pet/play` (POST): Plays with pet (boosts happiness, reduces energy).
   - `/api/pet/sleep` (POST): Puts pet to sleep (restores energy).
   - `/api/pet/evolve` (GET): Checks if the pet should evolve.

**Testing:**

6. Test all the features and functionalities in different environments and devices.

**Deployment:**

7. Deploy the game on a suitable web server.

**Maintenance and Updates:**

8. Regularly update the game based on user feedback and bug reports.