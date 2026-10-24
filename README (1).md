# CLI Quiz Application

A command-line quiz application built in Python. It loads questions from a JSON file, asks them in random order, accepts and validates answers, calculates the score, and displays a final result summary.

**Veda Technology – Python Programming Track | Level 1 | Task 24 (Day 24)**

## Features

- Questions stored separately in `questions.json` (data is separate from program logic)
- 12 multiple-choice questions (minimum requirement: 10)
- Randomized question order on every run
- Input validation: invalid answers are rejected and re-asked
- Instant feedback after every question
- Final summary with score, percentage, feedback and a list of questions to review
- Play-again option and graceful handling of `Ctrl+C`
- Error handling for a missing or malformed JSON file

## Tools Used

- Python 3
- JSON (`json` module)

## Project Structure

```
cli-quiz-app/
├── quiz.py          # Main program
├── questions.json   # Quiz questions (data file)
├── README.md
└── .gitignore
```

## How to Run

1. Make sure Python 3.8+ is installed:
   ```bash
   python --version
   ```
2. Clone the repository and move into it:
   ```bash
   git clone https://github.com/hemasrimalla/cli-quiz-app.git
   cd cli-quiz-app
   ```
3. Run the quiz:
   ```bash
   python quiz.py
   ```

## Sample Output

```
========================================
      WELCOME TO THE PYTHON QUIZ
========================================
This quiz has 12 questions. Answer with A, B, C or D.

Question 1/12
Which keyword is used to define a function in Python?
  A. func
  B. def
  C. function
  D. define
Your answer (A/B/C/D): b
  Correct!

...

========================================
           FINAL RESULT
========================================
Total questions : 12
Correct answers : 10
Wrong answers   : 2
Score           : 10/12 (83.3%)
Feedback        : Good job!
========================================
```

## Adding Your Own Questions

Edit `questions.json` and add an entry in this format:

```json
{
  "question": "Your question here?",
  "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
  "answer": "B"
}
```

`answer` is the letter (A, B, C, D) of the correct option. No change to `quiz.py` is needed.

## Concepts Practiced

- Dictionaries and lists
- Loops and conditionals
- Functions and application flow
- File handling and JSON parsing
- Input validation and error handling

## Interview Questions

**How would you store quiz questions?**
In a JSON file as a list of dictionaries, each with a question, options, and the correct answer.

**Why separate data from program logic?**
Questions can be added or edited without touching the code, which makes the program easier to maintain, test, and reuse.

**How would you randomly select questions?**
Use `random.sample(questions, n)` to pick `n` unique questions, or `random.shuffle()` to reorder the whole list.

## Author

Malla Hemasri – [@hemasrimalla](https://github.com/hemasrimalla)
