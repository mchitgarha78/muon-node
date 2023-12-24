from muon_node import MuonNode
from abstracts.validators import NodeValidators
from abstracts.node_data_manager import NodeDataManager
from abstracts.node_info import NodeInfo
from config import SECRETS
import logging
import sys
import os
import trio

if __name__ == "__main__":

    file_path = 'logs'
    file_name = 'test.log'
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

    node_number = int(sys.argv[1])
    data_manager = NodeDataManager(node_number + 1)
    node_info = NodeInfo()
    all_nodes = node_info.get_all_nodes()
    # TODO: Add multi instance
    peer_id = all_nodes[str(node_number + 1)][0]
    address = node_info.lookup_node(peer_id)[0]
    registry_url = 'http://127.0.0.1:8050/v1'
    muon_node = MuonNode(registry_url, data_manager, address, SECRETS[peer_id], node_info, NodeValidators.caller_validator,
                         NodeValidators.data_validator)

    try:
        trio.run(muon_node.run_process)
    except KeyboardInterrupt:
        pass
