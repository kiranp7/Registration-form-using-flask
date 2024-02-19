from flask import Flask, render_template ,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


    
@app.route('/kiran',methods=['POST'])
def krn():
    fname = request.form["fname"]
    dateofbirth = request.form["dateofbirth"]
    fav = request.form["fav"]

    return render_template('table.html', fname=fname, dateofbirth=dateofbirth, fav=fav )


if __name__=='__main__':
    app.run(debug=True)