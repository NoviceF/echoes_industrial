from werkzeug.utils import secure_filename

from app import app
from data_processing import calculate


def save_uploaded_file(fileob):
    filename = secure_filename(fileob.filename)
    error = None
    warning = None
    save_path = None

    if len(filename):
        save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)

        try:
            fileob.save(save_path)
        except FileNotFoundError:
            error = "Can't save selected file {}!".format(filename)
    else:
        warning = "Path to price file is empty, trying to use existing.."

    return error, warning, save_path


def read_variables(request):
    builder1 = request.form['builder1']
    builder2 = request.form['builder2']
    builder3 = request.form['builder3']
    blueprint = request.form['blueprint']
    fileob = request.files['jita_minerals_sell_prices']

    error, warning, save_path = save_uploaded_file(fileob)

    res = -1

    if not error:
        try:
            res = calculate(builder1, builder2, builder3, blueprint, save_path)
        except Exception as exception:
            error = exception

    return error, warning, res

