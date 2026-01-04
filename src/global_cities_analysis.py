"""
PROYECTO TLAZOLTÉOTL: GLOBAL CITIES IMPACT ANALYSIS
Author: Samuel Hernández
License: MIT Open Source

Analyzes the impact of Tlazoltéotl Tower in the world's 10 most polluted cities
with real 2025 data, climate adaptations, and economic projections.
"""

import json
import numpy as np
from typing import Dict, List
import os

# Top 10 Most Polluted Cities (2025 data)
GLOBAL_CITIES = {
    "Delhi_India": {
        "country": "India",
        "pm25_avg": 110,  # µg/m³ annual average
        "pm10_avg": 200,
        "humidity_avg": 65,  # %
        "temp_avg": 25,  # °C
        "wind_avg": 3.2,  # m/s
        "population": 32_000_000,
        "rainfall_mm": 714,
        "currency": "USD",  # for economic calc
        "carbon_credit_price": 25  # $/ton local market
    },
    "Dhaka_Bangladesh": {
        "country": "Bangladesh",
        "pm25_avg": 97,
        "pm10_avg": 185,
        "humidity_avg": 79,
        "temp_avg": 26,
        "wind_avg": 2.8,
        "population": 22_000_000,
        "rainfall_mm": 2076,
        "currency": "USD",
        "carbon_credit_price": 20
    },
    "Lahore_Pakistan": {
        "country": "Pakistan",
        "pm25_avg": 105,
        "pm10_avg": 195,
        "humidity_avg": 60,
        "temp_avg": 24,
        "wind_avg": 3.5,
        "population": 13_000_000,
        "rainfall_mm": 628,
        "currency": "USD",
        "carbon_credit_price": 22
    },
    "Beijing_China": {
        "country": "China",
        "pm25_avg": 85,
        "pm10_avg": 150,
        "humidity_avg": 55,
        "temp_avg": 12,
        "wind_avg": 4.2,
        "population": 21_000_000,
        "rainfall_mm": 571,
        "currency": "USD",
        "carbon_credit_price": 35
    },
    "Cairo_Egypt": {
        "country": "Egypt",
        "pm25_avg": 93,
        "pm10_avg": 175,
        "humidity_avg": 55,
        "temp_avg": 22,
        "wind_avg": 3.8,
        "population": 21_000_000,
        "rainfall_mm": 25,  # Very low
        "currency": "USD",
        "carbon_credit_price": 18
    },
    "Jakarta_Indonesia": {
        "country": "Indonesia",
        "pm25_avg": 78,
        "pm10_avg": 140,
        "humidity_avg": 82,
        "temp_avg": 27,
        "wind_avg": 2.5,
        "population": 34_000_000,
        "rainfall_mm": 1755,
        "currency": "USD",
        "carbon_credit_price": 20
    },
    "Kolkata_India": {
        "country": "India",
        "pm25_avg": 88,
        "pm10_avg": 165,
        "humidity_avg": 75,
        "temp_avg": 26,
        "wind_avg": 3.0,
        "population": 15_000_000,
        "rainfall_mm": 1582,
        "currency": "USD",
        "carbon_credit_price": 25
    },
    "Mumbai_India": {
        "country": "India",
        "pm25_avg": 82,
        "pm10_avg": 155,
        "humidity_avg": 77,
        "temp_avg": 27,
        "wind_avg": 3.5,
        "population": 21_000_000,
        "rainfall_mm": 2167,
        "currency": "USD",
        "carbon_credit_price": 25
    },
    "Baghdad_Iraq": {
        "country": "Iraq",
        "pm25_avg": 91,
        "pm10_avg": 170,
        "humidity_avg": 45,
        "temp_avg": 23,
        "wind_avg": 4.0,
        "population": 8_000_000,
        "rainfall_mm": 150,
        "currency": "USD",
        "carbon_credit_price": 15
    },
    "Lima_Peru": {
        "country": "Peru",
        "pm25_avg": 76,
        "pm10_avg": 135,
        "humidity_avg": 82,
        "temp_avg": 19,
        "wind_avg": 2.8,
        "population": 11_000_000,
        "rainfall_mm": 13,  # Coastal desert
        "currency": "USD",
        "carbon_credit_price": 28
    }
}

# Physical Constants
TOWER_HEIGHT = 100  # meters
THROAT_DIAMETER = 10  # meters
BASE_DIAMETER = 40  # meters
ELECTROSTATIC_EFFICIENCY = 0.97  # 97%
CO2_CAPTURE_ALGAE = 15.9  # kg/day (baseline CDMX)
ENERGY_GENERATION = 16.5  # kWh/day (baseline)

class GlobalCityAnalyzer:
    """Analyzes Tlazoltéotl Tower impact across different global cities."""
    
    def __init__(self, city_data: Dict):
        self.city_data = city_data
        self.results = {}
    
    def calculate_air_flow(self, wind_speed: float, temp: float) -> float:
        """Calculate air flow based on wind and temperature (Venturi effect)."""
        # Base flow: 4 m³/s (CDMX baseline at 3.5 m/s wind, 16°C)
        base_flow = 4.0
        wind_factor = wind_speed / 3.5
        # Temperature affects air density
        temp_factor = (273 + 16) / (273 + temp)
        
        return base_flow * wind_factor * temp_factor
    
    def calculate_particle_capture(self, pm25: float, pm10: float, air_flow: float) -> Dict:
        """Calculate daily particle capture."""
        # Air volume per day
        air_volume_day = air_flow * 86400  # m³/day
        
        # PM2.5 mass captured (µg/m³ → kg/day)
        pm25_captured = (air_volume_day * pm25 * 1e-9) * ELECTROSTATIC_EFFICIENCY
        
        # PM10 mass captured
        pm10_captured = (air_volume_day * pm10 * 1e-9) * ELECTROSTATIC_EFFICIENCY
        
        return {
            "air_volume_day": air_volume_day,
            "pm25_kg_day": pm25_captured,
            "pm10_kg_day": pm10_captured,
            "total_particulates_kg_day": pm25_captured + pm10_captured
        }
    
    def calculate_water_harvest(self, humidity: float, rainfall: float, air_flow: float) -> float:
        """Calculate water harvest (fog collection + rain)."""
        # Fog collection (Warka-style) - depends on humidity
        # Base: 7069 L/day at 65% humidity (CDMX)
        base_fog = 7069
        humidity_factor = humidity / 65
        fog_collection = base_fog * humidity_factor * (air_flow / 4.0)
        
        # Rainfall collection (tower catchment area)
        # Base diameter: 40m → Area ≈ 1256 m²
        catchment_area = np.pi * (BASE_DIAMETER/2)**2
        # Annual rainfall → daily collection
        rain_collection = (rainfall / 365) * catchment_area
        
        return fog_collection + rain_collection
    
    def calculate_energy(self, wind_speed: float) -> float:
        """Calculate energy generation from VAWT."""
        # Base: 16.5 kWh/day at 3.5 m/s
        # Wind power ∝ v³
        wind_factor = (wind_speed / 3.5) ** 3
        return ENERGY_GENERATION * wind_factor
    
    def calculate_co2_capture(self, temp: float, humidity: float) -> float:
        """Calculate CO2 capture (algae growth depends on climate)."""
        # Base: 15.9 kg/day (CDMX)
        # Optimal: 25-30°C, 60-80% humidity
        
        # Temperature factor (optimal 27°C)
        if 20 <= temp <= 32:
            temp_factor = 1.0 + (0.02 * (temp - 20))  # Better growth in warmer temps
        else:
            temp_factor = 0.8
        
        # Humidity factor
        if 60 <= humidity <= 85:
            humidity_factor = 1.1  # Optimal range
        else:
            humidity_factor = 0.9
        
        return CO2_CAPTURE_ALGAE * temp_factor * humidity_factor
    
    def calculate_economics(self, city: str, params: Dict, metrics: Dict) -> Dict:
        """Calculate economic impact."""
        # Annual metrics
        pm_captured_annual = metrics['particulates']['total_particulates_kg_day'] * 365 / 1000  # tons
        co2_annual = metrics['co2_kg_day'] * 365 / 1000  # tons
        water_annual = metrics['water_liters_day'] * 365
        energy_annual = metrics['energy_kwh_day'] * 365
        
        # Revenue streams
        carbon_credits = co2_annual * params['carbon_credit_price']
        
        # Water sales (varies by scarcity)
        water_scarcity_factor = max(0.1, 1 - (params['rainfall_mm'] / 2000))
        water_price_per_m3 = 0.5 + (water_scarcity_factor * 2)  # $0.5-2.5/m³
        water_revenue = (water_annual / 1000) * water_price_per_m3
        
        # Energy sales/savings
        energy_revenue = energy_annual * 0.12  # $0.12/kWh average
        
        # Health savings (air quality improvement)
        # WHO estimates: $1000-5000 per ton PM removed
        health_savings = pm_captured_annual * 2500
        
        total_annual_revenue = carbon_credits + water_revenue + energy_revenue + health_savings
        
        # CAPEX (construction)
        capex = 3_500_000  # $3.5M baseline
        
        # OPEX (maintenance)
        opex_annual = 85_000
        
        # ROI
        net_annual = total_annual_revenue - opex_annual
        roi_years = capex / net_annual if net_annual > 0 else 999
        
        return {
            "carbon_credits_usd": carbon_credits,
            "water_revenue_usd": water_revenue,
            "energy_revenue_usd": energy_revenue,
            "health_savings_usd": health_savings,
            "total_annual_revenue_usd": total_annual_revenue,
            "opex_annual_usd": opex_annual,
            "net_annual_usd": net_annual,
            "capex_usd": capex,
            "roi_years": roi_years
        }
    
    def analyze_city(self, city_name: str, params: Dict) -> Dict:
        """Complete analysis for one city."""
        print(f"\n{'='*60}")
        print(f"🌍 ANALYZING: {city_name.replace('_', ' ').upper()}")
        print(f"{'='*60}")
        
        # Calculate metrics
        air_flow = self.calculate_air_flow(params['wind_avg'], params['temp_avg'])
        particulates = self.calculate_particle_capture(params['pm25_avg'], params['pm10_avg'], air_flow)
        water_daily = self.calculate_water_harvest(params['humidity_avg'], params['rainfall_mm'], air_flow)
        energy_daily = self.calculate_energy(params['wind_avg'])
        co2_daily = self.calculate_co2_capture(params['temp_avg'], params['humidity_avg'])
        
        metrics = {
            "air_flow_m3_s": air_flow,
            "air_volume_day_m3": particulates['air_volume_day'],
            "particulates": particulates,
            "water_liters_day": water_daily,
            "energy_kwh_day": energy_daily,
            "co2_kg_day": co2_daily
        }
        
        economics = self.calculate_economics(city_name, params, metrics)
        
        # Print summary
        print(f"\n📊 CLIMATE PARAMETERS:")
        print(f"   PM2.5: {params['pm25_avg']} µg/m³ | PM10: {params['pm10_avg']} µg/m³")
        print(f"   Humidity: {params['humidity_avg']}% | Temp: {params['temp_avg']}°C")
        print(f"   Wind: {params['wind_avg']} m/s | Rainfall: {params['rainfall_mm']} mm/year")
        
        print(f"\n⚙️  PERFORMANCE (Daily):")
        print(f"   Air Processed: {particulates['air_volume_day']/1e6:.2f} Million m³")
        print(f"   PM Captured: {particulates['total_particulates_kg_day']:.2f} kg")
        print(f"   Water Harvested: {water_daily:,.0f} L")
        print(f"   CO₂ Sequestered: {co2_daily:.1f} kg")
        print(f"   Energy Generated: {energy_daily:.1f} kWh")
        
        print(f"\n💰 ECONOMICS (Annual):")
        print(f"   Total Revenue: ${economics['total_annual_revenue_usd']:,.0f}")
        print(f"   Net Profit: ${economics['net_annual_usd']:,.0f}")
        print(f"   ROI: {economics['roi_years']:.1f} years")
        
        return {
            "city": city_name,
            "country": params['country'],
            "parameters": params,
            "metrics": metrics,
            "economics": economics
        }
    
    def run_global_analysis(self):
        """Analyze all cities."""
        print("\n" + "="*60)
        print("🌍 TLAZOLTÉOTL TOWER: GLOBAL IMPACT ANALYSIS 2025")
        print("="*60)
        
        all_results = []
        
        for city_name, params in GLOBAL_CITIES.items():
            result = self.analyze_city(city_name, params)
            all_results.append(result)
        
        # Save results
        output_file = "results/global_cities_analysis_2025.json"
        os.makedirs("results", exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Results saved to: {output_file}")
        
        # Summary comparison
        self.print_comparison(all_results)
        
        return all_results
    
    def print_comparison(self, results: List[Dict]):
        """Print comparative summary."""
        print("\n" + "="*80)
        print("📊 COMPARATIVE SUMMARY: TOP 10 MOST POLLUTED CITIES")
        print("="*80)
        
        print(f"\n{'City':<20} {'PM/day (kg)':<15} {'Water/day (L)':<15} {'ROI (years)':<12} {'Annual Net ($)':<15}")
        print("-" * 80)
        
        for r in sorted(results, key=lambda x: x['economics']['roi_years']):
            city = r['city'].replace('_', ' ')
            pm = r['metrics']['particulates']['total_particulates_kg_day']
            water = r['metrics']['water_liters_day']
            roi = r['economics']['roi_years']
            net = r['economics']['net_annual_usd']
            
            print(f"{city:<20} {pm:>12.2f}   {water:>12,.0f}   {roi:>10.1f}   ${net:>12,.0f}")
        
        # Best opportunities
        best_roi = min(results, key=lambda x: x['economics']['roi_years'])
        most_profitable = max(results, key=lambda x: x['economics']['net_annual_usd'])
        most_water = max(results, key=lambda x: x['metrics']['water_liters_day'])
        
        print(f"\n🏆 BEST OPPORTUNITIES:")
        print(f"   Fastest ROI: {best_roi['city'].replace('_', ' ')} ({best_roi['economics']['roi_years']:.1f} years)")
        print(f"   Most Profitable: {most_profitable['city'].replace('_', ' ')} (${most_profitable['economics']['net_annual_usd']:,.0f}/year)")
        print(f"   Most Water: {most_water['city'].replace('_', ' ')} ({most_water['metrics']['water_liters_day']:,.0f} L/day)")

if __name__ == "__main__":
    analyzer = GlobalCityAnalyzer(GLOBAL_CITIES)
    results = analyzer.run_global_analysis()
    
    print("\n✅ Global analysis complete!")
    print(f"📁 Data for {len(results)} cities analyzed and saved.")
