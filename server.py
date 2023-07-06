from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def box():
    return render_template('index.html')

@app.route('/play/<int:num>')
def play(num):
    return render_template('index.html', num=num)

@app.route('/play/<int:x>/<string:color>')
def colors(x, color):
    return render_template('index.html', num=x, color=color)

if __name__=="__main__":
    app.run(debug=True, port=5050)

