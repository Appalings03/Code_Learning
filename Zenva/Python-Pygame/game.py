import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        self.s_size = (800, 800)
        self.i_size = (50, 50)
        self.s_rgb = (255, 255, 255)

        # game window
        self.game_window = pygame.display.set_mode(self.s_size)
        self.clock = pygame.time.Clock()

        self.background = GameObject(0, 0, self.s_size[0], self.s_size[1], 'assets/background.png')
        self.treasure = GameObject(375, 50, self.i_size[0], self.i_size[1], 'assets/treasure.png')

        self.level = 1.0
        self.reset_map()
            
    def reset_map(self):
        p_speed = 10
        self.player = Player(375, 700, self.i_size[0], self.i_size[1], 'assets/player.png', p_speed)
        e_speed = 5 + (self.level * 2)
        if self.level >= 4.0:
            self.enemies = [
                Enemy(0,600, self.i_size[0], self.i_size[1], 'assets/enemy.png', e_speed),
                Enemy(750,400, self.i_size[0], self.i_size[1], 'assets/enemy.png', e_speed),
                Enemy(0,200, self.i_size[0], self.i_size[1], 'assets/enemy.png', e_speed)
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0,600, self.i_size[0], self.i_size[1], 'assets/enemy.png', e_speed),
                Enemy(750,400, self.i_size[0], self.i_size[1], 'assets/enemy.png', e_speed)
            ]
        else:
            self.enemies = [
                Enemy(0,400, self.i_size[0], self.i_size[1], 'assets/enemy.png', e_speed)
            ]
        
    def draw_objects(self):
        self.game_window.fill(self.s_rgb)
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        pygame.display.update()
        
    def detectCollision(self, obj1, obj2):
        if obj1.y > (obj2.y + obj2.height):
            return False
        elif (obj1.y + obj1.height) < obj2.y:
            return False
        
        if obj1.x > (obj2.x + obj2.width):
            return False
        elif (obj1.x + obj1.width) < obj2.x:
            return False
        
        return True
    
    def checkCollisions(self):
        for enemy in self.enemies:
            if self.detectCollision(self.player, enemy):
                self.level = 1.0
                return 'enemy'
        if self.detectCollision(self.player, self.treasure):
            self.level += 0.5
            return 'treasure'
        return None
        
    def runGameLoop(self):
        player_direction = 0
        is_paused = False
        
        # game loop
        isGameOver = False
        while not isGameOver:
            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    isGameOver = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                    elif event.key == pygame.K_ESCAPE:
                        is_paused = not is_paused
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0
            
            if is_paused:
                continue
                 
            # Execute logic
            self.player.move(player_direction, self.s_size[1])
            for enemy in self.enemies:            
                enemy.move(self.s_size[0])
            
            # Draw objects
            self.draw_objects()
            
            # Check collisions
            
            collision_result = self.checkCollisions()
            if collision_result == 'enemy': 
                print("You lost! Collided with an enemy.")
                print("Resetting to level 1.")
                self.reset_map()
            elif collision_result == 'treasure':
                print("You won! You found the treasure.")
                print(f"Advancing to level {self.level}")
                self.reset_map()
            
            self.clock.tick(30)  