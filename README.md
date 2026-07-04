# Phy-MFN: Physics-informed Multimodal Fusion Network for Bridge Crack Evolution Prediction

This repository is the planned open research package for the manuscript:

> Physics-informed Multimodal Fusion Network for Robust Early-stage Crack Evolution Prediction in Long-span Concrete Bridges under Climatic Thermal Drifts

The repository is intended to host:

- A reproducible reference implementation of the Phy-MFN algorithm framework.
- Data preprocessing utilities for strain, temperature, and UAV-derived crack-width sequences.
- A de-identified 45-day monitoring sequence, subject to bridge-authority confidentiality approval.
- Scripts for reproducing the main model-training and evaluation workflow.

## Repository Status

This package is prepared for proof-stage release. Public release should occur only after institutional and bridge-authority review confirms that the de-identified data contain no bridge-identifying information, sensitive location details, or operationally restricted fields.

## Planned Structure

```text
src/phymfn/              Core algorithm modules
scripts/                 Data de-identification and training entry points
data/raw_private/        Local-only raw data folder, never committed
data/deidentified/       Public de-identified data files
docs/                    Data dictionary, de-identification notes, release checklist
notebooks/               Optional demonstration notebooks
```

## Data Availability

The public dataset should include only de-identified variables required to reproduce the main analyses, such as:

- Relative timestamp or day index
- Sensor channel pseudonym
- Strain residue after approved preprocessing
- Temperature sequence
- UAV-derived crack-width measurement
- Train/validation/test split labels

The public dataset must not include:

- Exact bridge name, administrative location, coordinates, or route identifiers
- Raw image files containing recognizable surroundings, license plates, workers, or site markers
- Exact structural drawings or restricted sensor coordinates
- Security-sensitive operational metadata

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After a de-identified CSV is placed in `data/deidentified/`, the reproduction workflow can be documented as:

```bash
python scripts/train_phymfn.py --data data/deidentified/monitoring_45day_deidentified.csv
python scripts/evaluate_phymfn.py --data data/deidentified/monitoring_45day_deidentified.csv
```

The current scaffold provides the public-release structure. Replace placeholder training code with the final reviewed implementation before creating the archival release.

## Citation

If you use this code or dataset, please cite the associated journal article and the repository DOI once available.

## Licenses

- Code: MIT License, unless otherwise noted.
- De-identified data: recommended CC BY 4.0 after institutional approval.

