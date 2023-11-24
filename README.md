A simple base I made for accelerating development in pygame.

Main/Engine file documentation

Methods:
    - __init__(self): Initializes the Game object, creates a game window, and calls the start method.
    - start(self): Logs a message indicating that the game has started.
    - update(self): Placeholder method for updating game logic. (Note: a print statement is included but should be replaced with actual update logic)
    - draw(self): Fills the screen with a black color and calls the draw method of the Engine class.



GameObject Module Documentation
This module defines a set of classes representing game objects using the Pygame library.

Classes:
    - GameObject: Base class for game objects with common properties such as position, size, and color.
    - Circle: Represents a circular game object derived from GameObject.
    - Rect: Represents a rectangular game object derived from GameObject.
    - Line: Represents a line game object derived from GameObject.
    - Polygon: Represents a polygonal game object derived from GameObject.
    - Sprite: Represents a game object with an image sprite derived from GameObject.
    - AnimatedSprite: Represents an animated game object with a sequence of image sprites derived from GameObject.
    - Text: Represents a text-based game object derived from GameObject.

Methods:
    - __init__(self, ...): Initializes the properties of each game object.
    - draw(self, screen): Draws the game object on the specified Pygame screen.

Usage:
    - Instantiate objects of the provided classes to represent different game elements.
    - Call the draw method of each object within the game loop to render them on the Pygame screen.

Example:

    # Creating a Rect Object
    rect = Rect(x=100, y=100, width=50, height=30, color=(255, 0, 0)).draw(self.screen)
    
    # Creating a Text Object
    Text("Hello, world!", 0, 0, "white", 20).draw(screen)
