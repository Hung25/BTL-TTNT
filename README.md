# Phân tích Cảm xúc Tiếng Việt với PhoBERT

Dự án sử dụng mô hình ngôn ngữ PhoBERT để phân tích cảm xúc văn bản tiếng Việt.

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

### 1. Tải dữ liệu
```bash
python get_data.py
```

### 2. Huấn luyện mô hình
```bash
python train_phobert.py
```

### 3. Chạy ứng dụng web
```bash
streamlit run app.py
```

## Cấu trúc dự án

- `app.py`: Ứng dụng web Streamlit
- `train_phobert.py`: Huấn luyện mô hình PhoBERT
- `get_data.py`: Tải dữ liệu từ Hugging Face
- `config.py`: Cấu hình dự án
- `utils.py`: Tiện ích và xử lý lỗi
- `evaluate.py`: Đánh giá mô hình

## Thư mục

- `phobert_sentiment_model/`: Lưu mô hình đã huấn luyện
- `logs/`: Lưu file log
- `data/`: Lưu dữ liệu

## Đánh giá mô hình

Chạy lệnh sau để đánh giá mô hình:
```bash
python evaluate.py
```

## Yêu cầu hệ thống

- Python 3.8+
- CUDA-capable GPU (khuyến nghị)
- RAM tối thiểu 8GB 

## Hệ thống thử nghiệm

- Python 3.10
- CPU i3-10105f
- GPU RX5600 Vram-6GB
- RAM 16GB 