# resource_group_plugin.py
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from plugin import Plugin
import os

class ResourceGroupPlugin(Plugin):
    def __init__(self):
        self.subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
        self.client = ResourceManagementClient(DefaultAzureCredential(), self.subscription_id)

    def create(self, name, location='eastus'):
        """
        Create a resource group.

        :param name: The name of the resource group.
        :param location: The location of the resource group.
        :return: The created resource group.
        """
        resource_group_params = {'location': location}
        resource_group = self.client.resource_groups.create_or_update(name, resource_group_params)
        return resource_group

    def read(self, name):
        """
        Read a resource group.

        :param name: The name of the resource group.
        :return: The resource group details.
        """
        resource_group = self.client.resource_groups.get(name)
        return resource_group

    def update(self, name, new_name):
        """
        Update a resource group.

        :param name: The current name of the resource group.
        :param new_name: The new name of the resource group.
        :return: The updated resource group.
        """
        resource_group = self.client.resource_groups.get(name)
        resource_group.name = new_name
        updated_resource_group = self.client.resource_groups.create_or_update(new_name, resource_group)
        self.client.resource_groups.delete(name)
        return updated_resource_group

    def delete(self, name):
        """
        Delete a resource group.

        :param name: The name of the resource group.
        :return: None
        """
        delete_async_operation = self.client.resource_groups.begin_delete(name)
        delete_async_operation.wait()