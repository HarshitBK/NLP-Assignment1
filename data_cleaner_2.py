import re
import os 

# List of words to remove
words_to_remove = [
    "ਕੁੱਤਾ", "ਕੁੱਤੀ", "ਚੂਤ", "ਮਾਦਰਚੋਦ", "ਬੇਨਚੋਦ", "ਭੈਂਚੋਦ", "ਗਾਂਡੂ", "ਗਾਂਡ", 
    "ਲੋੜੀ", "ਜਾਨਨੀ", "ਹਾਰਾਮੀ", "ਭੋਸੜਾ", "ਭੋਸੜੇ", "ਸੁਆਰ", "ਚੂਤਿਆਪਾ", "ਭੈਂਸ", 
    "ਘਾਂਟ", "ਪਟਾਕਾ", "ਚਮਾਰ", "ਲਾਂਡਾ", "ਮੁਫਤਖੋਰ", "ਕਮਬਖ਼ਤ", "ਬਾਵਲੀ ਬੂਚ", 
    "ਕੁੜਿਆਰਪਣ", "ਭੰਡ", "ਲੁੱਚੀ", "ਦੌੜੀ", "ਖੋਤੀਆ", "ਬੱਕਰੀ", "ਕਲੰਕਨੀ", "ਕਮੀਨੀ", 
    "ਰੰਡੀ", "ਚਮਕੀ", "ਫਾਹਿਸ਼ਾ", "ਗਰਾਂਡਾ", "ਹਜਾਰੀ", "ਚਾਕਲੀ", "ਧੋੜੀ", "ਡਿੱਗੇੜੀ", 
    "ਖਸਮਨੁੱਖ", "ਖੁਜਲੀ", "ਭੜਵਾ", "ਭੜਵੀ", "ਜੁੱਟ", "ਭੁੱਖੀ", "ਖੋਟਾ", "ਕੁੱਝੀ", 
    "ਕੁੱਤੇ ਦੀ ਪੁੱਤ", "ਤੂੰ ਤਾਂ ਮਰ", "ਮੱਕੀ ਮੱਟ", "ਫ਼ੁੱਦੂ", "ਲੁੱਚਾ", "ਗੱਲਾ ਪਾ ਕੇ", 
    "ਖੁੱਬਾ", "ਚਪੜਾਸੀ", "ਕੱਮਿਆਰ", "ਧੋਬੀ", "ਮੁਲਿਆਢੀ", "ਜ਼ਾਨਵਰ", "ਹੱਥੀ", "ਬੀੜੀ", 
    "ਖੋਪਰੀ", "ਤਿੰਨ ਕੁੜੀ", "ਤੌੜੀ", "ਖੱਬਾ ਖੱਜਲ", "ਭੋਣਦੀ", "ਤੂੰ ਛੱਡ", "ਲੰਬਾ ਸੂ", 
    "ਚੂੜੀ", "ਲਾਂਡੀਆ", "ਭੂਡਾ", "ਪਾਉਡਰ", "ਬੱਟੀ", "ਕੰਜਰ", "ਲਾਹਣਤ", "ਘੱਟੀਆ", 
    "ਧੱਕੜ", "ਚਮੜਾ", "ਚੂੜੀਮਾਰ", "ਕੱਬੜੀ", "ਲੂਜ ਮਾੜਾ", "ਕੂੜਾ", "ਭੱਠਰ", "ਨਿੱਕਮੀ", 
    "ਕੰਜਰਿਆ", "ਚੋਖਰੀ", "ਖੁਰਾਂਕਣ", "ਕੁੰਡੀ", "ਬਾਲਟਾ", "ਫੇਕੂ", "ਕੱਬੜਾ", "ਘੱਟੜਾ", 
    "ਡੋਰਾ", "ਚੱਪਲ", "ਫੁਟਿਆ", "ਭਟਵਾਰਾ", "ਲਤਵਾਰਾ", "ਬਾਲਟੀ", "ਮੁੰਮੀ", "ਬੋਟਾ", 
    "ਧਿੱਡ", "ਜਾਟੀ", "ਪਟਵਾਰੀ", "ਬੰਗੀ", "ਡਾਕੂ", "ਚੌਬਾ", "ਨਿੰਮ", "ਹੌਕਾ", "ਡੰਡਾ", "ਜੱਟ"
]

english_pattern = r'\b[a-zA-Z]+\b'
urdu_pattern = r'[\u0600-\u06FF]+'

def remove_words(text, words_to_remove):
    # Create a regular expression pattern for whole word matching
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b'
    
    # Remove the words
    cleaned_text = re.sub(pattern, '', text)
    cleaned_text = re.sub(english_pattern, '', cleaned_text)
    cleaned_text = re.sub(urdu_pattern, '', cleaned_text)
    # Remove extra whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text


def remove_invalid_symbols(file_path):
    # Read the file and remove invalid characters like the � symbol
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read().replace('�', '')
    
    # Write the cleaned content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Input and output file paths
input_dir = '/mnt/HDFS1/language_nlp/Punjabi_nlp_team4/Working/part 6'
output_dir = '/mnt/HDFS1/language_nlp/Punjabi_nlp_team4/Cleaned_Downloaded_Data'

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)  # Keep the same name
        
        if os.path.exists(output_file_path):
            print(f"{filename} is already cleaned, skipping.")
            continue

        #remove_invalid_symbols(input_file_path)

        with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
            print(f"Cleaning file {filename}")
            for line in infile:
                cleaned_line = remove_words(line, words_to_remove)
                outfile.write(cleaned_line + '\n')

        print(f"Cleaned text from {filename} and saved to {output_file_path}")

print("Cleaning process completed.")

