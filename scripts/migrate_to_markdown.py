from pathlib import Path
from subprocess import run
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".migration"
TARGET = ROOT / "_docs"
TARGET.mkdir(exist_ok=True)

GUIDES = {
    "connections": {
        "title": "Secure cluster connection",
        "summary": "Set up SSH keys, connect from Linux, macOS, or Windows, and use graphical access when available.",
        "step": "01",
        "next_label": "Next step",
        "next_title": "Learn the cluster basics",
        "next_url": "/docs/commands/",
    },
    "commands": {
        "title": "Cluster basics and commands",
        "summary": "Load modules, inspect partitions, monitor jobs, and understand the HPC environment before submitting work.",
        "step": "02",
        "next_label": "Next step",
        "next_title": "Write a Slurm job script",
        "next_url": "/docs/job-scripts/",
    },
    "job-scripts": {
        "title": "Writing Slurm job scripts",
        "summary": "Allocate resources, record logs, submit batch jobs, and run reproducible compute tasks safely.",
        "step": "03",
        "next_label": "Next step",
        "next_title": "Use Conda on the cluster",
        "next_url": "/docs/conda/",
    },
    "conda": {
        "title": "Conda environments on the cluster",
        "summary": "Create, activate, export, and use isolated software environments in HPC workflows.",
        "step": "04",
        "next_label": "Next step",
        "next_title": "Manage custom software",
        "next_url": "/docs/custom-modules/",
    },
    "custom-modules": {
        "title": "Custom software modules",
        "summary": "Create and use user-maintained module files for approved software on shared compute systems.",
        "step": "05",
        "next_label": "Next step",
        "next_title": "Get support",
        "next_url": "/docs/support/",
    },
    "support": {
        "title": "Support and troubleshooting",
        "summary": "Collect the right job details, log excerpts, and context before requesting technical support.",
        "step": "06",
    },
    "requests": {
        "title": "Questions and requests",
        "summary": "Use the support route for questions, access requests, and HPC help.",
        "step": "Support",
    },
}

for slug, meta in GUIDES.items():
    source = SOURCE / f"{slug}.html"
    result = run(["pandoc", "--from=html", "--to=gfm", "--wrap=none", str(source)], check=True, capture_output=True, text=True)
    markdown = result.stdout.replace("/docs/connections/", "{{ '/docs/connections/' | relative_url }}")
    markdown = markdown.replace("/docs/commands/", "{{ '/docs/commands/' | relative_url }}")
    markdown = markdown.replace("/docs/job-scripts/", "{{ '/docs/job-scripts/' | relative_url }}")
    markdown = markdown.replace("/docs/conda/", "{{ '/docs/conda/' | relative_url }}")
    markdown = markdown.replace("/docs/custom-modules/", "{{ '/docs/custom-modules/' | relative_url }}")
    markdown = markdown.replace("/docs/support/", "{{ '/docs/support/' | relative_url }}")
    markdown = re.sub(r'<a href="#[^"]*"[^>]*><img src="data:image/svg\+xml;base64,[^"]*"[^>]*></a>', "", markdown)
    for image_name in ["M1.png", "MA.png", "miniconda_installer.png", "anaconda_mothur_search_results.png", "anaconda_mothur_package_page.png", "n2.png", "nothing.png", "partitions.png"]:
        markdown = markdown.replace(f'src="{image_name}"', f'src="{{{{ \'/{image_name}\' | relative_url }}}}"')
        markdown = markdown.replace(f'href="{image_name}"', f'href="{{{{ \'/{image_name}\' | relative_url }}}}"')
    markdown = "\n".join(line.rstrip() for line in markdown.splitlines()) + "\n"
    front_matter = ["---"] + [f"{key}: {value!r}" for key, value in meta.items()] + ["---", ""]
    (TARGET / f"{slug}.md").write_text("\n".join(front_matter) + markdown, encoding="utf-8")
    print(f"Converted {slug}.html → _docs/{slug}.md")
