import os

from langchain.llms import OpenAI

API_SECRET_KEY = "sk-zk2db737fb7225636d3444c99de64c78cdd66092248dd3d0"
BASE_URL = "https://flag.smarttrot.com/v1/"

# 是指api密钥以及访问节点
os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_API_BASE"] = BASE_URL


def text():
    # 创建一个llm模型
    llm = OpenAI(temperature=0.9)
    text = "鲁迅是谁?"
    print(llm(text))


if __name__ == '__main__':
    text()