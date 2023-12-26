# Muon Node

This implementation represents Muon-Node version of [pyfrost](https://github.com/SAYaghoubnejad/pyfrost) library to run Nodes.

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
APPS_LIST_URL=<your-apps-url>
```

You also need to configure your `nodes.json` file in `abstracts` directory:

```bash
(venv) $ cp ./abstracts/nodes.json.example ./abstracts/nodes.json
```

Get your nodes data and add it to `nodes.json` file. 



## How to Run

Type the following command to run Muon node:

```bash
(venv) $ python main.py [nod id number] [resgistry apps data url]
```


When you run your node, the first lines illustrate your `Public key` and your `Peer ID`. You can add this data to your `nodes.json` files of all nodes, registry, and sa.
