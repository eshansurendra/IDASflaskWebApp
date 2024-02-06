from flask import Flask, request

app = Flask(__name__)

@app.route('/save', methods=['POST'])
def save_to_file():
    data = request.json  # assuming JSON data is sent in the request
    if data:
        with open('text.txt', 'a') as file:
            file.write(str(data) + '\n')
        return 'Data saved successfully!', 200
    else:
        return 'No data received!', 400

if __name__ == '__main__':
    app.run(debug=True)
