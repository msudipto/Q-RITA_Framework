# Contributing to Q-RITA Framework

Thank you for your interest in contributing to the Q-RITA Framework. We welcome community additions, enhancements, and bug fixes that advance reproducible research for RIS-assisted quantum networks.

## Development Rules & Environment

1. **Environment Consistency**: 
   Ensure your Python virtual environment matches the repository specifications:
   * Python ≥ 3.10
   * Qiskit ≥ 1.2
   * Qiskit-IBM-Runtime ≥ 0.20

2. **Testing Changes**:
   Before submitting your changes, run the pipeline execution sequence locally to confirm that code modifications do not break metric evaluation or figure rendering:
   ```bash
   python ibm_open_setup.py
   python collect_hardware_runs.py
   python build_metrics.py
   python plot_graphs.py
   ```

## Commit and Artifact Policies

* **Do Not Commit Raw Hardware Caches**: Avoid committing transient, local logs, repeated intermediate data matrices, or temporary cache buffers unless they are required to preserve historical baseline comparisons.
* **Git LFS**: Large research data objects, structural matrices, or publication assets should be intentionally tracked using **Git LFS** if archival versioning is necessary.
* **Code Formatting**: Ensure all Python files remain readable, include adequate commentary for custom mathematical proxies, and format shell blocks in standard backticks.

## How to Submit Changes

1. **Fork or Branch**: Create a new topic branch from the latest `main` branch.
2. **Commit clearly**: Write meaningful commit descriptions detailing the purpose of the adjustment (e.g., `Refactor rolling threshold in build_metrics`).
3. **Open a Pull Request**: Submit a Pull Request describing your changes, referencing any active tracking numbers from your configured issue template options.
