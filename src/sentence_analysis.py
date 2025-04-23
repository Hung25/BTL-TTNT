from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from config import MODEL_PATH
import os
import sys
import re
import json

# Thêm đường dẫn thư mục gốc vào PYTHONPATH
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)
sys.path.insert(0, os.path.join(ROOT_DIR, "dictionary"))

# Sử dụng DictionaryManager để nạp từ điển từ JSON
from dictionary.dict_manager import DictionaryManager

# Khởi tạo Dictionary Manager
dict_manager = DictionaryManager(os.path.join(ROOT_DIR, "dictionary"))

# Lấy các từ điển
SENTIMENT_DICT = dict_manager.get_sentiment_dict()
NEGATION_WORDS = dict_manager.get_negation_words()
INTENSIFIER_WORDS = dict_manager.get_intensifier_words()
DIMINISHER_WORDS = dict_manager.get_diminisher_words()
COMPOUND_WORDS = dict_manager.get_compound_words()
PUNCTUATION_ANALYSIS = dict_manager.get_punctuation_analysis()

# Load các cấu hình hiển thị từ sentiment_setting.json (hoặc tạo mới nếu không có)
settings_file = os.path.join(ROOT_DIR, "dictionary", "json", "sentiment_settings.json")
if os.path.exists(settings_file):
    with open(settings_file, 'r', encoding='utf-8') as f:
        settings = json.load(f)
        DISPLAY_CONTROLLER = settings.get('DISPLAY_CONTROLLER', {})
        CHART_CONFIG = settings.get('CHART_CONFIG', {})
        TEXT_DISPLAY = settings.get('TEXT_DISPLAY', {})
        CHART_PRIORITY = settings.get('CHART_PRIORITY', {})
        CHART_PALETTE = settings.get('CHART_PALETTE', {})
        SENTIMENT_RULES = settings.get('SENTIMENT_RULES', {})
else:
    # Mặc định nếu không có file settings
    DISPLAY_CONTROLLER = {"calculation": {"use_raw_values": True, "respect_signs": True}}
    CHART_CONFIG = {"display": {"enabled": True, "show_all_columns": True, "bars": {"show_values": True}}}
    TEXT_DISPLAY = {
        "sentiment": {
            "positive": {"text": "Tích cực", "icon": "😊"},
            "negative": {"text": "Tiêu cực", "icon": "🙁"},
            "neutral": {"text": "Trung lập", "icon": "😐"}
        },
        "confidence": {
            "high": {"text": "Độ tin cậy cao", "threshold": 70.0},
            "medium": {"text": "Độ tin cậy trung bình", "threshold": 40.0},
            "low": {"text": "Độ tin cậy thấp", "threshold": 0.0}
        }
    }
    CHART_PRIORITY = {"enforce_config": False, "confidence_min": 0.0, "rotate_labels": 0, "show_values": True, "relative_scaling": False}
    CHART_PALETTE = {"positive": "#2E7D32", "neutral": "#757575", "negative": "#F44336"}
    SENTIMENT_RULES = {"thresholds": {"positive": 0.1, "negative": -0.1, "neutral": [-0.1, 0.1]}}

class SentenceAnalyzer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("vinai/bertweet-base")
        self.model = AutoModelForSequenceClassification.from_pretrained("vinai/bertweet-base")
        
    def analyze_sentence(self, text, word_analysis_result=None):
        """
        Phân tích cảm xúc của toàn bộ câu văn và áp dụng cấu hình hiển thị
        
        Args:
            text: Văn bản cần phân tích
            word_analysis_result: Kết quả phân tích từng từ (nếu có)
        """
        try:
            # Tokenize và chuyển đổi thành tensor
            inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
            
            # Dự đoán
            with torch.no_grad():
                outputs = self.model(**inputs)
                predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
                
            # Lấy kết quả
            scores = predictions[0].tolist()
            
            # Kiểm tra số lượng nhãn
            if len(scores) == 3:  # Tiêu cực, Trung lập, Tích cực
                sentiment = {
                    "negative": scores[0],
                    "neutral": scores[1],
                    "positive": scores[2]
                }
            else:  # Nếu không phải 3 nhãn, xử lý khác
                sentiment = {
                    "negative": scores[0],
                    "neutral": 0.0,
                    "positive": scores[1] if len(scores) > 1 else 0.0
                }
            
            # Áp dụng quy tắc từ cấu hình
            adjusted_sentiment = self._adjust_sentiment(sentiment, word_analysis_result)
            
            # Xác định cảm xúc chính
            main_sentiment = max(adjusted_sentiment.items(), key=lambda x: x[1])[0]
            confidence = adjusted_sentiment[main_sentiment] * 100  # Chuyển về phần trăm
            
            # Giới hạn độ tin cậy trong khoảng 0-100%
            confidence = min(confidence, 100.0)
            
            # Áp dụng cấu hình hiển thị
            display_result = self._apply_display_config(adjusted_sentiment, main_sentiment, confidence, word_analysis_result)
            
            return display_result
            
        except Exception as e:
            print(f"Lỗi khi phân tích câu: {str(e)}")
            return {
                "sentiment": {"negative": 0.0, "neutral": 0.1, "positive": 0.9},
                "main_sentiment": "positive",
                "confidence": 0.9,
                "chart_data": self._get_default_chart_data()
            }
    
    def _adjust_sentiment(self, sentiment, word_analysis_result):
        """Điều chỉnh điểm sentiment dựa trên cấu hình và kết quả phân tích từ"""
        adjusted = sentiment.copy()
        
        # Nếu có kết quả phân tích từ, sử dụng để điều chỉnh
        if word_analysis_result:
            total_word_score = word_analysis_result.get("total_score", 0)
            
            # Điều chỉnh điểm dựa trên tổng điểm từ phân tích từ
            if total_word_score < 0:
                # Nếu tổng điểm âm, tăng điểm tiêu cực
                adjusted["negative"] = max(adjusted["negative"], abs(total_word_score))
                adjusted["positive"] = min(adjusted["positive"], 0.3)
            elif total_word_score > 0:
                # Nếu tổng điểm dương, tăng điểm tích cực
                adjusted["positive"] = max(adjusted["positive"], total_word_score)
                adjusted["negative"] = min(adjusted["negative"], 0.3)
            else:
                # Nếu tổng điểm = 0, tăng điểm trung lập
                adjusted["neutral"] = max(adjusted["neutral"], 0.5)
                
        # Đảm bảo tổng xác suất = 1
        total = sum(adjusted.values())
        if total > 0:
            for key in adjusted:
                adjusted[key] = adjusted[key] / total
                
        return adjusted
    
    def _apply_display_config(self, sentiment, main_sentiment, confidence, word_analysis_result=None):
        """Áp dụng cấu hình hiển thị cho kết quả phân tích"""
        # Xác định lại cảm xúc chính dựa trên giá trị thực
        if sentiment["negative"] > max(sentiment["positive"], sentiment["neutral"]):
            main_sentiment = "negative"
        elif sentiment["positive"] > max(sentiment["negative"], sentiment["neutral"]):
            main_sentiment = "positive"
        else:
            main_sentiment = "neutral"
        
        # Tính độ tin cậy dựa trên chênh lệch giữa các giá trị và dữ liệu từ phân tích từ
        max_value = max(sentiment.values())
        if max_value > 0:
            second_max = sorted(sentiment.values())[-2] if len(sentiment.values()) > 1 else 0
            base_confidence = ((max_value - second_max) / max_value) * 100
            
            # Kiểm tra nếu có dữ liệu từ phân tích từ
            if word_analysis_result and "words" in word_analysis_result:
                # Tính tổng điểm và số lượng từ có điểm
                words_with_score = [w for w in word_analysis_result["words"] if abs(w.get("score", 0)) > 0]
                total_word_score = sum(abs(w.get("score", 0)) for w in words_with_score)
                
                # Tăng độ tin cậy cho các cụm từ ngắn có ý nghĩa rõ ràng
                if len(words_with_score) <= 3 and total_word_score > 0.5:
                    # Tăng độ tin cậy khi có ít từ và điểm cao
                    confidence_boost = min(30, 40 - len(words_with_score) * 5)  # Tăng thêm tối đa 30%
                    confidence = min(98, base_confidence + confidence_boost)  # Giới hạn ở 98%
                elif len(word_analysis_result["words"]) <= 5:
                    # Tăng nhẹ cho các câu ngắn
                    confidence = min(95, base_confidence + 15)
                else:
                    confidence = base_confidence
            else:
                confidence = base_confidence
        else:
            # Trường hợp tất cả các giá trị đều = 0
            confidence = 0
        
        result = {
            "sentiment": sentiment,
            "main_sentiment": main_sentiment,
            "confidence": confidence,
            "display_text": self._get_display_text(main_sentiment, confidence),
            "chart_data": self._prepare_chart_data(sentiment)
        }
        
        return result
    
    def _get_display_text(self, sentiment_type, confidence):
        """Lấy văn bản hiển thị dựa trên loại cảm xúc và độ tin cậy"""
        # Lấy văn bản cảm xúc
        sentiment_text = TEXT_DISPLAY["sentiment"][sentiment_type]["text"]
        sentiment_icon = TEXT_DISPLAY["sentiment"][sentiment_type]["icon"]
        
        # Lấy văn bản độ tin cậy
        confidence_level = "low"
        if confidence >= TEXT_DISPLAY["confidence"]["high"]["threshold"]:
            confidence_level = "high"
        elif confidence >= TEXT_DISPLAY["confidence"]["medium"]["threshold"]:
            confidence_level = "medium"
            
        confidence_text = TEXT_DISPLAY["confidence"][confidence_level]["text"]
        
        return {
            "sentiment": f"{sentiment_icon} {sentiment_text}",
            "confidence": f"{confidence_text} ({confidence:.2f}%)"
        }
    
    def _prepare_chart_data(self, sentiment):
        """Chuẩn bị dữ liệu cho biểu đồ dựa trên cấu hình"""
        chart_data = {}
        
        # Kiểm tra cấu hình hiển thị
        display_config = CHART_CONFIG["display"]
        
        # Loại bỏ phần tiêu cực nếu cần
        if (display_config.get("remove_negative_completely", False) or 
            display_config.get("only_show_positive_neutral", False)):
            # Loại bỏ phần tiêu cực
            filtered_data = {k: v for k, v in sentiment.items() if k != "negative"}
            
            # Chuẩn hóa lại tổng = 1
            total = sum(filtered_data.values())
            if total > 0:
                chart_data = {k: v/total for k, v in filtered_data.items()}
            else:
                chart_data = {"positive": 1.0, "neutral": 0.0}
        else:
            chart_data = sentiment
            
        # Áp dụng màu sắc
        chart_colors = {
            "positive": CHART_PALETTE.get("positive", "#2E7D32"),
            "neutral": CHART_PALETTE.get("neutral", "#757575"),
            "negative": CHART_PALETTE.get("negative", "#F44336") if not display_config.get("hide_negative_axis", False) else None
        }
        
        return {
            "data": chart_data,
            "colors": chart_colors,
            "rotation": CHART_PRIORITY.get("rotate_labels", 90),
            "show_negative": not display_config.get("hide_negative_axis", False)
        }
    
    def _get_default_chart_data(self):
        """Trả về dữ liệu biểu đồ mặc định nếu có lỗi"""
        return {
            "data": {"positive": 1.0, "neutral": 0.0},
            "colors": {
                "positive": CHART_PALETTE.get("positive", "#2E7D32"),
                "neutral": CHART_PALETTE.get("neutral", "#757575")
            },
            "rotation": 90,
            "show_negative": False
        }
    
    def _get_last_punctuation(self, text):
        """Lấy dấu câu cuối cùng của văn bản"""
        punct_pattern = r'([!?.,]+|:\)|:\(|:D|:\'\(|😊|😔|😢|😍|\.{3,})$'
        match = re.search(punct_pattern, text)
        if match:
            return match.group(1)
        return None