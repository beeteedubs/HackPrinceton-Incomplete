from databaseAccessor import DatabaseAccessor

def main():
    db = DatabaseAccessor()
    print(db.createUser("John", "Smith"))
    print(db.loginUser("John", "Smith"))
    #print(db.loginUser("Hiterla", "Mary"))
    db.addSet("John", "Squats", 10, 155)
    db.addSet("John", "Squats", 8, 165)
    db.addSet("John", "Squats", 5, 175)
    db.addSet("John", "Squats", 15, 135)
    #print(db.deleteSet("John", "Squats", datetime))
    print(db.getAllSets("John"))
    print(db.getAllExerciseTypes())

main()