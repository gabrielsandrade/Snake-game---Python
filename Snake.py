import pygame, sys, os, time, copy, random
#VARIÁVEIS
width = 700
height = 700
size = (width, height)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255, 255)
clock = pygame.time.Clock()


class Food:
    def __init__(self):
        self.positionX = 0
        self.positionY = 0
        self.color = WHITE
        self.alive = False

    def rand(self, snake):
        x = random.randint(0, (width - 20)/20)*20
        y = random.randint(0, (height - 20)/20)*20
        z = False
        while z == False:
            z = True
            for i in range(snake.size + 1):
                if x == snake.body[i].positionX and y == snake.body[i].positionY:
                    z = False
                    return (x , y, z)
        return x, y, z

    def generate(self, snake):
        z = False
        while(z == False):
            x, y, z = self.rand(snake)
            print (x, y, z)
        self.positionX = x
        self.positionY = y
        self.alive = True

class Snake_body:
    def __init__(self, posX, posY):
        self.positionX = posX
        self.positionY = posY
        self.color = GREEN

class Snake:
    def __init__ (self):
        self.size = 4
        self.alive = True
        self.positionX = 0
        self.positionY = 0
        self.speed = 0.1
        self.direction = 'RIGHT'
        self.body = []

    def build_snake(self):
        head = Snake_body(240, 240)
        self.body.append(head)
        for i in range(self.size):
            last = len(self.body) - 1
            copia = copy.deepcopy(self.body)
            self.move()
            new_body = Snake_body(copia[last].positionX, copia[last].positionY)
            self.body.append(new_body)
            #body = Snake_body(self.body[last].positionX - 20, self.body[last].positionY)

    def add_body(self):
        self.size += 1
        last = len(self.body) - 1
        body = Snake_body(self.body[last].positionX, self.body[last].positionY)
        self.body.append(body)

    def move(self):
        ### VERIFICAR COLISÃO

        if self.direction == 'RIGHT':
            auxiliar = copy.deepcopy(self.body)
            self.body[0].positionX += 20

        if self.direction == 'LEFT':
            auxiliar = copy.deepcopy(self.body)
            self.body[0].positionX -= 20

        if self.direction == 'UP':
            auxiliar = copy.deepcopy(self.body)
            self.body[0].positionY -= 20

        if self.direction == 'DOWN':
            auxiliar = copy.deepcopy(self.body)
            self.body[0].positionY += 20

        for parte in range(len(self.body) - 1):
            self.body[parte + 1].positionX = auxiliar[parte].positionX
            self.body[parte + 1].positionY = auxiliar[parte].positionY

        if (self.body[0].positionX >= width or self.body[0].positionX < 0 or self.body[0].positionY >= height or self.body[0].positionY < 0):
            self.alive = False            

def check_collision(snake, food):
    if (snake.body[0].positionX == food.positionX and snake.body[0].positionY == food.positionY):
        food.alive = False
        snake.add_body()
        return True
    else:
        return False
def check_auto_collision(snake):
    for i in range(snake.size):
        if snake.body[0].positionX == snake.body[i + 1].positionX and snake.body[0].positionY == snake.body[i + 1].positionY:
            sys.exit()
            pygame.quit()
def main():
    pygame.init()
    #Iniciando interface
    interface = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake Game")
    snake = Snake()
    food = Food()
    snake.build_snake()
    food.generate(snake)

    while snake.alive :
        #Desenha todas as partes da snake
        for parte in range(len(snake.body)):
            pygame.draw.rect(interface, snake.body[parte].color, [snake.body[parte].positionX, snake.body[parte].positionY, 20, 20])
        if food.alive:
            pygame.draw.rect(interface, (0 , 0 , 255), [food.positionX, food.positionY, 20, 20])
        else:
            food = Food()
            food.generate(snake)
        pygame.display.flip()
        clock.tick(10)
        #time.sleep(snake.speed)
        interface.fill([0,0,0, 0])

        #Checa se setas direcionais foram pressionadas
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    for i in range(len(snake.body) - 1):
                        if (snake.body[i + 1].positionY == snake.body[0].positionY + 20):
                            break
                        snake.direction = 'DOWN'
                
                elif event.key == pygame.K_UP:
                    for i in range(len(snake.body) - 1):
                        if (snake.body[i + 1].positionY == snake.body[0].positionY - 20):
                            break
                        snake.direction = 'UP'

                elif event.key == pygame.K_LEFT:
                    for i in range(len(snake.body) - 1):
                        if (snake.body[i + 1].positionX == snake.body[0].positionX - 20):
                            break
                        snake.direction = 'LEFT'

                elif event.key == pygame.K_RIGHT:
                    for i in range(len(snake.body) - 1):
                        if (snake.body[i + 1].positionX == snake.body[0].positionX + 20):
                            break
                        snake.direction = 'RIGHT'
                        
        if check_collision(snake, food):
            print ('Comeu')
            last = len(snake.body)
            copia = copy.deepcopy(snake.body)
            snake.move()
            new_body = Snake_body(copia[last - 1].positionX, copia[last - 1].positionY)
            snake.body.append(new_body)
            snake.size += 1
        else:
            snake.move()

        if check_auto_collision(snake):
            sys.exit()
            pygame.quit()

    sys.exit()
    pygame.quit()

if __name__ == "__main__":
    main()