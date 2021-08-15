import pygame
import time
import random
import sys
import pickle

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
    msg = font.render("Press 'P' to play again", True, white)
    gameDisplay.blit(msg, [200, displayWidth/2])


def updateHighScore(score, update) :
    try:
        with open('score.dat', 'rb') as file:
            highScore = pickle.load(file)
    except:
        highScore = 0

    if update :
        if score > highScore :
            with open('score.dat', 'wb') as file:
                pickle.dump(score, file)
                return score

    return highScore


def displayScore(score, update) :
    valScore = scoreFont.render("Your score : " + str(score), True, white)
    gameDisplay.blit(valScore, [100,0])
    valHighScore = scoreFont.render("High Score : " + str(updateHighScore(score, update)), True, white)
    gameDisplay.blit(valHighScore, [300,0])


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
    dir = 0

    snakeList = []
    snakeLength = 1

    foodx = round(random.randrange(0, displayLength - snakeBody) / 10.0) * 10.0
    foody = round(random.randrange(0, displayWidth - snakeBody) / 10.0) * 10.0


    while playingGame :
        while displayingMsg :
            gameDisplay.fill(black)
            displayMessage()
            displayScore(snakeLength-1, True)
            pygame.display.update()

            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_p :
                        main()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    xChange = -snakeBody
                    yChange = 0
                    dir = 3

                elif event.key == pygame.K_RIGHT :
                    xChange = snakeBody
                    yChange = 0
                    dir = 4

                elif event.key == pygame.K_UP :
                    xChange = 0
                    yChange = -snakeBody
                    dir = 1

                elif event.key == pygame.K_DOWN :
                    xChange = 0
                    yChange = snakeBody
                    dir = 2

        if xCoordinate==0 and dir==3 :
            xCoordinate = displayLength
        if xCoordinate==displayLength and dir==4 :
            xCoordinate = 0
        if yCoordinate==0 and dir==1 :
            yCoordinate = displayWidth
        if yCoordinate==displayWidth and dir==2 :
            yCoordinate = 0
            
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
        displayScore(snakeLength-1, False)

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