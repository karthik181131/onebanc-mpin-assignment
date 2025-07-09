
from flask import Flask, render_template, request
from src.checker import evaluate_mpin

app = Flask(__name__)

REASON_MAP = {
    "COMMONLY_USED": "MPIN is commonly used by many users.",
    "DEMOGRAPHIC_DOB_SELF": "MPIN is similar to your Date of Birth.",
    "DEMOGRAPHIC_DOB_SPOUSE": "MPIN is similar to your Spouse's Date of Birth.",
    "DEMOGRAPHIC_ANNIVERSARY": "MPIN is similar to your Anniversary Date."
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    final_message = ""
    friendly_reasons = []

    if request.method == 'POST':
        mpin = request.form['mpin']
        dob = request.form['dob']
        spouse_dob = request.form['spouse_dob']
        anniversary = request.form['anniversary']

        result = evaluate_mpin(mpin, dob, spouse_dob, anniversary)

        if result["strength"] == "WEAK":
            friendly_reasons = [REASON_MAP.get(r, r) for r in result["reasons"]]
            final_message = "Your MPIN is considered weak. Please try a different MPIN."
        else:
            final_message = "MPIN is strong. Thank you for using the MPIN Strength Checker."

    return render_template('index.html', result=result, final_message=final_message, friendly_reasons=friendly_reasons)

if __name__ == '__main__':
    app.run(debug=True)
