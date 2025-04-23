## BTC price mcp

### How to use
1. 部署server
```commandline
python server.py 
```

2. [客户端例子](client.py)

### Use MCP Inspector Test in Local
修改[server.py](server.py)中的transport为`stdio`
```commandline
npx -y @modelcontextprotocol/inspector uv run server.py
```