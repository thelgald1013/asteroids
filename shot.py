import circleshape, pygame

from constants import SHOT_RADIUS, LINE_WIDTH
from pygame.surface import SurfaceType

class Shot(circleshape.CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: SurfaceType) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
