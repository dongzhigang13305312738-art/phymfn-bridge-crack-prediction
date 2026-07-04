# Proof-stage Open Release Checklist

## Before Upload

- [ ] Replace placeholder training/evaluation scripts with final reviewed code.
- [ ] Confirm that no raw private files are tracked by Git.
- [ ] Run the de-identification script on the approved raw CSV.
- [ ] Manually review the de-identified CSV.
- [ ] Confirm that no exact GPS, bridge name, route ID, or restricted coordinates remain.
- [ ] Confirm code license, data license, and citation metadata.
- [ ] Update `CITATION.cff` with the final repository URL and DOI.
- [ ] Update the manuscript proof with the final repository DOI if available.

## Recommended Release Flow

1. Create a GitHub repository for code and lightweight de-identified CSV files.
2. Create a Zenodo DOI from the GitHub release, or upload the archival package to OSF.
3. Add the DOI to the repository README and manuscript proof.
4. Keep raw private data outside GitHub and OSF public folders.

