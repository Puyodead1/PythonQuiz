import json

# This file is only for creating the data.json file


def createQuestions():
    questions = (
        "Who invented the telephone?",
        "Which nail grows fastest?",
        "What tempature does water boil at?",
        "Who discovered penicilin?",
        "What Spanish artist said he would eat his wife when she died?",
        "Who wrote Julius Caesar, Macbeth, and Hamlet?",
        "Who wrote Lazarillo de Tormes?",
        "What did the crocodile swallow in Peter Pan?",
        "Where was Lope de Vega born?",
        "Who did Lady Diana Spencer marry?",
        "Where is Mulhacen?",
        "How many states are there in the United States of America?",
        "Which river passes through Madrid?",
        "Which German city is famous for the perfume it produces?",
        "Who did Prince Rainier of Monaco Marry?",
    )

    answers = (
        ("Henry Bessemer", "Alexander Graham Bell", "Nikola Tesla", "Donald Trump"),
        ("Thumb", "Index", "Middle", "Pinky"),
        ("75C", "7F", "75F", "100C"),
        ("Fleming", "Florey", "Koch", "Eintoven"),
        ("Picasso", "Dali", "Van Gogh", "Changall"),
        ("Shakespeare", "Mark Twain", "Mr.Nelson", "Einstein"),
        ("Rick Riordan", "J.K. Rowling", "Anonymous", "Guy Fieri"),
        ("Alarm Clock", "Tooth Brush", "Book", "Toy Train"),
        ("Paris", "Turky", "Guatemala", "Madrid"),
        ("Prince", "Prince Andrew", "Prince Charles", "Prince Harry"),
        ("Granada Spain", "Wales", "Brazil", "Russia"),
        ("39", "50", "40", "33"),
        ("Nile", "Amazon", "Manzanares", "Mississippi"),
        ("Clogne", "Berlin", "Bonn", "Munich"),
        ("Marilyn Monroe", "Grace Kelly", "Queen Elizabeth II", "Ronda Rousey")
    )

    correctAnswers = (
        "Alexander Graham Bell",
        "Middle",
        "100C",
        "Fleming",
        "Dali",
        "Shakespeare",
        "Anonymous",
        "Alarm Clock",
        "Madrid",
        "Prince Charles",
        "Granada Spain",
        "50",
        "Manzanares",
        "Clogne",
        "Grace Kelly"
    )

    comments = (
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
        ("a", "https://google.com"),
    )

    a = {}
    for i in range(0, len(questions)):
        x = {
            "question": questions[i],
            "answers": answers[i],
            "correctAnswer": correctAnswers[i],
            "comments": comments[i]
        }
        a[i] = x
    with open("data.json", 'w') as f:
        json.dump(a, f)
