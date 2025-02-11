from flask import Flask
#crear isinstancia
app = Flask(_name_)
#ruta raiz
@app.route('/')
def hola_mundo():
    return 'Hola mundo'
if _name_ == '_main_':
    app.run(debug=True)