import pygame, os, sys, random

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
screen_width = screen.get_size()[0]
screen_height = screen.get_size()[1]
clock = pygame.time.Clock()
# font = pygame.font.SysFont(None, 48)
running = True
dt = 0

PLAYER_WIDTH = 80
PLAYER_HEIGHT = 80
PLAYER_ACCEL = 90
PLAYER_FRICTION = 0.95
PLAYER_COLLISION_BOUNCE = -1.15
player_x = screen_width / 2 - PLAYER_WIDTH / 2
player_y = screen_height / 2 - PLAYER_HEIGHT / 2
player_velocity_x = 0
player_velocity_y = 0



while running:
	screen_width = screen.get_size()[0]
	screen_height = screen.get_size()[1]
	os.system("clear")

	dt = clock.tick(240) / 1000
	fps = clock.get_fps()
	print(f"JOYFULLY AWESOME\ndt: {dt}\nfps: {fps}\npos: {player_x}, {player_y}\nvel: {player_velocity_x}, {player_velocity_y}")

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_a]:
		player_velocity_x -= PLAYER_ACCEL# * dt
	if keys[pygame.K_d]:
		player_velocity_x += PLAYER_ACCEL# * dt
	if keys[pygame.K_w]:
		player_velocity_y -= PLAYER_ACCEL# * dt
	if keys[pygame.K_s]:
		player_velocity_y += PLAYER_ACCEL# * dt
	if keys[pygame.K_SPACE]:
		player_velocity_x = random.randint(-100000, 100000)
		player_velocity_y = random.randint(-100000, 100000)

	player_velocity_x *= PLAYER_FRICTION
	player_velocity_y *= PLAYER_FRICTION
	# player_velocity_y += 10

	player_x += player_velocity_x * dt
	player_y += player_velocity_y * dt

	if player_x < 0:
		player_x = 0
		player_velocity_x *= PLAYER_COLLISION_BOUNCE
	if player_y < 0:
		player_y = 0
		player_velocity_y *= PLAYER_COLLISION_BOUNCE
	if player_x > screen_width - PLAYER_WIDTH:
		player_x = screen_width - PLAYER_WIDTH
		player_velocity_x *= PLAYER_COLLISION_BOUNCE
	if player_y > screen_height - PLAYER_HEIGHT:
		player_y = screen_height - PLAYER_HEIGHT
		player_velocity_y *= PLAYER_COLLISION_BOUNCE

	# stats = font.render(f"JOYFULLY AWESOME\ndt:z {dt}\nfps: {fps}\npos: {player_x}, {player_y}\nvel: {player_velocity_x}, {player_velocity_y}", True, (255,255,255))

	# screen.blit(stats, (100, 100))
	screen.fill("#1a1a1a")

	pygame.draw.rect(screen, "#4287f5", (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

	pygame.display.flip()
	clock.tick(240)

pygame.quit()
