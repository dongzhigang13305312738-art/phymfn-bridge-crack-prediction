# Data Dictionary for Public De-identified Monitoring Sequence

Recommended public CSV filename:

```text
data/deidentified/monitoring_45day_deidentified.csv
```

## Required Fields

| Column | Type | Description | Public Release Notes |
| --- | --- | --- | --- |
| day_index | float | Relative day from the beginning of the 45-day sequence | Use relative time, not exact timestamp |
| sensor_id | string | Pseudonymized sensor channel, e.g. S01, S02 | Do not publish original sensor labels |
| strain_raw_or_residue | float | Strain or AWT-decoupled strain residue | Prefer normalized or residue series |
| temperature | float | Ambient or local concrete temperature | Safe if no location metadata remains |
| crack_width_mm | float | UAV-derived crack-width measurement in mm | Aggregate or crop imagery if needed |
| split | string | train, validation, or test | Allows reproduction of reported metrics |

## Optional Fields

| Column | Type | Description |
| --- | --- | --- |
| baseline_temperature_component | float | Wavelet-estimated thermal baseline |
| uav_epoch_id | string | Pseudonymized UAV inspection epoch |
| quality_flag | string | Measurement quality indicator |

## Fields That Must Not Be Public

- Exact bridge name or administrative location
- GPS coordinates
- Route identifiers
- Restricted structural drawings
- Raw images with identifiable surroundings
- Original sensor installation coordinates if restricted
- Personnel, operator, or maintenance-team identifiers

