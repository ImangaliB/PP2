import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 30)

MUSIC_FOLDER = "Lab_7/music"  
playlist = [os.path.join(MUSIC_FOLDER, file) for file in os.listdir(MUSIC_FOLDER) if file.endswith(".mp3")]
current_track = 0  

def play_music(track_index):
    pygame.mixer.music.load(playlist[track_index])
    pygame.mixer.music.play()
    
def draw_interface():
    screen.fill(WHITE)
    
    if playlist:
        track_name = os.path.basename(playlist[current_track])
    else:
        track_name = "No music found"

    text = font.render(track_name, True, BLACK)
    screen.blit(text, (20, 50))
    
    pygame.display.flip()

if playlist:
    play_music(current_track)

running = True
while running:
    draw_interface()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play/Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_k:  # Stop
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:  # Next track
                current_track = (current_track + 1) % len(playlist)
                play_music(current_track)
            elif event.key == pygame.K_LEFT:  # Previous track
                current_track = (current_track - 1) % len(playlist)
                play_music(current_track)

pygame.quit()
