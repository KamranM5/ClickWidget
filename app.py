from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        name = request.form['name']

        message = f"Email: \n{email}\nНомер телефона: \n{phone}\nИмя: \n{name}"

        telegram_token = '6662517860:AAHF40LJ9JZlumBlqP_-_4J7W7P-BDyBc9A'
        telegram_chat_id = '5471677159'

        response = requests.post(
            f"https://api.telegram.org/bot{telegram_token}/sendMessage",
            data={'chat_id': telegram_chat_id, 'text': message}
        )

        if response.status_code == 200:
            return render_template('index.html')
        else:
            return render_template('index.html')

    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run()
