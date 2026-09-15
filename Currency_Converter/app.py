from urllib3.util import response
from flask import Flask, jsonify, request, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TIMEOUT = int(os.getenv("API_TIMEOUT", "10"))


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/convert")
def convert_currency():
    amount = request.args.get("amount", type=float)
    from_currency = request.args.get("from", type=str)
    to_currency = request.args.get("to", type=str)

    if amount is None or amount <= 0:
        return jsonify({
            "error": "Amount must be a positive number"
        }), 400

    if not from_currency or not to_currency:
        return jsonify({
            "error": "Please provide both from and to currencies"
        }), 400

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    url = f"https://api.frankfurter.dev/v2/rate/{from_currency}/{to_currency}"

    try:
        response = requests.get(url, timeout=API_TIMEOUT)

    except requests.exceptions.Timeout:
        return jsonify({
        "error": "Exchange rate service timed out"
    }), 504

    except requests.exceptions.RequestException:
        return jsonify({
        "error": "Unable to connect to exchange rate service"
    }), 503


    if response.status_code != 200:
        return jsonify({
        "error": "Invalid currency code or exchange rate unavailable"
    }), 400

    data = response.json()
    rate = data["rate"]

    converted_amount = amount * rate

    return jsonify({
        "amount": amount,
        "from": from_currency,
        "to": to_currency,
        "rate": rate,
        "converted_amount": round(converted_amount, 2)
    })    



if __name__ == "__main__":
    app.run(debug=True)