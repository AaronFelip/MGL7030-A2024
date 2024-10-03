from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, static_url_path="", static_folder="static")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == "GET":
        return render_template("index.html"), 200

    if request.method == "POST":
        username = request.form['username']
        radio = request.form.get('radio')
        select = request.form.get('liste-select')

        erreur = "Tous les champs doivent être remplis"

        if username == "" or radio is None or select == "":
            return render_template("index.html",
                                   erreur=erreur,
                                   username=username,
                                   radio=radio,
                                   select=select), 400
        else:

            log = open("log.txt", 'w')
            log.write("text %s " % username + "radio %s " % radio + "select %s " % select )
            log.close()

            return redirect(url_for('confirmation'), 302)


@app.route('/confirmation')
def confirmation():
    return render_template("confirmation.html")

if __name__ == '__main__':
    app.run()
