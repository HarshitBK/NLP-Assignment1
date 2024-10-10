import re
import os 
import argparse

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

def remove_words(text, words_to_remove):
    # Create a regular expression pattern for whole word matching
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b'
    
    # Remove the words
    cleaned_text = re.sub(pattern, '', text)
    
    # Remove extra whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

# Input and output file paths


def main(input_file):
    # Ensure output directory exist
    output_dir = '/mnt/HDFS1/language_nlp/Punjabi_nlp_team4/Cleaned_Downloaded_Data'
    output_file_path = os.path.join(output_dir, os.path.basename(input_file))

    # Read the input file, clean the text, and write to the output file
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
        print(f"Cleaning file {input_file}")
        for line in infile: 
            cleaned_line = remove_words(line, words_to_remove)
            outfile.write(cleaned_line + '\n')

    print(f"Cleaned text from {input_file} and saved to {output_file_path}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Remove specific words from a text file.')
    parser.add_argument('input_file', type=str, help='The path to the input text file.')
    args = parser.parse_args()

    # Run the main function with arguments
    main(args.input_file)

