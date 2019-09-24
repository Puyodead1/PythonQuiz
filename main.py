
import json
import random
from createQuestionData import createQuestions


# All questions from https://chartcons.com/100-general-trivia-questions-answers/

questionArray = []
score = 0


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
            answers = parsed_json[a]["answers"]
            correctAnswer = parsed_json[a]["correctAnswer"]
            comment = parsed_json[a]["comments"]
            self.QuestionGenerator(question, answers, correctAnswer, comment)

        for x in range(0, random.randrange(0, 100)):
            random.shuffle(questionArray)

        self.askQuestions()

    def QuestionGenerator(self, question, answers, correctAnswer, comment):
        question = {
            "question": question,
            "answers": answers,
            "correctAnswer": correctAnswer,
            "comments": comment
        }
        questionArray.append(question)

    def askQuestions(self):
        print("Type 'quit' at any time to exit.")
        for questionDict in questionArray:
            isCorrect = None
            question = questionDict["question"]
            answers = questionDict["answers"]
            correctAnswer = questionDict["correctAnswer"].lower()

            print(question)

            for x in answers:
                print("- " + x)

            answer = input("> ")

            a = answer.lower()
            if a == "quit":
                exit()
            elif a == correctAnswer:
                print(correctAnswer + " is correct!")
                global score
                score += 1
                print(str(score) + "/15")
            else:
                print("Incorrect, The correct answer is: " + correctAnswer)

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("-------Final Score: " + str(score) + "/15------")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


if __name__ == "__main__":
    Main()
