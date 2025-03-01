import json
import os

def validate_config(config):
  if ("PathToFolder" in config):
      if os.path.isdir(config["PathToFolder"]):
          print("All is well")
      else:
         raise Exception("The config file's 'PathToFolder' property is not a folder in the file system.")    
  else:
      raise Exception("The config file must contain a property called 'PathToFolder'.")

with open('config.json', 'r') as file:
    config = json.load(file)

validate_config(config)