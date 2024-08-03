from flask import Flask, render_template, request, jsonify
from train import train_model
from cloud_storage import CloudStorage
import os

app = Flask(__name__)
cloud_storage = CloudStorage('your-bucket-name')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    episodes = int(request.form.get('episodes', 1000))
    max_steps = int(request.form.get('max_steps', 500))
    train_model(episodes, max_steps)
    return jsonify({'message': 'Training completed'})

@app.route('/upload', methods=['POST'])
def upload():
    file_name = request.form.get('file_name')
    cloud_storage.upload_file(file_name)
    return jsonify({'message': 'File uploaded'})

@app.route('/download', methods=['POST'])
def download():
    file_name = request.form.get('file_name')
    cloud_storage.download_file(file_name)
    return jsonify({'message': 'File downloaded'})

if __name__ == '__main__':
    app.run(debug=True)
