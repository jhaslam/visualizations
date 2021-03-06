from pygal.maps.world import World

wm: World = World()
wm.title = "North, Central and South America"

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bx', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
