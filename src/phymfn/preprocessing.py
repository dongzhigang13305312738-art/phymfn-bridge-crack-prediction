"""Preprocessing utilities for de-identified bridge monitoring sequences."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pywt


@dataclass(frozen=True)
class WaveletConfig:
    """Configuration for adaptive wavelet thermal-drift separation."""

    wavelet: str = "sym8"
    level: int = 7


def separate_thermal_baseline(signal: np.ndarray, config: WaveletConfig = WaveletConfig()) -> tuple[np.ndarray, np.ndarray]:
    """Separate low-frequency thermal baseline from structural residue.

    Parameters
    ----------
    signal:
        One-dimensional strain sequence.
    config:
        Wavelet configuration. Re-identify this for new bridge types or climates.

    Returns
    -------
    baseline, residue:
        Reconstructed low-frequency baseline and residual structural component.
    """

    values = np.asarray(signal, dtype=float)
    coeffs = pywt.wavedec(values, config.wavelet, level=config.level, mode="symmetric")
    baseline_coeffs = [coeffs[0]] + [np.zeros_like(c) for c in coeffs[1:]]
    baseline = pywt.waverec(baseline_coeffs, config.wavelet, mode="symmetric")[: values.size]
    residue = values - baseline
    return baseline, residue

