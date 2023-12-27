# Muon Node

Muon-Node uses the [pyfrost](https://github.com/SAYaghoubnejad/pyfrost) library to implement a Python client for Muon network. Muon-Node along with the [Muon-SA](https://github.com/mchitgarha78/muon-sa), the [Muon-Registry](https://github.com/mchitgarha78/muon-registry), and apps runners ([python apps runner](https://github.com/mchitgarha78/muon-py-apps) and [js apps runner](https://github.com/mchitgarha78/muon-js-apps/tree/main)) represent the core of the Muon network to deploy and run apps and issue threshold signatures. For more insight on the Muon network, please read our [document](https://github.com/mchitgarha78/muon-node/wiki) describing the main functionalities of the muon system.

## How to Setup

To create a virtual environment (`venv`) and install the required packages, run the following commands:

```bash
$ git clone https://github.com/mchitgarha78/muon-node.git 
$ cd muon-node
$ virtualenv -p python3.10 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

**Note:** The required Python version is `3.10`.


After these installations, configure `.env` file. The file `.env.example` has the example of thie environment variables. So you can type the following command:
```bash
(venv) $ cp .env.example .env
```

Change your settings in the `.env` file:
```
PRIVATE_KEY=<your-private-key>
NODE_ID=<your-node-id>
HOST=0.0.0.0
PORT=5037
APPS_LIST_URL=<your-apps-list-url>
RUNNER_APP_URL=<your-node-runner_app>
```

You also need to configure your `nodes.json` file in `abstracts` directory:

```bash
(venv) $ cp ./abstracts/nodes.json.example ./abstracts/nodes.json
```

Get your nodes data and add it to `nodes.json` file. 

After running Muon SA and Muon Registry, enhance their permissions to request to node via updating `config.py` file by editing `VALIDATED_CALLES` variable.


## How to Run

Type the following command to run Muon node:

```bash
(venv) $ python main.py [nod id number] [resgistry apps data url]
```


When you run your node, the first lines illustrate your `Public key` and your `Peer ID`. You can add this data to your `nodes.json` files of all nodes, registry, and sa.
