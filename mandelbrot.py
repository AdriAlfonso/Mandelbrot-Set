import pygame

# Initialize pygame
pygame.init()

# Define the screen size
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Mandelbrot Set")

# Main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(screen_width):
        for y in range(screen_height):
            # Normalize coordinates
            x_norm = x / screen_width
            y_norm = y / screen_height

            c_real = (x_norm - 0.5) * 3.0  # Adjust coordinate range around 0
            c_imag = (y_norm - 0.5) * 2.0  # Adjust coordinate range around 0

            # Calculate the Mandelbrot set
            z_real = 0
            z_imag = 0
            max_iterations = 150
            n = 0
            while n < max_iterations:
                z_real, z_imag = z_real * z_real - z_imag * z_imag + c_real, 2 * z_real * z_imag + c_imag
                if abs(z_real + z_imag) > 2:
                    break
                n += 1

            # Assign a color based on the number of iterations
            if n == max_iterations:
                new_color = (0, 0, 0)  # Point inside the set (black)
            else:
                new_color = ((n * 2 % 256, n * 5 % 256, n * 10 % 256))  # Different colors for different values of n

            # Draw the pixel on the screen
            screen.set_at((x, y), new_color)

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()

