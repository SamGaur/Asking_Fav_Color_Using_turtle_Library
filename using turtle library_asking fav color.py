import turtle

feeling = input("How are you feeling today? ")
print("You are feeling:", feeling)

# Function to display the color template
def display_color_template(color):
    screen = turtle.Screen()
    screen.title("Your Favorite Color Display")

    # Create a turtle
    pen = turtle.Turtle()

    # Set the pen color
    pen.color(color)

    # Fill the rectangle with the favorite color
    pen.begin_fill()
    
    # Draw a rectangle
    for _ in range(2):
        pen.forward(100)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    
    pen.end_fill()

    # Hide the turtle and display the window
    pen.hideturtle()
    turtle.done()

# Ask the user for their favorite color
favorite_color = input("What is your favorite color? ")

# Display the favorite color using turtle graphics
display_color_template(favorite_color)