from flask import Flask, jsonify
from app.roi_calculator import calculate_roi_from_yaml

app = Flask(__name__)

@app.route("/calculate-roi", methods=["GET"])
def calculate_roi():
    file_path = "projects/roi/roi_outdoor_5ha_2025.yml"
    result = calculate_roi_from_yaml(file_path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
