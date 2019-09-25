
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
            comment = parsed_json[a]["comments"]
            self.QuestionGenerator(
                question, image, answers, correctAnswer, comment)

        for x in range(0, random.randrange(0, 100)):
            random.shuffle(questionArray)

        self.askQuestions()

    def QuestionGenerator(self, question, image, answers, correctAnswer, comment):
        question = {
            "question": question,
            "image": image,
            "answers": answers,
            "correctAnswer": correctAnswer,
            "comments": comment
        }
        questionArray.append(question)

    def ShowChoice(self):
        global questionsAnswered
        questionsAnswered += 1
        if answers[v.get()].lower() == correctAnswer.lower():
            print("correct")
            global score
            score += 1
            for rb in rbs:
                rb.destroy()
        else:
            print("wrong")
            for rb in rbs:
                rb.destroy()

    def askQuestions(self):

        img = canvas.create_image(
            150, 150, image=None, anchor='nw')

        questionText = canvas.create_text(
            250, 400, text="", font=("Arial", 12))

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

            # questionArray.remove(questionDict)
            canvas.wait_variable(v)

            # a = answer.lower()
            # if a == "quit":
            #     exit()
            # elif a == correctAnswer:
            #     print(correctAnswer + " is correct!")
            #     global score
            #     score += 1
            #     print(str(score) + "/15")
            # else:
            #     print("Incorrect, The correct answer is: " + correctAnswer)

        if questionsAnswered == len(questionArray):
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("-------Final Score: " + str(score) + "/15------")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


if __name__ == "__main__":
    Main()
