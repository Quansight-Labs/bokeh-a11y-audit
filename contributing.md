# Contributing

Thanks for contributing to this repository.
You can open issues to report bugs and open pull requests to contribute.

## Build documentation locally

The audit findings are organized and presented using Sphinx-based documentation website.
You can build a live development version locally with the following instructions.

1. Fork and clone the repository: `git clone https://github.com/<your_username>/bokeh-a11y-audit.git`
2. Create a [conda](https://docs.conda.io/projects/conda/en/stable/#) environment and download the dependencies: `conda env create -f environment-docs.yaml`
3. Activate the conda environment `conda activate bokeh-a11y-docs`
4. Start a live deployment of the documentation website: `sphinx-autobuild source build/html`
5. Open [localhost:8000](http://127.0.0.1:8000) to access the local website, this is re-built when you save local changes.
