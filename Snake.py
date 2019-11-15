import pygame, sys, os, time, copy
#VARIÁVEIS
width = 700
height = 700
size = (width, height)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255, 255)

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
        self.direction = 'UP'
        self.body = []
    
    def build_body(self):
        last = len(body)
        body = self.body[last].positionX - 20
        body = self.body[last].positionY

    def build_snake(self):
        head = Snake_body(340, 340)
        self.body.append(head)
        for i in range(self.size):
            last = len(self.body) - 1
            body = Snake_body(self.body[last].positionX - 20, self.body[last].positionY)
            self.body.append(body)

    def move(self):
        ### VERIFICAR SE O MOVIMENTO É POSSÍVEL

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

        if (self.body[0].positionX >= width or self.body[0].positionX <= 0 or self.body[0].positionY >= height or self.body[0].positionY <= 0):
            self.alive = False            


def load_images(image_name):
    image_name = os.path.join('images', image_name)
    try:
        image = pygame.image.load(image_name)
    except pygame.error:
        print ("Erro ao carregar imagem.")
        raise SystemExit
    return image

def main():
    pygame.init()
    #Iniciando interface
    interface = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake Game")
    snake_head = load_images('green_square.png').convert()
    snake = Snake()
    snake.build_snake()
    while snake.alive :
        #Desenha todas as partes da snake
        for parte in range(len(snake.body)):
            pygame.draw.rect(interface, snake.body[parte].color, [snake.body[parte].positionX, snake.body[parte].positionY, 20, 20])
        pygame.display.flip()
        time.sleep(snake.speed)
        interface.fill([0,0,0, 0])

        #Checa se setas direcionais foram pressionadas
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake.direction = 'DOWN'
                
                if event.key == pygame.K_UP:
                    snake.direction = 'UP'

                if event.key == pygame.K_LEFT:
                    snake.direction = 'LEFT'

                if event.key == pygame.K_RIGHT:
                    snake.direction = 'RIGHT'

        snake.move()

    sys.exit()
    pygame.quit()

if __name__ == "__main__":
    main()