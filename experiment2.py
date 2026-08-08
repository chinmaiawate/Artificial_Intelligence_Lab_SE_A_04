from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")
    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Artificial Intelligence'))
    def aids(self):
        print("Suggested Career Path: Artificial Intelligence & Data Science Engineering")
    @Rule(StudentFacts(likes='Graphics'), StudentFacts(likes='Maths'))
    def civil(self):
        print("Suggested Career Path: Civil Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def civil(self):
        print("Suggested Career Path: Robotics & Artificial Intelligence")
    
         
    

def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    print("Enter any 2 subjects from the list given:\nMaths\nPhysics\nProgramming\nBiology\nCircuits\nAritificial Intelligence\nGraphics\nChemistry")
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()

