## BTC price mcp server

> This repo is used to get btc price, data powered by APRO_Oracle.

### How to use

1. envs 
  copy `.env.example` to `.env` and set environments in the below
```dotenv
FEEDID= # APRO feed id
AUTH= # APRO auth token
PORT= # current mcp server port
```

2. Start server
```commandline
python server.py 
```

3. [example for client](client.py)

### Use MCP Inspector Test in Local
update the `transport` to `stdio` in the file [server.py](server.py), then run the command to start a web dashboard.
```commandline
npx -y @modelcontextprotocol/inspector uv run server.py
```