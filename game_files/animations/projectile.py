import pygame

from game_files.animations.animation_manager import AnimationManager


class Projectile:
    def __init__(self, sprite_sheets: dict, x, y):
        self.sprite_sheets = sprite_sheets
        self.x = x
        self.y = y
        self.velocity = 500
        self.direction = "right"

        self.animations = AnimationManager(sprite_sheets, 16, 2)
        self.animations.register_animation("projectile",
                                           [0, 1, 2, 3, 4],
                                           "projectile"
                                           )
        self.animations.activate_animation("projectile", 0.1, True)

    def move(self, dt):
        if self.direction == "up":
            self.y -= self.velocity * dt
        elif self.direction == "down":
            self.y += self.velocity * dt
        elif self.direction == "left":
            self.x -= self.velocity * dt
        elif self.direction == "right":
            self.x += self.velocity * dt

    def set_direction(self, new_direction: str):
        self.direction = new_direction

    def update(self, dt):
        self.animations.update(dt)
        self.move(dt)

    def render(self, screen: pygame.Surface, camera_adjustment: tuple):
        screen.blit(self.animations.get_current_sprite(),
                    (
                        self.x + camera_adjustment[0],
                        self.y + camera_adjustment[1]
                    )
                    )
