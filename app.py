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






























# Running the application
app.run(debug=True)