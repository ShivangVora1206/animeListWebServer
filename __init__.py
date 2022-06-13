from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        filew = open(r'static/ULTIMATE ANIME LISTO.txt','a')
        name = request.form['input']+'\n'
        filew.write(name)
        print(name)
        filew.close()

        return render_template('form.html')
    else:
        return render_template('form.html')

# @app.route("/upload")
# def upload_file():
#     return render_template("upload.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def _upload_file():
    if request.method == 'POST':
        global f
        f = request.files['file']
        os.chdir(r"Uploads")
        f.save(secure_filename(f.filename))
        print(f.filename)
        return render_template('upload_succ.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)