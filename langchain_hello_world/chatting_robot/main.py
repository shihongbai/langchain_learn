import os

from langchain import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

API_SECRET_KEY = "sk-zk2db737fb7225636d3444c99de64c78cdd66092248dd3d0"
BASE_URL = "https://flag.smarttrot.com/v1/"

# 是指api密钥以及访问节点
os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_API_BASE"] = BASE_URL

if __name__ == '__main__':
    # 初始化ChatOpenAI聊天模型, 泛化参数设为0
    chat = ChatOpenAI(temperature=0)

    # 定义系统消息模板
    template = (
        "You are a helpful assistant that translates {input_language} to"
        "{output_language}"
    )

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    # 定义人类消息模板
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # 将两个模板组合到聊天提示词模板中
    chat_prompt = ChatPromptTemplate.from_messages([
        system_message_prompt,
        human_message_prompt
    ])

    # 使用LLChain组合聊天模型组件和提示词模板
    chain = LLMChain(llm=chat, prompt_toolkit=chat_prompt)

    # 运行链，传入参数
    chain.run(
        input_language="English",
        output_language="Chinese",
        text="I love programming"
    )
