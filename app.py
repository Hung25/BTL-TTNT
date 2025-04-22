import sys
import os

# Lấy đường dẫn tuyệt đối của thư mục gốc
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Thêm các thư mục cần thiết vào PYTHONPATH
sys.path.insert(0, ROOT_DIR)
sys.path.insert(0, os.path.join(ROOT_DIR, "src"))
sys.path.insert(0, os.path.join(ROOT_DIR, "dictionary"))

# Fix for PyTorch and Streamlit compatibility issue
os.environ["STREAMLIT_WATCH_MODULES"] = "false"

import streamlit as st
from word_analysis import analyze_word_sentiment
from sentence_analysis import SentenceAnalyzer

# Cấu hình trang
st.set_page_config(
    page_title="Phân tích cảm xúc tiếng Việt",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Khởi tạo session state
if 'sentence_analyzer' not in st.session_state:
    st.session_state.sentence_analyzer = SentenceAnalyzer()

# Tiêu đề và mô tả
st.title("Phân tích cảm xúc tiếng Việt")
st.markdown("""
    Ứng dụng phân tích cảm xúc văn bản tiếng Việt, hỗ trợ:
    - Phân tích từng từ và cụm từ
    - Xác định cảm xúc tích cực, tiêu cực, trung lập
    - Hiển thị kết quả trực quan
""")

# Ô nhập văn bản
text = st.text_area("Nhập văn bản cần phân tích:", height=100, help="Nhập văn bản tiếng Việt cần phân tích cảm xúc")

# Xử lý phân tích
if st.button("Phân tích cảm xúc"):
    if not text.strip():
        st.warning("⚠️ Vui lòng nhập văn bản cần phân tích!")
    else:
        try:
            with st.spinner('Đang phân tích...'):
                # Phân tích từ ngữ
                word_analysis = analyze_word_sentiment(text)
                
                # Phân tích câu văn
                sentence_analysis = st.session_state.sentence_analyzer.analyze_sentence(text, word_analysis)
                
                # Hiển thị kết quả
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📝 Phân tích từng từ")
                    
                    # Tạo bảng phân tích từ
                    word_data = []
                    total_score = 0
                    
                    # Lưu điểm số trước khi xử lý dấu câu
                    pre_punct_score = 0
                    punct_effect = 0
                    
                    for word in word_analysis["words"]:
                        # Xác định loại cảm xúc
                        sentiment_type = {
                            "positive": "Tích cực 🟢",
                            "negative": "Tiêu cực 🔴",
                            "neutral": "Trung lập ⚪",
                            "negation": "Phủ định ❌",
                            "intensifier": "Tăng cường ⬆️",
                            "diminisher": "Giảm nhẹ ⬇️",
                            "compound": "Cụm từ 🔤",
                            "Tích cực 🟢": "Tích cực 🟢",
                            "Tiêu cực 🔴": "Tiêu cực 🔴",
                            "Trung lập ⚪": "Trung lập ⚪"
                        }.get(word["type"], word["type"])
                        
                        # Thêm mô tả nếu có
                        description = word.get("description", "")
                        
                        # Cộng điểm cho tất cả các loại từ và dấu câu
                        total_score += word["score"]
                        
                        # Thêm vào bảng dữ liệu
                        word_entry = {
                            "Từ/Cụm từ": word["word"],
                            "Loại": sentiment_type,
                            "Điểm": f"{word['score']:.2f}"
                        }
                        
                        # Thêm mô tả nếu có
                        if description:
                            word_entry["Mô tả"] = description
                            
                        word_data.append(word_entry)
                    
                    st.table(word_data)
                    
                    # Hiển thị tổng điểm
                    st.metric("Tổng điểm", f"{word_analysis['score']:.2f}")
                    
                    # Hiển thị thông tin về ảnh hưởng của dấu câu nếu có
                    if "pre_punct_score" in word_analysis and "punct_effect" in word_analysis:
                        pre_punct_score = word_analysis["pre_punct_score"]
                        punct_effect = word_analysis["punct_effect"]
                        
                        col1a, col1b = st.columns(2)
                        with col1a:
                            st.metric("Điểm trước dấu câu", f"{pre_punct_score:.2f}")
                        with col1b:
                            st.metric("Ảnh hưởng dấu câu", f"{punct_effect:.2f}", 
                                     delta_color="normal" if punct_effect == 0 else "off")
                
                with col2:
                    st.subheader("📊 Phân tích toàn câu")
                    
                    # Tính toán tỷ lệ cảm xúc dựa trên điểm thực
                    total_abs = sum(abs(word["score"]) for word in word_analysis["words"] 
                                  if word["type"] in ["positive", "negative", "compound"])
                    
                    # Chỉ tính các từ có ý nghĩa thực sự (loại bỏ các từ trung lập không có ý nghĩa)
                    meaningful_words = [word for word in word_analysis["words"] 
                                     if word["type"] in ["positive", "negative", "compound"] or 
                                     (word["type"] == "neutral" and abs(word["score"]) > 0.1)]
                    
                    if total_abs > 0:
                        sentiment_data = {
                            "Tích cực 🟢": sum(word["score"] for word in word_analysis["words"] 
                                           if word["score"] > 0),
                            "Tiêu cực 🔴": abs(sum(word["score"] for word in word_analysis["words"] 
                                           if word["score"] < 0))
                        }
                        
                        # Chỉ thêm trung lập nếu có từ trung lập có ý nghĩa
                        neutral_score = sum(1 for word in meaningful_words 
                                         if abs(word["score"]) <= 0.1) / len(meaningful_words) if meaningful_words else 0
                        
                        if neutral_score > 0:
                            sentiment_data["Trung lập ⚪"] = neutral_score
                        
                        # Chuẩn hóa để tổng = 1
                        total = sum(sentiment_data.values())
                        if total > 0:
                            for key in sentiment_data:
                                sentiment_data[key] = sentiment_data[key] / total
                    else:
                        sentiment_data = {
                            "Tích cực 🟢": 0,
                            "Tiêu cực 🔴": 0,
                            "Trung lập ⚪": 1
                        }
                    
                    # Xác định cảm xúc chính và tính độ tin cậy
                    if total_abs > 0:
                        # Tính tỷ lệ điểm số
                        positive_ratio = sum(word["score"] for word in word_analysis["words"] if word["score"] > 0) / total_abs
                        negative_ratio = abs(sum(word["score"] for word in word_analysis["words"] if word["score"] < 0)) / total_abs
                        
                        # Xác định cảm xúc chính dựa trên tổng điểm thực tế
                        if total_score < -0.1:  # Ngưỡng tiêu cực
                            main_sentiment = "Tiêu cực 🔴"
                            confidence = negative_ratio * 100
                        elif total_score > 0.1:  # Ngưỡng tích cực
                            main_sentiment = "Tích cực 🟢"
                            confidence = positive_ratio * 100
                        else:
                            main_sentiment = "Trung lập ⚪"
                            # Độ tin cậy trung lập dựa trên mức độ cân bằng giữa tích cực và tiêu cực
                            confidence = (1 - abs(positive_ratio - negative_ratio)) * 100
                    else:
                        # Nếu không có điểm số có ý nghĩa, thì là trung lập với độ tin cậy cao
                        main_sentiment = "Trung lập ⚪"
                        confidence = 100.0
                    
                    # Giới hạn độ tin cậy trong khoảng 0-100%
                    confidence = min(max(confidence, 0.0), 100.0)
                    
                    # Hiển thị kết quả chính
                    st.metric(
                        "Cảm xúc chính",
                        main_sentiment,
                        f"Độ tin cậy: {confidence:.1f}%"
                    )
                    
                    # Vẽ biểu đồ
                    chart = st.bar_chart(sentiment_data)
                    
                    # Thống kê chi tiết
                    st.markdown("**Chi tiết phân tích:**")
                    stats = {
                        "Số từ phân tích": len([w for w in word_analysis["words"] 
                                              if w["type"] not in ["intensifier", "diminisher", "negation"]]),
                        "Từ tích cực": sum(1 for w in word_analysis["words"] if w["score"] > 0),
                        "Từ tiêu cực": sum(1 for w in word_analysis["words"] if w["score"] < 0),
                        "Từ trung lập": sum(1 for w in word_analysis["words"] 
                                          if w["score"] == 0 and w["type"] not in ["intensifier", "diminisher", "negation"])
                    }
                    st.write(stats)
                    
        except Exception as e:
            st.error(f"❌ Có lỗi xảy ra: {str(e)}")
            st.error("Vui lòng thử lại hoặc liên hệ hỗ trợ!")