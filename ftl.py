import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("FTL Travel Simulation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Entities
observer_pos = (100, height // 2)
ftl_start_pos = (100, height // 2 + 50)
ftl_end_pos = (width - 100, height // 2 + 50)
entity_radius = 20

# Initialize FTL variables
def reset_ftl():
    global ftl_traveling, ftl_travel_time, show_ftl_end_ball
    ftl_traveling = False
    ftl_travel_time = 0
    show_ftl_end_ball = False

reset_ftl()

# Simulation loop
running = True
clock = pygame.time.Clock()
ftl_travel_duration = 2  # Duration of FTL travel in seconds

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ftl_traveling = True
                ftl_travel_time = 0
                show_ftl_end_ball = True
            elif event.key == pygame.K_r:
                reset_ftl()

    screen.fill((0, 0, 0))

    # Draw the start and finish lines
    pygame.draw.line(screen, WHITE, (ftl_start_pos[0], 0), (ftl_start_pos[0], height))
    pygame.draw.line(screen, WHITE, (ftl_end_pos[0], 0), (ftl_end_pos[0], height))

    # Draw the observer
    pygame.draw.circle(screen, BLUE, observer_pos, entity_radius)

    # Always draw the FTL traveler at the end position if the flag is set
    if show_ftl_end_ball:
        pygame.draw.circle(screen, RED, ftl_end_pos, entity_radius)

    # Handle FTL traveling
    if ftl_traveling:
        # Calculate the position of the FTL artifact traveling backwards
        ftl_artifact_pos = (
            ftl_end_pos[0] - (ftl_end_pos[0] - ftl_start_pos[0]) * (ftl_travel_time / ftl_travel_duration),
            ftl_end_pos[1]
        )
        # Draw the backwards traveling red ball if it hasn't reached the start line
        if ftl_artifact_pos[0] > ftl_start_pos[0]:
            pygame.draw.circle(screen, RED, ftl_artifact_pos, entity_radius)

        ftl_travel_time += clock.get_time() / 1000
        if ftl_travel_time >= ftl_travel_duration:
            ftl_traveling = False

    # Draw the FTL traveler at the start position when not traveling
    if not ftl_traveling and not show_ftl_end_ball:
        pygame.draw.circle(screen, RED, ftl_start_pos, entity_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
