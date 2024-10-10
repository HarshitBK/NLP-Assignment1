import pandas as pd
import os
import re
from Levenshtein import distance as levenshtein_distance
import hashlib

# Function to read text from files and split into sentences
def read_punjabi_text_file(file_path):
    """Read a Punjabi text file and split into sentences."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # Split by sentence end markers (adjusted for Gurmukhi punctuation)
    sentences = re.split(r'[।?!]|।।', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences

# Levenshtein Deduplication Function
def levenshtein_deduplication(df, max_distance=2):
    """Deduplicate sentences using Levenshtein distance."""
    to_remove = set()

    for i in range(len(df)):
        if i in to_remove:
            continue
        for j in range(i + 1, len(df)):
            if levenshtein_distance(df.iloc[i]["sentence"], df.iloc[j]["sentence"]) <= max_distance:
                to_remove.add(j)

    df_levenshtein = df.drop(index=to_remove).reset_index(drop=True)
    return df_levenshtein

# Fingerprinting Deduplication Function
def fingerprint_deduplication(df):
    """Deduplicate sentences using fingerprinting (hashing)."""
    df["hash"] = df["sentence"].apply(lambda x: hashlib.md5(x.encode('utf-8')).hexdigest())
    df_fingerprint = df.drop_duplicates(subset="hash").drop(columns=["hash"]).reset_index(drop=True)
    return df_fingerprint

# Main function to process files, create a DataFrame, deduplicate, and save the results
# def process_and_deduplicate_files(input_dir, output_dir):
#     all_sentences = []

#     # Read all files and gather sentences
#     for file_name in os.listdir(input_dir):
#         if file_name.endswith('.txt'):
#             input_file_path = os.path.join(input_dir, file_name)
#             print(f"Reading {input_file_path}...")
#             sentences = read_punjabi_text_file(input_file_path)
#             all_sentences.extend(sentences)

#     # Create a DataFrame for all sentences
#     df = pd.DataFrame(all_sentences, columns=["sentence"])
#     print(f"Length of DataFrame before deduplication: {len(df)}")
#     # Make a copy for both deduplication methods
#     df_copy_levenshtein = df.copy()

#     # Apply Levenshtein deduplication
#     df_levenshtein = levenshtein_deduplication(df_copy_levenshtein)
#     print(f"Levenshtein Deduplication - Number of unique sentences: {len(df_levenshtein)}")

#     # Save Levenshtein deduplicated data
#     levenshtein_output_path = os.path.join(output_dir, "deduplicated_levenshtein.txt")
#     df_levenshtein["sentence"].to_csv(levenshtein_output_path, index=False, header=False)
#     print(f"Levenshtein deduplicated file saved to {levenshtein_output_path}")

#     # Apply Fingerprinting deduplication
#     df_fingerprint = fingerprint_deduplication(df)
#     print(f"Fingerprint Deduplication - Number of unique sentences: {len(df_fingerprint)}")

#     # Save Fingerprint deduplicated data
#     fingerprint_output_path = os.path.join(output_dir, "deduplicated_fingerprint.txt")
#     df_fingerprint["sentence"].to_csv(fingerprint_output_path, index=False, header=False)
#     print(f"Fingerprint deduplicated file saved to {fingerprint_output_path}")


def process_and_deduplicate_files(input_dir, output_dir):
    # Process each file one by one
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.txt'):
            input_file_path = os.path.join(input_dir, file_name)
            levenshtein_output_path = os.path.join(output_dir, f"{file_name}_deduplicated_levenshtein.txt")
            fingerprint_output_path = os.path.join(output_dir, f"{file_name}_deduplicated_fingerprint.txt")
            
            print(f"Reading {input_file_path}...")
            
            # Read the file and create a DataFrame
            sentences = read_punjabi_text_file(input_file_path)
            df = pd.DataFrame(sentences, columns=["sentence"])
            print(f"Length of DataFrame before deduplication: {len(df)}")

            # Apply Levenshtein deduplication

            if not os.path.exists(levenshtein_output_path):
                df_levenshtein = levenshtein_deduplication(df)
                print(f"Levenshtein Deduplication - Number of unique sentences: {len(df_levenshtein)}")
                # Save Levenshtein deduplicated data
                df_levenshtein["sentence"].to_csv(levenshtein_output_path, index=False, header=False)
                print(f"Levenshtein deduplicated file saved to {levenshtein_output_path}")

            if not os.path.exists(fingerprint_output_path):
                df_fingerprint = fingerprint_deduplication(df)
                print(f"Fingerprint Deduplication - Number of unique sentences: {len(df_fingerprint)}")
                # Save Fingerprint deduplicated data
                df_fingerprint["sentence"].to_csv(fingerprint_output_path, index=False, header=False)
                print(f"Fingerprint deduplicated file saved to {fingerprint_output_path}")

# Example usage
input_dir = "/mnt/HDFS1/language_nlp/Punjabi_nlp_team4/Cleaned_Scraped_Data"  # Directory containing text files
output_dir = "/mnt/HDFS1/language_nlp/Punjabi_nlp_team4/Deduplicated_Scraped_Data"  # Directory to save output

# Run the process
process_and_deduplicate_files(input_dir, output_dir)
