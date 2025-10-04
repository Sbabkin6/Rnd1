

questions = [
    {
        "prompt": "What is NOT an example of an early Christian sect?",
        "options": ["A. Arianism", "B. Gnosticism", "C. Docetism", "D. Presbyterianism"],
        "answer": "D"
    },
    {
        "prompt": "Who was the king of France during the French Revolution?",
        "options": ["A. Louis XX", "B. Adrianople III", "C. Louis XVI", "D. Henry II (Henry the Forgotten)"],
        "answer": "C"
    },
    {
        "prompt": "Alexander the Great's empire split into several rival kingdoms after his death. Who did NOT inherit part of his empire?",
        "options": ["A. Ptolemy", "B. Cassander", "C. Lysimachus", "D. Phillip"],
        "answer": "D"
    }
]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter you answer (A, D, C, or D)")
        if answer == question["answer"]:
            print("Very Nice :D\n")
            score += 1
        else:
            print("This is wrong. The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")
    total = len(questions)
    percentage = (score / total) * 100
    print(f"Your score is: {percentage:.2f}%.")

run_quiz(questions)


# print(f"for a score of {print(percentage)}")