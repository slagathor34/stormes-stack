# resource_group_plugin.py
from src.plugin import Plugin

class ResourceGroupPlugin(Plugin):
    def create(self, name):
        print(f"Creating Resource Group: {name}")

    def read(self, name):
        print(f"Reading Resource Group: {name}")

    def update(self, name, new_name):
        print(f"Updating Resource Group: {name} to {new_name}")

    def delete(self, name):
        print(f"Deleting Resource Group: {name}")