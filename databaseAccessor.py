import psycopg2
import dbconfig

class DatabaseAccessor():
    def __init__(self):
        self.conn = psycopg2.connect(f"sslmode=disable dbname=postgres user=postgres hostaddr=35.185.104.52 password={dbconfig.dbpassword}")
   
    def createUser(self, username, password):
        cur = self.conn.cursor()  

        try:
            cur.execute("insert into lifter (username, passwd) values (%s, %s)", (username, password))
            self.conn.commit()
            success = cur.rowcount > 0
        except psycopg2.errors.UniqueViolation as exc:
            success = False
            self.conn.rollback()
        finally:
            cur.close()
            return success

    def loginUser(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("select * from lifter where username = %s and passwd = %s", (username, password))
        success = cursor.rowcount > 0
        cursor.close()
        return success

    def addSet(self, username, exercise_name, reps, weight):
        cur = self.conn.cursor()
        cur.execute("insert into exercise (exercise_name, reps, weight, username) values (%s, %s, %s, %s)",
            (exercise_name, reps, weight, username))
        self.conn.commit()
        cur.execute("select max(time_performed) from exercise where username = %s and exercise_name = %s", 
            (username, exercise_name))
        
        setAdded = cur.fetchone()
        cur.close()
        return setAdded

    def deleteSet(self, username, exercise_name, time_performed):
        cur = self.conn.cursor()
        cur.execute("delete from exercise where username = %s and exercise_name = %s and time_performed = %s",
            (username, exercise_name, time_performed))
        self.conn.commit()
        success = cur.rowcount > 0
        cur.close()
        return success

    def getAllSets(self, username):
        cur = self.conn.cursor()
        cur.execute("Select * from exercise where username = %s order by time_performed desc", (username,))
        allSets = cur.fetchall()
        cur.close()
        return allSets

    def getAllExerciseTypes(self):
        # create handle to make use of the connection
        curr = self.conn.cursor()

        # now do actualy query
        curr.execute("Select distinct exercise_name from musclegroup")

        # store that shit
        allSets = curr.fetchall()

        # close the handle, cuz?
        curr.close()

        #return the sets? but how to return a hashtable?
        return allSets


