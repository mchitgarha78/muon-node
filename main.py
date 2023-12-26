from abstracts.validators import NodeValidators
from abstracts.node_data_manager import NodeDataManager
from abstracts.node_info import NodeInfo
from abstracts.node_info import NodeInfo
from pyfrost.network.node import Node
from pyfrost.network.abstract import DataManager
from libp2p.crypto.secp256k1 import create_new_key_pair
from libp2p.peer.id import ID as PeerID
from dotenv import load_dotenv
from typing import Dict
import logging
import os
import trio
import types
import requests
import json


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
                    # TODO: Where should be used?
                    self.app_data[id] = json.dumps(data)
                # TODO: Revert to 5 mins after testing.
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


if __name__ == "__main__":

    load_dotenv()
    file_path = 'logs'
    file_name = 'node.log'
    log_formatter = logging.Formatter('%(asctime)s - %(message)s', )
    root_logger = logging.getLogger()
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with open(f'{file_path}/{file_name}', 'w'):
        pass
    file_handler = logging.FileHandler(f'{file_path}/{file_name}')
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)
    root_logger.setLevel(logging.DEBUG)

    node_number = os.getenv('NODE_ID')
    data_manager = NodeDataManager()
    node_info = NodeInfo()
    all_nodes = node_info.get_all_nodes()
    # TODO: Add multi instance 
    secret = bytes.fromhex(os.getenv('PRIVATE_KEY'))
    key_pair = create_new_key_pair(secret)
    peer_id: PeerID = PeerID.from_pubkey(key_pair.public_key)
    logging.info(f'Public Key: {key_pair.public_key.serialize().hex()}, PeerId: {peer_id.to_base58()}')
    address = node_info.lookup_node(peer_id.to_base58())[0]
    muon_node = MuonNode(os.getenv('APPS_LIST_URL'), data_manager, address, os.getenv('PRIVATE_KEY'), node_info, NodeValidators.caller_validator,
                         NodeValidators.data_validator)

    try:
        trio.run(muon_node.run_process)
    except KeyboardInterrupt:
        pass
