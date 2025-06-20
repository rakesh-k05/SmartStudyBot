import json
import random

def ask_questions(subject):
    try:
        with open(f"data/questions/{subject}.json", "r") as file:
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
