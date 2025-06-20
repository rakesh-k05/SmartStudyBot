from modules import summarize, tts, resource_fetcher, question_recommender

def main():
    print("🤖 Welcome to SmartStudyBot!")
    print("1. Summarize a topic")
    print("2. Get study resources")
    print("3. Practice questions")
    print("4. Hear a response")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        topic = input("Enter topic: ")
        summary = summarize.generate_summary(topic)
        print("\n🔎 Summary:\n", summary)

    elif choice == "2":
        topic = input("Enter topic: ")
        links = resource_fetcher.fetch_resources(topic)
        print("\n📚 Study Resources:")
        for link in links:
            print("-", link)

    elif choice == "3":
        subject = input("Enter subject (python/dsa): ").lower()
        question_recommender.ask_questions(subject)

    elif choice == "4":
        text = input("Enter what you want to hear: ")
        tts.speak(text)

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
