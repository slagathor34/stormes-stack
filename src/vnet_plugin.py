# vnet_plugin.py
from src.plugin import Plugin

class VNetPlugin(Plugin):
    def create(self, name):
        print(f"Creating VNet: {name}")

    def read(self, name):
        print(f"Reading VNet: {name}")

    def update(self, name, new_name):
        print(f"Updating VNet: {name} to {new_name}")

    def delete(self, name):
        print(f"Deleting VNet: {name}")