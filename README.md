# 🌿 PlantixAI: Production-Grade Plant Disease Diagnostic System

An end-to-end computer vision and deep learning diagnostic platform engineered in PyTorch to classify 38 distinct plant disease categories and healthy leaf conditions across 14 agricultural crop species. Powered by a custom 4-block Convolutional Neural Network (CNN), the system achieves **97.48% top-1 validation accuracy** and is deployed through an interactive, cached Streamlit web dashboard providing real-time foliar diagnostics, confidence analytics, and agronomic treatment protocols.

---

## 📑 Table of Contents
- [System Overview](#-system-overview)
- [Dataset Architecture & Pipeline](#-dataset-architecture--pipeline)
- [Neural Network Architecture](#-neural-network-architecture)
- [Training Dynamics & Convergence](#-training-dynamics--convergence)
- [Quantitative Evaluation & Error Analysis](#-quantitative-evaluation--error-analysis)
- [Streamlit Web Application](#-streamlit-web-application)
- [Repository Structure](#-repository-structure)
- [Installation & Environment Setup](#-installation--environment-setup)
- [Usage & Quick Start](#-usage--quick-start)
- [Tech Stack & Engineering Practices](#-tech-stack--engineering-practices)

---

## 🔬 System Overview
Crop leaf infections present severe threats to global food security. Early automated diagnostic identification mitigates pathogen spread before irreversible yield loss occurs. This repository implements:

1. **Robust Computer Vision Pipeline:** Multi-stage image preprocessing with deterministic inference transforms and memory-safe streaming using PyTorch `DataLoader` constructs.
2. **Custom CNN Architecture (`PlantDiseaseCNN`):** High-capacity 4-block deep feature extractor with BatchNorm regularization and a dual-dropout classification head.
3. **Comprehensive Diagnostic Evaluation:** Multi-class precision, recall, F1-scores, and normalized confusion matrix analysis identifying biological symptom overlaps.
4. **Interactive Agricultural Dashboard:** Streamlit UI utilizing `@st.cache_resource` for zero-redundancy model residency in VRAM, featuring automated disease treatment protocols and interactive Plotly confidence charts.
5. **Curated Agronomic Knowledge Base:** 38-class disease information dictionary covering symptoms, pathogen causes, chemical/organic treatments, and long-term prevention strategies.

---

## 📊 Dataset Architecture & Pipeline

The system is trained and evaluated on the **New Plant Diseases Dataset (Augmented)**, formatted in a strict hierarchical PyTorch `ImageFolder` structure:

* **Total Curated Samples:** 87,867 annotated RGB leaf images
  * **Training Split:** 70,295 images (80%)
  * **Validation Split:** 17,572 images (20%)
* **Taxonomic Breadth:** 38 classes spanning 14 agricultural plant species (Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Bell Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, and Tomato).
* **Input Spatial Dimensions:** $(3, 128, 128)$ representing $(\text{Channels}, \text{Height}, \text{Width})$.

### Inference Preprocessing Pipeline
The production inference transform in `utils.py` mirrors the validation pipeline used during training:

* **Bilinear Resize:** $128 \times 128$
* **Tensor Conversion:** uint8 $[0, 255] \to \text{float32 } [0.0, 1.0]$
* **Channel-wise Normalization:** $\mu = [0.485, 0.456, 0.406]$, $\sigma = [0.229, 0.224, 0.225]$ (ImageNet statistics)

---

## 🧠 Neural Network Architecture

The `PlantDiseaseCNN` class in `model.py` employs an idiomatic sequential design separating convolutional feature extraction from dense classification:

```
Input Image (3, 128, 128)
  │
  ├── [Block 1] Conv2D(3 -> 32, k=3, pad='same') → ReLU → BatchNorm2d(32) → MaxPool2d(2, 2)
  │             Output: (32, 64, 64)
  │
  ├── [Block 2] Conv2D(32 -> 64, k=3, pad='same') → ReLU → BatchNorm2d(64) → MaxPool2d(2, 2)
  │             Output: (64, 32, 32)
  │
  ├── [Block 3] Conv2D(64 -> 128, k=3, pad='same') → ReLU → BatchNorm2d(128) → MaxPool2d(2, 2)
  │             Output: (128, 16, 16)
  │
  ├── [Block 4] Conv2D(128 -> 128, k=3, pad='same') → ReLU → BatchNorm2d(128) → MaxPool2d(2, 2)
  │             Output: (128, 8, 8)
  │
  └── Dense Classifier Head
      ├── Flatten()                              → 128 × 8 × 8 = 8,192 features
      ├── Linear(8192 -> 256) → ReLU → Dropout(p=0.3)
      ├── Linear(256 -> 128)  → ReLU → Dropout(p=0.3)
      └── Linear(128 -> 38)   → Logits (Unnormalized class scores)
```

**Key Design Details:**
- **Feature Extractor:** 4 convolutional blocks with progressive channel expansion (3 → 32 → 64 → 128 → 128), each followed by ReLU activation, BatchNorm for stable gradient flow, and 2×2 max-pooling for spatial downsampling.
- **Classifier Head:** Three fully connected layers with dual Dropout($p = 0.3$) regularization to prevent co-adaptation of hidden units.
- **Inference Mode:** Model is set to `eval()` mode with `@torch.inference_mode()` decorator for optimized, gradient-free forward passes.

---

## 📈 Training Dynamics & Convergence

* **Optimizer:** Adam ($\text{lr} = 0.001$, $\text{weight\_decay} = 10^{-4}$)
* **Objective Function:** Multi-Class Cross-Entropy Loss (`nn.CrossEntropyLoss`)
* **Batch Configuration:** 32 samples per batch (2,197 training batches, 550 validation batches per epoch)
* **Epochs Trained:** 10 on NVIDIA RTX hardware acceleration

### Epoch-by-Epoch Convergence Table

| Epoch | Train Loss | Train Accuracy (%) | Validation Loss | Validation Accuracy (%) |
|:---:|:---:|:---:|:---:|:---:|
| **01** | 1.3515 | 60.89% | 0.4269 | 86.83% |
| **02** | 0.6033 | 82.09% | 0.3162 | 90.44% |
| **03** | 0.4170 | 87.88% | 0.2089 | 93.62% |
| **04** | 0.3227 | 90.75% | 0.1678 | 94.86% |
| **05** | 0.2687 | 92.24% | 0.1348 | 95.73% |
| **06** | 0.2269 | 93.48% | 0.0939 | 97.09% |
| **07** | 0.2092 | 93.96% | 0.1007 | 96.94% |
| **08** | 0.1871 | 94.73% | 0.1048 | 96.70% |
| **09** | 0.1777 | 95.00% | 0.1061 | 96.92% |
| **10** | **0.1633** | **95.43%** | **0.0866** | **97.48%** |

### Why Validation Performance Exceeds Training Performance
Validation accuracy ($97.48\%$) naturally exceeds training accuracy ($95.43\%$) due to three architectural design factors:
1. **Active Dropout Penalty:** Two `nn.Dropout(p=0.3)` layers deactivate 30% of hidden units during training passes, but all units are active during deterministic evaluation (`model.eval()`).
2. **Augmentation Noise:** Training samples are rotated and flipped dynamically, whereas validation samples are clean and centered.
3. **Loss Averaging:** Training loss is averaged across the epoch as weights adjust, while validation loss is evaluated at the epoch's culmination.

---

## 🎯 Quantitative Evaluation & Error Analysis

Across all **17,572 independent validation images**, the model maintained high classification metrics:

| Metric | Macro Average | Weighted Average |
|:---|:---:|:---:|
| **Precision** | **0.9741** | **0.9749** |
| **Recall** | **0.9732** | **0.9748** |
| **F1-Score** | **0.9735** | **0.9747** |
| **Overall Top-1 Accuracy** | — | **97.48%** |

### Top Biological Misclassifications (Off-Diagonal Residuals)
Error diagnostics on the row-normalized $38 \times 38$ confusion matrix reveal that rare errors correlate with biologically similar foliar lesions:

| True Class | Predicted Class | Misclassified Samples | Error Rate (%) | Biological Root Cause |
|:---|:---|:---:|:---:|:---|
| **Corn Gray Leaf Spot** | Corn Northern Leaf Blight | 33 | 8.05% | Similar elongated necrotic vein lesions |
| **Tomato Spider Mites** | Tomato Target Spot | 28 | 6.44% | Mite stippling mimics early concentric fungal spots |
| **Tomato Late Blight** | Tomato Early Blight | 18 | 3.89% | Co-occurring water-soaked brown foliar necrosis |
| **Bell Pepper (Healthy)**| Soybean (Healthy) | 13 | 2.62% | Clean dicot leaf surfaces without distinctive lesions |
| **Tomato Late Blight** | Potato Late Blight | 9 | 1.94% | Identical oomycete pathogen (*Phytophthora infestans*) |

---

## 💻 Streamlit Web Application

The deployment application (`app.py`) offers an intuitive, responsive interface tailored for farmers and agronomists:

* **Resource Caching:** Wrapped with `@st.cache_resource` to keep model weights loaded in VRAM/RAM across multi-user sessions without memory leakage.
* **Real-Time Preprocessing:** Exact mirror of validation transforms ensuring zero distribution shift between training and inference.
* **Top-5 Uncertainty Metrics:** Displays the primary diagnosis alongside an interactive Plotly horizontal bar chart breaking down probabilities across the top-5 candidate classes.
* **Colour-Coded Confidence Bands:**
  - 🟢 **High Confidence** (≥ 90%) — Green badge
  - 🟠 **Moderate Confidence** (70–89%) — Orange badge
  - 🔴 **Low / Very Low Confidence** (< 70%) — Red badge
* **Agronomic Knowledge Base (`disease_info.py`):** Automatically populates per-class information including:
  - Biological pathogen descriptions and causal agents
  - Visible symptom checklists
  - Chemical and organic treatment protocols
  - Long-term preventative agronomic practices
* **Healthy / Diseased Feedback:** Visual badge indicators and tabbed detail cards (🩺 Symptoms · 💊 Treatment · 🛡️ Prevention).
* **Sidebar Dashboard:** Model metadata (accuracy, architecture, input size, device), and a dynamically generated list of all 14 supported crop species.

---

## 📁 Repository Structure

```text
plant-disease-detection/
│
├── plant_disease_model.pth      # Serialized PyTorch state_dict & class label mapping
├── model.py                     # PlantDiseaseCNN architecture & cached model loader
├── utils.py                     # Image preprocessing, Softmax inference & formatting helpers
├── disease_info.py              # Curated knowledge base: symptoms, causes, treatments (38 classes)
├── app.py                       # Streamlit production web application dashboard
├── requirements.txt             # Pinned library dependencies
└── README.md                    # System documentation
```

### Module Responsibilities

| Module | Role |
|:---|:---|
| **`model.py`** | Defines `PlantDiseaseCNN` (4-block CNN), loads checkpoint weights via `load_model()` with `@lru_cache` singleton pattern, auto-detects CUDA/CPU device. |
| **`utils.py`** | Houses `inference_transform` pipeline, `predict()` function with `@torch.inference_mode()`, and formatting helpers (`parse_class_name`, `confidence_color`, `confidence_label`). |
| **`disease_info.py`** | Maps all 38 raw class labels to structured dicts containing plant species, disease name, symptoms list, causal agent, treatment steps, and prevention measures. |
| **`app.py`** | Full Streamlit UI — file upload, real-time inference, Plotly charts, tabbed info cards, sidebar with model metadata and supported crops list. |

---

## 🚀 Installation & Environment Setup

### 1. Clone the Repository
```bash
git clone https://github.com/KhushTrivedi445/Plant-disease-detection.git
cd Plant-disease-detection
```

### 2. Configure Virtual Environment (Python 3.10+)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **Note:** If you have an NVIDIA GPU, install PyTorch with CUDA support for accelerated inference:
> ```bash
> pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
> ```

---

## 🛠️ Usage & Quick Start

### Launch the Streamlit Web Application
Ensure `plant_disease_model.pth` is in the project root directory, then run:
```bash
streamlit run app.py
```
The application will open in your browser at `http://localhost:8501`. Upload a clear, well-lit photo of a single plant leaf to receive an instant diagnosis.

### Programmatic Python Inference
```python
from PIL import Image
from model import load_model
from utils import predict

# 1. Load model, class mappings, and runtime device
model, class_names, device = load_model()

# 2. Open a leaf image
img = Image.open("sample_leaf.jpg")

# 3. Execute inference — returns top-5 predictions
results = predict(image=img, model=model, class_names=class_names, device=device, top_k=5)

# 4. Display top prediction
top = results[0]
print(f"Prediction:  {top['display_name']}")
print(f"Plant:       {top['plant']}")
print(f"Condition:   {top['condition']}")
print(f"Confidence:  {top['probability']*100:.2f}%")
```

### Retrieve Disease Information Programmatically
```python
from disease_info import get_disease_info

info = get_disease_info("Tomato___Late_blight")
print(f"Disease:    {info['disease']}")
print(f"Cause:      {info['causes']}")
print(f"Symptoms:   {info['symptoms']}")
print(f"Treatment:  {info['treatment']}")
print(f"Prevention: {info['prevention']}")
```

---

## ⚙️ Tech Stack & Engineering Practices

| Layer | Technology |
|:---|:---|
| **Deep Learning Framework** | PyTorch & Torchvision |
| **Data Processing** | NumPy, Pillow (PIL) |
| **Interactive Visualisation** | Plotly |
| **Production UI** | Streamlit |
| **Model Caching** | `@functools.lru_cache` (model loader) + `@st.cache_resource` (Streamlit) |
| **Inference Optimisation** | `@torch.inference_mode()` for gradient-free forward passes |
| **Device Management** | Automatic CUDA / CPU detection and tensor placement |

---

## 🌱 Supported Crop Species & Disease Classes

<details>
<summary><strong>Click to expand full 38-class taxonomy</strong></summary>

| # | Plant | Condition |
|:---:|:---|:---|
| 1 | Apple | Apple Scab |
| 2 | Apple | Black Rot |
| 3 | Apple | Cedar Apple Rust |
| 4 | Apple | Healthy |
| 5 | Blueberry | Healthy |
| 6 | Cherry | Powdery Mildew |
| 7 | Cherry | Healthy |
| 8 | Corn (Maize) | Cercospora Leaf Spot / Gray Leaf Spot |
| 9 | Corn (Maize) | Common Rust |
| 10 | Corn (Maize) | Northern Leaf Blight |
| 11 | Corn (Maize) | Healthy |
| 12 | Grape | Black Rot |
| 13 | Grape | Esca (Black Measles) |
| 14 | Grape | Leaf Blight (Isariopsis Leaf Spot) |
| 15 | Grape | Healthy |
| 16 | Orange | Huanglongbing (Citrus Greening) |
| 17 | Peach | Bacterial Spot |
| 18 | Peach | Healthy |
| 19 | Bell Pepper | Bacterial Spot |
| 20 | Bell Pepper | Healthy |
| 21 | Potato | Early Blight |
| 22 | Potato | Late Blight |
| 23 | Potato | Healthy |
| 24 | Raspberry | Healthy |
| 25 | Soybean | Healthy |
| 26 | Squash | Powdery Mildew |
| 27 | Strawberry | Leaf Scorch |
| 28 | Strawberry | Healthy |
| 29 | Tomato | Bacterial Spot |
| 30 | Tomato | Early Blight |
| 31 | Tomato | Late Blight |
| 32 | Tomato | Leaf Mold |
| 33 | Tomato | Septoria Leaf Spot |
| 34 | Tomato | Spider Mites (Two-Spotted) |
| 35 | Tomato | Target Spot |
| 36 | Tomato | Yellow Leaf Curl Virus |
| 37 | Tomato | Mosaic Virus |
| 38 | Tomato | Healthy |

</details>

---

<p align="center">
  <strong>© 2026 Plant Disease Diagnostic System</strong><br>
  Built with Streamlit + PyTorch | Created by <a href="https://github.com/KhushTrivedi445">Khush Trivedi</a>
</p>


Author:Khush Trivedi
