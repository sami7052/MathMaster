import random
import time
import json
import os


def timed_input(question, timeout):
    return input(question)


def load_data():
    if os.path.exists("math_master_data.json"):
        try:
            with open("math_master_data.json", "r") as file:
                return json.load(file)
        except:
            print("⚠️ Could not load previous data.")

    return {
        "results": [],
        "badges": [],
        "high_score": 0
    }


def save_data(results, badges, high_score):
    data = {
        "results": results,
        "badges": badges,
        "high_score": high_score
    }

    try:
        with open("math_master_data.json", "w") as file:
            json.dump(data, file, indent=4)
    except:
        print("⚠️ Could not save data.")


def make_question(category, difficulty):
    if category == "1":
        # Addition and subtraction

        if difficulty == "1":
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)

        elif difficulty == "2":
            num1 = random.randint(20, 100)
            num2 = random.randint(10, 80)

        else:
            num1 = random.randint(50, 200)
            num2 = random.randint(20, 150)

        operation = random.choice(["+", "-"])

        if operation == "+":
            answer = num1 + num2
        else:
            answer = num1 - num2

        question = (
            "What is "
            + str(num1)
            + " "
            + operation
            + " "
            + str(num2)
            + "? "
        )

        return question, str(answer)

    elif category == "2":
        # Multiplication

        if difficulty == "1":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)

        elif difficulty == "2":
            num1 = random.randint(10, 50)
            num2 = random.randint(2, 20)

        else:
            num1 = random.randint(20, 100)
            num2 = random.randint(10, 50)

        answer = num1 * num2

        question = (
            "What is "
            + str(num1)
            + " * "
            + str(num2)
            + "? "
        )

        return question, str(answer)

    elif category == "3":
        # Powers

        if difficulty == "1":
            num = random.randint(2, 10)
            power = 2

        elif difficulty == "2":
            num = random.randint(3, 15)
            power = random.choice([2, 3])

        else:
            num = random.randint(5, 20)
            power = random.choice([2, 3])

        answer = num ** power

        question = (
            "What is "
            + str(num)
            + "^"
            + str(power)
            + "? "
        )

        return question, str(answer)

    return None, None


def generate_questions(difficulty, category):

    questions = []

    if category == "4":
        # Mixed Challenge

        categories = ["1", "2", "3"]

        for i in range(5):

            selected_category = random.choice(
                categories
            )

            question, answer = make_question(
                selected_category,
                difficulty
            )

            questions.append(
                (question, answer)
            )

        level = "Mixed Challenge"

    else:

        for i in range(5):

            question, answer = make_question(
                category,
                difficulty
            )

            if question is None:
                return None, None

            questions.append(
                (question, answer)
            )

        if category == "1":
            category_name = "Arithmetic"

        elif category == "2":
            category_name = "Multiplication"

        elif category == "3":
            category_name = "Powers"

        else:
            return None, None

        if difficulty == "1":
            difficulty_name = "Easy"

        elif difficulty == "2":
            difficulty_name = "Medium"

        elif difficulty == "3":
            difficulty_name = "Hard"

        else:
            return None, None

        level = (
            difficulty_name
            + " - "
            + category_name
        )

    return questions, level


def run_quiz(questions):

    score = 0

    for i, question_data in enumerate(
        questions,
        start=1
    ):

        question_text, correct_answer = question_data

        print(
            "\nQuestion",
            i,
            "of",
            len(questions)
        )

        answer = timed_input(
            question_text,
            15
        )

        if answer is None:

            print("⏱️ Time's up!")

            print(
                "The correct answer was:",
                correct_answer
            )

        elif answer.strip() == "":

            print(
                "Please enter an answer next time!"
            )

        elif not answer.strip().lstrip("-").isdigit():

            print(
                "Please enter a valid number."
            )

        elif answer.strip() == correct_answer:

            print(
                "✅ Correct! Well done!"
            )

            score = score + 1

        else:

            print(
                "❌ Incorrect. Try one more time!"
            )

            second_answer = input(
                "Your second chance: "
            )

            if second_answer.strip() == "":

                print(
                    "Please enter an answer."
                )

            elif not second_answer.strip().lstrip("-").isdigit():

                print(
                    "Please enter a valid number."
                )

            elif (
                second_answer.strip()
                == correct_answer
            ):

                print(
                    "✅ Correct! "
                    "You got it on your second try!"
                )

                score = score + 1

            else:

                print(
                    "❌ Incorrect again."
                )

                print(
                    "The correct answer was:",
                    correct_answer
                )

    return score


def show_statistics(results):

    print("\n📊 YOUR STATISTICS")
    print("===============================")

    if len(results) == 0:

        print("No attempts yet.")

        return

    total_attempts = len(results)

    total_score = 0
    total_percentage = 0
    best_score = 0

    for result in results:

        total_score = (
            total_score
            + result["score"]
        )

        total_percentage = (
            total_percentage
            + result["percentage"]
        )

        if result["score"] > best_score:

            best_score = result["score"]

    average_score = (
        total_score
        / total_attempts
    )

    average_percentage = (
        total_percentage
        / total_attempts
    )

    print(
        "Total Attempts:",
        total_attempts
    )

    print(
        "Best Score:",
        best_score,
        "/ 5"
    )

    print(
        "Average Score:",
        round(average_score, 2),
        "/ 5"
    )

    print(
        "Average Percentage:",
        round(average_percentage, 2),
        "%"
    )


def show_leaderboard(results):

    print("\n🏆 LEADERBOARD")
    print("===============================")

    if len(results) == 0:

        print("No scores yet.")

        return

    leaderboard = []

    for result in results:

        leaderboard.append(result)

    leaderboard.sort(
        key=lambda result:
        result["percentage"],
        reverse=True
    )

    for position, result in enumerate(
        leaderboard,
        start=1
    ):

        print(
            position,
            ".",
            result["difficulty"],
            "-",
            result["score"],
            "/ 5",
            "-",
            result["percentage"],
            "%"
        )


def show_achievements(badges):

    print("\n🏅 ACHIEVEMENTS")
    print("===============================")

    if len(badges) == 0:

        print(
            "No badges yet."
        )

        print(
            "Keep playing to unlock badges!"
        )

        return

    print(
        "Badges Earned:",
        len(badges)
    )

    print()

    for badge in badges:

        print(
            "🏅",
            badge
        )


def show_progress(results):

    print("\n📈 YOUR PROGRESS")
    print("===============================")

    if len(results) < 2:

        print(
            "You need at least 2 attempts "
            "to see your progress."
        )

        return

    total_percentage = 0

    for result in results:

        total_percentage = (
            total_percentage
            + result["percentage"]
        )

    current_average = (
        total_percentage
        / len(results)
    )

    previous_total = (
        total_percentage
        - results[-1]["percentage"]
    )

    previous_average = (
        previous_total
        / (len(results) - 1)
    )

    improvement = (
        current_average
        - previous_average
    )

    print(
        "Previous Average:",
        round(previous_average, 2),
        "%"
    )

    print(
        "Current Average:",
        round(current_average, 2),
        "%"
    )

    if improvement > 0:

        print(
            "Improvement: +",
            round(improvement, 2),
            "%"
        )

    elif improvement < 0:

        print(
            "Change:",
            round(improvement, 2),
            "%"
        )

    else:

        print(
            "No change: 0%"
        )

    print("\nAttempt History:")

    for attempt, result in enumerate(
        results,
        start=1
    ):

        print(
            "Attempt",
            attempt,
            ":",
            result["score"],
            "/ 5 -",
            result["percentage"],
            "%"
        )


def show_results(
    name,
    level,
    score,
    questions,
    high_score,
    results,
    badges
):

    if score > high_score:

        high_score = score

        print(
            "\n🏆 NEW HIGH SCORE!"
        )

    print("\n===============================")
    print("         QUIZ RESULTS")
    print("===============================")

    print(
        "Student:",
        name
    )

    print(
        "Difficulty:",
        level
    )

    print(
        "Your score:",
        score,
        "out of",
        len(questions)
    )

    percentage = (
        score / len(questions)
    ) * 100

    print(
        "Your percentage:",
        percentage,
        "%"
    )

    print(
        "Current High Score:",
        high_score,
        "/ 5"
    )

    if percentage >= 90:

        performance = "Excellent"

        print(
            "🏆 Excellent performance!"
        )

    elif percentage >= 70:

        performance = "Very Good"

        print(
            "⭐ Very good performance!"
        )

    elif percentage >= 50:

        performance = "Good"

        print(
            "👍 Good performance!"
        )

    else:

        performance = "Keep Practicing"

        print(
            "📚 Keep practicing. "
            "You can improve!"
        )

    results.append({
        "score": score,
        "percentage": percentage,
        "difficulty": level,
        "performance": performance
    })

    print("\n🏅 ACHIEVEMENTS")

    if (
        score == 5
        and "Perfect Score" not in badges
    ):

        badges.append("Perfect Score")

        print(
            "🥇 New Badge: Perfect Score!"
        )

    if (
        len(results) >= 5
        and "Persistent Learner" not in badges
    ):

        badges.append(
            "Persistent Learner"
        )

        print(
            "📚 New Badge: "
            "Persistent Learner!"
        )

    perfect_scores = 0

    for result in results:

        if result["score"] == 5:

            perfect_scores = (
                perfect_scores + 1
            )

    if (
        perfect_scores >= 3
        and "On Fire" not in badges
    ):

        badges.append("On Fire")

        print(
            "🔥 New Badge: On Fire!"
        )

    if (
        "Hard" in level
        and score == 5
        and "Hard Mode Master" not in badges
    ):

        badges.append(
            "Hard Mode Master"
        )

        print(
            "🧠 New Badge: "
            "Hard Mode Master!"
        )

    show_statistics(results)

    show_progress(results)

    show_leaderboard(results)

    return high_score


def save_report(
    name,
    high_score,
    results,
    badges
):

    try:

        with open(
            "math_master_report.txt",
            "w"
        ) as file:

            file.write(
                "====================================\n"
            )

            file.write(
                "      MATHMASTER PROGRESS REPORT\n"
            )

            file.write(
                "====================================\n"
            )

            file.write(
                "Student Name: "
                + name
                + "\n"
            )

            file.write(
                "Personal High Score: "
                + str(high_score)
                + " / 5\n"
            )

            file.write(
                "Total Attempts: "
                + str(len(results))
                + "\n"
            )

            file.write(
                "Total Badges: "
                + str(len(badges))
                + "\n\n"
            )

            file.write(
                "Badges Earned:\n"
            )

            if len(badges) == 0:

                file.write(
                    "  None yet\n"
                )

            else:

                for badge in badges:

                    file.write(
                        "  - "
                        + badge
                        + "\n"
                    )

            file.write(
                "\nDetailed History:\n\n"
            )

            for attempt, result in enumerate(
                results,
                start=1
            ):

                file.write(
                    "Attempt #"
                    + str(attempt)
                    + "\n"
                )

                file.write(
                    "Difficulty: "
                    + result["difficulty"]
                    + "\n"
                )

                file.write(
                    "Score: "
                    + str(result["score"])
                    + " / 5\n"
                )

                file.write(
                    "Percentage: "
                    + str(result["percentage"])
                    + "%\n"
                )

                file.write(
                    "Performance: "
                    + result["performance"]
                    + "\n\n"
                )

            file.write(
                "Keep on practicing!\n"
            )

    except:

        print(
            "⚠️ Could not save report."
        )


def show_menu(name):

    print("\n")
    print("==============================")
    print("        MATHMASTER")
    print("==============================")

    print(
        "\nWelcome,",
        name + "!"
    )

    print("\n1. 🧮 Start Quiz")
    print("2. 📊 View Statistics")
    print("3. 🏆 View Leaderboard")
    print("4. 🏅 View Achievements")
    print("5. 📈 View Progress")
    print("6. 🚪 Exit")

    print("==============================")


print("====================================")
print("      Welcome to MathMaster")
print("====================================")

name = input(
    "What is your name? "
).strip()

print(
    "\nHello",
    name
)

print(
    "Let's test your mathematics skills!"
)

data = load_data()

results = data["results"]
badges = data["badges"]
high_score = data["high_score"]

if len(results) > 0:

    print(
        "\n💾 Previous progress loaded!"
    )

    print(
        "Previous Attempts:",
        len(results)
    )

    print(
        "Previous High Score:",
        high_score,
        "/ 5"
    )


running = True

while running:

    show_menu(name)

    choice = input(
        "Choose an option: "
    ).strip()

    if choice == "1":

        print(
            "\nChoose your difficulty:"
        )

        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        difficulty = input(
            "Enter your choice: "
        ).strip()

        if difficulty not in ["1", "2", "3"]:

            print(
                "❌ Invalid difficulty."
            )

            continue

        print(
            "\nChoose a category:"
        )

        print("1. ➕ Addition & Subtraction")
        print("2. ✖️ Multiplication")
        print("3. 🔢 Powers")
        print("4. 🎲 Mixed Challenge")

        category = input(
            "Enter your choice: "
        ).strip()

        if category not in [
            "1",
            "2",
            "3",
            "4"
        ]:

            print(
                "❌ Invalid category."
            )

            continue

        questions, level = (
            generate_questions(
                difficulty,
                category
            )
        )

        if questions is None:

            print(
                "❌ Could not generate questions."
            )

            continue

        print(
            "\nYou selected:",
            level
        )

        print(
            "⏱️ Answer each question "
            "as quickly as you can!"
        )

        time.sleep(1)

        print(
            "------------------------"
        )

        print(
            "Get ready!"
        )

        time.sleep(3)

        score = run_quiz(
            questions
        )

        high_score = show_results(
            name,
            level,
            score,
            questions,
            high_score,
            results,
            badges
        )

        save_data(
            results,
            badges,
            high_score
        )

        print(
            "\n💾 Progress saved!"
        )

        input(
            "\nPress Enter to return "
            "to the main menu..."
        )

    elif choice == "2":

        show_statistics(results)

        input(
            "\nPress Enter to return "
            "to the main menu..."
        )

    elif choice == "3":

        show_leaderboard(results)

        input(
            "\nPress Enter to return "
            "to the main menu..."
        )

    elif choice == "4":

        show_achievements(badges)

        input(
            "\nPress Enter to return "
            "to the main menu..."
        )

    elif choice == "5":

        show_progress(results)

        input(
            "\nPress Enter to return "
            "to the main menu..."
        )

    elif choice == "6":

        save_data(
            results,
            badges,
            high_score
        )

        save_report(
            name,
            high_score,
            results,
            badges
        )

        print(
            "\n📊 Progress report saved!"
        )

        print(
            "\nGoodbye,",
            name + "!"
        )

        print(
            "Thanks for using MathMaster! 👋"
        )

        running = False

    else:

        print(
            "\n❌ Invalid option."
        )

        print(
            "Please choose a number from 1 to 6."
        )