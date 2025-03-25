import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings


host = os.getenv("CHROMA_HOST", "chromadb_server") 
port = int(os.getenv("CHROMA_PORT", 8000))

#換成你需要的 embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

chroma_client = chromadb.HttpClient(host='chromadb_server', port=8000)

# 檢查連線是否正常（heartbeat）
print("Heartbeat:", chroma_client.heartbeat())

# 建立名為 "alpha_formulas" 的 collection (若已建立則會變為取得該 collection)
collection = chroma_client.get_or_create_collection("alpha_formulas")
print("Collection 已建立或取得。")

# alpha 資料
alpha_data = [
    {
        "id": "alpha_01",
         "document": (
        "Alpha 1: rank(Ts_ArgMax(SignedPower((returns<0?stddev(returns,20):close), 2), 5))-0.5\n\n"
        "def WQAlpha1(close){\n"
        "    ts = mimax(pow(iif(ratios(close) - 1 < 0, mstd(ratios(close) - 1, 20), close), 2.0), 5)\n"
        "    return rowRank(X=ts, percent=true) - 0.5\n"
        "}"
    ),
        "metadata": {
            "source": "wq101 alpha"
        }
    },
     {
        "id": "alpha_02",
        "document": ("(-1 * correlation(rank(delta(log(volume), 2)), rank(((close - open) / open)), 6))\n\n"
        "def WQAlpha2(vol, close, open){\n"
        "delta = log(vol) - log(mfirst(vol, 3))\n"
        "rank1 = rowRank(delta, percent=true)\n"
        "rank2 = rowRank((close - open) \ open, percent=true)\n"
        "return -mcorr(rank1, rank2, 6)\n"
        "}"
    ),
        "metadata": {
            "source": "wq101 alpha"
        }
    }

]

# 從 alpha_data 中提取各項資訊
ids = [item["id"] for item in alpha_data]
documents = [item["document"] for item in alpha_data]
metadatas = [item["metadata"] for item in alpha_data]
embeddings = model.encode(documents)

# 將資料加入 collection
collection.add(
    documents=documents,
    ids=ids,
    embeddings=embeddings,
    metadatas=metadatas
)
print("Alpha 資料已成功加入 collection。")

# 簡單查詢
query_result = collection.query(
    query_texts=["close"],
    n_results=2
)
print("查詢結果：", query_result)

# 查看整個 collection 內容
print("Collection 全部資料：", collection.get())
