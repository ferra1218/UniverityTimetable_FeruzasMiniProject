from flask import Flask, render_template, request
import pg8000

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        classification = request.form["classification"]
        print(f"Selected classification (POST): {classification}")  # Debugging line
        return render_template("timetable.html", classification=classification, data=[], message="Loading timetable...")

    return render_template("index.html")

@app.route("/timetable", methods=["GET"])
def timetable():
    classification = request.args.get('classification')  # Get classification from the query parameters
    print(f"Received classification (GET): {classification}")  # Debugging line
    if not classification:
        return "Classification not provided", 400

    # Connect to the PostgreSQL database
    conn = pg8000.connect(
        user="postgres", 
        password="180879fra", 
        host="database-1.c5kcwmmy8hy9.us-east-1.rds.amazonaws.com", 
        port=5432, 
        database="postgres"
    )

    cur = conn.cursor()
    query = "SELECT course_name, classification, day, time FROM timetable WHERE classification = %s;"
    print(f"SQL Query: {query} with parameter: {classification}")  # Debugging line
    cur.execute(query, (classification,))
    rows = cur.fetchall()

    print(f"Query result rows: {rows}")  # Debugging line

    # Pass data to the template
    if rows:
        return render_template("timetable.html", classification=classification, data=rows, message="")
    else:
        return render_template("timetable.html", classification=classification, data=[], message="No timetable data available for this classification.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

