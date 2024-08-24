from llama_index.storage.docstore.mongodb import MongoDocumentStore
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    SimpleDirectoryReader,
    Settings,
)
from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client
from llama_index.embeddings.fastembed import FastEmbedEmbedding
from dotenv import load_dotenv

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

load_dotenv()

logging.info('loaded the dot evnv')
mongo_uri = 'mongodb://localhost:27017/'

client = qdrant_client.QdrantClient(
    # you can use :memory: mode for fast and light-weight experiments,
    # it does not require to have Qdrant deployed anywhere
    # but requires qdrant-client >= 1.1.1
    # location=":memory:"
    # otherwise set Qdrant instance address with:
    # url="http://<host>:<port>"
    # otherwise set Qdrant instance with host and port:
    host="localhost",
    port=6333
    # set API KEY for Qdrant Cloud
    # api_key="<qdrant-api-key>",
)
logging.info('succesfully made the client for qdrant')

client = qdrant_client.QdrantClient(location=":memory:")
vector_store = QdrantVectorStore(
    client=client, collection_name="fruit_collection"
)

logging.info('succesfully made qdrant  vector store')

documents = SimpleDirectoryReader("example3-pdfs",recursive=True).load_data()
logging.info('succesfully readed documents')

embed_model = FastEmbedEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.embed_model = embed_model


logging.info('succesfully loaded the fast embeddings')

# create parser and parse document into nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)
logging.info('succesfully made nodes')


# create (or load) docstore and add nodes
docstore = MongoDocumentStore.from_uri(uri=mongo_uri)
logging.info('successfully made doc store')

docstore.add_documents(nodes)
logging.info('successfully loaded in the doc store')


# create storage context
storage_context = StorageContext.from_defaults(docstore=docstore, vector_store=vector_store)
logging.info('successfully made storage_context')

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)
logging.info('successfullly made the index')

