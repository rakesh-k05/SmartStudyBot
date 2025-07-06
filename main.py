import logging
import os
from modules import summarize, tts, resource_fetcher, question_recommender, usage_guide

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_user_choice():
    """
    Get the user choice from environment variable or use default for non-interactive.
    """
    return os.getenv('USER_CHOICE', '1')  # Default to '1' if no environment variable

def main():
    """
    Main function to start the SmartStudyBot application.
    """
    logging.info("🤖 Welcome to SmartStudyBot!")
    logging.info("1. Summarize a topic")
    logging.info("2. Get study resources")
    logging.info("3. Practice questions")
    logging.info("4. Hear a response")
    logging.info("5. Help!")

    # Get the user choice
    choice = get_user_choice()

    logging.info(f"User chose option {choice}")

    if choice == "1":
        topic = os.getenv('TOPIC', 'Python Programming')  # Default topic
        summary = summarize.generate_summary(topic)
        logging.info("\n🔎 Summary:\n%s", summary)

    elif choice == "2":
        topic = os.getenv('TOPIC', 'Machine Learning')  # Default topic
        links = resource_fetcher.fetch_resources(topic)
        logging.info("\n📚 Study Resources:")
        for link in links:
            logging.info("%s", link)

    elif choice == "3":
        subject = os.getenv('SUBJECT', 'python')  # Default subject
        question_recommender.ask_questions(subject)

    elif choice == "4":
        text = os.getenv('TEXT_TO_SPEAK', 'Hello, this is SmartStudyBot!')  # Default text
        tts.speak(text)

    elif choice == "5":
        usage_guide.show_help()

    else:
        logging.error("❌ Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
