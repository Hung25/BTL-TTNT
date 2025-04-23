import os
import json
import importlib.util

# Directory containing the dictionary Python files
py_dict_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dictionary")
json_dict_dir = os.path.join(py_dict_dir, "json")

# Ensure the JSON directory exists
os.makedirs(json_dict_dir, exist_ok=True)

# Files to convert
dict_files = [
    "sentiment_dict_data.py",
    "punctuation_analysis_data.py",
    "compound_words_data.py",
    "diminisher_words_data.py",
    "intensifier_words_data.py",
    "negation_words_data.py"
]

for py_file in dict_files:
    # Load the Python module
    module_name = py_file.replace(".py", "")
    module_path = os.path.join(py_dict_dir, py_file)
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Get the dictionary name from the module
    dict_name = None
    for name in dir(module):
        if name.isupper() and not name.startswith("__"):
            dict_name = name
            break
    
    if dict_name:
        # Convert the dictionary to JSON
        dictionary = getattr(module, dict_name)
        json_file = os.path.join(json_dict_dir, f"{module_name}.json")
        
        # Handle different data types for JSON serialization
        if isinstance(dictionary, set):
            # Convert sets to lists for JSON serialization
            dictionary = list(dictionary)
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=4)
        
        print(f"Converted {py_file} to {json_file}")
    else:
        print(f"Could not find dictionary in {py_file}")

print("Conversion complete!")
