from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy function for backend processing
def process_input(input_data):
    # This could be any complex backend processing
    return input_data.upper()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        input_data = request.form['input_data']
        processed_data = process_input(input_data)
        return render_template('result.html', processed_data=processed_data)

if __name__ == '__main__':
    app.run(debug=True)

# run by right click and run python
