from common.node_info import NodeInfo
from common.node_data_manager import NodeDataManager
from common.validators import Validators

from muon_frost_py.common.configuration_settings import ConfigurationSettings
from muon_frost_py.node.node import Node

from node_config import SECRETS

import logging
import sys
import trio




async def run(node_number: int) -> None:
    node_info = NodeInfo()
    id = node_info.get_all_nodes()[node_number]
    data_manager = NodeDataManager()
    node = Node(data_manager, node_info.lookup_node(id), SECRETS[id], node_info, 
                Validators.caller_validator, Validators.data_validator)
    await node.run()

if __name__ == "__main__":


    # Define the logging configurations
    ConfigurationSettings.set_logging_options \
                        ('logs', f'node{sys.argv[1]}.log')
    
    # Increase the string max limit for integer string conversion
    sys.set_int_max_str_digits(0)

    node_number = int(sys.argv[1])
    try:
        # Run the libp2p node
        trio.run(run, node_number)
    except KeyboardInterrupt:
        pass