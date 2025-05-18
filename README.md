# Phân tích Cảm xúc Tiếng Việt với BERTweet

## Giới thiệu

Đây là dự án phân tích cảm xúc cho văn bản tiếng Việt sử dụng mô hình BERTweet. Dự án cung cấp một giao diện web để người dùng có thể nhập văn bản, nhận kết quả phân tích cảm xúc chi tiết, quản lý từ điển tùy chỉnh, xem lại lịch sử phân tích và xuất báo cáo.

## Tính năng chính

- **Phân tích Cảm xúc**: Sử dụng mô hình BERTweet để phân loại cảm xúc (tích cực, tiêu cực, trung lập) cho văn bản tiếng Việt.
- **Phân tích Từ và Câu**: Cung cấp phân tích cảm xúc ở cả cấp độ từ và câu.
- **Quản lý Từ điển**: Cho phép tùy chỉnh và mở rộng từ điển cảm xúc, từ ghép, từ phủ định, tăng cường, giảm nhẹ, thành ngữ/tục ngữ và dấu câu.
- **Lịch sử Phân tích**: Lưu trữ và hiển thị lịch sử các lần phân tích đã thực hiện.
- **Xuất Báo cáo**: Tạo báo cáo kết quả phân tích dưới định dạng DOCX.
- **Huấn luyện lại Mô hình (Tùy chọn)**: Hỗ trợ khả năng huấn luyện lại mô hình với dữ liệu mới (tính năng đang phát triển/có thể mở rộng).

## Cài đặt

Để cài đặt và chạy dự án, làm theo các bước sau:

1.  **Clone repository** (nếu có)

    ```bash
    git clone <gh repo clone Hung25/BTL-TTNT>
    cd BTL-TTNT
    ```

2.  **Cài đặt các thư viện cần thiết**: 

    Đảm bảo bạn đã cài đặt Python 3.6+ và `pip`. Sử dụng file `requirements.txt` để cài đặt các dependency:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Tải mô hình BERTweet**: (Bước này có thể được xử lý tự động bởi thư viện `transformers` khi chạy lần đầu, nhưng nếu cần tải thủ công)

    Mô hình `vinai/bertweet-base` sẽ được tải xuống tự động khi `SentenceAnalyzer` được khởi tạo lần đầu.

4.  **Cấu hình (Tùy chọn)**:
    - Chỉnh sửa `config.py` để thay đổi các cấu hình chung như ngưỡng điểm, trọng số.
    - Chỉnh sửa các file JSON trong thư mục `dictionary/json/` để cập nhật các từ điển tùy chỉnh và cấu hình hiển thị (`sentiment_settings.json`).

## Sử dụng

Để chạy ứng dụng web, sử dụng Streamlit (hoặc Flask tùy thuộc vào cách triển khai `app.py`):

Nếu sử dụng Streamlit (như trong các thảo luận trước):

```bash
streamlit run app.py
```

Ứng dụng sẽ mở trong trình duyệt web của bạn. Bạn có thể:

- Nhập văn bản vào ô input.
- Nhấn nút phân tích để xem kết quả chi tiết.
- Truy cập các mục Lịch sử Phân tích và Xuất Báo cáo trên giao diện (nếu được triển khai).

Nếu sử dụng Flask:

```bash
python app.py
```

Và truy cập ứng dụng qua địa chỉ hiển thị trên terminal (thường là `http://127.0.0.1:5000`).

## Cấu trúc Dự án

```
BTL-TTNT/
├── .devcontainer/
├── dictionary/
│   ├── json/          # Chứa các file JSON của từ điển
│   └── dict_manager.py  # Lớp quản lý từ điển
├── src/
│   ├── sentence_analysis.py # Logic phân tích câu
│   ├── word_analysis.py   # Logic phân tích từ
│   └── ... (các file khác nếu có)
├── .gitignore
├── app.py           # Điểm khởi chạy ứng dụng chính (Flask/Streamlit)
├── config.py        # File cấu hình chung
├── README.md        # File này
└── requirements.txt   # Danh sách các thư viện cần thiết
```

## Đóng góp

(Phần này có thể thêm hướng dẫn đóng góp nếu dự án là mã nguồn mở)

## Giấy phép

(Phần này có thể thêm thông tin về giấy phép của dự án)