import re
import os
import sys
from collections import defaultdict

# Thêm đường dẫn thư mục gốc vào PYTHONPATH
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)
sys.path.insert(0, os.path.join(ROOT_DIR, "dictionary"))

# Sử dụng DictionaryManager để nạp từ điển từ JSON
from dictionary.dict_manager import DictionaryManager
from config import SENTIMENT_CONFIG

# Khởi tạo Dictionary Manager
dict_manager = DictionaryManager(os.path.join(ROOT_DIR, "dictionary"))

# Biến toàn cục cho các từ điển
SENTIMENT_DICT = {}
NEGATION_WORDS = []
INTENSIFIER_WORDS = {}
DIMINISHER_WORDS = {}
COMPOUND_WORDS = {}
PROVERBS = {}
PUNCTUATION_ANALYSIS = {}

# Hàm tải lại tất cả từ điển
def reload_dictionaries():
    global SENTIMENT_DICT, NEGATION_WORDS, INTENSIFIER_WORDS, DIMINISHER_WORDS, COMPOUND_WORDS, PROVERBS, PUNCTUATION_ANALYSIS
    
    # Tải lại tất cả từ điển
    dict_manager.load_all()
    
    # Cập nhật các biến toàn cục
    SENTIMENT_DICT = dict_manager.get_sentiment_dict()
    NEGATION_WORDS = dict_manager.get_negation_words()
    INTENSIFIER_WORDS = dict_manager.get_intensifier_words()
    DIMINISHER_WORDS = dict_manager.get_diminisher_words()
    COMPOUND_WORDS = dict_manager.get_compound_words()
    PROVERBS = dict_manager.get_proverbs()
    PUNCTUATION_ANALYSIS = dict_manager.get_punctuation_analysis()
    
# Tải từ điển lần đầu
reload_dictionaries()

def determine_sentiment_type(score):
    thresholds = SENTIMENT_CONFIG['thresholds']
    if score >= thresholds['positive']:
        return 'positive'
    elif score <= thresholds['negative']:
        return 'negative'
    else:
        return 'neutral'

def analyze_word_sentiment(text):
    """
    Phân tích tình cảm của văn bản dựa trên từ góc
    """
    # Tải lại từ điển trước khi phân tích để cập nhật realtime
    reload_dictionaries()
    
    if not text.strip():
        return {
            "words": [],
            "score": 0,
            "sentiment": "neutral"
        }
    
    # Chuẩn hóa văn bản
    text = text.lower().strip()
    
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
    
    # Tạo danh sách các cụm từ cần kiểm tra
    compound_check_list = set(COMPOUND_WORDS.keys())
    
    # Hàm kiểm tra nếu nhiều từ liền nhau có thể là 1 cụm từ trong từ điển
    def check_proverb(start_idx, max_length=15):
        """
        Kiểm tra các thành ngữ/tục ngữ trong văn bản
        """
        if start_idx >= len(words_list):
            return None, 0
            
        for length in range(max_length, 0, -1):  # Kiểm tra các thành ngữ dài nhất trước
            if start_idx + length <= len(words_list):
                proverb_candidate = " ".join(words_list[start_idx:start_idx+length])
                if proverb_candidate in PROVERBS:
                    return proverb_candidate, length
        
        return None, 0

    def check_compound_phrase(start_idx, max_length=6):
        """
        Tối ưu hóa việc kiểm tra các cụm từ phức tạp
        """
        if start_idx >= len(words_list):
            return None, 0
            
        for length in range(max_length, 0, -1):  # Kiểm tra từ cụm từ dài nhất trước
            if start_idx + length <= len(words_list):
                compound_candidate = " ".join(words_list[start_idx:start_idx+length])
                if compound_candidate in COMPOUND_WORDS:
                    return compound_candidate, length
        
        return None, 0
    
    # Hàm kiểm tra nếu 2 từ liền nhau có thể là 1 cụm từ trong từ điển
    def check_if_compound(word1, word2):
        potential_compound = f"{word1} {word2}"
        if potential_compound in compound_check_list:
            return potential_compound
        return None
    
    # Phân tích từng từ
    result = {"words": [], "score": 0}
    total_score = 0
    
    # Xử lý các từ đơn và cụm từ
    i = 0
    # Lưu trữ vị trí đã xử lý để tránh xử lý lại
    processed_indices = set()
    
    # Xử lý tất cả thành ngữ/tục ngữ và cụm từ dài trước
    for i in range(len(words_list)):
        if i in processed_indices:
            continue
            
        # Bước 0: Ưu tiên tìm kiếm thành ngữ/tục ngữ trước
        proverb, proverb_length = check_proverb(i, 15)  # Thành ngữ có thể dài hơn cụm từ
        if proverb and proverb_length > 0:
            score = PROVERBS[proverb]
            # Xác định loại cảm xúc dựa trên điểm số
            word_type = "positive" if score > 0 else "negative" if score < 0 else "neutral"
            result["words"].append({
                "word": proverb,
                "type": "proverb",
                "score": score,
                "sentiment_type": word_type,  # Thêm loại cảm xúc
                "description": f"Thành ngữ/tục ngữ ({proverb_length} từ)"
            })
            total_score += score
            # Đánh dấu các vị trí đã xử lý
            for j in range(i, i + proverb_length):
                processed_indices.add(j)
            continue
            
        # Bước 1: Tối ưu hóa tìm kiếm cụm từ dài nhất trước
        compound_phrase, phrase_length = check_compound_phrase(i, 6)  # Cố gắng tìm cụm từ có tối đa 6 từ
        if compound_phrase and phrase_length > 0:
            score = COMPOUND_WORDS[compound_phrase]
            result["words"].append({
                "word": compound_phrase,
                "type": "compound",
                "score": score,
                "description": f"Cụm từ ({phrase_length} từ)"
            })
            total_score += score
            # Đánh dấu các vị trí đã xử lý
            for j in range(i, i + phrase_length):
                processed_indices.add(j)
            continue
                
        # Bước 2: Kiểm tra cụm 2 từ được viết có khoảng trắng
        if i + 1 < len(words_list) and i + 1 not in processed_indices:
            current_word = words_list[i]
            two_word_compound = f"{current_word} {words_list[i+1]}"
            if two_word_compound in COMPOUND_WORDS:
                score = COMPOUND_WORDS[two_word_compound]
                result["words"].append({
                    "word": two_word_compound,
                    "type": "compound",
                    "score": score,
                    "description": "Từ ghép (2 từ)"
                })
                total_score += score
                processed_indices.add(i)
                processed_indices.add(i+1)
                continue
        
        # Bước 3: Kiểm tra từ ghép có thể được viết liền nhau
        if i + 1 < len(words_list) and i + 1 not in processed_indices:
            current_word = words_list[i]
            # Kiểm tra nếu hai từ liền nhau có thể là một cụm từ trong từ điển
            # Ví dụ: 'lấp' và 'lánh' => 'lấp lánh'
            compound_word = check_if_compound(current_word, words_list[i+1])
            if compound_word:
                score = COMPOUND_WORDS[compound_word] 
                result["words"].append({
                    "word": compound_word,
                    "type": "compound",
                    "score": score,
                    "description": "Từ ghép không có khoảng trắng"
                })
                total_score += score
                processed_indices.add(i)
                processed_indices.add(i+1)
                continue
        
    # Xử lý các từ đơn chưa được xử lý trong cụm từ
    for i in range(len(words_list)):
        # Bỏ qua các từ đã xử lý trong cụm từ
        if i in processed_indices:
            continue
            
        current_word = words_list[i]
        
        # Kiểm tra nếu từ hiện tại là từ cảm xúc và từ trước hoặc sau là từ tăng cường
        # Đặc biệt xử lý trường hợp từ tăng cường đứng sau (đặc biệt là từ "quá")
        if current_word in SENTIMENT_DICT:
            # Kiểm tra nếu từ phía sau là từ tăng cường (ví dụ: "hay quá")
            if i + 1 < len(words_list) and words_list[i + 1] in INTENSIFIER_WORDS and i + 1 not in processed_indices:
                next_word = words_list[i + 1]
                # Đánh dấu cả hai từ đã được xử lý
                processed_indices.add(i + 1)
                # Tạo cụm từ tăng cường
                intensifier_value = INTENSIFIER_WORDS[next_word]
                score = SENTIMENT_DICT[current_word] * intensifier_value
                result["words"].append({
                    "word": f"{current_word} {next_word}",
                    "type": "compound",
                    "score": score,
                    "description": f"Từ cảm xúc với từ tăng cường đứng sau"
                })
                total_score += score
                continue
        
        processed_indices.add(i)
        
        # Kiểm tra từ phủ định
        if current_word in NEGATION_WORDS:
            result["words"].append({
                "word": current_word,
                "type": "negation",
                "score": 0,
                "description": "Từ phủ định"
            })
            
            # Nếu từ tiếp theo có trong từ điển cảm xúc, đảo ngược điểm số
            if i + 1 < len(words_list) and i + 1 not in processed_indices:
                next_word = words_list[i + 1]
                if next_word in SENTIMENT_DICT:
                    next_score = SENTIMENT_DICT[next_word]
                    # Đánh dấu từ đã bị phủ định
                    words_list[i + 1] = f"NEG_{next_word}"
            continue
        
        # Kiểm tra từ tăng cường
        elif current_word in INTENSIFIER_WORDS:
            result["words"].append({
                "word": current_word,
                "type": "intensifier",
                "score": 0,
                "description": "Từ tăng cường"
            })
            
            # Nếu từ tiếp theo có trong từ điển cảm xúc, tăng cường điểm số
            if i + 1 < len(words_list) and i + 1 not in processed_indices:
                next_word = words_list[i + 1]
                if next_word in SENTIMENT_DICT:
                    next_score = SENTIMENT_DICT[next_word]
                    # Tăng cường điểm số cho từ tiếp theo
                    words_list[i + 1] = f"INT_{next_word}"
            continue
        
        # Kiểm tra từ giảm nhẹ
        elif current_word in DIMINISHER_WORDS:
            result["words"].append({
                "word": current_word,
                "type": "diminisher",
                "score": 0,
                "description": "Từ giảm nhẹ"
            })
            
            # Nếu từ tiếp theo có trong từ điển cảm xúc, giảm nhẹ điểm số
            if i + 1 < len(words_list) and i + 1 not in processed_indices:
                next_word = words_list[i + 1]
                if next_word in SENTIMENT_DICT:
                    next_score = SENTIMENT_DICT[next_word]
                    # Giảm nhẹ điểm số cho từ tiếp theo
                    words_list[i + 1] = f"DIM_{next_word}"
            continue
            
        # Xử lý từ đơn
        word_type = "neutral"
        word_score = 0
        
        # Xử lý từ đã bị ảnh hưởng bởi từ phủ định
        if current_word.startswith("NEG_"):
            original_word = current_word[4:]
            if original_word in SENTIMENT_DICT:
                word_score = -SENTIMENT_DICT[original_word]
                word_type = "positive" if word_score > 0 else "negative" if word_score < 0 else "neutral"
                result["words"].append({
                    "word": original_word,
                    "type": word_type,
                    "score": word_score,
                    "description": "Bị phủ định"
                })
                total_score += word_score
                processed_indices.add(i)
                continue
        
        # Xử lý từ đã bị ảnh hưởng bởi từ tăng cường
        elif current_word.startswith("INT_"):
            original_word = current_word[4:]
            if original_word in SENTIMENT_DICT:
                # Tìm từ tăng cường đã ảnh hưởng đến từ này
                # Lấy từ tăng cường từ vị trí trước đó trong danh sách kết quả
                intensifier_word = result["words"][-1]["word"] if result["words"] and result["words"][-1]["type"] == "intensifier" else None
                
                # Lấy giá trị tăng cường từ từ điển nếu có
                if intensifier_word and intensifier_word in INTENSIFIER_WORDS:
                    intensifier = INTENSIFIER_WORDS[intensifier_word]
                else:
                    intensifier = list(INTENSIFIER_WORDS.values())[0]  # Giá trị mặc định nếu không tìm thấy
                
                word_score = SENTIMENT_DICT[original_word] * intensifier
                word_type = "positive" if word_score > 0 else "negative" if word_score < 0 else "neutral"
                result["words"].append({
                    "word": original_word,
                    "type": word_type,
                    "score": word_score,
                    "description": f"Tăng cường bởi '{intensifier_word}' (x{intensifier})"
                })
                total_score += word_score
                processed_indices.add(i)
                continue
        
        # Xử lý từ đã bị ảnh hưởng bởi từ giảm nhẹ
        elif current_word.startswith("DIM_"):
            original_word = current_word[4:]
            if original_word in SENTIMENT_DICT:
                # Tìm từ giảm nhẹ đã ảnh hưởng đến từ này
                # Lấy từ giảm nhẹ từ vị trí trước đó trong danh sách kết quả
                diminisher_word = result["words"][-1]["word"] if result["words"] and result["words"][-1]["type"] == "diminisher" else None
                
                # Lấy giá trị giảm nhẹ từ từ điển nếu có
                if diminisher_word and diminisher_word in DIMINISHER_WORDS:
                    diminisher = DIMINISHER_WORDS[diminisher_word]
                else:
                    diminisher = list(DIMINISHER_WORDS.values())[0]  # Giá trị mặc định nếu không tìm thấy
                
                word_score = SENTIMENT_DICT[original_word] * diminisher
                word_type = "positive" if word_score > 0 else "negative" if word_score < 0 else "neutral"
                result["words"].append({
                    "word": original_word,
                    "type": word_type,
                    "score": word_score,
                    "description": f"Giảm nhẹ bởi '{diminisher_word}' (x{diminisher})"
                })
                total_score += word_score
                processed_indices.add(i)
                continue

        # Kiểm tra từ trong từ điển cảm xúc
        elif current_word in SENTIMENT_DICT:
            word_score = SENTIMENT_DICT[current_word]
            word_type = determine_sentiment_type(word_score)
            result["words"].append({
                "word": current_word,
                "type": word_type,
                "score": word_score,
                "description": "Từ đơn"
            })
            total_score += word_score
        else:
            # Từ không có trong từ điển cảm xúc
            result["words"].append({
                "word": current_word,
                "type": "neutral",
                "score": 0,
                "description": "Từ không có trong từ điển"
            })
    
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