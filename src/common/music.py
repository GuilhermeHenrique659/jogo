import pygame

class MusicPlayer:
    def play_music(self, music_path, loops=-1):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(loops)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def fade_in(self, duration):
        current_volume = pygame.mixer.music.get_volume()
        target_volume = 1.0

        steps = int(duration * 60)  # 60 steps per second
        fade_step = (target_volume - current_volume) / steps

        for _ in range(steps):
            current_volume += fade_step
            pygame.mixer.music.set_volume(current_volume)
            pygame.time.Clock().tick(60)

    def fade_out(self, duration):
        current_volume = pygame.mixer.music.get_volume()

        steps = int(duration * 60)  # 60 steps per second
        fade_step = current_volume / steps

        for _ in range(steps):
            current_volume -= fade_step
            pygame.mixer.music.set_volume(current_volume)
            pygame.time.Clock().tick(60)