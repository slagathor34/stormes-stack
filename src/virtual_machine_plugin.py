# virtual_machine_plugin.py
from src.plugin import Plugin

class VirtualMachinePlugin(Plugin):
    def create(self, name):
        print(f"Creating Virtual Machine: {name}")

    def read(self, name):
        print(f"Reading Virtual Machine: {name}")

    def update(self, name, new_name):
        print(f"Updating Virtual Machine: {name} to {new_name}")

    def delete(self, name):
        print(f"Deleting Virtual Machine: {name}")