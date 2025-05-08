# Kindle Clippings to Markdown Notes  

## 📖 Overview  
This script extracts highlights and notes from Kindle's `MyClippings.txt` file and organizes them into structured **Markdown files**. Each book receives its own file, formatted according to a predefined template, making it easy to manage and review annotations efficiently.  

## 🚀 Features  
- Parses **MyClippings.txt** and extracts highlights per book.  
- Saves each book's highlights in an **individual Markdown file** with a structured format.  
- Includes **author details** and **keywords extraction** for better organization.  
- Supports **stopword filtering** to refine keyword selection.  

## 🛠️ Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/Kindle-Clippings-to-Markdown-Notes.git
   cd Kindle-Clippings-to-Markdown-Notes
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Download NLTK stopwords dataset (only needed once):  
   ```python
   import nltk
   nltk.download('stopwords')
   ```

## 📂 Repository Structure  
```
Kindle-Clippings-to-Markdown-Notes/
│── README.md              # Documentation
│── script/
│   └── process_clippings.py   # Main Python script
│── examples/
│   └── example_input.txt   # Sample Kindle clippings file
│   └── example_output.md   # Sample Markdown output
│── requirements.txt        # Dependencies
│── LICENSE                 # License file
```

## 🔧 Usage  
Place your `MyClippings.txt` file in the repository and run:  
```bash
python script/process_clippings.py MyClippings.txt
```
This generates Markdown notes for each book in the `citations_output/` directory.  

## 📜 Example Markdown Output  
```md
# Book Title

## Citazioni

- "Highlighted text from the book."
- "Another important passage."

*Author Name*

* * *

### *Keywords:*  
highlight, passage, insight, bookname  

### *GoodReads:*  
*Ho scritto su [GoodReads]():*  

* * *

### Quarta di copertina  
```

## ⚖️ License  
This project is licensed under the **MIT License**. Feel free to use, modify, and share.  
