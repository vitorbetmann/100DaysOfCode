import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
filename = "50_states.csv"
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
data = pandas.read_csv(filename)
states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    box_title = f"{len(guessed_states)}/50 Correct Guesses"
    prompt = "Please, guess a state name."
    answer_state = screen.textinput(box_title, prompt).title()

    if answer_state == "Exit":
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        new_turtle = turtle.Turtle(visible=False)
        new_turtle.penup()
        state = data[data.state == answer_state]
        new_turtle.goto(int(state.x), int(state.y))
        new_turtle.write(answer_state)

with open("states_to_learn.csv", "w") as learn_file:
    result = ""
    for state in states_list:
        if state in guessed_states:
            continue
        else:
            result += state + "\n"
    learn_file.write(result)
