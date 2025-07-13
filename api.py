from fastapi import APIRouter
from utils.roi_tools import calculate_roi_from_yaml

router = APIRouter()

@router.get("/calculate_roi_5ha")
def calculate_custom_roi():
    return calculate_roi_from_yaml("projects/roi/roi_5ha_integrated_cbd.yml")
