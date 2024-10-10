# NLP-Assignment1

## Answer 1
All the data can be viewed on the server in the Punjabi_nlp_team4 folder. The downloaded data is in the "Downloaded Data" folder, and Scraped data is in the "Scraped Data" folder.

## Answer 2
data_sources.xlxs - corresponds to the table of downloaded and scraped data sources along with their sizes in GBs.

## Answer 3
The datasets on the server are in .txt format.

## Answer 4
Punjabi_Bad_Words_list.txt is the list of Punjabi bad words used for cleaning

## Answer 5
"data_cleaner.py" is the code for removing bad words, pornographic content, hate, and abuse. We have made use of the "Punjabi_Bad_Words_list.txt."
"data_cleaner2.py" is an alternative code used specifically for the scraped data, which also removes some Urdu words along with the Punjabi bad words because a lot of our scraped data contained Urdu text.

## Answer 6
Cleaned_Downloaded_Data.csv - corresponds to the table of cleaned downloaded data

Cleaned_Scraped_Data.csv - corresponds to the table of cleaned scraped data

## Answer 8
Brief descriptions of the deduplication methods used:

**MinHash Jaccard Similarity**: This method estimates the similarity between two sets by hashing and comparing their elements, efficiently approximating Jaccard similarity for large datasets.
  
**Cosine Similarity**: It measures the angle between two vectors (representing documents) in a high-dimensional space, identifying duplicates based on how close their vectors are to each other.

**Levenshtein Distance**: Also known as edit distance, this method counts the minimum number of single-character edits (insertions, deletions, or substitutions) needed to change one string into another, identifying near-duplicate text.

**Fingerprinting**: A hashing-based technique that converts documents into fixed-size "fingerprints," allowing quick detection of identical or nearly identical text fragments.
