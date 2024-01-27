import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from Predictor import ClothesPricePredictor

class JSONRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        json_data = json.loads(post_data.decode('utf-8'))

        # Extraire les données du JSON
        brand = json_data.get('brand')
        size = json_data.get('size')
        status = json_data.get('status')
        cloth_type = json_data.get('type')
        price = json_data.get('price')

        # Créer une instance de la classe ClothesPricePredictor
        predictor = ClothesPricePredictor()

        # Prédiction du prix
        predicted_price = predictor.predict_price(brand, size, status, cloth_type, price)
        
        # Envoyer la réponse
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_data = {'estimated_price': predicted_price}
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, JSONRequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
