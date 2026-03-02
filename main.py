from js import document, localStorage
#localStorage, used to store items if you are still in a website, used in storing the section for the players, learned through w3schools
def PASS(e):
    User = str(document.getElementById("Name").value)
    Pass = str(document.getElementById("Pass").value)

    if any(User) and any(Pass):
        if len(User)>=7: #Checks if its less than 7 chars
            if len(Pass) >=10: #checks if the passwors is less than 10
                if Pass.isalnum() == True: #checks if it is not a special character to not interfere with code
                    if Pass.isdigit() == False:#checks if there are letters
                        if Pass.isalpha() == False: #checks if there are numbers
                            Respo = f"""Thank you {User}, you are now logged in"""
                        else:
                            Respo = "Please enter a number"
                    else:
                        Respo = "Please input a letter"
                else:
                    Respo = "Error: Special Characters"
            else:
                Respo = "The minimum requirement of character for a password is 10 "
        else:
            Respo = "7 is the minimum requirement of characters for a username"
    else:
        Respo = "Please input something first"
    document.getElementById("Respo").innerText = Respo
    print("")


def GET_TEAM(e):
    Reg = str(document.getElementById("Registered").value) #To get the value of each input, we must use get element by Id, and to ensure everything is the right value we have to put str to convert the value into a string
    Med = str(document.getElementById("Medic").value)
    Sec = str(document.getElementById("Section").value)
    Lev = str(document.getElementById("Grade").value)
    localStorage.setItem("section", Sec) #Used to store something specific inside the localStorage

    if Reg == "yes":#first if condition is to check if you are registered, most important
        if Med == "yes":
            if Sec == "Emerald":
                if Lev == "Grade7":
                    Ans = "Dear Grade 7 Student, You are in Blue Bears"
                elif Lev == "Grade8":
                    Ans = "Dear Grade 8 Student, You are in Blue Bears"
                elif Lev == "Grade9":
                    Ans = "Dear Grade 9 Student, You are in Blue Bears"
                elif Lev == "Grade10":
                    Ans = "Dear Grade 10 Student, You are in Blue Bears"
                pass # the pass condition is used to end the if statement as a way to not break codes
            elif Sec == "Ruby":
                if Lev == "Grade7":
                    Ans = "Dear Grade 7 Student, You are in Red Bulldogs"
                elif Lev == "Grade8":
                    Ans = "Dear Grade 8 Student, You are in Red Bulldogs"
                elif Lev == "Grade9":
                    Ans = "Dear Grade 9 Student, You are in Red Bulldogs"
                elif Lev == "Grade10":
                    Ans = "Dear Grade 10 Student, You are in Red Bulldogs"
                pass
            elif Sec == "Sapphire":
                if Lev == "Grade7":
                    Ans = "Dear Grade 7 Student, You are in Green Hornets"
                elif Lev == "Grade8":
                    Ans = "Dear Grade 8 Student, You are in Green Hornets"
                elif Lev == "Grade9":
                    Ans = "Dear Grade 9 Student, You are in Green Hornets"
                elif Lev == "Grade10":
                    Ans = "Dear Grade 10 Student, You are in Green Hornets"
                pass
            elif Sec == "Topaz":
                if Lev == "Grade7":
                    Ans = "Dear Grade 7 Student, You are in Yellow Tigers"
                elif Lev == "Grade8":
                    Ans = "Dear Grade 8 Student, You are in Yellow Tigers"
                elif Lev == "Grade9":
                    Ans = "Dear Grade 9 Student, You are in Yellow Tigers"
                elif Lev == "Grade10":
                    Ans = "Dear Grade 10 Student, You are in Yellow Tigers"
                pass
            elif Sec == "Jade":
                if Lev == "Grade7":
                    Ans = "Dear Grade 7 Student, You are in Yellow Tigers"
                elif Lev == "Grade8":
                    Ans = "Dear Grade 8 Student, You are in Red Bulldogs"
                elif Lev == "Grade9":
                    Ans = "Dear Grade 9 Student, You are in Green Hornets"
                elif Lev == "Grade10":
                    Ans = "Dear Grade 10 Student, You are in Blue Bears"
                pass
            pass
        elif Med == "no":
            Ans = "Please Get Checked Up"
        else:
            Ans = "Please Answer Properly"
    elif Reg == "no":
        Ans = "Please Register First"
    else:
        Ans = "Please Answer Properly"#This is here if you did anything wrong with the selector
    
    document.getElementById("ANSWER").innerText = Ans
    print("")

def PLAYER(e):

    Sec = localStorage.getItem("section")  #used in retriving the stored item from the local storage

    if Sec == "":
        players = "Please go to the previous page and get a team"
    elif Sec == "Ruby":
        players = f"""
        Ethan Belsa\n
        Judah Judge\n
        Ely Defensor\n
        """
    elif Sec =="Emerald":
        players = f"""
        Jairo Agudo\n
        Lucas Reyes\n
        Shia Cruz\n
        """
    elif Sec == "Sapphire":
        players = f"""
        Rohann Cruz\n
        Terd David\n
        Liam Lopez\n
        """
    elif Sec == "Topaz":
        players = f"""
        Jarix Zales\n
        Alfred Taruc\n
        Gio Escardo\n
        """
    elif Sec == "Jade":
        players = f"""
        Jarix Zales\n
        Alfred Taruc\n
        Gio Escardo\n
        """
    else:
        players="Select a team first"
    
    document.getElementById("players").innerText = players

    print("")

