import json
import tkinter as tk
from tkinter import messagebox

class CropRecommendationSystem:
    def __init__(self):
        # Predefined crop recommendations based on soil and weather conditions
        self.crop_data = [
            {"crop": "Rice", "pH_min": 5.0, "pH_max": 7.0, "nitrogen_min": 20, "nitrogen_max": 50, "temp_min": 20, "temp_max": 35, "rainfall_min": 100, "rainfall_max": 300},
            {"crop": "Wheat", "pH_min": 6.0, "pH_max": 8.0, "nitrogen_min": 30, "nitrogen_max": 60, "temp_min": 10, "temp_max": 25, "rainfall_min": 50, "rainfall_max": 150},
            {"crop": "Maize", "pH_min": 5.5, "pH_max": 7.5, "nitrogen_min": 25, "nitrogen_max": 50, "temp_min": 18, "temp_max": 30, "rainfall_min": 60, "rainfall_max": 200},
            {"crop": "Potato", "pH_min": 5.0, "pH_max": 6.5, "nitrogen_min": 20, "nitrogen_max": 40, "temp_min": 15, "temp_max": 25, "rainfall_min": 40, "rainfall_max": 100},
            {"crop": "Soybean", "pH_min": 6.0, "pH_max": 7.5, "nitrogen_min": 40, "nitrogen_max": 80, "temp_min": 20, "temp_max": 30, "rainfall_min": 50, "rainfall_max": 150},
            {"crop": "Barley", "pH_min": 6.0, "pH_max": 8.0, "nitrogen_min": 25, "nitrogen_max": 45, "temp_min": 10, "temp_max": 25, "rainfall_min": 40, "rainfall_max": 120},
        ]

    def recommend_crop(self, soil_pH, nitrogen, temperature, rainfall):
        recommendations = []
        for crop in self.crop_data:
            if (
                crop["pH_min"] <= soil_pH <= crop["pH_max"]
                and crop["nitrogen_min"] <= nitrogen <= crop["nitrogen_max"]
                and crop["temp_min"] <= temperature <= crop["temp_max"]
                and crop["rainfall_min"] <= rainfall <= crop["rainfall_max"]
            ):
                recommendations.append(crop["crop"])

        return recommendations

    def save_recommendations(self, recommendations):
        with open("crop_recommendations.json", "w") as file:
            json.dump(recommendations, file)

def submit():
    try:
        soil_pH = float(entry_pH.get())
        nitrogen = float(entry_nitrogen.get())
        temperature = float(entry_temperature.get())
        rainfall = float(entry_rainfall.get())
        
        system = CropRecommendationSystem()
        recommended_crops = system.recommend_crop(soil_pH, nitrogen, temperature, rainfall)
        
        if recommended_crops:
            system.save_recommendations(recommended_crops)
            messagebox.showinfo("Recommended Crops", "\n".join(recommended_crops))
        else:
            messagebox.showwarning("No Recommendations", "No crops found for the provided conditions.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# GUI Setup
app = tk.Tk()
app.title("Crop Recommendation System")

tk.Label(app, text="Soil pH:").pack()
entry_pH = tk.Entry(app)
entry_pH.pack()

tk.Label(app, text="Nitrogen (ppm):").pack()
entry_nitrogen = tk.Entry(app)
entry_nitrogen.pack()

tk.Label(app, text="Temperature (°C):").pack()
entry_temperature = tk.Entry(app)
entry_temperature.pack()

tk.Label(app, text="Rainfall (mm):").pack()
entry_rainfall = tk.Entry(app)
entry_rainfall.pack()

tk.Button(app, text="Submit", command=submit).pack()

app.mainloop()