import folium

# create map object
m = folium.Map(location =[-10.93934139,-37.06274211], zoom_start=12)

# Global tooltip
tooltip = 'Click For More Info'

# create markers
folium.Marker([-10.93934139,-37.06274211],
            popup='<strong>Location One</strong>',
            tooltip=tooltip).add_to(m)

folium.Marker([-10.94394907,-37.05233639],
            popup='<strong>Location One</strong>',
            tooltip=tooltip).add_to(m)

folium.Marker([-10.92374638,-37.10509667],
            popup='<strong>Location One</strong>',
            tooltip=tooltip).add_to(m)



# Generate map
m.save('map.html')
