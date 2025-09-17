import re
import os
import string
import spacy
import json 
from collections import Counter
from collections import defaultdict
from time import pthread_getcpuclockid

# Install required packages if not already installed
!pip install scikit-learn nltk
!python -m spacy download it_core_news_sm

from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

try:
    nlp = spacy.load("it_core_news_sm")
    print("SpaCy Italian model loaded successfully.")
except OSError:
    print("SpaCy Italian model 'it_core_news_sm' not found.")
    print("Please run: python -m spacy download it_core_news_sm")


# Function to clean and extract title and author from a given line
def extract_title_author(line):
    match = re.match(r"^(.*?)\((.*?)\)$", line.strip())
    if match:
        title = match.group(1).strip().replace("\uFEFF", "").strip()  # Remove unwanted characters
        author = match.group(2).strip()
        return title, author
    return None, None


# Main function to process Kindle clippings
def process_clippings(input_file, use_spacy=False, num_words=20):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Split entries using Kindle’s separator
    entries = content.split("==========")
    clippings = defaultdict(list)

    for entry in entries:
        lines = [line.strip() for line in entry.split("\n") if line.strip()]
        if not lines:
            continue

        # Extract title and author from the first line
        title, author = extract_title_author(lines[0])
        if not title or not author:
            continue

        # Extract the highlighted text (last non-empty line)
        highlight = lines[-1]

        # Store the highlight under the corresponding book
        clippings[(title, author)].append(f"- {highlight}")

    # Create output directory
    output_dir = "markdown_notes"
    os.makedirs(output_dir, exist_ok=True)

    for (title, author), quotes in clippings.items():
        filename = f"{title.strip()}.md"
        filepath = os.path.join(output_dir, filename)

        keywords = []
        
        if use_spacy:
            doc = nlp("".join(quotes).lower())    
            for token in doc:
              # Filter out punctuation, numbers, and very short words
              if token.is_punct or token.is_space or token.is_digit or len(token.text) <= 2:
                  continue
    
              # Filter out stopwords (SpaCy's built-in stopword list is generally good)
              if token.is_stop:
                  continue
    
              # --- Filter by POS Tag ---
              # SpaCy uses Universal POS tags (NOUN, ADJ, VERB, etc.) which are standard.
              # We want NOUNs (sostantivi) and ADJs (aggettivi).
              if token.pos_ == "NOUN" or token.pos_ == "ADJ":
                  # Lemmatize the word (get its base form)
                  keywords.append(token.lemma_)
    
            # Count word frequencies
            word_frequency = Counter(keywords)
    
            # Return the most common words
            keywords = [w for w, count in word_frequecy.most_common(num_words)]
        else:
            # Apply TF-IDF to extract keywords
            vectorizer = TfidfVectorizer(stop_words=stopwords.words('italian'), max_features=25)
            X = vectorizer.fit_transform(quotes)
            keywords = vectorizer.get_feature_names_out()

        # Write formatted Markdown file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n")
            f.write(f"\n## Highlights\n\n")
            f.write("\n".join(quotes))
            f.write(f"\n\n*{author}*")
            f.write("\n* * *")
            f.write("\n\n### *Keywords:*\n")
            f.write(", ".join(keywords))
            f.write("\n\n### *GoodReads:*")
            f.write("\n*I've written about this book on [GoodReads]():*")
            f.write("\n\n* * *")
            f.write("\n\n### Book Summary")

# Specify the input file
input_file = "MyClippings.txt"
process_clippings(input_file, use_spacy=True)
