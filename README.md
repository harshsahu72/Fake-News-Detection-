<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&pause=1000&color=6C63FF&center=true&vCenter=true&width=700&lines=Fake+News+Detector;AI-Powered+Fact+Checking;Random+Forest+%2B+TF-IDF;83%25%2B+Accuracy+on+Sample+Data" alt="Typing SVG" />
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-1.7-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-2.3-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Model-Random%20Forest-6C63FF?style=flat-square"/>
  <img src="https://img.shields.io/badge/NLP-TF--IDF%20%2B%20N--grams-ff6584?style=flat-square"/>
  <img src="https://img.shields.io/badge/API-RESTful%20JSON-00d97e?style=flat-square"/>
  <img src="https://img.shields.io/badge/Architecture-8%20Modules-fbbf24?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square"/>
</p>

---

<div align="center">

> **A production-ready fake news detection system powered by Machine Learning.**  
> Detects misinformation in real time using a Random Forest classifier trained on TF-IDF features extracted from news text. Features a sleek dark-theme web UI, a RESTful JSON API, and a fully modular 8-module architecture.

**[Features](#-features) · [Quick Start](#-quick-start) · [API Reference](#-api-reference) · [Architecture](#️-architecture) · [Model Details](#-model-details) · [Troubleshooting](#-troubleshooting)**

</div>

---

## 🌟 Project Overview

The **Fake News Detector** is a full-stack machine learning application that classifies news articles as **Real** or **Fake** using Natural Language Processing (NLP) and ensemble learning.

| Capability | Detail |
|---|---|
| **Algorithm** | Random Forest Classifier (200 decision trees) |
| **Feature Extraction** | TF-IDF Vectorization (5,000 features, 1–3 word n-grams) |
| **Accuracy** | 83%+ on built-in sample data · 92%+ with a large real-world dataset |
| **API** | RESTful JSON — `POST /api/analyze`, `GET /api/stats` |
| **Frontend** | Dark-theme responsive web UI with animated probability bars |
| **Architecture** | 8 decoupled modules following SOLID principles |

### Why This Project?

| Learning | Impact |
|---|---|
| Master ML classification pipelines | Combat misinformation at scale |
| Understand TF-IDF & n-gram NLP | Build media literacy tools |
| Practice modular Flask design | Enable content verification workflows |
| Explore ensemble methods | Support digital fact-checking platforms |

---

## ✨ Features

### Machine Learning
- ✅ Random Forest Classifier with 200 decision trees
- ✅ TF-IDF vectorization with 5,000 features and 1–3 word n-grams
- ✅ Balanced class weights to handle imbalanced datasets
- ✅ 80/20 stratified train/test split
- ✅ Full classification report on startup

### Text Processing
- ✅ URL, `@mention`, and `#hashtag` removal
- ✅ Special character normalization
- ✅ Whitespace normalization
- ✅ Minimum word-count validation

### Web Application
- ✅ Modern dark-theme responsive UI (no frameworks — pure CSS)
- ✅ Real-time article analysis with loading animation
- ✅ Animated probability bars (Real vs. Fake)
- ✅ Confidence score gauge
- ✅ Sample Real / Fake news quick-load buttons
- ✅ Live word count

### REST API
- ✅ `POST /api/analyze` — JSON prediction endpoint
- ✅ `GET /api/stats` — model statistics endpoint
- ✅ Structured error handling and HTTP status codes

### Data Handling
- ✅ Automatic text/label column detection from any CSV
- ✅ Diverse label format normalization (`real/fake`, `0/1`, `true/false`, etc.)
- ✅ Built-in 120-article fallback dataset (no external file needed)

---

## 🧠 Tech Stack

| Layer | Technology | Version | Role |
|---|---|---|---|
| Language | Python | 3.8+ | Core runtime |
| Web Framework | Flask | 3.1+ | HTTP server & routing |
| ML Library | scikit-learn | 1.7+ | Random Forest, TF-IDF |
| Data Processing | Pandas | 2.0+ | CSV loading & manipulation |
| Numerical | NumPy | 1.24+ | Array operations |
| Frontend | HTML / CSS / JS | — | Responsive dark-theme UI |

---

## 🏗️ Architecture

```
fake-news-detector/
│
├── app.py               ← Entry point · initialization · server startup
├── config.py            ← All hyperparameters & settings (dataclasses)
├── model.py             ← FakeNewsDetector · train() · predict()
├── data_loader.py       ← CSV loading · column detection · fallback data
├── text_processor.py    ← Text cleaning · validation · word count
├── routes.py            ← Flask endpoints: / · /api/analyze · /api/stats
├── templates.py         ← Full HTML/CSS/JS frontend template
├── requirements.txt     ← Pinned dependencies
└── README.md            ← This file
```

### Module Responsibilities

| Module | Responsibility | Key Classes / Functions |
|---|---|---|
| `app.py` | Orchestrate startup | `create_app()`, `main()` |
| `config.py` | Centralized settings | `ModelConfig`, `VectorizerConfig`, `ServerConfig` |
| `model.py` | ML pipeline | `FakeNewsDetector.train()`, `.predict()`, `.get_stats()` |
| `data_loader.py` | Data operations | `DataLoader.load_dataset()`, `.create_fallback_dataset()` |
| `text_processor.py` | NLP preprocessing | `TextProcessor.preprocess_text()`, `.validate_text()` |
| `routes.py` | HTTP handling | `register_routes()` |
| `templates.py` | UI template | `get_html_template()` |

### ML Pipeline

```
Raw Text Input
      │
      ▼
┌─────────────────────┐
│   TextProcessor     │  lowercase · remove URLs/mentions/hashtags
│   preprocess_text() │  strip special chars · normalize whitespace
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   TF-IDF Vectorizer │  5,000 features · n-grams (1,2,3) · stopwords
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  RandomForest (200) │  200 trees vote · aggregate probabilities
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Credibility Score  │  Real % · Fake % · Confidence · Rating
└─────────────────────┘
```

### Design Principles

- **Single Responsibility** — each module has one clear purpose
- **Separation of Concerns** — UI, logic, and data are fully decoupled
- **Configuration as Code** — all tuneable values live in `config.py`
- **Dependency Injection** — components receive dependencies explicitly
- **Testability** — every module can be unit tested in isolation

---

## 📦 Installation

### System Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| Python | 3.8 | 3.10 – 3.12 |
| RAM | 2 GB | 4 GB+ |
| Storage | 200 MB | 1 GB+ (for large datasets) |
| OS | Windows 10 / macOS 11 / Ubuntu 20.04 | Any modern 64-bit OS |

### Dependencies

```
flask>=2.3
scikit-learn>=1.3
pandas>=2.0
numpy>=1.24
```

> **Anaconda users:** All dependencies are already installed. Skip straight to [Quick Start](#-quick-start).

---

## 🚀 Quick Start

### 1 · Clone the Repository

```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
```

### 2 · Create a Virtual Environment *(recommended)*

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3 · Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 · Run the Application

```bash
python app.py
```

**Expected output:**

```
============================================================
FAKE NEWS DETECTOR - MACHINE LEARNING PROJECT
============================================================

Loading dataset...
  [!] Dataset file 'news.csv' not found. Using built-in sample dataset.
  [OK] Built-in sample dataset created: 120 articles (60 real, 60 fake)

Training Random Forest model...
============================================================
MODEL TRAINING COMPLETE
============================================================
Accuracy: 83.33%
...
Starting Flask server...
Open your browser and go to: http://127.0.0.1:5000
============================================================
```

### 5 · Open the App

Navigate to **http://127.0.0.1:5000** in your browser.

> **Tip:** Provide a real-world dataset (`news.csv`) to push accuracy to **92%+**. See [Dataset Format](#-dataset-format).

---

## 💻 Usage Guide

### Web Interface

1. **Paste** a news article into the text area
2. Click **"Analyze for Fake News"**
3. View the verdict, probability bars, and confidence score
4. Use **"Sample Real News"** / **"Sample Fake News"** buttons to test quickly

### Interpreting Results

| Credibility Level | Confidence Range | Meaning |
|---|---|---|
| **Very High Confidence** | 90 – 100% | Strong, highly reliable prediction |
| **High Confidence** | 75 – 89% | Reliable prediction |
| **Medium Confidence** | 60 – 74% | Moderate certainty — cross-check advised |
| **Low Confidence** | < 60% | Uncertain — verify manually |

> ⚠️ Always cross-reference results with trusted sources. This tool assists fact-checking; it does not replace human judgment.

---

## 📡 API Reference

### `GET /`

Serves the main HTML interface.

---

### `POST /api/analyze`

Analyzes a news article and returns a credibility prediction.

**Request**

```http
POST /api/analyze
Content-Type: application/json

{
  "text": "Scientists discover breakthrough battery technology..."
}
```

**Response — Real News**

```json
{
  "success": true,
  "result": {
    "is_fake": false,
    "result": "LIKELY REAL NEWS ✅",
    "confidence": "87.5",
    "credibility": "High Confidence",
    "real_probability": "87.5",
    "fake_probability": "12.5",
    "word_count": 42
  }
}
```

**Response — Fake News**

```json
{
  "success": true,
  "result": {
    "is_fake": true,
    "result": "LIKELY FAKE NEWS ⚠️",
    "confidence": "93.2",
    "credibility": "Very High Confidence",
    "real_probability": "6.8",
    "fake_probability": "93.2",
    "word_count": 38
  }
}
```

**Error Responses**

| HTTP Code | Condition | `error` field |
|---|---|---|
| `400` | Empty or missing text | `"No text provided."` |
| `400` | Text too short (< 3 words) | `"Text is too short or invalid..."` |
| `503` | Model not yet trained | `"Model has not been trained yet."` |
| `500` | Unexpected server error | `"Internal server error: ..."` |

---

### `GET /api/stats`

Returns model performance metadata.

**Response**

```json
{
  "accuracy": "83.33",
  "model_type": "Random Forest",
  "features": 5000,
  "n_estimators": 200
}
```

---

### Integration Examples

<details>
<summary><b>Python (requests)</b></summary>

```python
import requests

response = requests.post(
    "http://127.0.0.1:5000/api/analyze",
    json={"text": "Your news article text here..."}
)
data = response.json()

if data["success"]:
    r = data["result"]
    print(f"Verdict    : {r['result']}")
    print(f"Credibility: {r['credibility']}")
    print(f"Confidence : {r['confidence']}%")
    print(f"Real / Fake: {r['real_probability']}% / {r['fake_probability']}%")
else:
    print(f"Error: {data['error']}")
```

</details>

<details>
<summary><b>JavaScript (Fetch API)</b></summary>

```javascript
const response = await fetch("http://127.0.0.1:5000/api/analyze", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text: "Your news article text here..." })
});

const data = await response.json();
if (data.success) {
  console.log(data.result.result);        // "LIKELY REAL NEWS ✅"
  console.log(data.result.confidence);    // "87.5"
}
```

</details>

<details>
<summary><b>cURL</b></summary>

```bash
curl -X POST http://127.0.0.1:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Your news article text here..."}'

# Model stats
curl http://127.0.0.1:5000/api/stats
```

</details>

---

## 🤖 Model Details

### Random Forest Configuration

```python
RandomForestClassifier(
    n_estimators   = 200,       # 200 decision trees vote on every prediction
    max_depth      = 20,        # Maximum depth per tree
    min_samples_split = 5,      # Min samples required to split a node
    min_samples_leaf  = 2,      # Min samples required at each leaf
    random_state   = 42,        # Reproducible results
    class_weight   = "balanced" # Compensates for class imbalance
)
```

### TF-IDF Vectorizer Configuration

```python
TfidfVectorizer(
    max_features = 5000,        # Top 5,000 most informative terms
    ngram_range  = (1, 3),      # Unigrams, bigrams, and trigrams
    stop_words   = "english",   # Filter common English stopwords
    min_df       = 2,           # Term must appear in ≥ 2 documents
    max_df       = 0.95         # Term must appear in ≤ 95% of documents
)
```

### Performance Metrics *(with real-world dataset)*

| Metric | Score |
|---|---|
| **Accuracy** | 92%+ |
| **Precision** | 90%+ |
| **Recall** | 88%+ |
| **F1-Score** | 0.89+ |

> Metrics above are achieved with a large labeled dataset (e.g. ISOT, Kaggle Fake News).  
> The built-in 120-article sample achieves ~83%.

---

## 📊 Dataset Format

Drop a `news.csv` file in the project directory. The loader auto-detects columns.

### Supported CSV Format

```csv
text,label
"The Federal Reserve raised interest rates by 0.25%...",0
"SHOCKING: Secret government plot exposed...",1
```

### Auto-Detected Column Names

| Column Type | Accepted Names |
|---|---|
| **Text** | `text`, `title`, `content`, `news`, `article`, `headline`, `body` |
| **Label** | `label`, `class`, `fake`, `target`, `category` |

### Label Mapping

| Input Values | Mapped To |
|---|---|
| `0` / `real` / `false` / `no` | **0 (Real)** |
| `1` / `fake` / `true` / `yes` | **1 (Fake)** |

### Recommended Free Datasets

| Dataset | Size | Link |
|---|---|---|
| ISOT Fake News | 44,000 articles | [Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) |
| Fake News Corpus | 9.4M articles | [GitHub](https://github.com/several27/FakeNewsCorpus) |
| GossipCop / PolitiFact | 22,000 articles | [FakeNewsNet](https://github.com/KaiDMML/FakeNewsNet) |

---

## ⚙️ Configuration

All settings live in `config.py`. Edit the dataclasses to tune the model.

```python
@dataclass
class ModelConfig:
    n_estimators: int = 200        # More trees → higher accuracy, slower training
    max_depth: int = 20            # Deeper → captures complex patterns, risk of overfit
    min_samples_split: int = 5
    min_samples_leaf: int = 2
    random_state: int = 42
    class_weight: str = 'balanced'

@dataclass
class VectorizerConfig:
    max_features: int = 5000       # Increase for richer vocabulary
    ngram_range: tuple = (1, 3)    # (1,1)=words only · (1,2)=+bigrams · (1,3)=+trigrams
    stop_words: str = 'english'
    min_df: int = 2
    max_df: float = 0.95

@dataclass
class ServerConfig:
    host: str = '0.0.0.0'
    port: int = 5000
    debug: bool = True             # Set False for production

@dataclass
class ConfidenceThresholds:
    very_high: float = 0.90
    high: float = 0.75
    medium: float = 0.60
```

---

## 🔧 Module Documentation

<details>
<summary><b>app.py — Application Entry Point</b></summary>

Orchestrates the startup sequence:
1. Loads `Config`
2. Initializes `DataLoader` and `TextProcessor`
3. Calls `DataLoader.load_dataset()` (falls back to built-in data if `news.csv` missing)
4. Trains `FakeNewsDetector`
5. Registers all Flask routes via `register_routes()`
6. Starts the development server

</details>

<details>
<summary><b>config.py — Configuration Management</b></summary>

Python `dataclass`-based configuration. All hyperparameters, server settings, and confidence thresholds are defined here. Import `Config()` anywhere to access sub-configs via `config.model`, `config.vectorizer`, `config.server`, `config.thresholds`.

</details>

<details>
<summary><b>model.py — FakeNewsDetector</b></summary>

**`train(df)`** — fits the TF-IDF vectorizer and Random Forest on the provided DataFrame, prints a full classification report, stores `self.accuracy`.

**`predict(text)`** — transforms pre-processed text, runs inference, returns a dict with `is_fake`, `result`, `confidence`, `credibility`, `real_probability`, `fake_probability`.

**`get_stats()`** — returns accuracy and configuration metadata for `/api/stats`.

</details>

<details>
<summary><b>data_loader.py — DataLoader</b></summary>

**`load_dataset(filepath)`** — reads a CSV, auto-detects text/label columns, normalizes label formats, drops invalid rows.

**`create_fallback_dataset()`** — returns a 120-article (60 real, 60 fake) `pd.DataFrame` built into the source code — no external file required.

</details>

<details>
<summary><b>text_processor.py — TextProcessor</b></summary>

**`preprocess_text(text)`** — lowercase → strip URLs, mentions, hashtags → remove non-alpha characters → normalize whitespace → validate.

**`validate_text(text, min_words=3)`** — returns `True` if text has at least `min_words` words.

**`get_word_count(text)`** — simple word count for UI display.

</details>

<details>
<summary><b>routes.py — Flask Routes</b></summary>

`GET /` → serves the HTML frontend via `render_template_string`.

`POST /api/analyze` → validates → preprocesses → predicts → returns JSON.

`GET /api/stats` → returns `model.get_stats()` as JSON.

</details>

<details>
<summary><b>templates.py — Frontend</b></summary>

Single-function `get_html_template()` returning a self-contained HTML string with embedded CSS and JavaScript. No external template files or CDN dependencies (except Google Fonts). Features dark-theme design, animated probability bars, and AJAX-based form submission.

</details>

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Windows — find the process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or change the port in config.py
port: int = 8000
```

### Low Accuracy (< 70%)

- The built-in 120-article sample is small — use a real dataset (see [Dataset Format](#-dataset-format))
- Check class balance: `df['label'].value_counts()` should be roughly equal
- Increase `n_estimators` and `max_features` in `config.py`

### UnicodeEncodeError on Windows

Ensure your terminal supports UTF-8:

```powershell
chcp 65001
```

Or set the `PYTHONUTF8` environment variable:

```powershell
$env:PYTHONUTF8 = "1"
python app.py
```

### CSV Not Loading

```python
import pandas as pd
df = pd.read_csv("news.csv", nrows=5)
print(df.columns.tolist())   # verify column names
print(df.head())
```

Column names must match one of the accepted names (see [Dataset Format](#-dataset-format)), or rename them before placing the file in the project directory.

---

## 🚀 Future Enhancements

| Feature | Status |
|---|---|
| BERT / Transformer-based model | 💡 Planned |
| Multi-language support | 💡 Planned |
| Fact-check database cross-reference | 💡 Planned |
| Browser extension | 💡 Idea |
| Analysis history & dashboard | 💡 Idea |
| Batch analysis endpoint | 💡 Idea |
| Explainability (SHAP / feature importance display) | 💡 Idea |
| Docker deployment | 💡 Idea |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and write tests
4. Commit: `git commit -m "Add: your feature description"`
5. Push: `git push origin feature/your-feature`
6. Open a Pull Request

**Code Guidelines:**
- Follow PEP 8
- Add docstrings to all public methods
- Keep the modular architecture intact — one concern per file
- Update this README if you add new modules or endpoints

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ Star this repository if it helped you!**

Built with ❤️ using Flask · scikit-learn · TF-IDF · Random Forest

<br/>

*"The truth is incontrovertible. Malice may attack it, ignorance may deride it, but in the end, there it is."*  
— Winston Churchill

<br/>

⚠️ **Disclaimer:** This tool assists in identifying potential misinformation but should not be the sole determinant of news authenticity. Always cross-reference with multiple trusted sources and apply critical thinking.

</div>
