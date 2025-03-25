# chromaDB
build chromaDB

1. 啟動 ChromaDB Server（使用 Docker）
```bash
docker compose up -d
```

2. 安裝 Python 套件 (要使用 python 3.10 以上)
```bash
pip install sentence-transformers chromadb requests
```

3. 執行主程式 (寫了最基本會用到板塊，學長有其他需要的 method 可以看這裡: https://docs.trychroma.com/docs/collections/create-get-delete)
```bash
python chroma_test.py
```
