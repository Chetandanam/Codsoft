pip install Flask

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub To-Do List</title>
</head>
<body>
    <h1>GitHub To-Do List</h1>
    <form action="{{ url_for('add') }}" method="post">
        <label for="task">New Task:</label>
        <input type="text" id="task" name="task" required>
        <button type="submit">Add Task</button>
    </form>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
</body>
</html>
python app.py
