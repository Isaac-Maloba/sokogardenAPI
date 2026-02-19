# Import flask and its componets
from flask import *


# Import the pymysql module - It helps us to create a connection between python flask and my sql database
import pymysql

# Create a flask application and give it a name
app = Flask(__name__)

# Below is the sign up route
@app.route("/api/signup", methods = ["POST"])
def signup():
    if request.method == "POST":
        # Extract the different details entered on the form
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        phone = request.form["phone"]

        # By use of the print function, let's print all those details sent with the upcoming request

        # print(username, email, password, phone)
        # Establish a conneciton between flask/pytohn and mysql
        connection = pymysql.connect(host="localhost", user="root", password="", database="sokogardenonline")


        # Create a cursor to execute the sql queries
        cursor = connection.cursor()


        # structure an sql to insert the details received from the form in postman
        # The %s is a placeholder -> A placeholder stands in plav=ce of actual values i.e we sahll replace them later on
        sql = "INSERT INTO users(username,email,phone,password) VALUES(%s, %s, %s, %s)"


        # Create a tuple that will hold all the data received from the form
        data = (username, email, phone, password)


        # By use of the cursor, execute the sql ans you replace the placeholders with the actual values
        cursor.execute(sql, data)


        # commit the changes to the database
        connection.commit()



        return jsonify({"message" : "User Registered Successfully!"})


# Below is the login/sign in route
@app.route("/api/signin", methods = ["POST"])
def signin ():
    if request.method == "POST":
        # Extraxt the two details entered in the form
        email = request.form["email"]
        password = request.form["password"]


        # Print out the details entered
        # print(email, password)


        # create/ establish a connection to the database
        connection = pymysql.connect(host="localhost", user="root", password="", database="sokogardenonline")

        # create a cursor
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # structure an sql query that will check whether the email and password entered are correct
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        # Put the data received from the form into a tuple
        data = (email, password)

        # By use of the cursor, execute the sql and the data
        cursor.execute(sql, data)
        
        # Check whetehr there are rows returned and store the same on a variable
        count = cursor.rowcount

        # if there are recors records returned, it means the password and the email are correct; otherwise it means they are wrong
        if count == 0:
            return jsonify({"message" : "Login Failed!"})
        else:
            # There must be a user, so we create a variable that will hold the details of the user fetched from the database
            user = cursor.fetchone()
            # Return the details to the frontend as well as a message
            return jsonify({"message" : "Login Successful!", "user":user})



























# Running the application
app.run(debug=True)