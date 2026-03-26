import os
from flask import Flask, render_template, request, abort, send_file

app = Flask(__name__)

DOCS_DIR = os.path.join(os.path.dirname(__file__), 'docs')

@app.route('/')
def index():
    return render_template('index.html', title="Главная")

@app.route('/about')
def about():
    return render_template('about.html', title='О компании')

@app.route('/services')
def services():
    return render_template('services.html', title='Услуги')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакты')

@app.route('/view')
def view_doc():
    file_param = request.args.get('file', '')

    if not file_param:
        return render_template('view_doc.html', title='Просмотр документов', content='Не указан файл для просмотра', filename=None)
    

    filepath = os.path.join(DOCS_DIR, file_param)
    
    if  os.path.exists(filepath):

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        return render_template('view_doc.html', title='Просмотр документов',
                           content=content, filename=file_param)
    
    return render_template('view_doc.html', title='Просмотр документов',
                                content=f'Файл "{file_param}" не найден', filename=file_param)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
