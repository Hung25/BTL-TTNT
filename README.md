# Phân tích Cảm xúc Tiếng Việt với BERTweet

Dự án sử dụng mô hình ngôn ngữ BERTweet kết hợp với từ điển cảm xúc để phân tích cảm xúc văn bản tiếng Việt. Ứng dụng hỗ trợ phân tích cảm xúc từng từ, cụm từ, từ ghép, thành ngữ/tục ngữ và toàn bộ câu, hiển thị kết quả trực quan với biểu đồ và phân loại chi tiết.

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
- **Phân tích từng từ**: Hiển thị loại cảm xúc (tích cực, tiêu cực, trung lập) và điểm số của từng từ, từ ghép, thành ngữ/tục ngữ.
- **Phân tích toàn câu**: Hiển thị cảm xúc chính (tích cực, tiêu cực, trung lập) và độ tin cậy, cùng biểu đồ trực quan.
- **Quản lý từ điển**: Cho phép thêm, tìm kiếm và quản lý từ điển cảm xúc, từ ghép, thành ngữ/tục ngữ và biểu tượng cảm xúc.

## Cấu trúc dự án

- `app.py`: Ứng dụng web Streamlit.
- `src/sentence_analysis.py`: Phân tích cảm xúc toàn câu.
- `src/word_analysis.py`: Phân tích cảm xúc từng từ, từ ghép và thành ngữ/tục ngữ.
- `dictionary/dict_manager.py`: Quản lý từ điển cảm xúc.
- `dictionary/json/`: Thư mục chứa các từ điển JSON:
  - `sentiment_dict_data.json`: Từ điển cảm xúc từ đơn.
  - `compound_words_data.json`: Từ ghép và cụm từ.
  - `proverbs_data.json`: Thành ngữ và tục ngữ.
  - `intensifier_words_data.json`: Từ tăng cường.
  - `diminisher_words_data.json`: Từ giảm nhẹ.
  - `negation_words_data.json`: Từ phủ định.
  - `punctuation_analysis_data.json`: Phân tích dấu câu.
- `config.py`: Cấu hình dự án.

## Yêu cầu hệ thống

- Python 3.8+
- CUDA-capable GPU (khuyến nghị)
- RAM tối thiểu 8GB

## Tính năng nổi bật

### 1. Tương thích với nhiều loại từ
- **Phân tích thành ngữ/tục ngữ**: Nhận diện và phân tích cảm xúc của các thành ngữ/tục ngữ tiếng Việt.
- **Xử lý từ ghép và cụm từ**: Phân tích cảm xúc của các từ ghép và cụm từ.
- **Từ tăng cường và giảm nhẹ**: Xử lý các từ tăng cường và giảm nhẹ cảm xúc (ví dụ: "rất", "quá", "hơi").

### 2. Lưu trữ và quản lý từ điển
- **Từ điển JSON**: Tất cả các từ điển được lưu trữ dưới dạng JSON để dễ dàng cập nhật và quản lý.
- **Bảng điều khiển thân thiện**: Giao diện web cho phép thêm, tìm kiếm và quản lý các từ trong từ điển.

### 3. Phân tích cảm xúc chính xác
- **Ưu tiên phân tích**: Thứ tự ưu tiên trong phân tích: thành ngữ/tục ngữ > cụm từ > từ ghép > từ đơn.
- **Biểu đồ cảm xúc trực quan**: Hiển thị cảm xúc bằng biểu đồ tròn để dễ dàng nắm bắt.
- **Mô tả chi tiết**: Hỗ trợ hiển thị mô tả cho từng từ/cụm từ và độ tin cậy của phân tích.

## Hệ thống thử nghiệm

- Python 3.10
- CPU i3-10105f
- GPU RX5600 Vram-6GB
- RAM 16GB
