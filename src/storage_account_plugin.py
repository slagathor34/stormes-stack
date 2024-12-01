# storage_account_plugin.py
from src.plugin import Plugin

class StorageAccountPlugin(Plugin):
    def create(self, name):
        print(f"Creating Storage Account: {name}")

    def read(self, name):
        print(f"Reading Storage Account: {name}")

    def update(self, name, new_name):
        print(f"Updating Storage Account: {name} to {new_name}")

    def delete(self, name):
        print(f"Deleting Storage Account: {name}")