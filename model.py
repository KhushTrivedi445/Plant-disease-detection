"""
model.py — Exact PyTorch CNN architecture & cached model loader.

Architecture mirrors the training notebook:
  4 × (Conv2d → ReLU → BatchNorm2d → MaxPool2d)
  Flatten → FC(8192→256) → ReLU → Dropout → FC(256→128) → ReLU → Dropout → FC(128→38)

Input: 3×128×128 RGB image  |  Output: 38 class logits
"""

from __future__ import annotations

import os
import functools
from pathlib import Path

import torch
import torch.nn as nn

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
NUM_CLASSES: int = 38
INPUT_SIZE: int = 128          # H = W = 128
DEFAULT_WEIGHTS: str = "plant_disease_model.pth"

# ---------------------------------------------------------------------------
# Model Definition
# ---------------------------------------------------------------------------

class PlantDiseaseCNN(nn.Module):
    """Custom CNN for plant-leaf disease classification (38 classes)."""

    def __init__(self, num_classes: int = NUM_CLASSES) -> None:
        super().__init__()

        self.features = nn.Sequential(
            # Block 1 — 3 → 32
            nn.Conv2d(3, 32, kernel_size=3, padding=1),   # 0
            nn.ReLU(inplace=True),                         # 1
            nn.BatchNorm2d(32),                            # 2
            nn.MaxPool2d(2, 2),                            # 3  → 64×64

            # Block 2 — 32 → 64
            nn.Conv2d(32, 64, kernel_size=3, padding=1),   # 4
            nn.ReLU(inplace=True),                         # 5
            nn.BatchNorm2d(64),                            # 6
            nn.MaxPool2d(2, 2),                            # 7  → 32×32

            # Block 3 — 64 → 128
            nn.Conv2d(64, 128, kernel_size=3, padding=1),  # 8
            nn.ReLU(inplace=True),                         # 9
            nn.BatchNorm2d(128),                           # 10
            nn.MaxPool2d(2, 2),                            # 11 → 16×16

            # Block 4 — 128 → 128
            nn.Conv2d(128, 128, kernel_size=3, padding=1), # 12
            nn.ReLU(inplace=True),                         # 13
            nn.BatchNorm2d(128),                           # 14
            nn.MaxPool2d(2, 2),                            # 15 → 8×8
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),                                  # 0  → 128×8×8 = 8192
            nn.Linear(128 * 8 * 8, 256),                   # 1
            nn.ReLU(inplace=True),                         # 2
            nn.Dropout(0.3),                               # 3
            nn.Linear(256, 128),                           # 4
            nn.ReLU(inplace=True),                         # 5
            nn.Dropout(0.3),                               # 6
            nn.Linear(128, num_classes),                   # 7
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = self.classifier(x)
        return x


# ---------------------------------------------------------------------------
# Cached Loader
# ---------------------------------------------------------------------------

@functools.lru_cache(maxsize=1)
def load_model(
    checkpoint_path: str | Path | None = None,
    device: str | torch.device | None = None,
) -> tuple[PlantDiseaseCNN, list[str], torch.device]:
    """Load trained weights + metadata from checkpoint.

    Returns
    -------
    model : PlantDiseaseCNN  — eval-mode model on *device*
    class_names : list[str]  — ordered list of 38 class labels
    device : torch.device
    """
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        device = torch.device(device)

    if checkpoint_path is None:
        checkpoint_path = Path(__file__).resolve().parent / DEFAULT_WEIGHTS
    else:
        checkpoint_path = Path(checkpoint_path)

    if not checkpoint_path.exists():
        raise FileNotFoundError(
            f"Model checkpoint not found at {checkpoint_path}. "
            f"Place '{DEFAULT_WEIGHTS}' alongside this script."
        )

    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)

    model = PlantDiseaseCNN(num_classes=NUM_CLASSES)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(device)
    model.eval()

    class_names: list[str] = checkpoint.get("classes", [])
    if not class_names:
        # Fallback: reconstruct from class_to_idx
        c2i = checkpoint.get("class_to_idx", {})
        class_names = [k for k, _ in sorted(c2i.items(), key=lambda x: x[1])]

    return model, class_names, device

