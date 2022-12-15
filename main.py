from Test import Test

questions =[
    "1) When I do well in school or I pass an exam it is because it was easy.",
    "2) If I fail an exam that doesn't motivate me to learn for other exams.",
    "3) 'The right man at the right place' is the recipe for success.",
    "4) Participating in political meetings is usually ineffective, no one takes them into account.",
    "5) Intelligence is a skill you are born with, not a skill you can learn.",
    "6) Success is due to luck, not our abilities.",
    "7) The impression that people form about you depends on them and them alone and you can't do anything to change it.",
    "8) If you're going to get sick, you're going to get sick anyway and there's not much you can do about it.",
    "9) You can't escape destiny.",
    "10) If there is a soulmate somewhere in the world he/she will find you, it was written in the stars."
]

TheQuestions = [
    Test(questions[0], "1", "2", "3", "4"),
    Test(questions[1], "1", "2", "3", "4"),
    Test(questions[2], "1", "2", "3", "4"),
    Test(questions[3], "1", "2", "3", "4"),
    Test(questions[4], "1", "2", "3", "4"),
    Test(questions[5], "1", "2", "3", "4"),
    Test(questions[6], "1", "2", "3", "4"),
    Test(questions[7], "1", "2", "3", "4"),
    Test(questions[8], "1", "2", "3", "4"),
    Test(questions[9], "1", "2", "3", "4")
]

def run_test(Orice):
    score = 0
    for question in Orice:
        tst = 0
        while tst == 0:
            ans = input(question.prompt+"\n(1)Strongly disagree (2)Disagree (3)Agree (4)Strongly agree\n\n")
            if ans == "1" or ans == "2" or ans == "3" or ans == "4":
                tst = 1
            else:
                tst = 0
                print("Enter a valid answer (Example: 1 / 2 / 3 / 4)")

        if ans == question.answer1:
            score += 1
        elif ans == question.answer2:
            score += 2
        elif ans == question.answer3:
            score += 3
        elif ans == question.answer4:
            score += 4

    if score <= 15:
        print("Your psychological attribution style is: INTERNAL")
        info= input("Do you want to see some information about the INTERNAL attribution style? (Yes/No?)")
        if info.upper() == "YES":
            print("\nPeople with an internal attribution style are rarely prone to the feeling of learned helplessness that can be associated with certain different psychological disorders such as:")
            print( "depression, anxiety, loneliness or shyness.")
            print("They tend to succeed from an academic point of view, they search for information more actively and treat it more pertinently.")
            print("They have a level of aspirations that increases in case of success,but decreases in case of failure.")
            print("People with this attribution style tend to be involved in professional projects.")
            print("Internal subjects are less sensitive to social influences and control their emotional life better (they are less disturbed by stressful situations).")
        else:
            print("\nThank you very much for taking this test! ^.^")
    elif score <25:
        print("Your psychological attribution style is: MIXED (Both INTERNAL and EXTERNAL)")
        info = input("Do you want to see some information about the MIXED attribution style? (Yes/No?)")
        if info.upper() == "YES":
            print("\nPeople with a mixed attribution style are moderately prone to the feeling of learned helplessness that can be associated with certain different psychological disorders such as:")
            print("depression, anxiety, loneliness, shyness.")
            print("People with this attribution style have a level of aspirations that increases in the case of success and does not decrease in the case of failure.")
            print("The level of aspirations of people with an internal attribution style decreases when they encounter failure.")
            print("People with the mixed attribution style tend to be less disturbed in stressful situations and sometimes they can even control their emotions.")
            print("Usually this type of people are optimistic, but there are cases in which they tend to think only the worst outcome of a situation.")
    else:
        print("Your psychological attribution style is: EXTERNAL")
        info = input("Do you want to see some information about the EXTERNAL attribution style? (Yes/No?)")
        if info.upper() == "YES":
            print("\nPeople with an external attributional style are very prone to the feeling of learned helplessness that can be associated with certain different psychological disorders such as:")
            print("depression, anxiety, loneliness, shyness and suffer from more phobias than people with an internal/mixed attributional style.")
            print("People with the external attribution style tend to believe that their failures are due to external factors")
            print("(Ex: Poor test results are due to the fact that the tests were hard, not that the student did not learn.)")
            print("Althogh, external style people have a level of aspirations that increases in the case of success and does not decrease in the case of failure, something that happens to people with an internal style.")
            print("External subjects are more sensitive to social influences and have weaker control regarding their emotional life (they are more disturbed by stressful situations).")

run_test(TheQuestions)
