import pandas as pd
from geopy.geocoders import Nominatim

def geocode_address(address):
    geolocator = Nominatim(user_agent="geocoder_script")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return 0.0, 0.0
    except Exception as e:
        print(f"Error geocoding address '{address}': {str(e)}")
        return 0.0, 0.0

def geocode_csv(input_csv, output_csv):
    # Read the CSV file
    df = pd.read_csv(input_csv)

    # Create 'lat' and 'lng' columns if not already present
    if 'lat' not in df.columns:
        df['lat'] = None
    if 'lng' not in df.columns:
        df['lng'] = None

    # Geocode rows that don't have 'lat' and 'lng' values
    for index, row in df.iterrows():
        if pd.isnull(row['lat']) or pd.isnull(row['lng']):
            address = f"{row['num']} {row['street']} {row['type']}, {row['City']} {row['Zip']}"
            lat, lng = geocode_address(address)
            df.at[index, 'lat'] = lat
            df.at[index, 'lng'] = lng

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    input_csv_file = "input.csv"  # Replace with your input CSV file
    output_csv_file = "output.csv"  # Replace with your desired output CSV file

    geocode_csv(input_csv_file, output_csv_file)
    print(f"Geocoding completed. Results saved to {output_csv_file}")