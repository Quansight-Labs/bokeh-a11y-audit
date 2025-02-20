# Contributing

Thanks for contributing to this repository.

You can open [issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) to report problems and discuss new updates to the audit, and open [pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to contribute to the project.

## Contribute to audit documentation

The audit findings are organized and presented with [Sphinx](https://www.sphinx-doc.org/en/master/)-based documentation website, using the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/). The documentation files are written in [MyST Markdown](https://mystmd.org/guide/quickstart-myst-markdown).

## Notes for authoring markdown

- Ensure every page follows the heading hierarchy: H1, H2, and so on.
- Use the following syntax for embedding images:

  ````
    ```{figure} relative_path_to_image.png
        :width: 100%
        :alt: Alt-text for the imahe

        A scatter plot is shown. A plotting tool button is toggled active on the right. The contrast checking score is shown on the bottom left corner (fails).
    ```
  ````

- Use the following syntax for embedding videos:
  ````
    ```{video} relative_path_to_video.mp4
    :width: 100%
    :playsinline:
    ```
  ````

### Build documentation locally (optional)

For major updates to the documentation website, it's useful to test your contributions with a local live development of the website. You can build it with the following instructions.

1. Fork and clone the repository:
   ```
   git clone https://github.com/<your_username>/bokeh-a11y-audit.git
   ```
2. Create a [conda](https://docs.conda.io/projects/conda/en/stable/#) environment with the required dependencies and activate it:
   ```
   conda env create -f environment-docs.yaml
   conda activate bokeh-a11y-docs
   ```
3. Install pre-commit hooks (for linting and formatting):
   ```
   pre-commit install
   ```
4. Start a live deployment of the documentation website:
   ```
   sphinx-autobuild source build/html
   ```
   Your local website will be available at [localhost:8000](http://127.0.0.1:8000).
   This site is re-built when you save local changes.

## Contribute to the dashboard

The audit was performed on a Bokeh dashboard containing some primary components.

Read the [`dashboard/README`](dashboard/README.md) for more details about the dashboard source, local execution, and deployment.
