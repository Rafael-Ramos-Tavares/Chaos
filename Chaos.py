import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

# Variáveis do jogo
wall_thickness = 10
gravity = 0.5
bounce_stop = 0.3
max_y_speed = 17
min_y_speed = 10

class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass, retention, x_speed, y_speed, id):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.id = id
        self.circle = ''

    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def check_gravity(self):
        if self.y_pos < HEIGHT - self.radius - (wall_thickness / 2):
            self.y_speed += gravity
        else:
            if self.y_speed > bounce_stop:
                self.y_speed = self.y_speed * -1 * self.retention
                if self.y_speed > max_y_speed:
                    self.y_speed = max_y_speed
            else:
                if abs(self.y_speed) <= bounce_stop:
                    self.y_speed = 0
                    self.y_speed = min_y_speed

        return self.y_speed

    def update_pos(self):
        self.y_pos += self.y_speed


def draw_walls():
    left = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'white', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'white', (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'white', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list


ball1 = Ball(50, 300, 15, 'white', 100, 1, 0, 10, 1)
ball2 = Ball(150, 300, 15, 'white', 100, 1, 0, 11, 2)
ball3 = Ball(250, 300, 15, 'white', 100, 1, 0, 12, 3)
ball4 = Ball(350, 300, 15, 'white', 100, 1, 0, 13, 4)
ball5 = Ball(450, 300, 15, 'white', 100, 1, 0, 14, 5)
ball6 = Ball(550, 300, 15, 'white', 100, 1, 0, 15, 6)
ball7 = Ball(650, 300, 15, 'white', 100, 1, 0, 16, 7)
ball8 = Ball(750, 300, 15, 'white', 100, 1, 0, 17, 8)

balls = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8]


# loop principal
run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    walls = draw_walls()

    for ball in balls:
        ball.draw()
        ball.update_pos()
        ball.y_speed = ball.check_gravity()

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            pygame.draw.line(screen, 'white', (balls[i].x_pos, balls[i].y_pos), (balls[j].x_pos, balls[j].y_pos))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()