import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playing = False

    def load_track(self, track_filename):
        try:
            pygame.mixer.music.load(track_filename)
            print(f"{track_filename} har blitt lastet inn.")
        except pygame.error:
            print(f"Kunne ikke laste inn {track_filename}. Sjekk at filen eksisterer i samme mappe som Python-filen.")

    def play(self):
        if not self.playing:
            pygame.mixer.music.play()
            self.playing = True

    def stop(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False

    def quit(self):
        pygame.quit()

    def menu(self):
        while True:
            print("\nMusikkspillermeny:")
            print("1. Velg aktivt lydspor")
            print("2. Spill av aktivt lydspor")
            print("3. Stopp avspilling")
            print("4. Avslutt programmet")
            choice = input("Velg en handling (1/2/3/4): ")
            if choice == '1':
                track_filename = input("Skriv inn filnavnet til lydsporet (f.eks. Dreamscape.mp3): ")
                self.load_track(track_filename)
            elif choice == '2':
                self.play()
            elif choice == '3':
                self.stop()
            elif choice == '4':
                self.quit()
                break
            else:
                print("Ugyldig valg. Prøv igjen.")

if __name__ == "__main__":
    player = MusicPlayer()
    player.menu()

