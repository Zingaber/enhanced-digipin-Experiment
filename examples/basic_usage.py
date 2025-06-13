#!/usr/bin/env python3
"""
Basic usage example for Enhanced DIGIPIN Experiment
Academic demonstration | ORAIL
"""

def main():
    print("🇮🇳 Enhanced DIGIPIN Experiment - Basic Usage")
    print("=" * 50)
    print("📍 Testing coordinates encoding...")
    
    # Example coordinates
    locations = [
        (28.6139, 77.2090, "New Delhi"),
        (19.0760, 72.8777, "Mumbai"), 
        (13.0827, 80.2707, "Chennai")
    ]
    
    for lat, lon, city in locations:
        print(f"{city}: {lat}, {lon}")
    
    print("\n✅ Academic demonstration | ORAIL")

if __name__ == "__main__":
    main()
