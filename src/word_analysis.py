import re
import os
import sys
from collections import defaultdict

# Thêm đường dẫn thư mục gốc vào PYTHONPATH
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)
sys.path.insert(0, os.path.join(ROOT_DIR, "dictionary"))

from vietnamese_sentiment_dict import (
    SENTIMENT_DICT, NEGATION_WORDS, INTENSIFIER_WORDS, 
    DIMINISHER_WORDS, COMPOUND_WORDS, PUNCTUATION_ANALYSIS
)

def analyze_word_sentiment(text):
    """
    Phân tích cảm xúc của từng từ trong văn bản
    """
    if not text or not isinstance(text, str):
        return {"words": [], "score": 0}
    
    # Tiền xử lý văn bản
    text = text.lower()
    
    # Tách từ và dấu câu
    words = []
    punctuations = []
    
    # Tìm tất cả các dấu câu và biểu tượng cảm xúc
    punct_pattern = r'[!?.,]+|:\)|:\(|:D|:\'\(|😊|😔|😢|😍|\.{3,}'
    punct_matches = re.finditer(punct_pattern, text)
    
    # Lưu vị trí của các dấu câu
    punct_positions = []
    for match in punct_matches:
        punct_positions.append((match.start(), match.end(), match.group()))
    
    # Tách từ và loại bỏ dấu câu
    cleaned_text = re.sub(punct_pattern, ' ', text)
    words_list = cleaned_text.split()
    
    # Phân tích từng từ
    result = {"words": [], "score": 0}
    total_score = 0
    
    # Xử lý các từ đơn và cụm từ
    i = 0
    while i < len(words_list):
        current_word = words_list[i]
        
        # Kiểm tra cụm từ
        found_compound = False
        for length in range(min(5, len(words_list) - i), 1, -1):
            compound = " ".join(words_list[i:i+length])
            if compound in COMPOUND_WORDS:
                score = COMPOUND_WORDS[compound]
                result["words"].append({
                    "word": compound,
                    "type": "compound",
                    "score": score
                })
                total_score += score
                i += length
                found_compound = True
                break
        
        if found_compound:
            continue
        
        # Xử lý từ đơn
        word_type = "neutral"
        word_score = 0
        
        # Kiểm tra từ phủ định
        if current_word in NEGATION_WORDS:
            result["words"].append({
                "word": current_word,
                "type": "negation",
                "score": 0
            })
            
            # Nếu từ tiếp theo có trong từ điển cảm xúc, đảo ngược điểm số
            if i + 1 < len(words_list):
                next_word = words_list[i + 1]
                if next_word in SENTIMENT_DICT:
                    next_score = SENTIMENT_DICT[next_word]
                    # Đảo ngược điểm số cho từ tiếp theo
                    words_list[i + 1] = f"NEG_{next_word}"
            
            i += 1
            continue
        
        # Kiểm tra từ tăng cường
        elif current_word in INTENSIFIER_WORDS:
            result["words"].append({
                "word": current_word,
                "type": "intensifier",
                "score": 0
            })
            
            # Nếu từ tiếp theo có trong từ điển cảm xúc, tăng cường điểm số
            if i + 1 < len(words_list):
                next_word = words_list[i + 1]
                if next_word in SENTIMENT_DICT:
                    next_score = SENTIMENT_DICT[next_word]
                    # Tăng cường điểm số cho từ tiếp theo
                    words_list[i + 1] = f"INT_{next_word}"
            
            i += 1
            continue
        
        # Kiểm tra từ giảm nhẹ
        elif current_word in DIMINISHER_WORDS:
            result["words"].append({
                "word": current_word,
                "type": "diminisher",
                "score": 0
            })
            
            # Nếu từ tiếp theo có trong từ điển cảm xúc, giảm nhẹ điểm số
            if i + 1 < len(words_list):
                next_word = words_list[i + 1]
                if next_word in SENTIMENT_DICT:
                    next_score = SENTIMENT_DICT[next_word]
                    # Giảm nhẹ điểm số cho từ tiếp theo
                    words_list[i + 1] = f"DIM_{next_word}"
            
            i += 1
            continue
        
        # Xử lý từ đã bị ảnh hưởng bởi từ phủ định
        elif current_word.startswith("NEG_"):
            original_word = current_word[4:]
            if original_word in SENTIMENT_DICT:
                word_score = -SENTIMENT_DICT[original_word]
                word_type = "positive" if word_score > 0 else "negative" if word_score < 0 else "neutral"
                result["words"].append({
                    "word": original_word,
                    "type": word_type,
                    "score": word_score
                })
                total_score += word_score
            i += 1
            continue
        
        # Xử lý từ đã bị ảnh hưởng bởi từ tăng cường
        elif current_word.startswith("INT_"):
            original_word = current_word[4:]
            if original_word in SENTIMENT_DICT:
                intensifier = list(INTENSIFIER_WORDS.values())[0]  # Lấy giá trị mặc định
                word_score = SENTIMENT_DICT[original_word] * intensifier
                word_type = "positive" if word_score > 0 else "negative" if word_score < 0 else "neutral"
                result["words"].append({
                    "word": original_word,
                    "type": word_type,
                    "score": word_score
                })
                total_score += word_score
            i += 1
            continue
        
        # Xử lý từ đã bị ảnh hưởng bởi từ giảm nhẹ
        elif current_word.startswith("DIM_"):
            original_word = current_word[4:]
            if original_word in SENTIMENT_DICT:
                diminisher = list(DIMINISHER_WORDS.values())[0]  # Lấy giá trị mặc định
                word_score = SENTIMENT_DICT[original_word] * diminisher
                word_type = "positive" if word_score > 0 else "negative" if word_score < 0 else "neutral"
                result["words"].append({
                    "word": original_word,
                    "type": word_type,
                    "score": word_score
                })
                total_score += word_score
            i += 1
            continue
        
        # Xử lý từ thông thường
        elif current_word in SENTIMENT_DICT:
            word_score = SENTIMENT_DICT[current_word]
            word_type = "positive" if word_score > 0 else "negative" if word_score < 0 else "neutral"
        
        result["words"].append({
            "word": current_word,
            "type": word_type,
            "score": word_score
        })
        total_score += word_score
        i += 1
    
    # Lưu điểm số trước khi xử lý dấu câu để debug
    pre_punct_score = total_score
    
    # Phân tích dấu câu và thêm vào kết quả
    for start, end, punct in punct_positions:
        # Xử lý các dấu câu đặc biệt
        if punct in PUNCTUATION_ANALYSIS:
            punct_info = PUNCTUATION_ANALYSIS[punct]
            
            # Thêm dấu câu vào kết quả
            if punct_info["effect"] == "intensify":
                # Nếu là dấu tăng cường, áp dụng hệ số nhân cho tổng điểm
                multiplier = punct_info["multiplier"]
                # Tính điểm ảnh hưởng của dấu câu
                punct_score = total_score * (multiplier - 1)  # Chỉ tính phần tăng thêm
                
                # Thêm vào kết quả với loại rõ ràng hơn
                result["words"].append({
                    "word": punct,
                    "type": "Tích cực 🟢" if punct_score > 0 else "Tiêu cực 🔴" if punct_score < 0 else "Trung lập ⚪",
                    "score": punct_score,  # Hiển thị điểm ảnh hưởng
                    "description": f"Dấu tăng cường (x{multiplier})"
                })
                
                # Cập nhật tổng điểm
                total_score = total_score * multiplier
            
            elif punct_info["effect"] == "question":
                # Nếu là dấu hỏi, giảm nhẹ tổng điểm
                multiplier = punct_info["multiplier"]
                # Tính điểm ảnh hưởng của dấu câu
                punct_score = total_score * (multiplier - 1)  # Chỉ tính phần giảm đi
                
                # Thêm vào kết quả với loại rõ ràng hơn
                result["words"].append({
                    "word": punct,
                    "type": "Tích cực 🟢" if punct_score > 0 else "Tiêu cực 🔴" if punct_score < 0 else "Trung lập ⚪",
                    "score": punct_score,  # Hiển thị điểm ảnh hưởng
                    "description": f"Dấu nghi vấn (x{multiplier})"
                })
                
                # Cập nhật tổng điểm
                total_score = total_score * multiplier
            
            elif "value" in punct_info:
                # Nếu là biểu tượng cảm xúc, thêm giá trị vào tổng điểm
                value = punct_info["value"]
                
                # Thêm vào kết quả với loại rõ ràng hơn
                sentiment_type = "Tích cực 🟢" if value > 0 else "Tiêu cực 🔴" if value < 0 else "Trung lập ⚪"
                effect_type = "tích cực" if value > 0 else "tiêu cực" if value < 0 else "trung lập"
                
                result["words"].append({
                    "word": punct,
                    "type": sentiment_type,
                    "score": value,  # Hiển thị điểm trực tiếp
                    "description": f"Biểu tượng cảm xúc {effect_type}"
                })
                
                # Cập nhật tổng điểm
                total_score += value
            
            else:
                # Các dấu câu khác
                result["words"].append({
                    "word": punct,
                    "type": "Trung lập ⚪",
                    "score": 0,
                    "description": f"Dấu câu bình thường"
                })
    
    # Lưu thông tin debug vào kết quả
    result["pre_punct_score"] = pre_punct_score
    result["punct_effect"] = total_score - pre_punct_score
    
    # Cập nhật tổng điểm
    result["score"] = total_score
    
    return result