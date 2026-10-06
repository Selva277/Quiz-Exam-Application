from Quiz_database import connection

class Question:
    def __init__(self,text,correct_answer,points=1):
        self.text = text
        self.correct_answer = correct_answer
        self.points = points
        
    def is_correct(self, answer):
        pass
    
class MCQuestions(Question):
    def __init__(self,text,options,correct_answer,points=1):
        super().__init__(text,correct_answer,points)
        self.options = options
        
    def display(self):
        print(self.text)
        
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")
            
    def is_correct(self, answer):
        return answer == self.correct_answer
    
            
    
class TorFquestions(Question):
    def __init__(self,text,correct_answer,points=1):
        super().__init__(text,correct_answer,points)
        
    def display(self):
        print(self.text)
        print("1. True")
        print("2. False")
        
        
        
    def is_correct(self, answer):
            return answer == self.correct_answer
        
        
class Quiz:
    def __init__(self, title, connection):
        self.title = title
        self.questions = []
        self.connection = connection

        cursor = self.connection.cursor()

        query = "INSERT INTO quizzes (title) VALUES (%s)"
        cursor.execute(query, (self.title,))

        self.connection.commit()

        self.quiz_id = cursor.lastrowid

        cursor.close()
        
    def add_questions(self,question):
        self.questions.append(question)
        
    def take_quiz(self):
        score = 0
        for question in self.questions:
            question.display()
            answer = input("Your answer: ")
            if question.is_correct(answer):
                print("Correct!")
                score += question.points
            else:
                print(f"Incorrect! The correct answer is: {question.correct_answer}")
                
        total_points = sum(question.points for question in self.questions)
        print(f"Quiz completed! Your score: {score}/{total_points}")
        return score

        
class Student:
    def __init__(self, name, connection):
        self.name = name
        self.connection = connection
        self.quizzes_taken = {}

        cursor = self.connection.cursor()

        query = "INSERT INTO students (name) VALUES (%s)"
        cursor.execute(query, (self.name,))

        self.connection.commit()

        self.student_id = cursor.lastrowid

        cursor.close()
        
    def take_quiz(self,quiz):
        print(f"{self.name} is taking the quiz: {quiz.title}")
        
        score = quiz.take_quiz()
        self.add_results(quiz,score)
        
        
    def add_results(self,quiz,score):
        self.quizzes_taken[quiz.title] = score
