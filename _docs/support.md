---
title: 'Support and troubleshooting'
summary: 'Turn an HPC problem into a concise, reproducible support request with the information needed to resolve it.'
step: '06'
---

<section class="support-lead">
  <p class="support-label">A practical support route</p>
  <h2>Get unstuck with useful evidence</h2>
  <p>Most HPC issues can be resolved much faster when the error, job details, environment, and expected result are captured together. Follow this short route before sending a request.</p>
</section>

<nav class="support-actions" aria-label="Get Support actions">
  <a class="support-action-primary" href="mailto:nmabbasi@gmail.com?subject=HPC%20Guide%20support%20request"><span>Direct contact</span><strong>Email for support <span aria-hidden="true">→</span></strong></a>
  <a class="support-action-secondary" href="#capture-the-essentials"><span>Before you contact</span><strong>Collect job details <span aria-hidden="true">↓</span></strong></a>
</nav>

<div class="support-grid" aria-label="Support triage steps">
  <section class="support-card">
    <p class="support-number">01</p>
    <h3>Locate the failure</h3>
    <p>Write down the exact command or job step that failed, together with the time it occurred and the result you expected.</p>
  </section>
  <section class="support-card">
    <p class="support-number">02</p>
    <h3>Capture the evidence</h3>
    <p>Keep the job ID, full error message, relevant output files, and tool or environment version. Do not paraphrase an error when you can paste it.</p>
  </section>
  <section class="support-card">
    <p class="support-number">03</p>
    <h3>Send a focused request</h3>
    <p>Explain what you tried, what happened, and what you need next. Remove passwords, access tokens, and restricted research data.</p>
  </section>
</div>

## Capture the essentials

For a Slurm job, begin with the scheduler record and the final lines of both output files. Replace the placeholder job ID and filenames with your own values.

```bash
squeue --job JOB_ID
sacct --jobs JOB_ID --format=JobID,State,ExitCode,Elapsed,MaxRSS
tail -n 40 job-output.out
tail -n 40 job-error.err
```

For an environment or software problem, capture the executable and version after loading the modules or activating Conda.

```bash
module list
conda info
which TOOL_NAME
TOOL_NAME --version
```

## Use this request template

Copy this compact template into an email. A request with this context lets another researcher reproduce the problem without guessing about the command, system state, or intended output.

```text
Subject: HPC Guide support request: short description

Goal: What I am trying to run.
Where it fails: Command or workflow step.
Expected result: What I expected to happen.
Observed result: Exact error or scheduler state.
Job ID: If applicable.
Environment: Modules, Conda environment, or tool version.
What I already tried: Brief list of troubleshooting steps.
Attachments: Relevant job script and small log excerpts only.
```

<section class="support-contact">
  <div>
    <p class="support-label">Contact route</p>
    <h2>Send a concise support request</h2>
    <p>Include the template above and only the smallest useful log excerpt. The contact route is intended for technical questions about the guidance, reproducible workflow problems, and document corrections.</p>
  </div>
  <a class="support-email" href="mailto:nmabbasi@gmail.com?subject=HPC%20Guide%20support%20request">Email nmabbasi@gmail.com <span aria-hidden="true">→</span></a>
</section>

## Choose the right support route

<div class="support-links">
  <a href="{{ '/docs/connections/' | relative_url }}"><strong>Connection support</strong><span>Recheck access, SSH syntax, and authentication.</span></a>
  <a href="{{ '/docs/commands/' | relative_url }}"><strong>Command and module support</strong><span>Review paths, modules, and basic cluster commands.</span></a>
  <a href="{{ '/docs/job-scripts/' | relative_url }}"><strong>Slurm job support</strong><span>Inspect resource requests, job state, and log files.</span></a>
  <a href="{{ '/docs/conda/' | relative_url }}"><strong>Conda environment support</strong><span>Check channels, activation, and the exported YAML file.</span></a>
</div>

> **Safe sharing rule:** never include passwords, private SSH keys, access tokens, participant information, or restricted research data in a support request.
