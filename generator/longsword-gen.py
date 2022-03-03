'''
x starts at 11
y starts at 9

pivot coord = -(1+sqrt(2))
'''
import math
import json
with open('sword_base.json') as f:
  model = json.loads(f.read())
x = 10
y = 8
cpv = lambda n: -(1+math.sqrt(2))*n
for n in range(2048): #change 2048 to whatever for a different length sword
  x += 1
  y += 1
  model['elements'].append({
			"name": f"line{n+1}",
			"from": [0, 0, 7.5],
			"to": [0.70711, 3.53553, 8.5],
			"rotation": {"angle": 0, "axis": "z", "origin": [cpv(x), cpv(y), 0], "rescale": True},
			"faces": {
				"north": {"uv": [9, 9, 10, 4], "rotation": 180, "texture": "#0"},
				"east": {"uv": [9, 4, 10, 9], "texture": "#0"},
				"south": {"uv": [9, 4, 10, 9], "texture": "#0"},
				"west": {"uv": [9, 4, 10, 9], "texture": "#0"},
				"up": {"uv": [10, 4, 9, 5], "rotation": 180, "texture": "#0"},
				"down": {"uv": [9, 8, 10, 9], "texture": "#0"}
			}
		})
model['elements'].extend(
  [
    {
      "name": "tip",
      "from": [0.70711, 0.70711, 7.5],
      "to": [1.41421, 4.24264, 8.5],
      "rotation": {"angle": 0, "axis": "z", "origin": [cpv(x), cpv(y), 0], "rescale": True},
      "faces": {
        "north": {"uv": [13, 5, 14, 0], "rotation": 180, "texture": "#0"},
        "east": {"uv": [13, 0, 14, 5], "texture": "#0"},
        "south": {"uv": [13, 0, 14, 5], "texture": "#0"},
        "west": {"uv": [13, 0, 14, 5], "texture": "#0"},
        "up": {"uv": [14, 0, 13, 1], "rotation": 180, "texture": "#0"},
        "down": {"uv": [13, 4, 14, 5], "texture": "#0"}
      }
    },
    {
      "name": "tip2",
      "from": [1.41421, 1.41421, 7.5],
      "to": [2.12132, 4.24264, 8.5],
      "rotation": {"angle": 0, "axis": "z", "origin": [cpv(x), cpv(y), 0], "rescale": True},
      "faces": {
        "north": {"uv": [14, 0, 15, 4], "texture": "#0"},
        "east": {"uv": [14, 0, 15, 4], "texture": "#0"},
        "south": {"uv": [14, 0, 15, 4], "texture": "#0"},
        "west": {"uv": [14, 0, 15, 4], "texture": "#0"},
        "up": {"uv": [15, 0, 14, 1], "rotation": 180, "texture": "#0"},
        "down": {"uv": [14, 3, 15, 4], "texture": "#0"}
      }
    },
    {
      "name": "tip3",
      "from": [2.12132, 2.1213, 7.5],
      "to": [2.82843, 4.24262, 8.5],
      "rotation": {"angle": 0, "axis": "z", "origin": [cpv(x), cpv(y), 0], "rescale": True},
      "faces": {
        "north": {"uv": [15, 0, 16, 3], "texture": "#0"},
        "east": {"uv": [15, 0, 16, 3], "texture": "#0"},
        "south": {"uv": [15, 0, 16, 3], "texture": "#0"},
        "west": {"uv": [15, 0, 16, 3], "texture": "#0"},
        "up": {"uv": [16, 0, 15, 1], "rotation": 180, "texture": "#0"},
        "down": {"uv": [15, 2, 16, 3], "texture": "#0"}
      }
    }
  ]
)
with open('../§rLong Swords §8[§71.16+§8]/assets/minecraft/models/item/sword.json','w+') as f:
  json.dump(model,f,indent=4)