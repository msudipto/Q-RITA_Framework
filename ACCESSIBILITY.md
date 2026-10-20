# Accessibility Statement

We want the Q-RITA Framework to be accessible to everyone, including researchers, students, and practitioners with disabilities. This document outlines our current accessibility focus and how you can report barriers.

## Priorities

Our priority is ensuring that our research codebases, hardware setup files, and data logs are readable and usable by all developers. We focus on:
* **Text Readability**: Structuring project scripts, pipeline execution instructions, and metrics definitions to be clear and compatible with screen readers.
* **Vector Graphics**: Exporting evaluation plots and charts inside the `figures/` folder using stable vector file structures like SVG and PDF to support high-contrast scaling.
* **Keyboard-Only Operation**: Ensuring that our main workflow sequences can be completely executed and monitored via standard keyboard terminal interactions.

## Contributor expectations

When contributing new hardware collection steps, metric synthesizers, or data scripts:
* Use high-contrast color palettes for code execution figures and charts to assist color-blind reviewers.
* Document any changes to configuration keys or metrics in clear, semantic plain text within documentation files or script headers.

## Reporting accessibility issues

If you encounter an accessibility barrier while running our scripts, reading the framework logs, or inspecting the publication charts, please report it privately via email:

* **Mubassir Serneabat Sudipto** — msudipto@iastate.edu

Please describe the barrier you encountered, the relevant script or file path, and any assistive technology you were using.

### How we respond

We will acknowledge your report within 5 business days and work to implement a clear text workaround or graphical update in the primary development branch.

## Supported environments

This framework is tested on standard terminal environments (Windows PowerShell and Unix Bash). We recommend using high-contrast terminal themes and vector-capable document viewers to inspect output charts under the `figures/` folder.
