from math import trunc
from flask import Flask,jsonify,redirect,url_for,render_template,request

from baseDeDatos import datos

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return jsonify({'message':'You are in home!!'})
        
@app.route('/expotronica/home',methods=['GET','POST'])
def expotronicaHome():
    return render_template('expotronica/expotronicaHome.html')
    
@app.route('/expotronica/proyecto/1',methods=['GET','POST'])
def expotronicaProyecto1():
    return render_template('expotronica/expotronicaProyecto1.html')

@app.route('/expotronica/team/<nombre>',methods=['GET','POST'])
def expotronicaTeam(nombre):
    for i in datos:
        if nombre == i['ruta']:
            return render_template(f'expotronica/expotronicaTeam.html')
    
    return jsonify('hola')


if __name__ == '__main__':
    app.run(debug=True)


