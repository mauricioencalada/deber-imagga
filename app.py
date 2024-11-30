from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'acc_689ee8104dc852c' 
API_SECRET = '2a5558cba8a86c70bc7c52a0dba9272a' 
IMAGGA_URL = 'https://api.imagga.com/v2/tags'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    # Obtener la URL de la imagen desde la solicitud
    data = request.get_json()
    image_url = data.get('image_url')
    
    # Hacer la solicitud a la API de Imagga
    response = requests.get(
        IMAGGA_URL,
        params={'image_url': image_url},
        auth=(API_KEY, API_SECRET)
    )
    
    if response.status_code == 200:
        result = response.json()
        tags = result['result']['tags'][:2]  # Obtener las dos etiquetas más confiables
        return jsonify(tags=tags)  # Enviar los resultados de vuelta al frontend
    else:
        return jsonify({"error": "Error en la API de Imagga"}), 400

if __name__ == '__main__':
    app.run(debug=True)