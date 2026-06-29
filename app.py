from flask import Flask, render_template, request

app = Flask(__name__)

# Display Registration Form
@app.route('/')
def home():
    return render_template('register.html')

# Handle Form Submission
@app.route('/register', methods=['POST'])
def register():

    name = request.form['name']
    city = request.form['city']
    phone = request.form['phone']

    return render_template(
        'success.html',
        name=name,
        city=city,
        phone=phone
    )

if __name__ == '__main__':
    app.run(debug=True)