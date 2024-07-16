from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def base():
    # Base map
    map = folium.Map(
        location=[45.52336, -122.6750],
        zoom_start=12
    )
    return map._repr_html_()

@app.route("/open-street-map")
def open_street_map():
    try:
        # Map using OpenStreetMap tiles
        map = folium.Map(
            location=[45.52336, -122.6750],
            tiles='OpenStreetMap',
            zoom_start=13
        )

        folium.Marker(
            location=[45.52336, -122.6750],
            popup="<b>Marker here</b>",
            tooltip="Click Here!"
        ).add_to(map)
        
        return map._repr_html_()
    except Exception as e:
        return f"Error generating open street map: {str(e)}"

@app.route("/map-marker")
def map_marker():
    try:
        # Map using Stamen Terrain tiles with attribution
        map = folium.Map(
            location=[45.52336, -122.6750],
            tiles='Stamen Terrain',
            zoom_start=12,
            attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
        )

        # Adding markers to the map
        folium.Marker(
            location=[45.52336, -122.6750],
            popup="<b>Marker 1 here</b>",
            tooltip="Click Here!"
        ).add_to(map)

        folium.Marker(
            location=[45.55736, -122.8750],
            popup="<b>Marker 2 here</b>",
            tooltip="Click Here!",
            icon=folium.Icon(color='green')
        ).add_to(map)

        folium.Marker(
            location=[45.53236, -122.8750],
            popup="<b>Marker 3 here</b>",
            tooltip="Click Here!",
            icon=folium.Icon(color='red')
        ).add_to(map)

        return map._repr_html_()
    except Exception as e:
        return f"Error generating map with markers: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
