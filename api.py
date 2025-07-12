from flask import Flask, request, jsonify
import yaml
import os

app = Flask(__name__)

BASE_PATH = "projects/roi/"

def load_yaml(project_name):
    file_path = os.path.join(BASE_PATH, f"{project_name}.yml")
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

@app.route('/calculate-roi', methods=['GET'])
def calculate_roi():
    project_name = request.args.get('project', 'roi_outdoor_5ha_2025')
    data = load_yaml(project_name)
    if not data:
        return jsonify({"error": "Project not found"}), 404

    budget = data['budget_usd']
    yield_kg = data['yield_flower_kg_per_cycle']
    top_ratio = data['biomass_distribution']['top_flower_ratio']
    extract_ratio = data['biomass_distribution']['extract_biomass_ratio']

    prices = data['prices']
    yields = data['extraction_yields']

    top_flower_kg = yield_kg * top_ratio
    extract_kg = yield_kg * extract_ratio

    rosin_kg = extract_kg * (yields['rosin_percent'] / 100)
    distillate_kg = extract_kg * (yields['distillate_percent'] / 100)
    isolate_kg = extract_kg * (yields['isolate_percent'] / 100)

    revenue = (
        top_flower_kg * prices['top_flower_per_kg'] +
        rosin_kg * prices['rosin_per_kg'] +
        distillate_kg * prices['distillate_per_kg'] +
        isolate_kg * prices['isolate_per_kg']
    )

    roi = ((revenue - budget) / budget) * 100

    return jsonify({
        "Revenue ($)": round(revenue, 2),
        "ROI (%)": round(roi, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
