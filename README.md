# NLP-Assignment1

## Answer 1
All the data can be viewed on the server in the Punjabi_nlp_team4 folder. The downloaded data is in the "Downloaded Data" folder, and Scraped data is in the "Scraped Data" folder.

## Answer 2
data_sources.xlsx - corresponds to the table of downloaded and scraped data sources along with their sizes in GBs.

## Answer 3
The datasets on the server are in .txt format.

## Answer 4
Punjabi_Bad_Words_list.txt is the list of Punjabi bad words used for cleaning

## Answer 5
"data_cleaner.py" is the code for removing bad words, pornographic content, hate, and abuse. We have made use of the "Punjabi_Bad_Words_list.txt."
"data_cleaner2.py" is an alternative code used specifically for the scraped data, which also removes some Urdu words along with the Punjabi bad words because a lot of our scraped data contained Urdu text.

## Answer 6
data_sources.xlsx contains the table for cleaned data.

## Answer 7
Brief descriptions of the deduplication methods used:

*MinHash Jaccard Similarity*: This method estimates the similarity between two sets by hashing and comparing their elements, efficiently approximating Jaccard similarity for large datasets.
  
*Cosine Similarity*: It measures the angle between two vectors (representing documents) in a high-dimensional space, identifying duplicates based on how close their vectors are to each other.

*Levenshtein Distance*: Also known as edit distance, this method counts the minimum number of single-character edits (insertions, deletions, or substitutions) needed to change one string into another, identifying near-duplicate text.

*Fingerprinting*: A hashing-based technique that converts documents into fixed-size "fingerprints," allowing quick detection of identical or nearly identical text fragments.

Codes for all the methods have been written in the de_duplication.ipynb file

## Answer 8 

The size chart after deduplication can be found at data_sources.xlsx.

Note:- Please note that it was taking too much time on the server to run the code for deduplication for the downloaded data since it was too big, hence we ran the code for deduplication on scraped data only.

## CONTRIBUTION
* Hirva Patel - Collected data by downloading and scraping, Wrote and ran codes for de-duplication, and cleaning.
* Khushal Ramani -  Collected data by downloading and scraping, Wrote and ran codes for cleaning.
* Harshi Chandrafari - Collected data by downloading and scraping, Wrote and ran codes for de-duplication.
* Rushi Glasswala - Collected data by downloading and scraping, Wrote and ran codes for cleaning.
* Harshit Kothari - Collected data by downloading and scraping, Wrote and ran codes for de-duplication.

  Note - everyone contributed individually to the tables

