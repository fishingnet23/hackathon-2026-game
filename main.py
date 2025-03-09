import pygame

pygame.init()

# idea notes
# add function to convert a number from 0 to 1 into a position on screen (0 = 0, 1 = WIDTH)


base_width = 1920
base_height = 1080

WIDTH = 1920 * 0.8
HEIGHT = 1080 * 0.8

SCALE_FACTOR_LIST = [WIDTH / base_width, HEIGHT / base_height]

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

run = True
FPS = 60
main_clock = pygame.time.Clock()


def load_image_with_scale(path, factors: list, dimesions=(1, 1)):
    global WIDTH, HEIGHT
    image = pygame.image.load(path)
    image = pygame.transform.scale(image,(base_width * dimesions[0] * factors[0], base_height * dimesions[1] * factors[1]))
    return image


def smart_blit(surf, image, xScale, yScale, center_x=False, center_y=False):

        surf.blit(image, (WIDTH * xScale - image.get_width() / 2, HEIGHT * yScale - image.get_height() / 2))



while run:

    screen.fill((0, 0, 0))

    WIDTH, HEIGHT = pygame.display.get_window_size()
    SCALE_FACTOR_LIST = [WIDTH / base_width, HEIGHT / base_height]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    img = load_image_with_scale("data_folder/test_img/bg.jpg", SCALE_FACTOR_LIST, (0.5, 0.5))

    smart_blit(screen, img, 0.5, 0.5, )

    main_clock.tick(FPS)
    pygame.display.flip()
