import pygame
import time
import random

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

displayLength = 600
displayWidth = 600

gameDisplay = pygame.display.set_mode((displayLength, displayWidth))
pygame.display.set_caption("SnakeGame by Kkft9!")

clock = pygame.time.Clock()

snakeBody = 10
snakeSpeed = 10

font = pygame.font.SysFont("arial", 25)
scoreFont = pygame.font.SysFont("comicsansms", 20)


def displayMessage() :
    msg = font.render("YOU LOST!!! Press 'P' to play again or 'Q' to quit.", True, white)
    gameDisplay.blit(msg, [100, displayWidth/2])


def displayScore(score) :
    val = scoreFont.render("Your score : " + str(score), True, white)
    gameDisplay.blit(val, [250,0])


def displaySnake(body, list) :
    for i in list :
        pygame.draw.rect(gameDisplay, green, [i[0], i[1], body, body])


def main() :
    playingGame = True
    displayingMsg = False

    xCoordinate = displayLength/2
    yCoordinate = displayWidth/2

    xChange = 0
    yChange = 0

    snakeList = []
    snakeLength = 1

    foodx = round(random.randrange(0, displayLength - snakeBody) / 10.0) * 10.0
    foody = round(random.randrange(0, displayWidth - snakeBody) / 10.0) * 10.0


    while playingGame :
        while displayingMsg :
            gameDisplay.fill(black)
            displayMessage()
            displayScore(snakeLength-1)
            pygame.display.update()

            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q :
                        playingGame = False
                        displayingMsg = False
                    elif event.key == pygame.K_p :
                        main()
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                playingGame = False

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    xChange = -snakeBody
                    yChange = 0

                elif event.key == pygame.K_RIGHT :
                    xChange = snakeBody
                    yChange = 0

                elif event.key == pygame.K_UP :
                    xChange = 0
                    yChange = -snakeBody

                elif event.key == pygame.K_DOWN :
                    xChange = 0
                    yChange = snakeBody

        if xCoordinate>=displayLength or xCoordinate<0 or yCoordinate>=displayWidth or yCoordinate<0 :
            displayingMsg = True
        xCoordinate += xChange
        yCoordinate += yChange

        gameDisplay.fill(black)

        pygame.draw.rect(gameDisplay, blue, [foodx, foody, snakeBody, snakeBody])

        snakeList.append([xCoordinate, yCoordinate])

        if len(snakeList) > snakeLength :
            del snakeList[0]

        for i in snakeList[:-1] :
            if i == [xCoordinate, yCoordinate] :
                displayingMsg = True
        
        displaySnake(snakeBody, snakeList)
        displayScore(snakeLength-1)

        pygame.display.update()

        if xCoordinate==foodx and yCoordinate==foody :
            snakeLength += 1
            foodx = round(random.randrange(0, displayLength - snakeBody) / 10.0) * 10.0
            foody = round(random.randrange(0, displayWidth - snakeBody) / 10.0) * 10.0
        
        clock.tick(snakeSpeed)
    
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()