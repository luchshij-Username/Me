#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_html = request.form.get('button_html')
    button_telegram = request.form.get('button_telegram')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_html=button_html, button_telegram=button_telegram, button_db=button_db)



if __name__ == "__main__":
    app.run(debug=True)