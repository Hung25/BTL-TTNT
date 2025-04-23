import os
import json

class DictionaryManager:
    """
    Manager class to handle dictionary operations using JSON files
    instead of Python modules for better stability and safety
    """
    def __init__(self, dict_dir):
        self.dict_dir = dict_dir
        self.json_dir = os.path.join(dict_dir, "json")
        
        # Initialize dictionaries
        self.sentiment_dict = {}
        self.punctuation_analysis = {}
        self.compound_words = {}
        self.diminisher_words = {}
        self.intensifier_words = {}
        self.negation_words = []
        self.proverbs = {}
        
        # Load all dictionaries
        self.load_all()
    
    def load_json(self, filename):
        """Load a dictionary from a JSON file"""
        filepath = os.path.join(self.json_dir, filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading {filename}: {str(e)}")
                return None
        else:
            print(f"Dictionary file {filename} not found.")
            return None
    
    def save_json(self, data, filename):
        """Save a dictionary to a JSON file"""
        filepath = os.path.join(self.json_dir, filename)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Error saving {filename}: {str(e)}")
            return False
    
    def load_all(self):
        """Load all dictionaries at once"""
        # Load sentiment dictionary
        data = self.load_json("sentiment_dict_data.json")
        if data:
            self.sentiment_dict = data
        
        # Load punctuation analysis dictionary
        data = self.load_json("punctuation_analysis_data.json")
        if data:
            self.punctuation_analysis = data
        
        # Load compound words dictionary
        data = self.load_json("compound_words_data.json")
        if data:
            self.compound_words = data
        
        # Load diminisher words dictionary
        data = self.load_json("diminisher_words_data.json")
        if data:
            self.diminisher_words = data
        
        # Load intensifier words dictionary
        data = self.load_json("intensifier_words_data.json")
        if data:
            self.intensifier_words = data
        
        # Load negation words dictionary (stored as list in JSON)
        data = self.load_json("negation_words_data.json")
        if data:
            self.negation_words = data
        
        # Load proverbs dictionary
        data = self.load_json("proverbs_data.json")
        if data:
            self.proverbs = data
    
    def add_word_to_sentiment_dict(self, word, score):
        """Add a word to the sentiment dictionary"""
        # Check if the word already exists in the dictionary
        if word in self.sentiment_dict:
            return False, "Từ đã tồn tại trong từ điển"
        
        # Add the word if it doesn't exist
        self.sentiment_dict[word] = score
        success = self.save_json(self.sentiment_dict, "sentiment_dict_data.json")
        return success, "Thêm từ thành công" if success else "Lỗi khi lưu từ điển"
    
    def add_emoji_to_punctuation(self, emoji, effect, value, description):
        """Add an emoji to the punctuation analysis dictionary"""
        self.punctuation_analysis[emoji] = {
            "effect": effect,
            "value": value,
            "description": description
        }
        return self.save_json(self.punctuation_analysis, "punctuation_analysis_data.json")
    
    def add_compound_word(self, compound, score):
        """Add a compound word to the compound words dictionary"""
        self.compound_words[compound] = score
        return self.save_json(self.compound_words, "compound_words_data.json")
    
    def get_sentiment_dict(self):
        return self.sentiment_dict
    
    def get_punctuation_analysis(self):
        return self.punctuation_analysis
    
    def get_compound_words(self):
        return self.compound_words
    
    def get_diminisher_words(self):
        return self.diminisher_words
    
    def get_intensifier_words(self):
        return self.intensifier_words
    
    def get_negation_words(self):
        return self.negation_words
        
    def get_proverbs(self):
        return self.proverbs
        
    def add_proverb(self, proverb, score):
        """Add a proverb to the proverbs dictionary"""
        if proverb in self.proverbs:
            return False, "Thành ngữ/tục ngữ đã tồn tại trong từ điển"
            
        # Add the proverb
        self.proverbs[proverb] = score
        
        # Also add to sentiment dictionary for consistency
        self.sentiment_dict[proverb] = score
        
        # Save both dictionaries
        success1 = self.save_json(self.proverbs, "proverbs_data.json")
        success2 = self.save_json(self.sentiment_dict, "sentiment_dict_data.json")
        
        if success1 and success2:
            return True, "Thêm thành ngữ/tục ngữ thành công"
        else:
            return False, "Lỗi khi lưu từ điển"
