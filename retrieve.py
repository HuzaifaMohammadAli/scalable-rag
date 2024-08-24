import qdrant_client
from llama_index.embeddings.fastembed import FastEmbedEmbedding

embed_model = FastEmbedEmbedding(model_name="BAAI/bge-base-en-v1.5")

# encoder=SentenceTransformer('BAAI/bge-large-zh-v1.5')
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
text = """
1000 Chapter 25. Robotics\nstartgoal\n start goal\n(a) (b)\nFigure 25.23 Potential \ufb01eld control. The robot ascends a potential \ufb01eld composed of\nrepelling forces asserted from the obstacles and an attracting force that corresponds to thegoal con\ufb01guration. (a) Successful path. (b) Local optimum.\nthe goal con\ufb01guration, and the value is the sum of the distance to this goal con\ufb01guration\nand the proximity to obstacles. No planning was involved in generating the potential \ufb01eldshown in the \ufb01gure. Because of this, potential \ufb01elds are well suited to real-time control.Figure 25.23(a) shows a trajectory of a robot that performs hill climbing in the potential\ufb01eld. In many applications, the potential \ufb01eld can be calculated ef\ufb01ciently for any givencon\ufb01guration. Moreover, optimizing the potential amounts to calculating the gradient of the\npotential for the present robot con\ufb01guration. These calculations can be extremely ef\ufb01cient,\nespecially when compared to path-planning algorithms, all of which are exponential in thedimensionality of the con\ufb01guration space (the DOFs) in the worst case.\nThe fact that the potential \ufb01eld approach manages to \ufb01nd a path to the goal in such\nan ef\ufb01cient manner, even over long distances in con\ufb01guration space, raises the question as\nto whether there is a need for planning in robotics at all. Are potential \ufb01eld techniques\nsuf\ufb01cient, or were we just lucky in our example? The answer is that we were indeed lucky.\nPotential \ufb01elds have many local minima that can trap the robot. In Figure 25.23(b), the robotapproaches the obstacle by simply rotating its shoulder joint, until it gets stuck on the wrongside of the obstacle. The potential \ufb01eld is not rich enough to make the robot bend its elbowso that the arm \ufb01ts under the obstacle. In other words, potential \ufb01eld control is great for local\nrobot motion but sometimes we still need global planning. Another important drawback with\npotential \ufb01elds is that the forces they generate depend only on the obstacle and robot positions,not on the robot\u2019s velocity. Thus, potential \ufb01eld control is really a kinematic method and mayfail if the robot is moving quickly.
"""
hits = client.search(
    collection_name="fruit_collection",
    query_vector=embed_model.get_text_embedding(text),
    limit=3,
)
for hit in hits:
    print(hit.payload, "score:", hit.score)