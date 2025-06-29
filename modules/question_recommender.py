import json
import random

def ask_questions(subject):
    """
    Displays a multiple-choice quiz to the user based on the given subject.

    The function attempts to load a list of questions from a JSON file located
    at 'data/questions/{subject}.json' using UTF-8 encoding. If the file is found,
    it selects the first 5 questions after shuffling and presents them one by one
    to the user. The user inputs their answer, and the function provides feedback
    and tracks the score.

    Parameters:
        subject (str): The name of the subject whose questions will be loaded.

    Returns:
        None
    """

    try:
        with open(f"data/questions/{subject}.json", encoding="utf-8") as file:
            questions = json.load(file)
    except FileNotFoundError:
        print("Subject not found.")
        return

    random.shuffle(questions)
    score = 0

    for q in questions[:5]:
        print("\n❓", q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"  {i}. {option}")
        answer = input("Enter your choice (1-4): ")
        if q["options"][int(answer) - 1] == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Incorrect! Correct answer:", q["answer"])

    print(f"\n📊 Your Score: {score}/5")
