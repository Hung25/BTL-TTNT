import os

# Lấy đường dẫn thư mục gốc của dự án
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Các đường dẫn quan trọng
MODEL_PATH = os.path.join(BASE_DIR, "models")
DICTIONARY_PATH = os.path.join(BASE_DIR, "dictionary")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Cấu hình phân tích cảm xúc
SENTIMENT_CONFIG = {
    "thresholds": {
        "positive": 0.1,     # > 0.1 là tích cực
        "negative": -0.1,    # < -0.1 là tiêu cực
        "neutral": [-0.1, 0.1]  # [-0.1, 0.1] là trung lập
    },
    "weights": {
        "word_level": 0.6,    # Trọng số cho phân tích từ
        "sentence_level": 0.4  # Trọng số cho phân tích câu
    },
    "display": {
        "show_all_scores": True,  # Hiển thị tất cả điểm số
        "normalize_scores": True,  # Chuẩn hóa điểm về [-1, 1]
        "min_confidence": 0.0,    # Ngưỡng độ tin cậy tối thiểu
        "chart_colors": {
            "positive": "#2E7D32",  # Xanh lá
            "neutral": "#757575",   # Xám
            "negative": "#F44336"   # Đỏ
        }
    }
}

# Cấu hình mô hình
MODEL_CONFIG = {
    "tokenizer": "vinai/bertweet-base",
    "model": "vinai/bertweet-base",
    "max_length": 128,
    "batch_size": 32
}

# Cấu hình huấn luyện
TRAINING_ARGS = {
    "num_train_epochs": 3,
    "per_device_train_batch_size": 8,
    "per_device_eval_batch_size": 8,
    "warmup_steps": 500,
    "weight_decay": 0.01,
    "logging_steps": 10
} 