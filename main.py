from flask import Flask, request,render_template
import requests
site_url='http://127.0.0.1/'
app = Flask(__name__)
var='a'
# Replace with your ESP8266's IP address
ESP_IP = "192.168.251.185"
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/hall')
def hall():
    var='a'
    return render_template('sheghu.html')
@app.route('/wash')
def washroom():
    var='b'
    return render_template('sheghu1.html')
@app.route('/send_string', methods=['POST'])
def send_string():
    string_value = request.form['string_value']
    # Send the string value to ESP8266 using HTTP POST request
    url = "http://{}/process_string".format(ESP_IP)
    data = {'string_value': string_value}
    response = requests.post(url, data=data)
    # if response.status_code == 200:
    #     return "String value sent successfully to ESP8266"
    # else:
    #     return "Failed to send string value to ESP8266"
    if var=='a':
        return render_template('sheghu.html')
    if var=='b':
        return render_template('sheghu1.html')
    else:
        return render_template('home.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
