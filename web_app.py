from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve customer data from the form
        cust_name = request.form['cust_name']
        address = request.form['address']
        contact_no = request.form['contact_no']
        age = request.form['age']
        gender = request.form['gender']
        id_proof = request.form['id_proof']

        # Create a dictionary with the customer data
        customer_info = {
            "cust_name": cust_name,
            "address": address,
            "contact_no": contact_no,
            "age": age,
            "gender": gender,
            "id_proof": id_proof
        }

        # Write the customer data to a JSON file
        with open('customer_data.json', 'a') as file:
            json.dump(customer_info, file)
            file.write("\n")
        return "Customer data saved successfully!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

