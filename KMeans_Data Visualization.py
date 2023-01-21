import pygame
from random import randint
from math import *
from sklearn.cluster import KMeans

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

pygame.init()

screen = pygame.display.set_mode((1200, 700))

#dat ten chuong trinh
pygame.display.set_caption("kmeans visualization")

running = True

clock = pygame.time.Clock()

BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
WHITE = (255, 255, 255)

RED = (250, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (147, 153, 35)
PURPLE = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRAPE = (100, 25, 125)
GRASS = (55, 155, 65)
COLORS = [RED, GREEN ,BLUE, YELLOW, PURPLE, SKY, ORANGE, GRAPE, GRASS]

#tao font chu 
font = pygame.font.SysFont('sans', 35)
font_small = pygame.font.SysFont('sans', 20)
text_plus = font.render('+', True, WHITE) #dau cong
text_minus = font.render('-', True, WHITE)
text_run = font.render('Run', True, WHITE)
text_random = font.render('Random', True, WHITE)
text_algorithm = font.render('Algorithm', True, WHITE)
text_reset = font.render('Reset', True, WHITE)

K = 0
error = 0
points = []
clusters = []
labels = []

while running:
    #set fps
    clock.tick(60)
    screen.fill(BACKGROUND)
    mouse_x, mouse_y = pygame.mouse.get_pos() #toa do nut

    #draw interface
    #draw panel
    pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490))

    #draw k button +
    pygame.draw.rect(screen, BLACK, (850, 50, 50, 50))
    screen.blit(text_plus, (863, 51)) #lenh ve len man hinh

    #draw k button -
    pygame.draw.rect(screen,BLACK, (950, 50, 50, 50))
    screen.blit(text_minus, (967, 51))

    #k value
    text_k = font.render("K = " + str(K), True, BLACK)
    screen.blit(text_k , (1050, 50))

    #run button
    pygame.draw.rect(screen, BLACK, (850, 150, 150, 50))
    screen.blit(text_run, (890, 150))

    #random button
    pygame.draw.rect(screen, BLACK, (850, 250, 150, 50))
    screen.blit(text_random, (850, 250))
    
    # Reset button
    pygame.draw.rect(screen, BLACK, (850,550,150,50))
    screen.blit(text_reset, (850,550))	

	# Algorithm button
    pygame.draw.rect(screen, BLACK, (850,450,150,50))
    screen.blit(text_algorithm, (850,450))	

    #draw mouse position when mouse is in panel
    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        text_mouse = font_small.render("(" + str(mouse_x - 55) + ',' + str(mouse_y - 55) + ')', True, BLACK)
        screen.blit(text_mouse, (mouse_x + 10, mouse_y))
    #end draw interface

    #xu li nut bam
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #create a point on panel
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                labels = []
                point = [mouse_x - 55, mouse_y - 55]
                points.append(point)
        
            # change k button +
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                if K < 8:
                    K += 1
                print("+")

            # change k button -
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if K > 0:
                    K -= 1
                print("-")
            # run button
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                labels = []

                if clusters == []:
                    continue
                #assign points to closet clusters
                for p in points:
                    distance_to_clusters = []
                    for c in clusters:
                        d = distance(p, c)
                        distance_to_clusters.append(d)

                    min_distance = min(distance_to_clusters)
                    label = distance_to_clusters.index(min_distance)
                    labels.append(label)

                #update clusters 
                for i in range(K):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count += 1
                    
                    if count != 0:
                        new_cluster_x = sum_x / count
                        new_cluster_y = sum_y / count
                        clusters[i] = [new_cluster_x, new_cluster_y]

                print("run")

            # Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                labels = []
                clusters = []
                for i in range(K):
                    random_point = [randint(0, 700), randint(0, 500)]
                    clusters.append(random_point)
                print("random pressed")

			# Reset button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                points = []
                labels = []
                clusters = []
                K = 0
                error = 0
                print("reset button pressed")

			# Algorithm 
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                try:
                    kmeans = KMeans(n_clusters=K).fit(points) # fit = huan luyen thuat toan
                    print(kmeans.cluster_centers_)
                    labels = kmeans.predict(points)
                    clusters = kmeans.cluster_centers_
                except:
                    print("error")
                
                print("Algorithm button pressed")

    #draw clusters
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLORS[i], (int(clusters[i][0] + 55), int(clusters[i][1] + 55)), 10)

    # draw a point
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0] + 55, points[i][1] + 55), 6)
        if labels == []:
            pygame.draw.circle(screen, WHITE, (points[i][0] + 55, points[i][1] + 55), 5)
        else:
            pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0] + 55, points[i][1] + 55), 6)

    #calculate and draw error
    error = 0
    if labels != [] and clusters != []:
        for i in range(len(points)):
            error += distance(points[i], clusters[labels[i]]) 
    text_error = font.render("Error = " + str(int(error)), True, BLACK)
    screen.blit(text_error, (850,350))
    #cau lenh de tat ca cac lenh in co hieu luc
    pygame.display.flip()

#xoa bo nho
pygame.quit()
