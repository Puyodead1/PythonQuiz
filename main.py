
import json
import random
from createQuestionData import createQuestions
from tkinter import *
from PIL import Image
from PIL import ImageTk


# All questions from https://chartcons.com/100-general-trivia-questions-answers/

questionArray = []
score = 0
questionsAnswered = 0

tk = Tk()
tk.title("PythonQuiz")
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
v = IntVar()
v.set(1)
rbs = []
answers = []
correctAnswer = ""


class Main():

    # Reads the data.json file (auto created) and loads questions, answers, picture locations, correct answer
    def __init__(self):
        # Generate the data.json file
        createQuestions()

        parsed_json = None
        with open("data.json", 'r') as f:
            parsed_json = json.load(f)
            f.close()

        for a in range(0, len(parsed_json)):
            a = str(a)
            question = parsed_json[a]["question"]
            image = parsed_json[a]["image"]
            answers = parsed_json[a]["answers"]
            correctAnswer = parsed_json[a]["correctAnswer"]
            self.QuestionGenerator(
                question, image, answers, correctAnswer)

        # shuffle the question array
        for x in range(0, random.randrange(0, 100)):
            random.shuffle(questionArray)

        # ask questions after question data is loaded
        self.askQuestions()

    # used for creating the array of questions
    def QuestionGenerator(self, question, image, answers, correctAnswer):
        question = {
            "question": question,
            "image": image,
            "answers": answers,
            "correctAnswer": correctAnswer
        }
        questionArray.append(question)

    # Callback for radiobutton answer click, handles score, removes old radio buttons and questions answered
    def ShowChoice(self):
        global questionsAnswered
        questionsAnswered += 1
        if answers[v.get()].lower() == correctAnswer.lower():
            print("correct") # kinda debug but kinda useful to keep enabled as it shows if the answer is right or wrong before seeing score
            global score
            score += 1
            for rb in rbs:
                rb.destroy()
        else:
            print("wrong") # kinda debug but kinda useful to keep enabled as it shows if the answer is right or wrong before seeing score
            for rb in rbs:
                rb.destroy()

    # function to create UI widgets that are presented to the user
    # waiting for button press reference: https://stackoverflow.com/questions/44790449/making-tkinter-wait-untill-button-is-pressed
    def askQuestions(self):

        img = canvas.create_image(
            150, 150, image=None, anchor='nw')

        questionText = canvas.create_text(
            250, 400, text="", font=("Arial", 12))

        # loops the questions in the array
        for questionDict in questionArray:
            global correctAnswer
            global answers
            isCorrect = None
            question = questionDict["question"]
            answers = questionDict["answers"]
            correctAnswer = questionDict["correctAnswer"].lower()

            image = Image.open(questionDict["image"])
            image = image.resize((196, 186))
            image = ImageTk.PhotoImage(image)
            canvas.itemconfig(img, image=image)
            canvas.itemconfig(questionText, text=question)

            # radio buttons defined seperatly due to issues with freezing
            rb = Radiobutton(tk,
                             text=answers[0],
                             padx=20,
                             variable=v,
                             value=0,
                             command=self.ShowChoice)

            rb1 = Radiobutton(tk,
                              text=answers[1],
                              padx=20,
                              variable=v,
                              value=1,
                              command=self.ShowChoice)

            rb2 = Radiobutton(tk,
                              text=answers[2],
                              padx=20,
                              variable=v,
                              value=2,
                              command=self.ShowChoice)

            rb3 = Radiobutton(tk,
                              text=answers[3],
                              padx=20,
                              variable=v,
                              value=3,
                              command=self.ShowChoice)
            rb.pack()
            rb1.pack()
            rb2.pack()
            rb3.pack()
            rbs.append(rb)
            rbs.append(rb1)
            rbs.append(rb2)
            rbs.append(rb3)

            # wait for a radio button to be pressed, then move on to next question
            canvas.wait_variable(v)
        # if the questions answered is the same as the max quesions, show the score
        if questionsAnswered == len(questionArray):
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("-------Final Score: " + str(score) + "/15------")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


if __name__ == "__main__":
    Main()
