# test_resource_group_plugin.py
import pytest
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential
from src.resource_group_plugin import ResourceGroupPlugin
from unittest.mock import patch, MagicMock

@pytest.fixture
def resource_group_plugin():
    with patch.object(DefaultAzureCredential, '__init__', lambda self: None):
        plugin = ResourceGroupPlugin()
        plugin.client = MagicMock(spec=ResourceManagementClient)
        return plugin

def test_create_resource_group(resource_group_plugin):
    resource_group_plugin.client.resource_groups.create_or_update.return_value = {'name': 'test_rg'}
    result = resource_group_plugin.create('test_rg')
    assert result['name'] == 'test_rg'

def test_read_resource_group(resource_group_plugin):
    resource_group_plugin.client.resource_groups.get.return_value = {'name': 'test_rg'}
    result = resource_group_plugin.read('test_rg')
    assert result['name'] == 'test_rg'

def test_update_resource_group(resource_group_plugin):
    resource_group_plugin.client.resource_groups.get.return_value = {'name': 'test_rg'}
    resource_group_plugin.client.resource_groups.create_or_update.return_value = {'name': 'new_test_rg'}
    result = resource_group_plugin.update('test_rg', 'new_test_rg')
    assert result['name'] == 'new_test_rg'

def test_delete_resource_group(resource_group_plugin):
    delete_operation = MagicMock()
    delete_operation.wait.return_value = None
    resource_group_plugin.client.resource_groups.begin_delete.return_value = delete_operation
    resource_group_plugin.delete('test_rg')
    resource_group_plugin.client.resource_groups.begin_delete.assert_called_with('test_rg')