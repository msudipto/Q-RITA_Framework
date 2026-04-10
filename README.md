# Q-RITA Framework  
**Deadline-Aware Entanglement Routing for RIS-Assisted Terrestrial Quantum Links and IBM Hardware Evaluation**

---

## Abstract  

This repository presents the experimental and implementation workflow used to evaluate **Q-RITA (Quantum Reconfigurable Intelligent Transmission Architecture)**, a **deadline-aware entanglement-routing framework** for **RIS-assisted terrestrial quantum links**.  
The framework integrates **IBM Quantum hardware experimentation**, **RIS-aware link evaluation**, and **publication-oriented metric synthesis** to support reproducible analysis of entanglement-service behavior under time-sensitive operating constraints.  
The implementation is designed for research-grade reproducibility and supports backend selection, hardware job collection, metric construction, figure generation, and artifact preparation for manuscript development and experimental verification.

---

## Repository Structure  

```text
Q-RITA/
├── build_metrics.py                   # Computes derived evaluation metrics from raw hardware results
├── collect_hardware_runs.py           # Submits and monitors IBM Quantum Sampler hardware runs
├── ibm_open_setup.py                  # Configures IBM Quantum access and selects an available backend
├── plot_graphs.py                     # Generates publication-ready figures from processed metrics
│
├── data/                              # Local hardware outputs, processed metrics, and backend metadata
│   ├── backend.json                   # Selected backend metadata and timestamp
│   ├── distance_metrics.csv           # Averaged metrics versus distance-ratio stress settings
│   ├── distance_sweep.csv             # Raw sampler outcomes for distance-ratio experiments
│   ├── raw_jobs.jsonl                 # Full hardware job log with job IDs, timestamps, and results
│   ├── sd_pairs_metrics.csv           # Averaged metrics versus offered-load / SD-pair settings
│   ├── sd_pairs_sweep.csv             # Raw sampler outcomes for SD-pair variation
│   ├── timeseries.csv                 # Base success values over time
│   ├── timeseries_satisfaction.csv    # Derived rolling compliance values over time
│   └── timeseries_throughput.csv      # Derived yield values over time
│
├── figures/                           # Curated publication-facing visual outputs
│   ├── distance_ratio_impact.png
│   ├── distance_ratio_impact.svg
│   ├── distance_ratio_impact.pdf
│   ├── edr_over_time.png
│   ├── edr_over_time.svg
│   ├── edr_over_time.pdf
│   ├── lcr_over_time.png
│   ├── lcr_over_time.svg
│   ├── lcr_over_time.pdf
│   ├── sd_pairs_impact.png
│   ├── sd_pairs_impact.svg
│   └── sd_pairs_impact.pdf
│
└── README.md                          # Repository overview and reproducibility guide
```

---

## Environment Configuration  

### Requirements  
- Python ≥ 3.10  
- Qiskit ≥ 1.2  
- Qiskit-IBM-Runtime ≥ 0.20  
- Matplotlib ≥ 3.9  
- IBM Quantum account and API token  
- Git LFS for selected large research assets, when intentionally versioned  

### Installation  
```bash
python -m venv .venv
source .venv/bin/activate       # (Windows) .venv\Scripts\activate
pip install qiskit qiskit-ibm-runtime matplotlib
git lfs install
```

### Repository Setup  
Clone the repository and initialize the local environment:

```bash
git clone https://github.com/<your-username>/Q-RITA.git
cd Q-RITA
```

If the repository contains LFS-tracked files, retrieve them using:

```bash
git lfs pull
```

### IBM Quantum Setup  
Obtain your **IBM Quantum API token** from your IBM Quantum account and export it locally:

```bash
export IBM_QUANTUM_TOKEN="your_token_here"
```

---

## Experimental Methodology  

### Backend Configuration  
The hardware workflow begins by identifying and recording an available IBM Quantum backend:

```bash
python ibm_open_setup.py
```

This stage generates `data/backend.json`, which records the selected backend and the associated timestamp.

### Hardware Data Acquisition  
The hardware-collection stage submits controlled Sampler runs to the selected backend:

```bash
python collect_hardware_runs.py
```

This stage is designed to execute:

- time-series experiments across 2 scenarios, 3 algorithms, and 36 epochs
- distance-ratio sweeps across 7 logarithmic stress settings in `[0.01, 1.0]`
- offered-load sweeps across `{10, 15, 20, 25, 30}` source-destination (SD) pair settings

Outputs include raw quasi-probabilities, success values, elapsed runtime information, and job identifiers stored in `data/raw_jobs.jsonl`.

### Metric Synthesis  
The metric-building stage converts raw hardware outputs into manuscript-facing evaluation summaries:

```bash
python build_metrics.py
```

This stage computes:

- **Yield proxy** from measured Bell outcomes  
  \[
  \text{Yield Proxy} = (P_{00}+P_{11}) \times 1000
  \]
- **Rolling compliance proxy** from success values using a rolling window of size 5 and threshold condition  
  \[
  P_{\text{succ}} \ge 0.5
  \]

The resulting outputs include:

- `timeseries_throughput.csv`
- `timeseries_satisfaction.csv`
- `distance_metrics.csv`
- `sd_pairs_metrics.csv`

### Visualization  
The figure-generation stage produces publication-oriented visual outputs:

```bash
python plot_graphs.py
```

Each figure is exported in stable formats such as `.png`, `.svg`, and `.pdf` under the `figures/` directory.

### Execution Flow  
A typical end-to-end workflow is therefore:

```bash
python ibm_open_setup.py
python collect_hardware_runs.py
python build_metrics.py
python plot_graphs.py
```

---

## Result Summary  

| Component | Purpose | Research Role |
|----------|---------|---------------|
| **Backend Configuration** | Selects and records the execution backend | Supports traceable hardware provenance |
| **Hardware Run Collection** | Executes Sampler-based IBM Quantum experiments | Produces raw backend-grounded success data |
| **Metric Synthesis Pipeline** | Converts raw outcomes into yield and compliance summaries | Supports reproducible quantitative analysis |
| **Figure Generation Workflow** | Produces publication-ready plots and visual artifacts | Facilitates manuscript figures and reporting |

---

## Reproducibility Notes  

- Experiment behavior should remain consistent with the checked-in Python scripts and any repository-side configuration choices.
- Backend identity, runtime metadata, and timestamps should be retained for all manuscript-facing experiments.
- Large curated research assets should be tracked with **Git LFS** only when intentional archival versioning is required.
- Temporary caches, repeated intermediate files, and regenerable outputs should remain untracked unless explicitly needed for reproducibility.
- Metric definitions, rolling-window assumptions, threshold choices, and stress-setting conventions should be documented for every published experiment.
- Hardware availability, queue conditions, and backend drift may affect absolute runtime and measurement characteristics across reruns.

---

## Data Notes  

The repository is built around **IBM Quantum hardware outputs** and their derived evaluation files.  
The `data/` directory is intended to store:

- backend metadata
- raw hardware job logs
- sweep outputs across time, distance ratio, and offered load
- processed metric summaries used for plotting and manuscript tables

If any external or derived datasets are added in future extensions, redistribution should only be performed when permitted by the original source and applicable license terms.

---

## Artifact Policy  

The `figures/` directory is intended for curated research outputs such as:

- final plots used in manuscripts
- publication-ready PDF/SVG/PNG exports
- reproducible benchmark summaries
- intentionally shared result bundles

Large temporary logs, duplicate raw outputs, and repeatedly generated intermediate files should not be committed unless explicitly required for archival reproducibility.

---

## Figures and Publication Assets  

This repository is structured to support publication-oriented asset generation, including:

- temporal yield and compliance plots
- stress-response summaries versus distance ratio
- offered-load summaries versus SD-pair count
- reproducibility-ready PDF/SVG/PNG figure bundles

Where applicable, publication assets should be exported in stable formats and retained under curated artifact directories.

---

## Authors and Collaborators  

**Shakil Ahmed, Member, IEEE**  
Department of Electrical and Computer Engineering, Iowa State University, Ames, Iowa, USA  
Email: [shakil@iastate.edu](mailto:shakil@iastate.edu)

**Mubassir Sudipto**  
Department of Electrical and Computer Engineering, Iowa State University, Ames, Iowa, USA  
Email: [msudipto@iastate.edu](mailto:msudipto@iastate.edu)

**Ashfaq Khokhar, Fellow, IEEE**  
Department of Electrical and Computer Engineering, Iowa State University, Ames, Iowa, USA  
Email: [ashfaq@iastate.edu](mailto:ashfaq@iastate.edu)

---

## Citation  

If you use this repository in academic work, please cite the associated paper and, where appropriate, the software repository itself.

Bibtex repository citation:

```bibtex
@misc{qrita_framework_2025,
  author       = {Shakil Ahmed and Mubassir Serneabat Sudipto and Ashfaq Khokhar},
  title        = {Q-RITA Framework: Deadline-Aware Entanglement Routing for RIS-Assisted Terrestrial Quantum Links},
  year         = {2025},
  howpublished = {\url{https://github.com/msudipto/Q-RITA_Framework}},
  note         = {Code repository}
}
```

---

## License  

This repository is released under the **MIT License**.  
See the [`LICENSE`](LICENSE) file for complete terms.

---

## Acknowledgment  

This research repository supports ongoing work in **RIS-assisted quantum networking**, **deadline-aware entanglement service**, and **hardware-grounded quantum network evaluation**, with emphasis on reproducible methodology and publication-oriented artifact generation.

---

**Correspondence:** *Prof. Shakil Ahmed, Member, IEEE; Mr. Mubassir Serneabat Sudipto; and Prof. Ashfaq Khokhar, Fellow, IEEE*  
**Emails:** [shakil@iastate.edu](mailto:shakil@iastate.edu), [msudipto@iastate.edu](mailto:msudipto@iastate.edu), [ashfaq@iastate.edu](mailto:ashfaq@iastate.edu)  
**Affiliation:** Department of Electrical and Computer Engineering, Iowa State University, Ames, Iowa, USA
