import subprocess

class Utils:
  def __init__(self):
    pass

  def run_cmd(self, _args = [], stdo = False):
    if stdo:
      out = subprocess.run(_args)
    else:
      out = subprocess.run(_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    return out

  def prepare_path(self, pwd, name):
    path = f'{pwd.stdout.decode("utf-8").strip()}/{name}'

    return path

