from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/receive_data', methods=['GET','POST'])
def receive_data():
    data = request.get_json()
    
    print("Received data:", data)

    template_data = {
        'message': 'Data received successfully',
        'data': data 
    }

    return render_template('index.html', **template_data)

if __name__ == '__main__':
    app.run(debug=True)  

    #from power_plant import power_plant
    #power_plant()
