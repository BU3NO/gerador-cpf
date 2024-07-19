import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def generate_cpf():
    def calculate_digit(digs):
        s = sum([(len(digs) + 1 - i) * int(dig) for i, dig in enumerate(digs)])
        res = 11 - s % 11
        return res if res < 10 else 0

    digits = [random.randint(0, 9) for _ in range(9)]
    d1 = calculate_digit(digits)
    d2 = calculate_digit(digits + [d1])
    cpf = ''.join(map(str, digits + [d1, d2]))
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

@app.route('/')
def home():
    cpf = generate_cpf()
    return render_template('index.html', cpf=cpf)

@app.route('/api/generate_cpf', methods=['GET'])
def api_generate_cpf():
    cpf = generate_cpf()
    return jsonify(cpf=cpf)

if __name__ == '__main__':
    app.run(debug=True)
