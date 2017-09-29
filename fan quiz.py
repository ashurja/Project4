# Jamshed Ashurov
# 09/29/2017
# fan quiz.py
# This program creates a Pirates of Caribbean: Dead Man Tell No Tales quiz!

print("Welcome to the Pirates of the Caribbean: Dead Man Tell No Tales quiz!")
print("Get ready,because you are about to use your brain like you never did!")
print("Let's go!")


def question_1():
    """
    This function aks a multiple choice question from the user
    :return:
    """
    print("1) What is the name of the villain that wants to kill Captain Sparrow? Please enter a letter")
    print("a) Orlando Bloom")
    print("b) Will Smith")
    print("c) His son")
    print("d) Salazar")
    villain = input()
    if villain == "d":
        print("Correct!")
        return 1
    else:
        print("Wrong answer! The correct answer is d) Salazar.")
        return 0


def question_2():
    """
    This function asks a multiple choice question from the user returning 1 for correct and 0 for wrong answer
    :return:
    """
    print("2) What was the object that kept Jack safe from Salazar? Please enter a letter")
    print("a) Knife")
    print("b) Compass")
    print("c) Hat")
    print("d) Mustache")
    safe_object = input()
    if safe_object == "b":
        print("Correct! Good Work.")
        return 1
    else:
        print("Wrong answer! The correct answer is b) Compass.")
        return 0


def question_3():
    """
    This function asks an open ended question from the user returning 1 for correct and 0 for wrong answer
    :return:
    """
    print("3) How many children does Barborossa have? Please enter an integer")
    number = input()
    if int(number) == 1:
        print("Correct! Good Work.")
        return 1
    else:
        print("Wrong answer! The correct answer is 1.")
        return 0


def question_4():
    """
    This function asks the user the true or false question returning 1 for correct and 0 for wrong answer
    :return:
    """
    print("4) True or False: Barborossa dies at the end of the movie. Please print 1 for True and 0 for False")
    answer = input()
    if int(answer) == 1:
        print("Correct! Good Work.")
        return 1
    else:
        print("Wrong answer! The correct answer is True ")
        return 0


def question_5():
    """
    This function aks a multiple choice question from the user returning 1 for correct and 0 for wrong answer
    :return:
    """
    print("5) Who is Barborossa's daughter? Please enter a letter")
    print("a) Carina Smyth")
    print("b) Elizabeth Swan")
    print("c) Haifaa Meni")
    print("d) Angelica")
    daughter = input()
    if daughter == "a":
        print("Correct! Good Work.")
        return 1
    else:
        print("Wrong answer! The correct answer is a) Carina Smyth.")
        return 0


def question_6():
    """
    This function asks the user the true or false question returning 1 for correct and 0 for wrong answer
    :return:
    """
    print("6) True or False: Jack Sparrow kills Salazar. Please print 1 for True and 0 for False")
    answer = input()
    if int(answer) == 0:
        print("Correct! Good Work.")
        return 1
    else:
        print(" Wrong answer! The correct answer is False.")
        return 0


def question_7():
    """
    This function asks an open ended question from the user returning 1 for correct and 0 for wrong answer
    :return:
    """
    print("7) How many children does Will Turner have? Please enter an integer")
    number = input()
    if int(number) == 1:
        print("Correct! Good Work.")
        return 1
    else:
        print("Wrong answer! The correct answer is 1.")
        return 0


def question_8():
    """
    This function aks a multiple choice question from the user returning 1 for correct and 0 for wrong answer
    :return:
    """
    print("8) Who kills Salazar? Please enter a letter")
    print("a) Carina Smyth")
    print("b) Will Turner")
    print("c) Henry Turner")
    print("d) Barborossa")
    killer = input()
    if killer == "d":
        print("Correct! Good Work.")
        return 1
    else:
        print("Wrong answer! The correct answer is a) Carina Smyth.")
        return 0


def question_9():
    """
    This function aks a multiple choice question from the user returning 1 for correct and 0 for wrong answer
    :return:
    """
    print("9) What was the name of the cursed ship that Will Turner was in? Please enter a letter")
    print("a) Black Pearl")
    print("b) Flying Dutch")
    print("c) Devil's Triangle")
    print("d) Trident of Pasidon")
    ship = input()
    if ship == "b":
        print("Correct! Good Work.")
        return 1
    else:
        print("Wrong answer! The correct answer is a) Carina Smyth.")
        return 0


def question_10():
    """
    This function asks the user the true or false question returning 1 for correct and 0 for wrong answer
    :return:
    """
    print("10) Jack Sparrow decided to stop being a pirate. Please print 1 for True and 0 for False")
    answer = input()
    if int(answer) == 0:
        print("Correct! Good Work.")
        return 1
    else:
        print(" Wrong answer! The correct answer is False.")
        return 0


def main():
    point_1 = question_1()
    point_2 = question_2()
    point_3 = question_3()
    point_4 = question_4()
    point_5 = question_5()
    point_6 = question_6()
    point_7 = question_7()
    point_8 = question_8()
    point_9 = question_9()
    point_10 = question_10()
    result = point_1 + point_2 + point_3 + point_4 + point_5 + point_6 + point_7 + point_8 + point_9 + point_10
    print("Congratulations! You scored", result, "out of 10")
    if int(result) <= 4:
        print("It seems like you are not much of Pirates of Caribbean fan")
    elif result <= 7:
        print("Good work! Looks like you are fan of Pirates of Caribbean")
    else:
        print("You are the true fan of the movie")

main()
