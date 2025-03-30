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
    image = pygame.transform.scale(image,
                                   (base_width * dimesions[0] * factors[0], base_height * dimesions[1] * factors[1]))
    return image


def smart_blit(surf, imageOrRectAndColor, xScale, yScale, center_x=False, center_y=False):
    image = imageOrRectAndColor
    surf.blit(image, (WIDTH * xScale - (image.get_width() / 2 * center_x.__bool__()),
                      HEIGHT * yScale - (image.get_height() / 2) * center_y.__bool__()))


class Object:
    def __init__(self, image,rect):
        self.rect = pygame.Rect(rect)
        self.image = image


    def draw(self, screen,pos=(0.5,0.5), scale=(1, 1),center_x=True,center_y=True):
        img = load_image_with_scale(self.image, SCALE_FACTOR_LIST, scale)


        smart_blit(screen, img, pos[0], pos[1], center_x, center_y)


rect = Object("data_folder/test_img/bg.jpg",(10, 10, 10, 10))

while run:
    screen.fill((0, 0, 0))

    WIDTH, HEIGHT = pygame.display.get_window_size()
    SCALE_FACTOR_LIST = [WIDTH / base_width, HEIGHT / base_height]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rect.draw(screen, (0.5, 0.5), (0.5, 0.5), True, True)

    main_clock.tick(FPS)
    pygame.display.flip()
