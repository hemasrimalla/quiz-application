"""CLI Quiz Application

Loads questions from a JSON file, asks them in random order, validates
answers, calculates the score and prints a final summary.
"""

import json
import random
import sys
from pathlib import Path

QUESTIONS_FILE = Path(__file__).parent / "questions.json"
LABELS = ["A", "B", "C", "D", "E", "F"]


def load_questions(filepath):
    """Load and validate questions from a JSON file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            questions = json.load(file)
    except FileNotFoundError:
        sys.exit(f"Error: '{filepath}' not found.")
    except json.JSONDecodeError as error:
        sys.exit(f"Error: invalid JSON in '{filepath}': {error}")

    if not isinstance(questions, list) or not questions:
        sys.exit("Error: the questions file must contain a non-empty list.")

    for number, item in enumerate(questions, start=1):
        if not all(key in item for key in ("question", "options", "answer")):
            sys.exit(f"Error: question {number} is missing required fields.")
    return questions


def get_valid_answer(valid_choices):
    """Keep asking until the user enters a valid option letter."""
    while True:
        choice = input(f"Your answer ({'/'.join(valid_choices)}): ").strip().upper()
        if choice in valid_choices:
            return choice
        print(f"  Invalid input. Please enter one of: {', '.join(valid_choices)}.")


def ask_question(number, total, item):
    """Display one question, return (is_correct, user_choice)."""
    print(f"\nQuestion {number}/{total}")
    print(item["question"])

    labels = LABELS[: len(item["options"])]
    for label, option in zip(labels, item["options"]):
        print(f"  {label}. {option}")

    choice = get_valid_answer(labels)
    correct = choice == item["answer"].upper()

    if correct:
        print("  Correct!")
    else:
        print(f"  Wrong. The correct answer is {item['answer'].upper()}.")
    return correct, choice


def get_grade(percentage):
    """Return a short feedback message for the score."""
    if percentage >= 90:
        return "Excellent!"
    if percentage >= 70:
        return "Good job!"
    if percentage >= 50:
        return "Not bad, keep practicing!"
    return "Needs improvement. Try again!"


def show_summary(score, total, wrong_items):
    """Print the final result summary."""
    percentage = (score / total) * 100
    print("\n" + "=" * 40)
    print("           FINAL RESULT")
    print("=" * 40)
    print(f"Total questions : {total}")
    print(f"Correct answers : {score}")
    print(f"Wrong answers   : {total - score}")
    print(f"Score           : {score}/{total} ({percentage:.1f}%)")
    print(f"Feedback        : {get_grade(percentage)}")

    if wrong_items:
        print("\nQuestions to review:")
        for item in wrong_items:
            print(f"  - {item['question']}")
            print(f"    Correct answer: {item['answer'].upper()}")
    print("=" * 40)


def run_quiz(questions):
    """Run one full round of the quiz."""
    shuffled = random.sample(questions, len(questions))  # randomized order
    score = 0
    wrong_items = []

    for number, item in enumerate(shuffled, start=1):
        correct, _ = ask_question(number, len(shuffled), item)
        if correct:
            score += 1
        else:
            wrong_items.append(item)

    show_summary(score, len(shuffled), wrong_items)


def main():
    questions = load_questions(QUESTIONS_FILE)

    print("=" * 40)
    print("      WELCOME TO THE PYTHON QUIZ")
    print("=" * 40)
    print(f"This quiz has {len(questions)} questions. Answer with A, B, C or D.")

    while True:
        input("\nPress Enter to start...")
        run_quiz(questions)
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nQuiz interrupted. Goodbye!")
