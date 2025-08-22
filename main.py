from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')

# Обработка нажатия кнопок проектов
@app.route('/', methods=['POST'])
def process_form():
    project_type = request.form.get('project')
    return render_template('index.html', project_type=project_type)

# Обработка формы обратной связи
@app.route('/feedback', methods=['POST'])
def feedback():
    email = request.form.get('email')
    text = request.form.get('text')
    # Здесь можно добавить логику отправки email или сохранения в БД
    print(f"Feedback from {email}: {text}")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
