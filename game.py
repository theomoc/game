# resolution 500x500


from tkinter import *
import random
from tkinter.ttk import *

global direction
from tkinter import simpledialog


def save():
    """Save the game data"""
    f = open("saved.txt", "w")
    f.write(str(score))
    f.write(str("\n"))
    f.write(str(canvas.coords(student[0])))
    f.write(str("\n"))
    f.write(str(canvas.coords(guard)))
    f.write(str("\n"))
    f.write(str(canvas.coords(guard1)))
    f.write(str("\n"))
    f.write(str(canvas.coords(guard2)))
    f.write(str("\n"))
    f.write(str(canvas.coords(fence1)))
    f.write(str("\n"))
    f.write(str(canvas.coords(fence2)))
    f.write(str("\n"))
    f.write(str(canvas.coords(fence3)))
    f.write(str("\n"))
    f.write(str(canvas.coords(fence4)))
    f.write(str("\n"))
    f.write(str(canvas.coords(fence5)))


def load():
    """Load the last game saved"""
    global x, score
    canvas.delete("text")
    position = []
    x = 0
    # read the saved data
    f = open("saved.txt", "r")
    # update the score
    score = int(f.readline())
    txt = "Score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)

    print(score)
    # update the position of the player
    savedstudent = f.readline()
    for word in savedstudent:
        if "0" <= word <= "9":
            x = x * 10 + int(word)
        else:
            position.append(x)
            x = 0
    canvas.coords(student[0], position[1], position[4], position[7], position[10])
    # update the position of the guard
    position = []
    x = 0
    savedguard = f.readline()
    for word in savedguard:
        if "0" <= word <= "9":
            x = x * 10 + int(word)
        else:
            position.append(x)
            x = 0
    canvas.coords(guard, position[1], position[4], position[7], position[10])
    # update the position of the guard1
    position = []
    x = 0
    savedguard1 = f.readline()
    for word in savedguard1:
        if "0" <= word <= "9":
            x = x * 10 + int(word)
        else:
            position.append(x)
            x = 0
    canvas.coords(guard1, position[1], position[4], position[7], position[10])
    # update the position of the guard2
    position = []
    x = 0
    savedguard2 = f.readline()
    for word in savedguard2:
        if "0" <= word <= "9":
            x = x * 10 + int(word)
        else:
            position.append(x)
            x = 0
    canvas.coords(guard2, position[1], position[4], position[7], position[10])
    # update the position of the fence1
    position = []
    x = 0
    savedfence = f.readline()
    for word in savedfence:
        if "0" <= word <= "9":
            x = x * 10 + int(word)
        else:
            position.append(x)
            x = 0
    canvas.coords(fence1, position[1], position[4], position[7], position[10])
    # update the position of the fence2
    position = []
    x = 0
    savedfence = f.readline()
    for word in savedfence:
        if "0" <= word <= "9":
            x = x * 10 + int(word)
        else:
            position.append(x)
            x = 0
    canvas.coords(fence2, position[1], position[4], position[7], position[10])
    # update the position of the fence3
    position = []
    x = 0
    savedfence = f.readline()
    for word in savedfence:
        if "0" <= word <= "9":
            x = x * 10 + int(word)
        else:
            position.append(x)
            x = 0
    canvas.coords(fence3, position[1], position[4], position[7], position[10])
    # update the position of the fence4
    position = []
    x = 0
    savedfence = f.readline()
    for word in savedfence:
        if "0" <= word <= "9":
            x = x * 10 + int(word)
        else:
            position.append(x)
            x = 0
    canvas.coords(fence4, position[1], position[4], position[7], position[10])
    # update the position of the fence5
    position = []
    x = 0
    savedfence = f.readline()
    for word in savedfence:
        if "0" <= word <= "9":
            x = x * 10 + int(word)
        else:
            position.append(x)
            x = 0
    canvas.coords(fence5, position[1], position[4], position[7], position[10])


def board():
    """Create and update leader board"""
    # the user is asked to introduce his/her name
    user_inp = simpledialog.askstring(title="Good job!", prompt="What's your Name?:)")
    # the leader board will appear on a new window
    board = Toplevel()
    board.geometry("200x100")
    # getting the last data from the leader board files
    x = y = z = poz = 0
    xname = yname = zname = ""
    with open("score.txt", "r") as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                if not x:
                    x = int(word)
                elif not y:
                    y = int(word)
                elif not z:
                    z = int(word)
    with open("name.txt", "r") as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                if not xname:
                    xname = word
                elif not yname:
                    yname = word
                elif not zname:
                    zname = word
    # asking if the new score is better than the ones from the leader board
    if score > x:
        z = y
        y = x
        zname = yname
        yname = xname
        x = score
        xname = user_inp
    elif score > y:
        z = y
        zname = yname
        y = score
        yname = user_inp
    elif score > z:
        z = score
        poz = 3
        zname = user_inp
    # updating the files
    f = open("score.txt", "w")
    f.write(str(x) + "\n" + str(y) + "\n" + str(z))
    f.close()
    f = open("name.txt", "w")
    f.write(str(xname) + "\n" + str(yname) + "\n" + str(zname))
    f.close()
    leader = (
        "1. "
        + str(x)
        + " "
        + str(xname)
        + "\n"
        + "2. "
        + str(y)
        + " "
        + str(yname)
        + "\n"
        + "3. "
        + str(z)
        + " "
        + str(zname)
    )
    # displaying the top at the end of the game
    myLabel1 = Label(board, text="Leader Board")
    my_label = Label(board, text=leader)
    myLabel1.pack()
    my_label.pack()
    button = Button(board, text="Restart", command=donothing).pack()
    board.mainloop()


# pausing the game
def onclick():
    global direction, copydirection
    if direction is None:
        direction = copydirection
        canvas.bind("a", left_key)
        canvas.bind("d", right_key)
        canvas.bind("w", up_key)
        canvas.bind("s", down_key)
        canvas.focus_set()

    else:
        copydirection = direction
        direction = None


def place_safe_party():
    """Place the safe party/yellow rectangle"""
    global safe
    safe = canvas.create_rectangle(0, 0, studentSize, studentSize, fill="gold")
    canvas.move(safe, 0, 0)


def donothing():
    # creating the scoreText
    global score, direction, student
    canvas.delete(student)
    student = []
    student_size = 15
    student.append(
        canvas.create_rectangle(
            student_size, student_size, student_size * 2, student_size * 2, fill="white"
        )
    )

    score = 0
    txt = "Score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)

    # calling the functions
    direction = None
    canvas.bind("a", left_key)
    canvas.bind("d", right_key)
    canvas.bind("w", up_key)
    canvas.bind("s", down_key)
    canvas.bind("e", see_key)
    canvas.bind("q", hide_key)
    canvas.bind("<space>", pause_key)
    canvas.focus_set()
    move_party()
    move_guard()
    move_student()

    # delete the Game Over text
    canvas.delete("text")


def open_new_window():
    """Open a new window with the story/instructions"""
    global my_img
    top = Toplevel()
    my_img = PhotoImage(file="story-instructions.png")
    lbl = Label(top, image=my_img).pack()
    top.geometry("500x500")


def set_window_dimensions(w, h):
    # set window dimensions
    window = Tk()
    window.title("Freshers'")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    window.geometry("500x500")
    # create the menu bar
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Save game", command=save)
    filemenu.add_command(label="Load saved game", command=load)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="Options", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instructions", command=open_new_window)
    menubar.add_cascade(label="Instructions", menu=helpmenu)

    window.config(menu=menubar)

    return window


def place_party():
    """Place the party/indigo rectangle"""
    global party, partyX, partyY
    party = canvas.create_rectangle(0, 0, studentSize, studentSize, fill="indigo")
    partyX = random.randint(0, width - studentSize)
    partyY = random.randint(0, height - studentSize)
    canvas.move(party, partyX, partyY)
    party_pos = canvas.coords(party)
    fence_pos1 = canvas.coords(fence1)
    fence_pos2 = canvas.coords(fence2)
    fence_pos3 = canvas.coords(fence3)
    fence_pos4 = canvas.coords(fence4)
    fence_pos5 = canvas.coords(fence5)
    # check if the party is overlapping the other objects from the code
    while (
        overlapping(party_pos, fence_pos1)
        or overlapping(party_pos, fence_pos2)
        or overlapping(party_pos, fence_pos3)
        or overlapping(party_pos, fence_pos4)
        or overlapping(party_pos, fence_pos5)
    ):
        partyX = random.randint(0, width - studentSize)
        partyY = random.randint(0, height - studentSize)
        canvas.move(party, partyX, partyY)
        party_pos = canvas.coords(party)
    positions = []
    positions.append(canvas.coords(party))
    # check if the position of the party is not outside the canvas
    while (
        positions[0][0] < 0
        or positions[0][2] > width
        or positions[0][3] > height
        or positions[0][1] < 0
    ):
        partyX = random.randint(0, width - studentSize)
        partyY = random.randint(0, height - studentSize)
        canvas.move(party, partyX, partyY)
    positions.clear()
    positions.append(canvas.coords(party))


def place_guards():
    """Place the guards/darkblue rectangles"""
    global guard, guardX, guardY, guard1, guard1, guard2, guard1X, guard1Y, guard2X, guard2Y
    guard = canvas.create_rectangle(
        0, 0, studentSize * 2, studentSize * 2, fill="darkblue"
    )
    guardX = random.randint(0, width - studentSize)
    guardY = random.randint(0, height - studentSize)
    canvas.move(guard, guardX, guardY)
    s_pos = canvas.coords(student[0])
    party_guard = canvas.coords(guard)
    fence_pos1 = canvas.coords(fence1)
    fence_pos2 = canvas.coords(fence2)
    fence_pos3 = canvas.coords(fence3)
    fence_pos4 = canvas.coords(fence4)
    fence_pos5 = canvas.coords(fence5)
    party_pos = canvas.coords(party)
    # checking for each guard is the position is overlapping
    while (
        overlapping(party_guard, s_pos)
        or overlapping(party_guard, party_pos)
        or overlapping(party_guard, fence_pos1)
        or overlapping(party_guard, fence_pos2)
        or overlapping(party_guard, fence_pos3)
        or overlapping(party_guard, fence_pos4)
        or overlapping(party_guard, fence_pos5)
    ):
        guardX = random.randint(0, width - studentSize)
        guardY = random.randint(0, height - studentSize)
        canvas.move(guard, guardX, guardY)
        party_guard = canvas.coords(guard)
    guard1 = canvas.create_rectangle(
        0, 0, studentSize * 2, studentSize * 2, fill="darkblue"
    )
    guard1X = random.randint(0, width - studentSize)
    guard1Y = random.randint(0, height - studentSize)
    canvas.move(guard1, guard1X, guard1Y)
    party_guard = canvas.coords(guard1)
    while (
        overlapping(party_guard, s_pos)
        or overlapping(party_guard, party_pos)
        or overlapping(party_guard, fence_pos1)
        or overlapping(party_guard, fence_pos2)
        or overlapping(party_guard, fence_pos3)
        or overlapping(party_guard, fence_pos4)
        or overlapping(party_guard, fence_pos5)
    ):
        guard1X = random.randint(0, width - studentSize)
        guard1Y = random.randint(0, height - studentSize)
        canvas.move(guard1, guard1X, guard1Y)
        party_guard = canvas.coords(guard1)
    guard2 = canvas.create_rectangle(
        0, 0, studentSize * 2, studentSize * 2, fill="darkblue"
    )
    guard2X = random.randint(0, width - studentSize)
    guard2Y = random.randint(0, height - studentSize)
    canvas.move(guard2, guard2X, guard2Y)
    party_guard = canvas.coords(guard2)
    while (
        overlapping(party_guard, s_pos)
        or overlapping(party_guard, party_pos)
        or overlapping(party_guard, fence_pos1)
        or overlapping(party_guard, fence_pos2)
        or overlapping(party_guard, fence_pos3)
        or overlapping(party_guard, fence_pos4)
        or overlapping(party_guard, fence_pos5)
    ):
        guard2X = random.randint(0, width - studentSize)
        guard2Y = random.randint(0, height - studentSize)
        canvas.move(guard2, guard2X, guard2Y)
        party_guard = canvas.coords(guard2)


def place_fence():
    """Place the fences/grey rectangles"""
    global fence1, fence2, fence3, fenceX, fenceY, fence4, fence5, fence2X, fence2Y, fence3X, fence3Y, fence4X, fence4Y, fence5X, fence5Y
    fence1 = canvas.create_rectangle(0, 0, studentSize, studentSize * 10, fill="grey")
    fenceX = random.randint(50, 400)
    fenceY = random.randint(50, 400)
    canvas.move(fence1, fenceX, fenceY)
    fence2 = canvas.create_rectangle(0, 0, studentSize, studentSize * 10, fill="grey")
    fence2X = random.randint(50, 400)
    fence2Y = random.randint(50, 400)
    canvas.move(fence2, fence2X, fence2Y)
    fence_pos1 = canvas.coords(fence1)
    fence_pos2 = canvas.coords(fence2)
    # check in order for the fences to not overlap each other
    while overlapping(fence_pos1, fence_pos2):
        fence2X = random.randint(0, 400)
        fence2Y = random.randint(0, 400)
        canvas.move(fence2, fence2X, fence2Y)
        fence_pos2 = canvas.coords(fence2)
    fence3 = canvas.create_rectangle(0, 0, studentSize * 10, studentSize, fill="grey")
    fence3X = random.randint(50, 400)
    fence3Y = random.randint(50, 400)
    canvas.move(fence3, fence3X, fence3Y)
    fence_pos3 = canvas.coords(fence3)
    while overlapping(fence_pos3, fence_pos2) or overlapping(fence_pos1, fence_pos3):
        fence3X = random.randint(0, 400)
        fence3Y = random.randint(0, 400)
        canvas.move(fence3, fence3X, fence3Y)
        fence_pos3 = canvas.coords(fence3)
    fence4 = canvas.create_rectangle(0, 0, studentSize * 20, studentSize, fill="grey")
    fence4X = random.randint(50, 400)
    fence4Y = random.randint(50, 400)
    canvas.move(fence4, fence4X, fence4Y)
    fence_pos4 = canvas.coords(fence4)
    while (
        overlapping(fence_pos1, fence_pos4)
        or overlapping(fence_pos2, fence_pos4)
        or overlapping(fence_pos3, fence_pos4)
    ):
        fence4X = random.randint(0, 400)
        fence4Y = random.randint(0, 400)
        canvas.move(fence4, fence4X, fence4Y)
        fence_pos4 = canvas.coords(fence4)
    fence5 = canvas.create_rectangle(0, 0, studentSize, studentSize * 15, fill="grey")
    fence5X = random.randint(50, 400)
    fence5Y = random.randint(50, 400)
    canvas.move(fence5, fence5X, fence5Y)
    fence_pos5 = canvas.coords(fence5)
    while (
        overlapping(fence_pos1, fence_pos5)
        or overlapping(fence_pos2, fence_pos5)
        or overlapping(fence_pos3, fence_pos5)
        or overlapping(fence_pos4, fence_pos5)
    ):
        fence5X = random.randint(0, 400)
        fence5Y = random.randint(0, 400)
        canvas.move(fence5, fence5X, fence5Y)
        fence_pos5 = canvas.coords(fence5)


# functions that give the direction of the player once the keys are pressed
def left_key(event):
    global direction
    direction = "left"


def right_key(event):
    global direction
    direction = "right"


def up_key(event):
    global direction
    direction = "up"


def down_key(event):
    global direction
    direction = "down"


def pause_key(event):
    onclick()


# the cheat code - code that is going to help the user see the guards
def see_key(event):
    canvas.itemconfig(guard, fill="darkblue")
    canvas.itemconfig(guard1, fill="darkblue")
    canvas.itemconfig(guard2, fill="darkblue")


# the boss key - code that is going to help the user hide the game
def hide_key(event):
    global direction
    direction = None
    window.withdraw()
    window.after(5000, show)
    canvas.create_text(
        width / 2,
        height / 2,
        fill="white",
        font="Corbel 30 italic bold",
        text="Busted!Exit Game!",
    )


def show():
    window.deiconify()


def change_score():
    """Change the score by 10"""
    global score
    score += 10
    txt = "Score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)


def move_party():
    """Move the party to a random position"""
    global party, partyX, partyY
    canvas.move(party, (partyX * (-1)), (partyY * (-1)))
    partyX = random.randint(0, width - studentSize)
    partyY = random.randint(0, height - studentSize)
    canvas.move(party, partyX, partyY)


# once the player gets to the party, the guards move in another random position
def move_guard():
    global guard, guardX, guardY, guard1, guard2, guard1X, guard1Y, guard2X, guard2Y
    canvas.move(guard, (guardX * (-1)), (guardY * (-1)))
    canvas.itemconfig(guard, fill="darkblue")
    guardX = random.randint(0, width - studentSize)
    guardY = random.randint(0, height - studentSize)
    canvas.move(guard, guardX, guardY)
    party_pos = canvas.coords(party)
    fence_pos1 = canvas.coords(fence1)
    fence_pos2 = canvas.coords(fence2)
    fence_pos3 = canvas.coords(fence3)
    fence_pos4 = canvas.coords(fence4)
    fence_pos5 = canvas.coords(fence5)
    guard_pos = canvas.coords(guard)
    while (
        overlapping(guard_pos, party_pos)
        or overlapping(guard_pos, fence_pos1)
        or overlapping(guard_pos, fence_pos2)
        or overlapping(guard_pos, fence_pos3)
        or overlapping(guard_pos, fence_pos4)
        or overlapping(guard_pos, fence_pos5)
    ):
        guardX = random.randint(0, width - studentSize)
        guardY = random.randint(0, height - studentSize)
        canvas.move(guard, guardX, guardY)
        guard_pos = canvas.coords(guard)
    canvas.move(guard1, (guard1X * (-1)), (guard1Y * (-1)))
    canvas.itemconfig(guard1, fill="darkblue")
    guard1X = random.randint(0, width - studentSize)
    guard1Y = random.randint(0, height - studentSize)
    canvas.move(guard1, guard1X, guard1Y)
    guard_pos = canvas.coords(guard1)
    while (
        overlapping(guard_pos, party_pos)
        or overlapping(guard_pos, fence_pos1)
        or overlapping(guard_pos, fence_pos2)
        or overlapping(guard_pos, fence_pos3)
        or overlapping(guard_pos, fence_pos4)
        or overlapping(guard_pos, fence_pos5)
    ):
        guard1X = random.randint(0, width - studentSize)
        guard1Y = random.randint(0, height - studentSize)
        canvas.move(guard1, guard1X, guard1Y)
        guard_pos = canvas.coords(guard1)
    canvas.move(guard2, (guard2X * (-1)), (guard2Y * (-1)))
    canvas.itemconfig(guard2, fill="darkblue")
    guard2X = random.randint(0, width - studentSize)
    guard2Y = random.randint(0, height - studentSize)
    canvas.move(guard2, guard2X, guard2Y)
    guard_pos = canvas.coords(guard1)
    while (
        overlapping(guard_pos, party_pos)
        or overlapping(guard_pos, fence_pos1)
        or overlapping(guard_pos, fence_pos2)
        or overlapping(guard_pos, fence_pos3)
        or overlapping(guard_pos, fence_pos4)
        or overlapping(guard_pos, fence_pos5)
    ):
        guard2X = random.randint(0, width - studentSize)
        guard2Y = random.randint(0, height - studentSize)
        canvas.move(guard2, guard2X, guard2Y)
        guard_pos = canvas.coords(guard2)

    # after 2.5 sec, the colour of the guards turns black
    window.after(2500, change_color)


def overlapping(a, b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False


def move_student():
    canvas.pack()
    # changing the position of the player once he gets out of the canvas
    positions = []
    positions.append(canvas.coords(student[0]))
    if positions[0][0] < 0:
        canvas.coords(
            student[0], width, positions[0][1], width - studentSize, positions[0][3]
        )
    elif positions[0][2] > width:
        canvas.coords(student[0], 0 - studentSize, positions[0][1], 0, positions[0][3])
    elif positions[0][3] > height:
        canvas.coords(student[0], positions[0][0], 0 - studentSize, positions[0][2], 0)
    elif positions[0][1] < 0:
        canvas.coords(
            student[0], positions[0][0], height, positions[0][2], height - studentSize
        )
    positions.clear()
    positions.append(canvas.coords(student[0]))
    # the movementof the student
    if direction == "left":
        canvas.move(student[0], -studentSize, 0)
    elif direction == "right":
        canvas.move(student[0], studentSize, 0)
    elif direction == "up":
        canvas.move(student[0], 0, -studentSize)
    elif direction == "down":
        canvas.move(student[0], 0, studentSize)

    s_head_pos = canvas.coords(student[0])
    party_pos = canvas.coords(party)
    safe_pos = canvas.coords(safe)
    # if the student gets to the party
    if overlapping(s_head_pos, party_pos):
        move_party()
        move_guard()
        change_score()
    # if the student gets to the safePlace
    if overlapping(s_head_pos, safe_pos):
        move_party()
    guard_pos = canvas.coords(guard)
    # if the student meets the guard - game over
    if overlapping(s_head_pos, guard_pos):
        game_over = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    guard_pos = canvas.coords(guard1)
    if overlapping(s_head_pos, guard_pos):
        game_over = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    guard_pos = canvas.coords(guard2)
    if overlapping(s_head_pos, guard_pos):
        game_over = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    # if the student meets the fence - game over
    fence_pos = canvas.coords(fence1)
    if overlapping(s_head_pos, fence_pos):
        game_over = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    fence_pos = canvas.coords(fence2)
    if overlapping(s_head_pos, fence_pos):
        game_over = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    fence_pos = canvas.coords(fence3)
    if overlapping(s_head_pos, fence_pos):
        game_over = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    fence_pos = canvas.coords(fence4)
    if overlapping(s_head_pos, fence_pos):
        game_over = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    fence_pos = canvas.coords(fence5)
    if overlapping(s_head_pos, fence_pos):
        game_over = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    # if not gameOver - the speed of the player changes

    if "gameOver" not in locals():
        if score > 150:
            window.after(20, move_student)
        elif score > 100:
            window.after(40, move_student)
        elif score > 50:
            window.after(60, move_student)
        else:
            window.after(120, move_student)
    # else the leader board appears
    else:
        board()


# changing the color of the guards
def change_color():
    canvas.itemconfig(guard, fill="black")
    canvas.itemconfig(guard1, fill="black")
    canvas.itemconfig(guard2, fill="black")


# size of window/canvas
width = 500
height = 500
window = set_window_dimensions(width, height)
canvas = Canvas(window, bg="black", width=width, height=height)
# declare the variable student
student = []
studentSize = 15
student.append(
    canvas.create_rectangle(
        studentSize, studentSize, studentSize * 2, studentSize * 2, fill="white"
    )
)

# creating the scoreText
score = 0
txt = "Score:" + str(score)
scoreText = canvas.create_text(
    width / 2, 10, fill="white", font="corbel 20 italic bold", text=txt, tag="score"
)

# calling the functions that are used to update the player s location
canvas.bind("a", left_key)
canvas.bind("d", right_key)
canvas.bind("w", up_key)
canvas.bind("s", down_key)
canvas.bind("e", see_key)
canvas.bind("q", hide_key)
canvas.bind("<space>", pause_key)
canvas.focus_set()
direction = None

# calling the functions
place_fence()
place_party()
place_guards()
place_safe_party()
move_student()

window.after(2500, change_color)

window.mainloop()
