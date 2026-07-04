"""Minimal Phy-MFN model scaffold.

Replace this scaffold with the final reviewed implementation before public
archival release.
"""

from __future__ import annotations

import torch
from torch import nn


class SignalEncoder(nn.Module):
    """1D CNN-GRU temporal encoder for strain/temperature sequences."""

    def __init__(self, input_channels: int = 2, hidden_dim: int = 128):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv1d(input_channels, 64, kernel_size=7, stride=2, padding=3),
            nn.ReLU(),
        )
        self.gru = nn.GRU(input_size=64, hidden_size=hidden_dim, num_layers=2, batch_first=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.conv(x).transpose(1, 2)
        encoded, _ = self.gru(x)
        return encoded


class CrossModalFusion(nn.Module):
    """Cross-modal attention fusion layer."""

    def __init__(self, dim: int = 128, heads: int = 4):
        super().__init__()
        self.attn = nn.MultiheadAttention(embed_dim=dim, num_heads=heads, batch_first=True)

    def forward(self, signal_features: torch.Tensor, vision_features: torch.Tensor) -> torch.Tensor:
        fused, _ = self.attn(query=signal_features, key=vision_features, value=vision_features)
        return fused


class PhyMFN(nn.Module):
    """Compact reference scaffold for Phy-MFN."""

    def __init__(self, signal_channels: int = 2, hidden_dim: int = 128):
        super().__init__()
        self.signal_encoder = SignalEncoder(signal_channels, hidden_dim)
        self.vision_projection = nn.Linear(hidden_dim, hidden_dim)
        self.fusion = CrossModalFusion(hidden_dim)
        self.regressor = nn.Sequential(nn.Linear(hidden_dim, hidden_dim), nn.ReLU(), nn.Linear(hidden_dim, 1))

    def forward(self, signal_sequence: torch.Tensor, vision_features: torch.Tensor) -> torch.Tensor:
        signal_features = self.signal_encoder(signal_sequence)
        vision_features = self.vision_projection(vision_features)
        fused = self.fusion(signal_features, vision_features)
        return self.regressor(fused).squeeze(-1)

