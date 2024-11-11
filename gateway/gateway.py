from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URLs der Microservices
SERVICES = {
    "customer": "http://localhost:5001/customer/",
    "employee": "http://localhost:5002/employee/",
    "order": "http://localhost:5003/order/",
    "product": "http://localhost:5004/product/",
    "tax": "http://localhost:5005/tax/",
    "ticket": "http://localhost:5006/ticket/"
}

# Gateway-Routing für alle Microservices
@app.route('/<service>/<path:path>', methods=["GET", "POST", "PUT", "DELETE"])
def gateway(service, path):
    if service in SERVICES:
        url = f"{SERVICES[service]}{path}"
        method = request.method

        headers = {"Content-Type": "application/json"} if request.is_json else {}
        
        try:
            response = requests.request(method, url, json=request.get_json(silent=True), headers=headers)
            return (jsonify(response.json()) if response.headers.get("Content-Type") == "application/json" else response.text), response.status_code
        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 503  # 503 für Service nicht erreichbar
    else:
        return jsonify({"error": "Service not found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
