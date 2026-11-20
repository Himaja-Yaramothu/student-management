
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

students = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Management Portal</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f3f6fb; }
        h1 { color: #244a82; }
        input, button { padding: 10px; margin: 5px; }
        table { width: 100%; border-collapse: collapse; background: white; }
        th, td { padding: 12px; border: 1px solid #ddd; }
        th { background: #244a82; color: white; }
    </style>
</head>
<body>
    <h1>Student Management Portal</h1>
    <form method="POST" action="/add">
        <input name="name" placeholder="Student name" required>
        <input name="course" placeholder="Course" required>
        <button type="submit">Add Student</button>
    </form>
    <h2>Student Records</h2>
    <table>
        <tr><th>Name</th><th>Course</th></tr>
        {% for student in students %}
        <tr>
            <td>{{ student.name }}</td>
            <td>{{ student.course }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    course = request.form["course"]
    students.append({"name": name, "course": course})
    return redirect("/")

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
