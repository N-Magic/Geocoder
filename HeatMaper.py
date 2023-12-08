import pandas as pd
import folium
from folium.plugins import HeatMap

def create_dot_map(df, output_html):
    dot_map = folium.Map(location=[df['lat'].median(), df['lng'].median()], zoom_start=10, control_scale=True)

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['lat'], row['lng']],
            radius=5,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6,
            popup=f"{row['num']} {row['street']} {row['type']}, {row['City']} {row['Zip']}"
        ).add_to(dot_map)

    dot_map.save(output_html)

def create_heat_map(df, output_html):
    heat_map = folium.Map(location=[df['lat'].median(), df['lng'].median()], zoom_start=10, control_scale=True)

    locations = df[['lat', 'lng']].dropna().values.tolist()
    HeatMap(locations).add_to(heat_map)

    heat_map.save(output_html)

if __name__ == "__main__":
    input_csv_file = "output.csv"  # Replace with the path to your output CSV file
    output_dot_map_html = "dot_map.html"
    output_heat_map_html = "heat_map.html"

    df = pd.read_csv(input_csv_file)

    create_dot_map(df, output_dot_map_html)
    print(f"Dot map created. Open {output_dot_map_html} in a web browser to view.")

    create_heat_map(df, output_heat_map_html)
    print(f"Heat map created. Open {output_heat_map_html} in a web browser to view.")
