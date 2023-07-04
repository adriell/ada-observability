from flask import Flask, jsonify, request, render_template, abort
import logging

app = Flask(__name__)
app.logger.setLevel(logging.ERROR)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    #name = request.form.get('name')
    try:
        # Simulando um erro no código
        return render_template('result.html', name=name)
    except Exception as e:
        # Abortar com erro 500i
        app.logger.exception('Ocorreu um erro interno')

        abort(500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
