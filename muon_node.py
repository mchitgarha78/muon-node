import json
from common.node_info import NodeInfo
from pyfrost.network.node import Node
from pyfrost.network.abstract import DataManager
from typing import Dict

import types
import requests
import trio
import logging


class MuonNode(Node):
    def __init__(self, registry_url, data_manager: DataManager, address: Dict[str, str],
                 secret: str, node_info: NodeInfo, caller_validator: types.FunctionType,
                 data_validator: types.FunctionType) -> None:

        super().__init__(data_manager, address,
                         secret, node_info, caller_validator,
                         data_validator)
        self.registry_url = registry_url
        self.app_data = {}

    async def maintain_dkg_list(self):
        while True:
            try:
                new_data: Dict = requests.get(self.registry_url).json()
                for id, data in new_data.items():
                    self.app_data[id] = json.dumps(data)
                await trio.sleep(5)  # wait for 5 mins
            except Exception as e:
                logging.error(
                    f'Muon Node => Exception occurred.{type(e).__name__}: {e}')
                await trio.sleep(1)
                continue

    async def run_process(self) -> None:
        async with trio.open_nursery() as nursery:
            nursery.start_soon(self.run)
            nursery.start_soon(self.maintain_dkg_list)
