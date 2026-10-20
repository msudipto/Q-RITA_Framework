## Description
Provide a clear description of the modifications, script optimizations, or mathematical logic adjustments introduced by this PR. 

## Related Issue
Fixes # (link your configured Bug Report or Feature Request issue number here)

## Change Type
- [ ] Bug fix (non-breaking change fixing an execution crash or calibration file error)
- [ ] New feature (non-breaking extension adding routing metrics or ansatz layers)
- [ ] Refactoring / Documentation update

## Pipeline Verification & Local Testing Checklist
Please verify that you have tested your modifications locally by checking the boxes below:
- [ ] `python ibm_open_setup.py` runs and updates backend logs safely.
- [ ] `python collect_hardware_runs.py` executes or successfully models sampler outputs.
- [ ] `python build_metrics.py` synthesizes yield and compliance proxies without formatting issues.
- [ ] `python plot_graphs.py` correctly renders stable `.png`, `.svg`, and `.pdf` assets into the `figures/` directory.

## Artifact and Git Integrity
- [ ] I have **NOT** included transient execution caches, duplicate local logs, or heavy raw matrix arrays in this commit.
- [ ] Any necessary large research assets have been explicitly declared via Git LFS.
