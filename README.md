# chromaDB

colone this repository

1. 啟動 ChromaDB Server（使用 Docker）
```bash
docker compose up -d
```

2. 安裝 Python 套件 (要使用 python 3.10 以上)
```bash
pip install sentence-transformers chromadb requests
```

3. 新增 chroma-data 資料夾在根目錄存放 data
  <img width="238" alt="螢幕擷取畫面 2025-03-25 153818" src="https://github.com/user-attachments/assets/a4cbafb8-00d3-48e1-b290-4fb357805022" />

4. 執行主程式 (寫了最基本會用到板塊，學長有其他需要的 method 可以看這裡: https://docs.trychroma.com/docs/collections/create-get-delete)
```bash
python chroma_test.py
```
