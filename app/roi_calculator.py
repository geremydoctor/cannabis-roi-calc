import yaml

def calculate_roi_from_yaml(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    biomass = data['yield_flower_kg_per_cycle']
    top_ratio = data['biomass_distribution']['top_flower_ratio']
    extract_ratio = data['biomass_distribution']['extract_biomass_ratio']

    top_kg = biomass * top_ratio
    extract_kg = biomass * extract_ratio

    rosin_kg = extract_kg * (data['extraction_yields']['rosin_percent'] / 100)
    distillate_kg = extract_kg * (data['extraction_yields']['distillate_percent'] / 100)
    isolate_kg = extract_kg * (data['extraction_yields']['isolate_percent'] / 100)

    revenue = (
        top_kg * data['prices']['top_flower_per_kg'] +
        rosin_kg * data['prices']['rosin_per_kg'] +
        distillate_kg * data['prices']['distillate_per_kg'] +
        isolate_kg * data['prices']['isolate_per_kg']
    )

    roi_percent = (revenue - data['budget_usd']) / data['budget_usd'] * 100

    return {
        "Revenue ($)": round(revenue, 2),
        "ROI (%)": round(roi_percent, 2)
    }
