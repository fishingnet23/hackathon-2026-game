import pygame

pygame.init()

base_width = 1920
base_height = 1080

WIDTH = 1600
HEIGHT = 800

SCALE_FACTOR_LIST = [WIDTH / base_width, HEIGHT / base_height]

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

run = True
FPS = 60
main_clock = pygame.time.Clock()


def load_image_with_scale(path, factors: list):
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (image.get_width() * factors[0], image.get_height() * factors[1]))
    return image


while run:

    screen.fill((0, 0, 0))

    WIDTH, HEIGHT = pygame.display.get_window_size()
    SCALE_FACTOR_LIST = [WIDTH / base_width, HEIGHT / base_height]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    img = load_image_with_scale("data_folder/test_img/bg.jpg", SCALE_FACTOR_LIST)

    screen.blit(img, (WIDTH / 2 - img.get_width() / 2, HEIGHT / 2 - img.get_height() / 2))

    main_clock.tick(FPS)
    pygame.display.flip()
