import webview
import folium
m = folium.Map(tiles="Stamen Terrain", zoom_start=13)

folium.Marker([46.8354, -121.7325], popup="Camp Muir").add_to(m)

m.add_child(folium.ClickForMarker(popup="Waypoint"))
m.save('map.html')
window = webview.create_window("Folium Widnow", url='map.html', width=800, height=600,
                               resizable=True, fullscreen=False, min_size=(200, 100),
                               hidden=False, frameless=False, easy_drag=True,
                               minimized=False, on_top=False, confirm_close=False,
                               transparent=False, text_select=True, zoomable=True, draggable=True,
                               )
webview.start()


# def get_current_url(window):
#     print(window.get_current_url())


# if __name__ == '__main__':
#     window = webview.create_window('Get current URL', 'map.html')
#     webview.start(get_current_url, window)
