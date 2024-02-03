from tkinter import *
import tkinter.messagebox as tmsg
import random
import time

Userscore = 0
Computerscore = 0
No_of_draws = 0


def Complete_game():
    def main_Window():
        roots.destroy()

        def game_function_handler():
            global Userscore, Computerscore, No_of_draws
            snake_value_get = snake.get()
            water_value_get = water.get()
            gun_value_get = gun.get()
            # colors changing
            color_list = ['red', 'blue', "pink", 'green']
            random_colors = random.choice(color_list)
            mainlabel.config(fg=random_colors)
            selections.config(fg=random_colors)
            # enter values compared by random s,w,g
            list_hidden_values = ["s", "w", "g"]
            random_hidden = random.choice(list_hidden_values)

            def results(string):
                global Userscore, Computerscore, No_of_draws
                res = tmsg.askokcancel("Results", f'{string}\nWould you like to play again?')
                root.destroy()
                if res:
                    Userscore = 0
                    Computerscore = 0
                    No_of_draws = 0
                    Complete_game()
                elif not res:
                    quit()

            def foe_user():
                global Userscore
                Userscore += 1
                resultvalue.set("")
                result.insert(0, "YOU WON")

            def for_computer():
                global Computerscore
                Computerscore += 1
                resultvalue.set("")
                result.insert(0, "Computer Won")

            def for_draw():
                global No_of_draws
                No_of_draws += 1
                resultvalue.set("")
                result.insert(0, "Draw")

            if snake_value_get == 1 and water_value_get == 0 and gun_value_get == 0 and random_hidden == "s":
                snake.set(0)
                for_draw()
            elif snake_value_get == 0 and water_value_get == 1 and gun_value_get == 0 and random_hidden == "w":
                water.set(0)
                for_draw()
            elif snake_value_get == 0 and water_value_get == 0 and gun_value_get == 1 and random_hidden == "g":
                gun.set(0)
                for_draw()
            elif snake_value_get == 1 and water_value_get == 0 and gun_value_get == 0:
                snake.set(0)
                if random_hidden == "w":
                    for_computer()
                elif random_hidden == "g":
                    foe_user()
            elif snake_value_get == 0 and water_value_get == 1 and gun_value_get == 0:
                water.set(0)
                if random_hidden == "s":
                    for_computer()
                elif random_hidden == "g":
                    foe_user()
            elif snake_value_get == 0 and water_value_get == 0 and gun_value_get == 1:
                gun.set(0)
                if random_hidden == "s":
                    foe_user()
                elif random_hidden == "w":
                    for_computer()
            # 2 options conditions
            elif snake_value_get == 1 and water_value_get == 1 and gun_value_get == 0:
                time.sleep(0.1)
                resultvalue.set("")
                water.set(0)
                snake.set(0)
                resultvalue.set("Error(At least 1)")
            elif snake_value_get == 0 and water_value_get == 1 and gun_value_get == 1:
                resultvalue.set("")
                gun.set(0)
                water.set(0)
                resultvalue.set("Error(At least 1)")
            elif snake_value_get == 1 and water_value_get == 0 and gun_value_get == 1:
                resultvalue.set("")
                gun.set(0)
                snake.set(0)
                resultvalue.set("Error(At least 1)")
            # other conditions
            # TODO: ctrl+shift+backspace used to see history
            else:
                time.sleep(0.1)
                water.set(0)
                snake.set(0)
                gun.set(0)
                resultvalue.set("Please choose at-leas 1 option")
            status_userscore.set(f"{find} score: {Userscore}")
            status_computerscore.set(f"Computer score: {Computerscore}")
            status_noofdraws.set(f"Number Of Draws: {No_of_draws}")
            if Userscore == 10:
                results("The User Won.")
            elif Computerscore == 10:
                results("The Computer Won.")
            elif No_of_draws == 10:
                results("The Match is draw")

        # Window settings
        find = value.get()
        screen_widthm = 566
        screen_heightm = 475
        root = Tk()
        root.geometry(f"{screen_widthm}x{screen_heightm}")
        root.title("Snake-Water-Gun Game")
        root.config(bg="#32ADCF")
        # Game Variables
        mainlabel = Label(root, text="SWG Game", bg="#32ADCF", font="timesnewroman 20 bold", fg="#22FF86")
        mainlabel.pack()
        selections = Label(root, text="Choose Your Selection", bg="#32ADCF", font="timesnewroman 10 bold")
        selections.pack(side=TOP, anchor=W)
        # GAme button Values
        snake = IntVar()
        water = IntVar()
        gun = IntVar()
        resultvalue = StringVar()
        status_userscore = StringVar()
        status_computerscore = StringVar()
        status_noofdraws = StringVar()
        # Button Frame
        buttonframe = Frame(root)
        snakebutton = Checkbutton(text="Snake", variable=snake, bg="#32ADCF", font="timesnewroman 8 bold").pack(side=TOP,anchor=W,padx=1,pady=1)
        waterbutton = Checkbutton(text="Water", variable=water, bg="#32ADCF", font="timesnewroman 8 bold").pack(side=TOP,anchor=W,padx=1,pady=1)
        gunbutton = Checkbutton(text="Gun", variable=gun, bg="#32ADCF", font="timesnewroman 8 bold").pack(side=TOP,anchor=W,padx=1,pady=1)
        buttonframe.pack()
        game_main_buttons = Button(root, text="GO!!!!", borderwidth=2, relief=GROOVE, bg="#32ADCF",command=game_function_handler)
        game_main_buttons.pack(side=TOP, anchor=W, padx=1, pady=1, fill=X)
        # Crating a Entry Widget
        result = Entry(root, bg="blue", font="timesnewroman 20 italic ", textvariable=resultvalue, borderwidth=0)
        result.pack(fill=X, padx=1, pady=2, )
        # Status for result
        Label(root, font="timesnewroman 8 italic", anchor="e", bg="#32ADCF", textvariable=status_userscore).pack(fill=X, side=BOTTOM)
        Label(root, font="timesnewroman 8 italic", anchor="e", bg="#32ADCF", textvariable=status_computerscore).pack(fill=X, side=BOTTOM)
        Label(root, font="timesnewroman 8 italic", anchor="e", bg="#32ADCF", textvariable=status_noofdraws).pack(fill=X, side=BOTTOM)
        root.mainloop()

    screen_width = 260
    screen_height = 100
    roots = Tk()
    roots.geometry(f"{screen_width}x{screen_height}")
    roots.title("Snake-Water-Gun Game")
    roots.config(bg="#32ADCF")
    selection = Label(roots, text="Welcome TO SWG", bg="#FF9B39", font="timesnewroman 10 italic", )
    selection.pack(side=TOP, anchor="w", fill=X, padx=2, pady=2)
    selection2 = Label(roots, text="Enter Your Name: ", bg="#32ADCF", font="timesnewroman 10 italic")
    selection2.pack(side=TOP, anchor="w", padx=2, pady=2)
    value = StringVar()
    name = Entry(roots, font="timesnewroman 10 italic ", textvariable=value, borderwidth=0)
    name.pack(side=TOP, anchor="w", padx=2, pady=2)
    game_main_button = Button(roots, text="OK", borderwidth=2, relief=GROOVE, bg="#32ADCF", padx=20,command=main_Window)

    game_main_button.pack(anchor="nw", padx=2, pady=2)
    roots.bind("<Return>", lambda e: main_Window())
    roots.mainloop()



