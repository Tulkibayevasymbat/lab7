import pygame
import os

pygame.init()

# Creating the Pygame window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# List of music files
music_files = [r"C:\Users\АНЭЛ\Desktop\lab7\jah.khalib.911.mp3.mp3", r"C:\Users\АНЭЛ\Desktop\lab7\begimai.MP3.mp3", r"C:\Users\АНЭЛ\Desktop\lab7\тырядом.mp3.mp3", r"c:\Users\АНЭЛ\Downloads\Қайрат Нұртас-Астана.mp3.mp3"]
current_track = 0

# Loading the first music file
pygame.mixer.music.load(music_files[current_track])

playing = False

running = True
while running:
    # Clearing the screen
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()  # probel-pause
                    playing = False
                else:
                    pygame.mixer.music.unpause()  # Unpause the music
                    playing = True
            elif event.key == pygame.K_s:  # s-Stop the music
                pygame.mixer.music.stop()
                playing = False
            elif event.key == pygame.K_n:  # n-the next music
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
                playing = True
            elif event.key == pygame.K_p:  # p-previous music
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
                playing = True

    pygame.display.update()

pygame.quit()