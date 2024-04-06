import os

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import AgentType

os.environ["SERPAPI_API_KEY"] = '4745fc0739c5152f60255e7758298665b5ad47c49c3006bcfd1c3d209a98f57b'
API_SECRET_KEY = "sk-zk2db737fb7225636d3444c99de6adasdasdasdqwrqt"
BASE_URL = "https://flag.smarttrot.com/v1/"

# 是指api密钥以及访问节点
os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_API_BASE"] = BASE_URL

# 加载 OpenAI模型
llm = OpenAI(temperature=0)

# 加载serpapi工具
tools = load_tools(["serpapi"])

# 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
#  OpenAI api 联网搜索，并返回答案给我们
# zero-shot-react-description: 根据工具的描述和请求内容的来决定使用哪个工具（最常用）
# 在 chain 和 agent 对象上都会有 verbose 这个参数，这个是个非常有用的参数，开启他后我们可以看到完整的 chain 执行过程
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 运行 agent
agent.run("What's the date today? What great events have taken place today in history?")

