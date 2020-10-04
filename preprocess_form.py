import json

from werkzeug.utils import secure_filename

from blueprints import bpList
from data_processing import calculate


def save_uploaded_file(app, fileob):
    filename = secure_filename(fileob.filename)
    error = None
    warning = None

    if len(filename):
        save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)

        try:
            fileob.save(save_path)
        except FileNotFoundError:
            error = "Can't save selected file {}!".format(filename)
    else:
        warning = "Path to price file is empty, trying to use existing.."
        load_file = "{}/{}".format(app.config["UPLOAD_FOLDER"], 'stats.csv')

        return error, warning, load_file

    return error, warning, save_path


def read_variables(app, request):
    builder1 = int(request.form['builder1'] if request.form['builder1'] else 0)
    builder2 = int(request.form['builder2'] if request.form['builder2'] else 0)
    builder3 = int(request.form['builder3'] if request.form['builder3'] else 0)
    blueprint = bpList.get(int(request.form['blueprint']))
    fileob = request.files['market_prices']

    error, warning, save_path = save_uploaded_file(app, fileob)

    res = -1

    if not error:
        try:
            res = calculate(builder1, builder2, builder3, blueprint, save_path)
        except Exception as exception:
            error = exception

    res = "\n{}".format(json.dumps(res, sort_keys=False, indent=4, separators=(',', ': ')))

    return error, warning, res

