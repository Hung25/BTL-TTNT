# Phân tích Cảm xúc Tiếng Việt với BERTweet

Dự án sử dụng mô hình ngôn ngữ BERTweet để phân tích cảm xúc văn bản tiếng Việt. Ứng dụng hỗ trợ phân tích cảm xúc từng từ và toàn bộ câu, hiển thị kết quả trực quan.

## Cài đặt

1. Tạo môi trường ảo Python:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Sử dụng

### 1. Chạy ứng dụng web
```bash
streamlit run app.py
```

### 2. Nhập văn bản
- Nhập văn bản tiếng Việt vào ô nhập liệu.
- Nhấn nút **Phân tích cảm xúc** để xem kết quả.

### 3. Kết quả hiển thị
- **Phân tích từng từ**: Hiển thị loại cảm xúc (tích cực, tiêu cực, trung lập) và điểm số của từng từ hoặc cụm từ.
- **Phân tích toàn câu**: Hiển thị cảm xúc chính (tích cực, tiêu cực, trung lập) và độ tin cậy, cùng biểu đồ trực quan.

## Cấu trúc dự án

- `app.py`: Ứng dụng web Streamlit.
- `src/sentence_analysis.py`: Phân tích cảm xúc toàn câu.
- `src/word_analysis.py`: Phân tích cảm xúc từng từ.
- `dictionary/vietnamese_sentiment_dict.py`: Từ điển cảm xúc tiếng Việt.
- `config.py`: Cấu hình dự án.

## Yêu cầu hệ thống

- Python 3.8+
- CUDA-capable GPU (khuyến nghị)
- RAM tối thiểu 8GB

## Hệ thống thử nghiệm

- Python 3.10
- CPU i3-10105f
- GPU RX5600 Vram-6GB
- RAM 16GB