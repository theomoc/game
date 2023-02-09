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
        if word >= "0" and word <= "9":
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
        if word >= "0" and word <= "9":
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
        if word >= "0" and word <= "9":
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
        if word >= "0" and word <= "9":
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
        if word >= "0" and word <= "9":
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
        if word >= "0" and word <= "9":
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
        if word >= "0" and word <= "9":
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
        if word >= "0" and word <= "9":
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
        if word >= "0" and word <= "9":
            x = x * 10 + int(word)
        else:
            position.append(x)
            x = 0
    canvas.coords(fence5, position[1], position[4], position[7], position[10])


def board():
    """Create and update leader board"""
    # the user is asked to introduce his/her name
    USER_INP = simpledialog.askstring(title="Good job!", prompt="What's your Name?:)")
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
        xname = USER_INP
    elif score > y:
        z = y
        zname = yname
        y = score
        yname = USER_INP
    elif score > z:
        z = score
        poz = 3
        zname = USER_INP
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
    myLabel = Label(board, text=leader)
    myLabel1.pack()
    myLabel.pack()
    button = Button(board, text="Restart", command=donothing).pack()
    board.mainloop()


# pausing the game
def onclick():
    global direction, copydirection
    if direction == None:
        direction = copydirection
        canvas.bind("a", leftKey)
        canvas.bind("d", rightKey)
        canvas.bind("w", upKey)
        canvas.bind("s", downKey)
        canvas.focus_set()

    else:
        copydirection = direction
        direction = None


def placeSafeParty():
    """Place the safe party/yellow rectangle"""
    global safe
    safe = canvas.create_rectangle(0, 0, studentSize, studentSize, fill="gold")
    canvas.move(safe, 0, 0)


def donothing():
    # creating the scoreText
    global score, direction, student
    canvas.delete(student)
    student = []
    studentSize = 15
    student.append(
        canvas.create_rectangle(
            studentSize, studentSize, studentSize * 2, studentSize * 2, fill="white"
        )
    )

    score = 0
    txt = "Score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)

    # calling the functions
    direction = None
    canvas.bind("a", leftKey)
    canvas.bind("d", rightKey)
    canvas.bind("w", upKey)
    canvas.bind("s", downKey)
    canvas.bind("e", SeeKey)
    canvas.bind("q", HideKey)
    canvas.bind("<space>", PauseKey)
    canvas.focus_set()
    moveParty()
    moveGuard()
    moveStudent()

    # delete the Game Over text
    canvas.delete("text")


def openNewWindow():
    """Open a new window with the story/instructions"""
    global my_img
    top = Toplevel()
    my_img = PhotoImage(file="story-instructions.png")
    lbl = Label(top, image=my_img).pack()
    top.geometry("500x500")


def setWindowDimensions(w, h):
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
    helpmenu.add_command(label="Instructions", command=openNewWindow)
    menubar.add_cascade(label="Instructions", menu=helpmenu)

    window.config(menu=menubar)

    return window


def placeParty():
    """Place the party/indigo rectangle"""
    global party, partyX, partyY
    party = canvas.create_rectangle(0, 0, studentSize, studentSize, fill="indigo")
    partyX = random.randint(0, width - studentSize)
    partyY = random.randint(0, height - studentSize)
    canvas.move(party, partyX, partyY)
    partyPos = canvas.coords(party)
    fencePos1 = canvas.coords(fence1)
    fencePos2 = canvas.coords(fence2)
    fencePos3 = canvas.coords(fence3)
    fencePos4 = canvas.coords(fence4)
    fencePos5 = canvas.coords(fence5)
    # check if the party is overlapping the other objects from the code
    while (
        overlapping(partyPos, fencePos1)
        or overlapping(partyPos, fencePos2)
        or overlapping(partyPos, fencePos3)
        or overlapping(partyPos, fencePos4)
        or overlapping(partyPos, fencePos5)
    ):
        partyX = random.randint(0, width - studentSize)
        partyY = random.randint(0, height - studentSize)
        canvas.move(party, partyX, partyY)
        partyPos = canvas.coords(party)
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


def placeGuards():
    """Place the guards/darkblue rectangles"""
    global guard, guardX, guardY, guard1, guard1, guard2, guard1X, guard1Y, guard2X, guard2Y
    guard = canvas.create_rectangle(
        0, 0, studentSize * 2, studentSize * 2, fill="darkblue"
    )
    guardX = random.randint(0, width - studentSize)
    guardY = random.randint(0, height - studentSize)
    canvas.move(guard, guardX, guardY)
    Spos = canvas.coords(student[0])
    partyGuard = canvas.coords(guard)
    fencePos1 = canvas.coords(fence1)
    fencePos2 = canvas.coords(fence2)
    fencePos3 = canvas.coords(fence3)
    fencePos4 = canvas.coords(fence4)
    fencePos5 = canvas.coords(fence5)
    partyPos = canvas.coords(party)
    # checking for each guard is the position is overlapping
    while (
        overlapping(partyGuard, Spos)
        or overlapping(partyGuard, partyPos)
        or overlapping(partyGuard, fencePos1)
        or overlapping(partyGuard, fencePos2)
        or overlapping(partyGuard, fencePos3)
        or overlapping(partyGuard, fencePos4)
        or overlapping(partyGuard, fencePos5)
    ):
        guardX = random.randint(0, width - studentSize)
        guardY = random.randint(0, height - studentSize)
        canvas.move(guard, guardX, guardY)
        partyGuard = canvas.coords(guard)
    guard1 = canvas.create_rectangle(
        0, 0, studentSize * 2, studentSize * 2, fill="darkblue"
    )
    guard1X = random.randint(0, width - studentSize)
    guard1Y = random.randint(0, height - studentSize)
    canvas.move(guard1, guard1X, guard1Y)
    partyGuard = canvas.coords(guard1)
    while (
        overlapping(partyGuard, Spos)
        or overlapping(partyGuard, partyPos)
        or overlapping(partyGuard, fencePos1)
        or overlapping(partyGuard, fencePos2)
        or overlapping(partyGuard, fencePos3)
        or overlapping(partyGuard, fencePos4)
        or overlapping(partyGuard, fencePos5)
    ):
        guard1X = random.randint(0, width - studentSize)
        guard1Y = random.randint(0, height - studentSize)
        canvas.move(guard1, guard1X, guard1Y)
        partyGuard = canvas.coords(guard1)
    guard2 = canvas.create_rectangle(
        0, 0, studentSize * 2, studentSize * 2, fill="darkblue"
    )
    guard2X = random.randint(0, width - studentSize)
    guard2Y = random.randint(0, height - studentSize)
    canvas.move(guard2, guard2X, guard2Y)
    partyGuard = canvas.coords(guard2)
    while (
        overlapping(partyGuard, Spos)
        or overlapping(partyGuard, partyPos)
        or overlapping(partyGuard, fencePos1)
        or overlapping(partyGuard, fencePos2)
        or overlapping(partyGuard, fencePos3)
        or overlapping(partyGuard, fencePos4)
        or overlapping(partyGuard, fencePos5)
    ):
        guard2X = random.randint(0, width - studentSize)
        guard2Y = random.randint(0, height - studentSize)
        canvas.move(guard2, guard2X, guard2Y)
        partyGuard = canvas.coords(guard2)


def placeFence():
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
    fencePos1 = canvas.coords(fence1)
    fencePos2 = canvas.coords(fence2)
    # check in order for the fences to not overlap each other
    while overlapping(fencePos1, fencePos2):
        fence2X = random.randint(0, 400)
        fence2Y = random.randint(0, 400)
        canvas.move(fence2, fence2X, fence2Y)
        fencePos2 = canvas.coords(fence2)
    fence3 = canvas.create_rectangle(0, 0, studentSize * 10, studentSize, fill="grey")
    fence3X = random.randint(50, 400)
    fence3Y = random.randint(50, 400)
    canvas.move(fence3, fence3X, fence3Y)
    fencePos3 = canvas.coords(fence3)
    while overlapping(fencePos3, fencePos2) or overlapping(fencePos1, fencePos3):
        fence3X = random.randint(0, 400)
        fence3Y = random.randint(0, 400)
        canvas.move(fence3, fence3X, fence3Y)
        fencePos3 = canvas.coords(fence3)
    fence4 = canvas.create_rectangle(0, 0, studentSize * 20, studentSize, fill="grey")
    fence4X = random.randint(50, 400)
    fence4Y = random.randint(50, 400)
    canvas.move(fence4, fence4X, fence4Y)
    fencePos4 = canvas.coords(fence4)
    while (
        overlapping(fencePos1, fencePos4)
        or overlapping(fencePos2, fencePos4)
        or overlapping(fencePos3, fencePos4)
    ):
        fence4X = random.randint(0, 400)
        fence4Y = random.randint(0, 400)
        canvas.move(fence4, fence4X, fence4Y)
        fencePos4 = canvas.coords(fence4)
    fence5 = canvas.create_rectangle(0, 0, studentSize, studentSize * 15, fill="grey")
    fence5X = random.randint(50, 400)
    fence5Y = random.randint(50, 400)
    canvas.move(fence5, fence5X, fence5Y)
    fencePos5 = canvas.coords(fence5)
    while (
        overlapping(fencePos1, fencePos5)
        or overlapping(fencePos2, fencePos5)
        or overlapping(fencePos3, fencePos5)
        or overlapping(fencePos4, fencePos5)
    ):
        fence5X = random.randint(0, 400)
        fence5Y = random.randint(0, 400)
        canvas.move(fence5, fence5X, fence5Y)
        fencePos5 = canvas.coords(fence5)


# functions that give the direction of the player once the keys are pressed
def leftKey(event):
    global direction
    direction = "left"


def rightKey(event):
    global direction
    direction = "right"


def upKey(event):
    global direction
    direction = "up"


def downKey(event):
    global direction
    direction = "down"


def PauseKey(event):
    onclick()


# the cheat code - code that is going to help the user see the guards
def SeeKey(event):
    canvas.itemconfig(guard, fill="darkblue")
    canvas.itemconfig(guard1, fill="darkblue")
    canvas.itemconfig(guard2, fill="darkblue")


# the boss key - code that is going to help the user hide the game
def HideKey(event):
    global direction
    direction = None
    window.withdraw()
    window.after(5000, Show)
    canvas.create_text(
        width / 2,
        height / 2,
        fill="white",
        font="Corbel 30 italic bold",
        text="Busted!Exit Game!",
    )


def Show():
    window.deiconify()


def ChangeScore():
    """Change the score by 10"""
    global score
    score += 10
    txt = "Score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)


def moveParty():
    """Move the party to a random position"""
    global party, partyX, partyY
    canvas.move(party, (partyX * (-1)), (partyY * (-1)))
    partyX = random.randint(0, width - studentSize)
    partyY = random.randint(0, height - studentSize)
    canvas.move(party, partyX, partyY)


# once the player gets to the party, the guards move in another random position
def moveGuard():
    global guard, guardX, guardY, guard1, guard2, guard1X, guard1Y, guard2X, guard2Y
    canvas.move(guard, (guardX * (-1)), (guardY * (-1)))
    canvas.itemconfig(guard, fill="darkblue")
    guardX = random.randint(0, width - studentSize)
    guardY = random.randint(0, height - studentSize)
    canvas.move(guard, guardX, guardY)
    partyPos = canvas.coords(party)
    fencePos1 = canvas.coords(fence1)
    fencePos2 = canvas.coords(fence2)
    fencePos3 = canvas.coords(fence3)
    fencePos4 = canvas.coords(fence4)
    fencePos5 = canvas.coords(fence5)
    GuardPos = canvas.coords(guard)
    while (
        overlapping(GuardPos, partyPos)
        or overlapping(GuardPos, fencePos1)
        or overlapping(GuardPos, fencePos2)
        or overlapping(GuardPos, fencePos3)
        or overlapping(GuardPos, fencePos4)
        or overlapping(GuardPos, fencePos5)
    ):
        guardX = random.randint(0, width - studentSize)
        guardY = random.randint(0, height - studentSize)
        canvas.move(guard, guardX, guardY)
        GuardPos = canvas.coords(guard)
    canvas.move(guard1, (guard1X * (-1)), (guard1Y * (-1)))
    canvas.itemconfig(guard1, fill="darkblue")
    guard1X = random.randint(0, width - studentSize)
    guard1Y = random.randint(0, height - studentSize)
    canvas.move(guard1, guard1X, guard1Y)
    GuardPos = canvas.coords(guard1)
    while (
        overlapping(GuardPos, partyPos)
        or overlapping(GuardPos, fencePos1)
        or overlapping(GuardPos, fencePos2)
        or overlapping(GuardPos, fencePos3)
        or overlapping(GuardPos, fencePos4)
        or overlapping(GuardPos, fencePos5)
    ):
        guard1X = random.randint(0, width - studentSize)
        guard1Y = random.randint(0, height - studentSize)
        canvas.move(guard1, guard1X, guard1Y)
        GuardPos = canvas.coords(guard1)
    canvas.move(guard2, (guard2X * (-1)), (guard2Y * (-1)))
    canvas.itemconfig(guard2, fill="darkblue")
    guard2X = random.randint(0, width - studentSize)
    guard2Y = random.randint(0, height - studentSize)
    canvas.move(guard2, guard2X, guard2Y)
    GuardPos = canvas.coords(guard1)
    while (
        overlapping(GuardPos, partyPos)
        or overlapping(GuardPos, fencePos1)
        or overlapping(GuardPos, fencePos2)
        or overlapping(GuardPos, fencePos3)
        or overlapping(GuardPos, fencePos4)
        or overlapping(GuardPos, fencePos5)
    ):
        guard2X = random.randint(0, width - studentSize)
        guard2Y = random.randint(0, height - studentSize)
        canvas.move(guard2, guard2X, guard2Y)
        GuardPos = canvas.coords(guard2)

    # after 2.5 sec, the colour of the guards turns black
    window.after(2500, change_color)


def overlapping(a, b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False


def moveStudent():
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

    sHeadPos = canvas.coords(student[0])
    partyPos = canvas.coords(party)
    SafePos = canvas.coords(safe)
    # if the student gets to the party
    if overlapping(sHeadPos, partyPos):
        moveParty()
        moveGuard()
        ChangeScore()
    # if the student gets to the safePlace
    if overlapping(sHeadPos, SafePos):
        moveParty()
    GuardPos = canvas.coords(guard)
    # if the student meets the guard - game over
    if overlapping(sHeadPos, GuardPos):
        gameOver = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    GuardPos = canvas.coords(guard1)
    if overlapping(sHeadPos, GuardPos):
        gameOver = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    GuardPos = canvas.coords(guard2)
    if overlapping(sHeadPos, GuardPos):
        gameOver = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    # if the student meets the fence - game over
    fencePos = canvas.coords(fence1)
    if overlapping(sHeadPos, fencePos):
        gameOver = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    fencePos = canvas.coords(fence2)
    if overlapping(sHeadPos, fencePos):
        gameOver = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    fencePos = canvas.coords(fence3)
    if overlapping(sHeadPos, fencePos):
        gameOver = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    fencePos = canvas.coords(fence4)
    if overlapping(sHeadPos, fencePos):
        gameOver = True
        canvas.create_text(
            width / 2,
            height / 2,
            fill="white",
            font="corbel 20 italic bold",
            text="Game over! Close the program.",
            tag="text",
        )
    fencePos = canvas.coords(fence5)
    if overlapping(sHeadPos, fencePos):
        gameOver = True
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
            window.after(20, moveStudent)
        elif score > 100:
            window.after(40, moveStudent)
        elif score > 50:
            window.after(60, moveStudent)
        else:
            window.after(120, moveStudent)
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
window = setWindowDimensions(width, height)
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
canvas.bind("a", leftKey)
canvas.bind("d", rightKey)
canvas.bind("w", upKey)
canvas.bind("s", downKey)
canvas.bind("e", SeeKey)
canvas.bind("q", HideKey)
canvas.bind("<space>", PauseKey)
canvas.focus_set()
direction = None

# calling the functions
placeFence()
placeParty()
placeGuards()
placeSafeParty()
moveStudent()

window.after(2500, change_color)

window.mainloop()
