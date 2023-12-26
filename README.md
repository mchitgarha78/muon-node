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

**Note:** Don't forget to set `RUNNER_APP_URL` for your runner app by changing the value of `RUNNER_APP_URL` in `configs.py` directory and also `APPS_LIST_URL` for retrieving the `apps.json`.

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



## How to Run

Type the following command to run Muon node:

```bash
(venv) $ python main.py [nod id number] [resgistry apps data url]
```



