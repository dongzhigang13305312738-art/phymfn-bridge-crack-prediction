"""Physics-informed loss terms used by Phy-MFN."""

from __future__ import annotations

import torch


def paris_monotonicity_loss(predicted_width: torch.Tensor, epsilon: float = 1e-3) -> torch.Tensor:
    """One-sided Paris-law monotonicity penalty.

    Penalizes non-physical decreases in predicted crack width while allowing
    monotonic growth trajectories.
    """

    diffs = predicted_width[..., :-1] - predicted_width[..., 1:] + epsilon
    return torch.relu(diffs).mean()


def griffith_energy_admissibility_loss(energy_release_rate: torch.Tensor) -> torch.Tensor:
    """Sign-preserving Griffith energy admissibility penalty.

    This term is intended as an admissibility constraint that penalizes negative
    energy-release states, not as an exact absolute fracture-energy estimator.
    """

    return torch.relu(-energy_release_rate).mean()


def total_physics_informed_loss(
    reconstruction_loss: torch.Tensor,
    predicted_width: torch.Tensor,
    energy_release_rate: torch.Tensor,
    alpha_1: float = 0.6,
    alpha_2: float = 0.4,
    epsilon: float = 1e-3,
) -> torch.Tensor:
    """Hybrid Phy-MFN training objective."""

    return (
        reconstruction_loss
        + alpha_1 * paris_monotonicity_loss(predicted_width, epsilon=epsilon)
        + alpha_2 * griffith_energy_admissibility_loss(energy_release_rate)
    )

