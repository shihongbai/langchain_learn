import os

from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import OpenAI

API_SECRET_KEY = "sk-zk2db737fb7225636d3444c99de64c78cdd66092248dd3d0"
BASE_URL = "https://flag.smarttrot.com/v1/"

# 是指api密钥以及访问节点
os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_API_BASE"] = BASE_URL

llm = OpenAI(model_name="text-davinci-003")

# 告诉他我们生成的内容需要哪些字段，每个字段类型式啥
response_schemas = [
    ResponseSchema(name="bad_string", description="This a poorly formatted user input string"),
    ResponseSchema(name="good_string", description="This is your response, a reformatted response")
]

# 初始化解析器
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# 生成的格式提示符
# {
#	"bad_string": string  // This a poorly formatted user input string
#	"good_string": string  // This is your response, a reformatted response
# }
format_instructions = output_parser.get_format_instructions()

template = """
You will be given a poorly formatted string from a user.
Reformat it and make sure all the words are spelled correctly

{format_instructions}

% USER INPUT:
{user_input}

YOUR RESPONSE:
"""

# 将我们的格式描述嵌入到 prompt 中去，告诉 llm 我们需要他输出什么样格式的内容
prompt = PromptTemplate(
    input_variables=["user_input"],
    partial_variables={"format_instructions": format_instructions},
    template=template
)
#
# promptValue = prompt.format(user_input="welcom to califonya!")
# llm_output = llm(prompt.format(user_input="welcom to califonya!"))

# 使用解析器进行解析生成的内容
output_parser.parse(llm(prompt.format(user_input="welcom to califonya!")))
