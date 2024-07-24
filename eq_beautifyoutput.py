from pathlib import Path
import json

path = Path('eq_data/2024_july.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

