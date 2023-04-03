from utils import Utils
import json
import os

class Boiler(Utils):
  def __init__(self):
    super().__init__()

  def node(self, name, deps="None"):
    pwd = self.run_cmd("pwd")
    path = self.prepare_path(pwd, name)

    self.run_cmd(["chmod", "+x", "src/cli/node.sh"])
    # lazy way of doing this
    self.run_cmd(["/home/kata/boilerplate/cli/node.sh", path])

    try:
      with open(f'{path}/package.json', 'r') as f1, open(f'{path}/package.json.tmp', 'w') as f2:
        content = json.load(f1)
        scripts = content.get('scripts', {})
        scripts['start'] = 'node src/index.js'
        scripts['dev'] = 'nodemon src/index.js'
        content['scripts'] = scripts
        json.dump(content, f2, indent=2)
        os.replace(f'{path}/package.json.tmp', f'{path}/package.json')
    except (IOError, json.JSONDecodeError) as e:
      print("Error:", e)
      return

    if deps != "None":
      self.load_node_deps(deps, path)

  def load_node_deps(self, type, path):
    if type == "express-server":
      os.chdir(path)
      self.run_cmd(["npm", "install", "express", "body-parser", "cors", ])
      self.run_cmd(["npm", "install", "--save-dev", "nodemon"])
    else:
      print("Error: Unknown type")

    
        