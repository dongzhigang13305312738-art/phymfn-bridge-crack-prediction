# Step-by-step GitHub and OSF Release Guide

## Option A: GitHub First, Then DOI

1. Create a GitHub account or log in.
2. Create a new repository named `phymfn-bridge-crack-prediction`.
3. Set visibility to `Public` only after data and code review are complete.
4. Upload all repository files except `data/raw_private/`.
5. Add the approved de-identified CSV to `data/deidentified/`.
6. Commit changes with a message such as `Initial proof-stage open release`.
7. Create a GitHub release, e.g. `v1.0.0`.
8. Use Zenodo or OSF to archive the release and obtain a DOI.
9. Update `README.md`, `CITATION.cff`, and the manuscript proof with the DOI.

## Option B: OSF Project

1. Log in to OSF.
2. Create a new project named `Phy-MFN bridge crack prediction`.
3. Add project description and manuscript citation.
4. Upload the repository ZIP and the approved de-identified dataset.
5. Add license and data-use notes.
6. Register or archive the project when ready for citation.
7. Copy the OSF URL or DOI into the manuscript proof.

## Suggested Manuscript Availability Text

The publicly shareable Phy-MFN algorithm framework code and de-identified 45-day monitoring sequence will be deposited in an open scholarly repository at the proof stage. The public dataset removes bridge-identifying information, sensitive location details, and operationally restricted fields while preserving the variables required to reproduce the main analyses.

