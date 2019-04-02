from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root(rows=8, cols=8):
    return render_template('index.htm', rows=int(rows), cols=int(cols))


@app.route('/<rows>/<cols>')
def set_size(rows =8, cols=8):
    return render_template('index.htm', rows=int(rows), cols=int(cols))

@app.route('/<rows>/<cols>/<color1>/<color2>')
def set_it_all(rows = 8, cols =8, color1 = 'black', color2 = 'red'):
    return render_template('index.htm', rows = int(rows), cols = int(cols), color1 = color1, color2 = color2)



if __name__ == "__main__":
    app.run(debug = True)