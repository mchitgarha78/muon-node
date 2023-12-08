from muon_frost_py.common.configuration_settings import ConfigurationSettings
from node_process import NodeProcess
import logging
import sys
import trio





 
if __name__ == "__main__":


    # Define the logging configurations
    ConfigurationSettings.set_logging_options \
                        ('logs', f'node{sys.argv[1]}.log')
    
    # Increase the string max limit for integer string conversion
    sys.set_int_max_str_digits(0)

    node_number = int(sys.argv[1])
    registry_url = ''
    node_process = NodeProcess(registry_url)
    
    try:
        # Run the libp2p node
        trio.run(node_process.run, node_number)
    except KeyboardInterrupt:
        pass