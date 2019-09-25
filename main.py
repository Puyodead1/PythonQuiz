
import json
import random
from createQuestionData import createQuestions
from tkinter import *
from PIL import Image
from PIL import ImageTk


# All questions from https://chartcons.com/100-general-trivia-questions-answers/

questionArray = []
score = 0

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
        for rb in rbs:
            rb.destroy()

        if answers[v.get()].lower() == correctAnswer.lower():
            print("correct")
        else:
            print("wrong")

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

            for answerText in answers:
                rb = Radiobutton(tk,
                                 text=answerText,
                                 padx=20,
                                 variable=v,
                                 value=answers.index(answerText),
                                 command=self.ShowChoice)
                rb.pack()
                rbs.append(rb)

                # TODO: wait for the first question to be answered

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

        # print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        # print("-------Final Score: " + str(score) + "/15------")
        # print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        mainloop()


if __name__ == "__main__":
    Main()
