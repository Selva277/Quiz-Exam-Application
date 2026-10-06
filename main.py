from Quiz_Exams import MCQuestions, TorFquestions, Quiz, Student
from Quiz_database import connection


Q1 = MCQuestions(
    "What is Python?",
    [
        "A programming language",
        "A snake",
        "A car"
    ],
    "1",
    1
)

Q2 = TorFquestions(
    "Python is a programming language.",
    "1",
    1
)
python_q1 = MCQuestions(
    "Which keyword is used to define a function in Python?",
    [
        "func",
        "def",
        "function",
        "define"
    ],
    "2",
    1
)

python_q2 = TorFquestions(
    "Python is dynamically typed.",
    "1",
    1
)

python_q3 = MCQuestions(
    "Which data type stores key-value pairs?",
    [
        "List",
        "Tuple",
        "Dictionary",
        "Set"
    ],
    "3",
    1
)

sql_q1 = MCQuestions(
    "Which SQL command is used to retrieve data?",
    [
        "INSERT",
        "SELECT",
        "UPDATE",
        "DELETE"
    ],
    "2",
    1
)

sql_q2 = TorFquestions(
    "A PRIMARY KEY uniquely identifies a row in a table.",
    "1",
    1
)

sql_q3 = MCQuestions(
    "Which SQL command is used to add a new row?",
    [
        "INSERT",
        "ADD",
        "CREATE",
        "APPEND"
    ],
    "1",
    1
)

sql_quiz = Quiz("SQL Basics", connection)

sql_quiz.add_questions(sql_q1)
sql_quiz.add_questions(sql_q2)
sql_quiz.add_questions(sql_q3)


quiz1 = Quiz("Python Basics", connection)

quiz1.add_questions(Q1)
quiz1.add_questions(Q2)


quiz1.add_questions(python_q1)
quiz1.add_questions(python_q2)
quiz1.add_questions(python_q3)


student1 = Student("Alice", connection)

student1.take_quiz(quiz1)

print(student1.quizzes_taken)