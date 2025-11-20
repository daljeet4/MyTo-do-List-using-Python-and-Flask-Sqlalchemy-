from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# In-memory storage for todos
todos = []
todo_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    global todo_id_counter
    task = request.form.get('task')
    if task:
        todos.append({
            'id': todo_id_counter,
            'task': task,
            'completed': False
        })
        todo_id_counter += 1
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)