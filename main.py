import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess = pandas.read_csv("50_states.csv")
all_state = guess.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_state)}/ 50 states", prompt="What's another states name?").title()
    if answer_states == "Exit":
        missing_states = [state for state in all_state if state not in guessed_state]
        # for state in all_state:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        break
    if answer_states in all_state:
        guessed_state.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = guess[guess.state == answer_states]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_states)

data = pandas.DataFrame(missing_states)
data.to_csv("learn.csv")


# screen.exitonclick()
