import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA

API_SECRET_KEY = "sk-zk2db737fb7225636d3444c99de64c78cdd66092248dd3d0"
BASE_URL = "https://flag.smarttrot.com/v1/"

# 是指api密钥以及访问节点
os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_API_BASE"] = BASE_URL

# 加载文件夹中的所有txt类型的文件
loader = DirectoryLoader('D:\pythonprojects\langchain_learn\data_enhance\content\sample_data\data', glob='**/*.txt')
# 将数据转成 document 对象，每个文件会作为一个 document
documents = loader.load()

# 初始化加载器
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
# 切割加载的 document
split_docs = text_splitter.split_documents(documents)

# 初始化 openai 的 embeddings 对象
embeddings = OpenAIEmbeddings()
# 将 document 通过 openai 的 embeddings 对象计算 embedding 向量信息并临时存入 Chroma 向量数据库，用于后续匹配查询
docsearch = Chroma.from_documents(split_docs, embeddings)

# 创建问答对象
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(),
                                 return_source_documents=True)
# 进行问答
result = qa({"query": "科大讯飞今年第一季度收入是多少？"})
print(result)
