def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("נכון!")
        return 1
    else:
        print("טעות!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("תוצאה")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("התוצאה שלך: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("רוצה לשחק עוד הפעם? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "אני הלכתי למכולת וקניתי הרבה ממתקים למסיבה. באיזה זמן המילה קניתי?: ": "A",
 "הוא ילך לגרש את החזיר בר? באיזה זמן המילה ילך?: ": "C",
 "אחרי סדר פסח ,הילדים פינו את השולחן מזבל. מה הזמן של פינו?: ": "A",
 "הלכתי אחרי בית הספר הביתה לעזור לאמא שלי. מה הזמן של הלכתי?: ": "A",
 "שני היתכתבה בטלפון עם יעל וסיפרה לה שהיום יום השופינג הבין לאומי ויש מבצעים כמעט בכל מקום ": "D",
 " בבית ספר אלון יתקיים תחרות ליצוג העבר בהיסטוריה לכיתות ז עד ח ": "B",
 " יואב מספר סיפור לאחותו הקטנה כדי שהיא תירדם ": "B",
 " המילה חללית היתה מחודשת בתחילת שנות החמישים. באיזה זמן נמצא המשפט הזה? ": "A"
}

options = [["A. עבר", "B. הווה", "C. עתיד", "D.לא יודע"],
           ["A. עבר", "B. הווה", "C. עתיד", "D.לא יודע"],
           ["A. עבר", "B. הווה", "C. עתיד", "D.לא יודע"],
           ["A. עבר", "B. הווה", "C. עתיד", "D.לא יודע"],
           ["A. עבר", "B. הווה", "C. עתיד", "D.לא יודע"],
           ["A. היתכתבה, סיפרה, שופינג זמן הווה", "B. היתכתבה, סיפרה זמן הווה", "C.היתכתבה, סיפרה, שופינג זמן עבר", "D.היתכתבה, סיפרה זמן עבר"],
           ["A. יתקיים, ליצוג זמן עבר", "B. יתקיים זמן עתיד", "C. יתקיים, ליצוג זמן עתיד", "D.יתקיים זמן עבר"],
           ["A. מספר, תירדם  זמן הווה", "B. מספר זמן הווה", "C. מספר זמן עבר", "D.מספר, תירדם  זמן עתיד"],
           ["A. עבר", "B. הווה", "C. עתיד", "D.לא יודע"]]

new_game()

while play_again():
    new_game()

print("תודה שיחקתם")