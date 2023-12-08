from common.node_info import NodeInfo
from common.node_data_manager import NodeDataManager
from common.validators import Validators

from muon_frost_py.node.node import Node
from muon_frost_py.common.utils import Utils

from node_config import SECRETS
from typing import Dict

import trio


class NodeProcess:
    def __init__(self, registry_url) -> None:
        self.data_manager = NodeDataManager()
        self.registry_url = registry_url

    async def run(self, node_number: int) -> None:
        node_info = NodeInfo()
        id = node_info.get_all_nodes()[node_number]
        self.node = Node(self.data_manager, node_info.lookup_node(id), SECRETS[id], node_info, 
                    Validators.caller_validator, Validators.data_validator)
        async with trio.open_nursery() as nursery:
            nursery.start_soon(self.node.run)
            nursery.start_soon(self.maintain_dkg_list)

    async def maintain_dkg_list(self):
        while True:
            new_data: Dict = Utils.get_request(self.registry_url)
            if not new_data:
                await trio.sleep(0.5)
                continue
            for id, data in new_data.items():
                self.data_manager.set_dkg_key(id, data)
            await trio.sleep(5 * 60) # wait for 5 mins