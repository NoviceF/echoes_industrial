from flask import Flask, render_template, request

from blueprints import bpList
from preprocess_form import read_variables

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "uploads"


@app.route('/')
def main():
    return render_template('app.html', bpList=bpList)


@app.route('/sendBuilder', methods=['POST'])
def send():
    if request.method == 'POST':
        error, warning, res = read_variables(request)
        return render_template(
            'app.html', bpList=bpList, sum=333, error=error, warning=warning)


if __name__ == '__main__':
    app.run()



# две формы: одна считает цену крафта по навыкам майнера для известных рецептов
# берет цену ресов и рецепта из житы + цена запуска производства

# вторая предлагает как руда нужна для требуемого набора минералов, учитывает навык
# переработчика
