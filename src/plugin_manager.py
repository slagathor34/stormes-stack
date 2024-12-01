# plugin_manager.py
class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        self.plugins[name] = plugin

    def execute(self, plugin_name, operation, *args, **kwargs):
        plugin = self.plugins.get(plugin_name)
        if not plugin:
            raise ValueError(f"Plugin {plugin_name} not found")
        method = getattr(plugin, operation, None)
        if not method:
            raise ValueError(f"Operation {operation} not supported by plugin {plugin_name}")
        return method(*args, **kwargs)