# test_plugins.py
import pytest
from src.resource_group_plugin import ResourceGroupPlugin
from src.vnet_plugin import VNetPlugin
from src.storage_account_plugin import StorageAccountPlugin
from src.virtual_machine_plugin import VirtualMachinePlugin
from src.plugin_manager import PluginManager

@pytest.fixture
def plugin_manager():
    manager = PluginManager()
    manager.register_plugin('resource_group', ResourceGroupPlugin())
    manager.register_plugin('vnet', VNetPlugin())
    manager.register_plugin('storage_account', StorageAccountPlugin())
    manager.register_plugin('virtual_machine', VirtualMachinePlugin())
    return manager

def test_create_resource_group(plugin_manager):
    plugin_manager.execute('resource_group', 'create', 'test_rg')

def test_read_resource_group(plugin_manager):
    plugin_manager.execute('resource_group', 'read', 'test_rg')

def test_update_resource_group(plugin_manager):
    plugin_manager.execute('resource_group', 'update', 'test_rg', 'new_test_rg')

def test_delete_resource_group(plugin_manager):
    plugin_manager.execute('resource_group', 'delete', 'test_rg')

def test_create_vnet(plugin_manager):
    plugin_manager.execute('vnet', 'create', 'test_vnet')

def test_read_vnet(plugin_manager):
    plugin_manager.execute('vnet', 'read', 'test_vnet')

def test_update_vnet(plugin_manager):
    plugin_manager.execute('vnet', 'update', 'test_vnet', 'new_test_vnet')

def test_delete_vnet(plugin_manager):
    plugin_manager.execute('vnet', 'delete', 'test_vnet')

def test_create_storage_account(plugin_manager):
    plugin_manager.execute('storage_account', 'create', 'test_sa')

def test_read_storage_account(plugin_manager):
    plugin_manager.execute('storage_account', 'read', 'test_sa')

def test_update_storage_account(plugin_manager):
    plugin_manager.execute('storage_account', 'update', 'test_sa', 'new_test_sa')

def test_delete_storage_account(plugin_manager):
    plugin_manager.execute('storage_account', 'delete', 'test_sa')

def test_create_virtual_machine(plugin_manager):
    plugin_manager.execute('virtual_machine', 'create', 'test_vm')

def test_read_virtual_machine(plugin_manager):
    plugin_manager.execute('virtual_machine', 'read', 'test_vm')

def test_update_virtual_machine(plugin_manager):
    plugin_manager.execute('virtual_machine', 'update', 'test_vm', 'new_test_vm')

def test_delete_virtual_machine(plugin_manager):
    plugin_manager.execute('virtual_machine', 'delete', 'test_vm')