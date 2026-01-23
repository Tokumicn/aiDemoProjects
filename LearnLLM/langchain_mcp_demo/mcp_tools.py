from fastmcp import FastMCP
# from langchain_mcp_adapters.client import MultiServerMCPClient



mcp_server = FastMCP(name="xhMcpServer", instructions="XH 的测试 MCP 服务器")

#
# def my_search(query: str) -> str:
#     """搜索互联网上的内容，包括实时天气"""
#     try:
#         print("执行我的工具，输入参数为：", query)

@mcp_server.tool
def say_hello(username:str) -> str:
    """给用户打个招呼"""
    return f"Hello, {username}!"


@mcp_server.prompt
def ask_about_topic(topic:str) -> str:
    """解释用户传入的主题的含义"""
    return f"解释一下'{topic}'这个概念"


@mcp_server.resource("resource://config")
def get_config() -> dict:
    """已JSON格式获取配置文件"""
    return {
        "username": "tom",
        "password": "<PASSWORD>",
        "age": 22
    }