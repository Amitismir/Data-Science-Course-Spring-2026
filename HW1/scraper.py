import requests
import pandas as pd
import time

# --- Configuration ---
TARGET_COUNT = 50
MIN_YEAR = 1386  
# The URL structure I found from DevTools
BASE_URL = "https://bama.ir/cad/api/search?vehicle=samand&pageIndex={page}&pageSize=24"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

def scrape_bama_samand():
    all_cars = []
    page = 0
    
    print(f"--- Starting Scraper: Target {TARGET_COUNT} Samand cars (Year > 1385) ---")

    while len(all_cars) < TARGET_COUNT:
        url = BASE_URL.format(page=page)
        print(f"Requesting Page {page}...")
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=15)
            response.raise_for_status()
            json_data = response.json()
            
            # Navigate the JSON structure: data -> ads
            ads = json_data.get('data', {}).get('ads', [])
            
            if not ads:
                print("No more ads found on this page. Stopping.")
                break
                
            for ad in ads:
                # 1. Skip if it's an advertisement (not a car listing)
                if ad.get('type') != 'ad':
                    continue
                
                detail = ad.get('detail', {})
                price_info = ad.get('price', {})
                
                # 2. Year Filter (Manufactured after 1385)
                try:
                    year = int(detail.get('year', 0))
                except (ValueError, TypeError):
                    year = 0
                    
                if year < MIN_YEAR:
                    continue  # Skip cars older than 1386
                
                # 3. Extract Fields
                car_data = {
                    "Price": price_info.get('price', 'Call for price'),
                    "Mileage": detail.get('mileage', '0'),
                    "Color": detail.get('body_color', 'N/A'),
                    "Production Year": year,
                    "Transmission": detail.get('transmission', 'N/A'),
                    "Description": detail.get('description', 'No description provided')
                }
                
                all_cars.append(car_data)
                
                # Stop if we hit 50
                if len(all_cars) >= TARGET_COUNT:
                    break
            
            print(f"Currently collected: {len(all_cars)} items.")
            page += 1
            time.sleep(1.5) # Polite delay to avoid IP blocking
            
        except Exception as e:
            print(f"An error occurred on page {page}: {e}")
            break

    # --- Save to Excel ---
    if all_cars:
        df = pd.DataFrame(all_cars[:TARGET_COUNT]) # Ensure exactly 50
        filename = "bama_samand_results.xlsx"
        
        try:
            df.to_excel(filename, index=False)
            print("-" * 40)
            print(f"SUCCESS! {len(df)} cars saved to: {filename}")
            print("-" * 40)
        except PermissionError:
            print(f"ERROR: Cannot save. Please close '{filename}' if it is open in Excel!")
    else:
        print("No data collected. Check your internet or filters.")

if __name__ == "__main__":
    scrape_bama_samand()
