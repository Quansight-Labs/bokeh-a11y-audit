# Bokeh dashboard for accessibility audit

This repository contains assets and artefacts related to Bokeh accessibility audits:

- [A dashboard with commonly used Bokeh plot elements](./dashboard.ipynb).

This dashboard can be accessed at <https://quansight-labs.github.io/bokeh-a11y-audit/>.

## Run the dashboard code locally

1. Clone the repository: `git clone https://github.com/Quansight-Labs/bokeh-a11y-audit.git`

2. Navigate to the dashboard folder: `cd bokeh-a11y-audit/dashboard`

3. Install `conda` if needed and create a `conda` environment with the required packages: `conda env create -f environment.yml`

4. Activate the environment: `conda activate bokeh-dashboard`

5. Start JupyterLab: `jupyter lab`

6. Run and the update the code in `dashboard.ipynb`.

## Deploy dashboard with GitHub pages

The final section in `dashboard.ipynb` exports the dashboard as an HTML file (`index.html`) at the root of the repository.
Check the file into git in the `pages` branch, which is served using GitHub pages.
Go to the repo settings to update GitHub pages configurations, if needed.
