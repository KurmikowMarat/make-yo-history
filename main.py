import pygame
import sys

pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Инициализация окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Создай свою историю")

# Шрифты
font = pygame.font.Font(None, 32)

class StoryModel:
    def __init__(self):
        self.story = []

    def add_event(self, event):
        self.story.append(event)

    def get_story(self):
        return self.story


class StoryView:
    def __init__(self):
        self.texts = []

    def display_story(self, story):
        self.texts.clear()
        for i, event in enumerate(story, start=1):
            text_surface = font.render(f"{i}. {event}", True, BLACK)
            self.texts.append(text_surface)

    def draw(self, screen):
        y = 50
        for text_surface in self.texts:
            screen.blit(text_surface, (50, y))
            y += 30


class StoryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == pygame.K_RETURN:
                        new_event = input("Введите следующее событие: ")
                        self.model.add_event(new_event)

            story = self.model.get_story()
            self.view.display_story(story)

            screen.fill(WHITE)
            self.view.draw(screen)
            pygame.display.flip()

model = StoryModel()
view = StoryView()
controller = StoryController(model, view)

controller.run()
