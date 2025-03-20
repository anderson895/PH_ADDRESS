from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Absolute path to the static folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_FOLDER = os.path.join(BASE_DIR, "static/ph_json")

@app.get("/static/ph_json/barangay.json")
def serve_barangay_json():
    return FileResponse(os.path.join(STATIC_FOLDER, "barangay.json"))

@app.get("/static/ph_json/city.json")
def serve_city_json():
    return FileResponse(os.path.join(STATIC_FOLDER, "city.json"))

@app.get("/static/ph_json/province.json")
def serve_province_json():
    return FileResponse(os.path.join(STATIC_FOLDER, "province.json"))

@app.get("/static/ph_json/region.json")
def serve_region_json():
    return FileResponse(os.path.join(STATIC_FOLDER, "region.json"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001, reload=True)
