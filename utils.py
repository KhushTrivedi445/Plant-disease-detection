"""
utils.py — Preprocessing transforms, inference & formatting helpers.

All image pre-processing mirrors the original training pipeline:
  Resize(128, 128) → ToTensor() → Normalize(mean=[0.485, 0.456, 0.406],
                                              std =[0.229, 0.224, 0.225])
"""

from __future__ import annotations

from typing import Any

import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import numpy as np

from model import INPUT_SIZE, PlantDiseaseCNN

# ---------------------------------------------------------------------------
# Transform (mirrors training validation pipeline)
# ---------------------------------------------------------------------------

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD  = [0.229, 0.224, 0.225]

inference_transform = transforms.Compose([
    transforms.Resize((INPUT_SIZE, INPUT_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
])


# ---------------------------------------------------------------------------
# Inference
# ---------------------------------------------------------------------------

@torch.inference_mode()
def predict(
    image: Image.Image,
    model: PlantDiseaseCNN,
    class_names: list[str],
    device: torch.device,
    top_k: int = 5,
) -> list[dict[str, Any]]:
    """Run inference on a single PIL image.

    Returns
    -------
    list of dicts sorted by descending probability, each containing:
        {"class_name": str, "display_name": str, "plant": str,
         "condition": str, "probability": float, "index": int}
    """
    tensor = inference_transform(image.convert("RGB"))
    batch = tensor.unsqueeze(0).to(device)

    logits = model(batch)
    probs = F.softmax(logits, dim=1).squeeze(0).cpu().numpy()

    top_indices = probs.argsort()[::-1][:top_k]

    results: list[dict[str, Any]] = []
    for idx in top_indices:
        idx = int(idx)
        raw_name = class_names[idx]
        plant, condition = parse_class_name(raw_name)
        results.append({
            "class_name": raw_name,
            "display_name": format_class_name(raw_name),
            "plant": plant,
            "condition": condition,
            "probability": float(probs[idx]),
            "index": idx,
        })
    return results


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def parse_class_name(raw: str) -> tuple[str, str]:
    """Split 'Apple___Black_rot' → ('Apple', 'Black Rot')."""
    parts = raw.split("___")
    plant = parts[0].replace("_", " ").strip()
    condition = parts[1].replace("_", " ").strip() if len(parts) > 1 else "Unknown"
    return plant, condition.title()


def format_class_name(raw: str) -> str:
    """'Apple___Black_rot' → 'Apple — Black Rot'."""
    plant, condition = parse_class_name(raw)
    return f"{plant} — {condition}"


def is_healthy(class_name: str) -> bool:
    """Check if a class name indicates a healthy plant."""
    return "healthy" in class_name.lower()


def confidence_color(prob: float) -> str:
    """Return a CSS-friendly color string based on confidence."""
    if prob >= 0.90:
        return "#2ecc71"   # green
    if prob >= 0.70:
        return "#f39c12"   # orange
    return "#e74c3c"       # red


def confidence_label(prob: float) -> str:
    """Human-readable confidence band."""
    if prob >= 0.90:
        return "High Confidence"
    if prob >= 0.70:
        return "Moderate Confidence"
    if prob >= 0.50:
        return "Low Confidence"
    return "Very Low Confidence"

