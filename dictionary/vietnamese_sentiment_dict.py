# Từ điển cảm xúc tiếng Việt
SENTIMENT_DICT = {
    # Từ tích cực
    "ngon": 0.8,
    "tốt": 0.8,
    "hay": 0.7,
    "đẹp": 0.7,
    "tuyệt": 0.9,
    "xuất sắc": 0.9,
    "hài lòng": 0.8,
    "thích": 0.7,
    "vui": 0.8,
    "hạnh phúc": 0.9,
    "thú vị": 0.8,
    "ấn tượng": 0.8,
    "yêu": 0.9,
    "thương": 0.8,
    "dễ thương": 0.8,
    "nắng ấm": 0.8,       
    "kỷ niệm": 0.1,         
    "tìm": 0.1,           
    "bước về phía": 0.5,
    "đáng yêu": 0.8,
    "tài năng": 0.5,
    "thông minh": 0.8,
    "xinh": 0.9,
    "đẹp trai": 0.7,
    "xinh đẹp": 0.8,
    "tận tâm": 0.8,
    "nhiệt tình": 0.8,
    "chu đáo": 0.8,
    "chuyên nghiệp": 0.8,
    "sáng tạo": 0.8,
    "độc đáo": 0.7,
    "dũng cảm": 0.9,
    "anh dũng": 0.9,
    "hy sinh": 0.8,
    "kiên cường": 0.8,
    "kiên quyết": 0.8,
    "sáng ngời": 0.9,
    "cao cả": 0.9,
    "vì nước": 0.9,
    "vì dân": 0.9,
    "phục vụ": 0.8,
    "trách nhiệm": 0.8,
    "tinh thần": 0.7,
    "ý chí": 0.8,
    "quyết tâm": 0.8,
    "chiến đấu": 0.8,
    "bảo vệ": 0.8,
    "trung thành": 0.8,
    "quên mình": 0.8,
    "quên thân": 0.8,
    "liệt sĩ": 0.8,
    "chiến sĩ": 0.8,
    "tuyệt hảo": 0.9,
    "hoàn hảo": 0.9,
    "tuyệt đỉnh": 0.9,
    "đỉnh cao": 0.9,
    "ưu tú": 0.8,
    "tài giỏi": 0.8,
    "thông thái": 0.8,
    "sáng suốt": 0.8,
    "khôn ngoan": 0.8,
    "tinh tế": 0.8,
    "tinh xảo": 0.8,
    "tinh vi": 0.8,
    "tuyệt diệu": 0.9,
    "kỳ diệu": 0.8,
    "thần kỳ": 0.8,
    "phi thường": 0.8,
    "vượt trội": 0.8,
    "ưu việt": 0.8,
    "tuyệt phẩm": 0.9,
    "tuyệt tác": 0.9,
    "kiệt tác": 0.9,
    "tuyệt mỹ": 0.9,
    "tuyệt sắc": 0.9,
    "tuyệt trần": 0.9,
    "tuyệt thế": 0.9,
    "cao quý": 0.8,
    "thanh cao": 0.8,
    "cao thượng": 0.8,
    "rực rỡ": 0.8,
    "chói lọi": 0.8,
    "lấp lánh": 0.7,
    "lung linh": 0.7,
    "huy hoàng": 0.8,
    "tráng lệ": 0.8,
    "uy nghi": 0.8,
    "oai phong": 0.8,
    "hùng dũng": 0.8,
    "hùng tráng": 0.8,
    "hùng vĩ": 0.8,
    "kỳ vĩ": 0.8,
    "uy nghiêm": 0.8,
    "oai hùng": 0.8,
    "yêu thương": 0.9,
    "quý mến": 0.8,
    "trân trọng": 0.8,
    "kính trọng": 0.8,
    "ngưỡng mộ": 0.8,
    "khâm phục": 0.8,
    "tôn vinh": 0.8,
    "ca ngợi": 0.8,
    "khen ngợi": 0.8,
    "tán dương": 0.8,
    "cổ vũ": 0.8,
    "động viên": 0.8,
    "khích lệ": 0.8,
    "ủng hộ": 0.8,
    "giúp đỡ": 0.8,
    "hỗ trợ": 0.8,
    "chia sẻ": 0.8,
    "đồng cảm": 0.8,
    "thấu hiểu": 0.8,
    "thông cảm": 0.8,
    "bao dung": 0.8,
    "tha thứ": 0.8,
    "khoan dung": 0.8,
    "độ lượng": 0.8,
    "nhân ái": 0.8,
    "nhân hậu": 0.8,
    "nhân từ": 0.8,
    "từ bi": 0.8,
    "hiền lành": 0.8,
    "hiền hậu": 0.8,
    "hiền từ": 0.8,
    "hiền dịu": 0.8,
    "hiền hòa": 0.8,
    "hiền minh": 0.8,
    "hiền triết": 0.8,
    "hiền nhân": 0.8,
    "hiền thánh": 0.8,
    "hiền tài": 0.8,
    "hiền sĩ": 0.8,
    "hiền đức": 0.8,
    "hiền lương": 0.8,
    "hiền thục": 0.8,
    "hiền thảo": 0.8,
    "tuyệt đối": 0.9,
    "hoàn toàn": 0.8,
    "mì ăn liền": 0.5,
    "không ngon": -0.3,
    "đâu": 0.0,
    "anh": 0.2,
    "à": 0.0,

    # Từ tiêu cực
    "tệ": -1.0,
    "kém": -0.8,
    "thất vọng": -0.9,
    "chán": -0.7,
    "khó chịu": -0.8,
    "xấu": -0.7,
    "tồi": -0.9,
    "không thích": -0.7,
    "phiền": -0.6,
    "ghét": -1.0,
    "giận": -0.9,
    "bực": -0.8,
    "tức": -0.8,
    "dở": -0.7,
    "kém cỏi": -0.8,
    "yếu": -0.6,
    "trách": -0.6,
    "trách tội": -0.8,
    "tội": -0.4,
    "tệ hại": -1.0,
    "thảm hại": -1.0,
    "kinh khủng": -0.9,
    "khủng khiếp": -0.9,
    "tồi tệ": -1.0,
    "dốt": -0.8,
    "ngu": -0.9,
    "xấu xí": -0.8,
    "thô lỗ": -0.8,
    "giày_vò":-0.8,
    "cẩu thả": -0.7,
    "lười": -0.7,
    "tội phạm": -0.9,
    "thiếu chuyên nghiệp": -0.8,
    "kém chất lượng": -0.8,
    "chơ vơ": -0.8,      
    "tan vỡ": -0.9,
    "vụn vỡ": -0.9, 
    "vỡ": -0.4,  
    "mất":-0.4,
    "chìm đắm": -0.7,     
    "lầm lỡ": -0.8,      
    "phai mờ": -0.8,      
    "xa cách": -0.9,      
    "nỗi đau": -0.9,      
    "chết lặng": -0.9,    
    "hao gầy": -0.8,      
    "người dưng": -0.8,   
    "khác lạ": -0.7,     
    "tổn thương": -0.9, 
    "cố chấp": -0.6,
    "âm thầm": -0.5,   
    "cố xóa": -0.7, 
    "đợi chờ": -0.7,   
    "ngu ngơ": -0.6,   
    "níu kéo": -0.8,    
    "hằn sâu": -0.8,
    "khóc": -0.9,
    "đau": -0.9,
    "buồn": -0.8,
    "đau khổ": -0.9,
    "đau đớn": -0.9,
    "khổ sở": -0.9,
    "đau lòng": -0.9,
    "thương tâm": -0.9,
    "xót xa": -0.9,
    "thê thảm": -1.0,
    "bi thương": -0.9,
    "bi đát": -0.9,
    "ai oán": -0.9,
    "thống khổ": -1.0,

    # Từ trung lập
    "bình thường": 0.0,
    "thường": 0.0,
    "vừa": 0.0,
    "tạm": 0.0,
    "được": 0.0,
    "tàm tạm": 0.0,
    "trung bình": 0.0,
    "không đặc biệt": 0.0,
    "bình thường thôi": 0.0,
    "tạm được": 0.1,
    "tạm ổn": 0.1,
    "không tệ": 0.2,
    "không tốt không xấu": 0.0,
    "không hay không dở": 0.0,
    "không ra gì": -0.2,
    "nghĩ": 0.0,
    "suy nghĩ": 0.0,
    "tưởng tượng": 0.0,
    "mơ tưởng": 0.0,
    "mơ mộng": 0.0,
    "mơ màng": 0.0,
    "mơ hồ": 0.0,
    "mơ mơ": 0.0,

    # Từ mới
    "lương thiện": 0.9,
    "tử tế": 0.9,
    "đơn giản": 0.7,
    "vui vẻ": 0.8,
    "chọn lựa": 0.6,
    "cuộc sống": 0.7,
    "dành": 0.4,
    "sự": 0.3,
    "một": 0.1,
    "mỗi": 0.5,
    "ngày": 0.5,
    "trời": 0.6,
    "ban": 0.6,
    "sống": 0.7,
    "hạ giá": 0.8,
    "người đẹp": 0.9,
    "dành cho": 0.7,
    "nè": 0.5,
    "tướng": 0.6,
    "cho": 0.3,
    "các": 0.2,
    "người": 0.4,
    "trắng": 0.8,
    "càng": 0.6,
    "em": 0.3,
    "với": 0.2,
    "kỉ_niệm":0.3,
    "gìn_giữ": 0.7,     
    "trân_trọng": 0.8,  
    "yêu_thương": 0.9,   
    "thời_gian": 0.0,    
    "bình_yên": 0.8,     
    "quan_trọng": 0.7,   
    "hồn_nhiên": 0.7,    
    "lấp_lánh": 0.7,     
    "âu_yếm": 0.8,       
    "lặng_lẽ": 0.0,      
    "lặng_im": 0.0,      
    "tương_lai": 0.0,    
    "hiện_tại": 0.0,     
    "vô_định": -0.3,     
    "toan_tính": -0.4,   
    "úa_tàn": -0.7,      
    "vỡ_tan": -0.8,      
    "khổ_tâm": -0.7,    
    "lùi_bước": -0.4,
    "giết": -0.3,
    "chết": -0.4,
    "bỗng_chốc": 0.0,    
    "mãi_mãi": 0.7,
    "thi thoảng": 0.1, 
    "nhà": 0.3,     
    "bên": 0.2,            
    "họ": 0.0,             
    "nghe": 0.1,          
    "thấy": 0.1,         
    "tiếng": 0.0,          
    "ta": 0.1,             
    "hoặc": 0.0,           
    "đập": -0.5,           
    "phá": -0.6,           
    "như": 0.0,            
    "đang": 0.0,           
    "tức_giận": -0.8,  
    "hết":-0.2,
    "xa":-0.1,    
    "điều": 0.0,           
    "gì": 0.0,             
    "nỡ": 0.0,           
    "chia_lìa": -0.7,    
    "chốn": 0.0,         
    "dương": 0.1,        
    "trần": 0.0,
    "phòng": 0.0,    
    "này": 0.0,      
    "thiếu": -0.4,     
    "bàn": 0.2,         
    "học": 0.3,           
    "ai": 0.0,           
    "nhớ": -0.6,        
    "sầu": -0.8,        
    "biết": 0.0,          
    "mấy": 0.0,        
    "duyên": 0.5,        
    "sao": 0.0,          
    "giờ": 0.0,         
    "tan_tành": -0.8
}

# Từ phủ định
NEGATION_WORDS = {
    "không",
    "chẳng",
    "chả",
    "đừng",
    "đừng có",
    "không phải",
    "không thể",
    "không nên",
    "không được",
    "không còn",
    "chưa",
    "chưa từng",
    "chưa bao giờ",
    "không bao giờ",
    "không hề",
    "không có",
    # Thêm từ phủ định mới
    "đừng",
    "đừng có",
    "không phải",
    "không thể",
    "không nên",
    "không được",
    "không còn",
    "chưa",
    "chưa từng",
    "chưa bao giờ",
    "không bao giờ",
    "không hề",
    "không có",
    "chẳng",
    "chả",
    "đừng",
    "đừng có",
    "không phải",
    "không thể",
    "không nên",
    "không được",
    "không còn",
    "chưa",
    "chưa từng",
    "chưa bao giờ",
    "không bao giờ",
    "không hề",
    "không có"
}

# Từ tăng cường
INTENSIFIER_WORDS = {
    "rất": 1.5,
    "quá": 1.5,
    "cực kỳ": 2.0,
    "vô cùng": 2.0,
    "hết sức": 1.8,
    "cực": 1.8,
    "siêu": 1.7,
    "đặc biệt": 1.6,
    "vô địch": 2.0,
    "tuyệt_đối": 2.0,
    "cực_phẩm": 2.0,
    "đỉnh": 1.8,
    "max": 1.8,
    "khủng": 1.7,
    "bá đạo": 1.8,
    "xịn": 1.6,
    "đáng kinh ngạc": 1.7,
    "phi thường": 1.8,
    "xuất thần": 1.9,
    "tối cao": 2.0,
    "các": 1.2,
    "càng": 1.8,
    "càng ngày càng": 2.0,
    "càng ngày càng trắng": 1.5,
    "càng ngày càng xinh": 1.5
}

# Từ giảm nhẹ
DIMINISHER_WORDS = {
    "hơi": 0.7,
    "khá": 0.8,
    "tương đối": 0.8,
    "gần như": 0.9,
    "gần": 0.9,
    "tàm tạm": 0.6,
    "có vẻ": 0.8,
    "có lẽ": 0.7,
    "không quá": 0.7,
    "không hẳn": 0.6,
    "không nhiều": 0.6,
    "không lắm": 0.7,
    "không đến nỗi": 0.7,
    "không đáng kể": 0.5,
    "không đủ": 0.6,
}

# Từ kết hợp
COMPOUND_WORDS = {
    # Cụm từ tích cực
    "càng ngày càng": 1.2,  
    "càng ngày càng trắng": 1.5,  
    "càng ngày càng xinh": 1.5,  
    "hạ giá tướng": 1.0,  
    "dành cho người đẹp": 1.0,  
    "trắng với xinh": 1.2,  

    # Cụm từ tiêu cực
    "không ngon": -0.3,  
    "không được tốt": -0.6,  
    "không được đẹp": -0.6,  
    "thiếu chuyên nghiệp": -0.8,
    "kém chất lượng": -0.8,
    
    # Cụm từ với ý nghĩa đặc biệt
    "vì nước quên thân": 1.0,  
    "vì dân phục vụ": 1.0,  
    "hy sinh vì": 1.0,  

    "gìn giữ trân trọng": 0.9,    
    "yêu thương em": 0.9,        
    "dành thời gian": 0.7,         
    "cuộc sống vô định": -0.5,     
    "lời xin lỗi": 0.3,            
    "tình yêu vỡ tan": -0.9,       
    "ngắm em từ xa": 0.6,          
    "lặng lẽ kế bên": 0.5,         
    "ánh mắt lấp lánh": 0.8,       
    "hiểu thấu lòng": 0.7,         
    "người quan trọng": 0.8,       
    "tổn thương xước": -0.8,       
    "khổ tâm gượng sống": -0.7,    
    "ngắt cánh hoa": -0.6,         
    "duyên trời ban": 0.8,
     "trái tim vẫn không ngừng nhớ": -0.8,  
    "tình yêu đã phai mờ": -0.9,          
    "cuộc đời lắm vô thường": -0.8,  
    "mất cả đời": -0.8,
    "tự mình ôm lấy tổn thương": -0.9,    
    "âm thầm bước về phía nắng ấm": 0.3,  
    "cơn mưa đêm xóa hết kỷ niệm": -0.9,   
    "hoa nở không màu": -0.8,   
    "kí ức cố xóa": -0.9,              
    "đoạn tình ban sơ": -0.7,         
    "đại lộ tan vỡ": -0.9,         
    "chìm đắm trong lầm lỡ": -0.9,   
    "không ngừng nhớ": -0.8,        
    "tình yêu đã phai mờ": -0.9, 
    "hoa nở không màu": -0.8,    
    "càng níu kéo càng xa cách": -0.9, 
    "ôm nỗi đau": -0.9,              
    "chết lặng giữa trời mây": -0.9,  
    "trái tim hao gầy": -0.9,         
    "hai người dưng khác lạ": -0.9,   
    "chẳng thể nói ra": -0.8,         
    "ôm lấy tổn thương": -0.9,         
    "cơn mưa đêm xóa hết kỷ niệm": -0.9,      
    "duyên tan": -0.7,  
    "tan tành": -0.8,        
    "buồn sầu": -0.8,   
    "sầu muộn": -0.8,   
    "giết chết":-0.8,
}

# Cấu hình hiển thị biểu đồ
CHART_CONFIG = {
    "display": {
        "enabled": True,
        "show_all_columns": True,
        "bars": {
            "show_values": True
        }
    }
}

# Cấu hình hiển thị
DISPLAY_CONTROLLER = {
    "calculation": {
        "use_raw_values": True,
        "respect_signs": True
    }
}

# Quy tắc phân tích cảm xúc
SENTIMENT_RULES = {
    "thresholds": {
        "positive": 0.1,     # > 0.1 là tích cực
        "negative": -0.1,    # < -0.1 là tiêu cực
        "neutral": [-0.1, 0.1]  # [-0.1, 0.1] là trung lập
    }
}

# Cấu hình ưu tiên biểu đồ
CHART_PRIORITY = {
    "enforce_config": False,
    "confidence_min": 0.0,
    "rotate_labels": 0,
    "show_values": True,
    "relative_scaling": False
}

# Cấu hình hiển thị văn bản
TEXT_DISPLAY = {
    "sentiment": {
        "positive": {
            "text": "Tích cực",
            "icon": "😊"
        },
        "neutral": {
            "text": "Trung lập",
            "icon": "😐"
        },
        "negative": {
            "text": "Tiêu cực", 
            "icon": "😔"
        }
    },
    "confidence": {
        "high": {
            "text": "Độ tin cậy cao",
            "threshold": 0.7
        },
        "medium": {
            "text": "Độ tin cậy trung bình",
            "threshold": 0.4
        },
        "low": {
            "text": "Độ tin cậy thấp",
            "threshold": 0.0
        }
    }
}

# Màu sắc cơ bản
CHART_PALETTE = {
    "positive": "#2E7D32",  # Xanh lá
    "neutral": "#757575",   # Xám
    "negative": "#F44336"   # Đỏ
}

# Phân tích dấu câu
PUNCTUATION_ANALYSIS = {
    "!": {
        "effect": "intensify",
        "multiplier": 1.5,
        "description": "Dấu chấm than làm tăng cường cảm xúc"
    },
    "!!": {
        "effect": "intensify",
        "multiplier": 2.0,
        "description": "Nhiều dấu chấm than làm tăng cường cảm xúc mạnh hơn"
    },
    "!!!": {
        "effect": "intensify",
        "multiplier": 2.5,
        "description": "Rất nhiều dấu chấm than làm tăng cường cảm xúc rất mạnh"
    },
    "?": {
        "effect": "question",
        "multiplier": 0.8,
        "description": "Dấu hỏi có thể làm giảm nhẹ mức độ chắc chắn"
    },
    "??": {
        "effect": "question",
        "multiplier": 0.6,
        "description": "Nhiều dấu hỏi thể hiện sự nghi ngờ cao"
    },
    "...": {
        "effect": "pause",
        "multiplier": 0.9,
        "description": "Dấu ba chấm thể hiện sự ngập ngừng hoặc không chắc chắn"
    },
    ".": {
        "effect": "neutral",
        "multiplier": 1.0,
        "description": "Dấu chấm câu bình thường"
    },
    ",": {
        "effect": "neutral",
        "multiplier": 1.0,
        "description": "Dấu phẩy không ảnh hưởng đến cảm xúc"
    },
    ":)": {
        "effect": "positive",
        "value": 0.5,
        "description": "Biểu tượng mặt cười thể hiện cảm xúc tích cực"
    },
    ":(": {
        "effect": "negative",
        "value": -0.5,
        "description": "Biểu tượng mặt buồn thể hiện cảm xúc tiêu cực"
    },
    ":D": {
        "effect": "positive",
        "value": 0.7,
        "description": "Biểu tượng cười lớn thể hiện cảm xúc rất tích cực"
    },
    ":'(": {
        "effect": "negative",
        "value": -0.8,
        "description": "Biểu tượng khóc thể hiện cảm xúc rất tiêu cực"
    },
    "😊": {
        "effect": "positive",
        "value": 0.6,
        "description": "Emoji mặt cười thể hiện cảm xúc tích cực"
    },
    "😔": {
        "effect": "negative",
        "value": -0.6,
        "description": "Emoji buồn thể hiện cảm xúc tiêu cực"
    },
    "😢": {
        "effect": "negative",
        "value": -0.7,
        "description": "Emoji khóc thể hiện cảm xúc tiêu cực"
    },
    "😍": {
        "effect": "positive",
        "value": 0.9,
        "description": "Emoji yêu thích thể hiện cảm xúc rất tích cực"
    }
}

# Cấu hình hiển thị biểu đồ
CHART_CONFIG = {
    "display": {
        "enabled": True,
        "show_all_columns": True,
        "bars": {
            "show_values": True
        }
    }
}

# Cấu hình hiển thị
DISPLAY_CONTROLLER = {
    "calculation": {
        "use_raw_values": True,
        "respect_signs": True
    }
}

# Quy tắc phân tích cảm xúc
SENTIMENT_RULES = {
    "thresholds": {
        "positive": 0.1,     # > 0.1 là tích cực
        "negative": -0.1,    # < -0.1 là tiêu cực
        "neutral": [-0.1, 0.1]  # [-0.1, 0.1] là trung lập
    }
}

# Cấu hình ưu tiên biểu đồ
CHART_PRIORITY = {
    "enforce_config": False,
    "confidence_min": 0.0,
    "rotate_labels": 0,
    "show_values": True,
    "relative_scaling": False
}

# Cấu hình hiển thị văn bản
TEXT_DISPLAY = {
    "sentiment": {
        "positive": {
            "text": "Tích cực",
            "icon": "😊"
        },
        "neutral": {
            "text": "Trung lập",
            "icon": "😐"
        },
        "negative": {
            "text": "Tiêu cực", 
            "icon": "😔"
        }
    },
    "confidence": {
        "high": {
            "text": "Độ tin cậy cao",
            "threshold": 0.7
        },
        "medium": {
            "text": "Độ tin cậy trung bình",
            "threshold": 0.4
        },
        "low": {
            "text": "Độ tin cậy thấp",
            "threshold": 0.0
        }
    }
}

# Màu sắc cơ bản
CHART_PALETTE = {
    "positive": "#2E7D32",  # Xanh lá
    "neutral": "#757575",   # Xám
    "negative": "#F44336"   # Đỏ
}

