import yaml

def calculate_roi_from_yaml(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    yield_kg = data["yield_flower_kg_per_cycle"]
    top_flower_ratio = data["top_flower_ratio"]
    extract_biomass_ratio = data["extract_biomass_ratio"]
    prices = data["prices"]
    yields = data["extraction_yields"]

    revenue_top = yield_kg * top_flower_ratio * prices["top_flower_per_kg"]
    biomass_for_extract = yield_kg * extract_biomass_ratio

    revenue_rosin = biomass_for_extract * (yields["rosin_percent"] / 100) * prices["rosin_per_kg"]
    revenue_distillate = biomass_for_extract * (yields["distillate_percent"] / 100) * prices["distillate_per_kg"]
    revenue_isolate = biomass_for_extract * (yields["isolate_percent"] / 100) * prices["isolate_per_kg"]

    total_revenue = revenue_top + revenue_rosin + revenue_distillate + revenue_isolate

    capex = data.get("budget_usd", 0)
    opex = data.get("opex_usd_per_year", 0)
    total_cost = capex + opex

    roi_percent = ((total_revenue - total_cost) / total_cost) * 100

    return {
        "Revenue ($)": round(total_revenue, 2),
        "CAPEX+OPEX ($)": total_cost,
        "ROI (%)": round(roi_percent, 2)
    }
