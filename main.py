from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/haqqımızda")
def about():
    return render_template('about.html', title='Haqqımızda')

@app.route("/daxilol")
def login():
    return render_template('about.html', title='Daxil Ol')

@app.route("/qeydiyyat")
def register():
    return render_template('about.html', title='Qeydiyyat')

@app.route('/riyaziyyat-olimpiadaları')
def olympiad():
    return render_template('olympiad.html', title="Riyaziyyat Olimpiadaları")

@app.route('/məsləhət-bloqu')
def advice():
    return render_template('advice.html', title="Məsləhət Bloqu")

@app.route('/müzakirə')
def discUSS():
    return render_template('discuss.html', title="Müzakirə")



if __name__ == '__main__':
    app.run(debug=True)