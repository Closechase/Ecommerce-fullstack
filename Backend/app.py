from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Caraxes#1",
    database="ecom"
)
cursor = mydb.cursor()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    name = data.get('name')
    dob = data.get('dob')
    mobile = data.get('mobile')
    email = data.get('email')
    address = data.get('address')
    
    # Insert data into MySQL table
    cursor.execute("INSERT INTO users (name, dob, mobile, email, address) VALUES (%s, %s, %s, %s, %s)",
                   (name, dob, mobile, email, address))
    mydb.commit()
    
    return jsonify({"message": "Data inserted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
