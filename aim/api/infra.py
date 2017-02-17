# Copyright (c) 2016 Cisco Systems
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from aim.api import resource
from aim.api import types as t


class HostLink(resource.ResourceBase):
    """Switch-port connection information for a host node."""

    identity_attributes = t.identity(
        ('host_name', t.string(36)),
        ('interface_name', t.string(36)))
    other_attributes = t.other(
        ('interface_mac', t.mac_address),
        ('switch_id', t.string()),
        ('module', t.string()),
        ('port', t.string()),
        ('path', t.string()))

    def __init__(self, **kwargs):
        super(HostLink, self).__init__({'interface_mac': '',
                                        'switch_id': '',
                                        'module': '',
                                        'port': '',
                                        'path': ''}, **kwargs)
