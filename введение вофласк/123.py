from flask import Flask

app = Flask(__name__)


@app.route('/')
def wow():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "Мы создадим новую реальность...\n" \
           "Ты, наверное, устал от этой планеты, да?\n" \
           "Ничего-ничего, осталось потерпеть совсем чуть-чуть...\n".replace('\n', '<br>')


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/image.jpg" alt="здесь должна была быть картинка, но не нашлась">
                        <p>Это просто сногсшибательно!</p>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
