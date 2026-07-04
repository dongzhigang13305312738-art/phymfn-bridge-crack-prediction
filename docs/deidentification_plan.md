# De-identification Plan

Before uploading the 45-day monitoring sequence to GitHub, OSF, Zenodo, or another public archive, complete the following checks.

## 1. Remove Direct Identifiers

- Bridge name
- Route number
- Administrative district
- GPS coordinates
- Camera EXIF location metadata
- Bridge authority internal IDs
- Operator names and contact details

## 2. Reduce Re-identification Risk

- Convert absolute timestamps to relative `day_index`.
- Replace original sensor IDs with pseudonyms such as `S01`, `S02`, and `S03`.
- Remove exact sensor coordinates if they are restricted.
- Do not publish raw UAV images unless every frame is reviewed for sensitive visual details.
- Prefer derived crack-width sequences or cropped/blurred crack patches over full-scene images.

## 3. Preserve Scientific Reproducibility

Keep the variables needed to reproduce the manuscript:

- Relative time index
- Pseudonymized sensor channel
- Strain or decoupled strain residue
- Temperature
- UAV-derived crack width
- Train/validation/test split
- Model configuration used for the reported experiments

## 4. Approval Record

Before public release, record:

- Date of institutional approval
- Date of bridge-authority approval
- Person responsible for data review
- Repository URL and DOI

