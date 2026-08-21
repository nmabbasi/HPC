---
title: 'Support and troubleshooting'
summary: 'Turn an HPC problem into a concise, reproducible support request with the information needed to resolve it.'
step: '06'
---

<section class="support-lead">
  <p class="support-label">A practical learning route</p>
  <h2>Turn errors into reusable knowledge</h2>
  <p>HPC learning becomes much clearer when the error, job details, environment, and expected result are captured together. Follow this short route to understand a problem before asking for local account guidance.</p>
</section>

<section class="support-actions" aria-label="Learning actions">
  <div class="support-action-primary"><span>Guided practice</span><strong>Start with the evidence</strong></div>
  <div class="support-action-secondary"><span>Learning habit</span><strong>Keep one small reproducible example</strong></div>
</section>

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

## Use this learning checklist

Copy this compact template into your study notes. It helps you reproduce a problem without guessing about the command, system state, or intended output.

```text
Topic: Short description of the issue

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
    <p class="support-label">Local guidance</p>
    <h2>Know what to ask for</h2>
    <p>Use the checklist above to describe the issue clearly. For local accounts, access, or allocation policies, follow the process supplied for your own system.</p>
  </div>
  <p class="support-email"><span>Local access questions</span><strong>Contact the administrator of University responsible for your system.</strong></p>
</section>

## Choose the right learning focus

<div class="support-links">
  <section class="support-resource-card"><strong>Connection practice</strong><span>Review SSH keys, profile syntax, and safe authentication habits.</span></section>
  <section class="support-resource-card"><strong>Command practice</strong><span>Review paths, modules, and basic cluster commands with short examples.</span></section>
  <section class="support-resource-card"><strong>Slurm practice</strong><span>Inspect resource requests, job state, and log files after a small test run.</span></section>
  <section class="support-resource-card"><strong>Conda practice</strong><span>Check activation, installed tools, and a reproducible environment description.</span></section>
</div>

<section class="learning-resources" aria-labelledby="learn-more-title">
  <div class="learning-resources-heading">
    <p class="support-label">Continue learning</p>
    <h2 id="learn-more-title">Build a focused HPC study routine</h2>
    <p>Use these reputable external lessons to deepen your command-line foundations, scheduler understanding, and reproducibility habits. Local access and account rules always come from your own system.</p>
  </div>
  <div class="learning-resource-grid">
    <a class="learning-resource-card" href="https://swcarpentry.github.io/shell-novice/" target="_blank" rel="noopener noreferrer"><span class="resource-type">Foundation lesson</span><strong>Software Carpentry: The Unix Shell <span aria-hidden="true">↗</span></strong><small>Build confidence with navigation, files, permissions, and small shell scripts.</small></a>
    <a class="learning-resource-card" href="https://www.hpc-carpentry.org/hpc-shell/" target="_blank" rel="noopener noreferrer"><span class="resource-type">HPC workflow</span><strong>HPC Carpentry: Using the Shell <span aria-hidden="true">↗</span></strong><small>Learn how command-line skills connect to shared research-computing workflows.</small></a>
    <a class="learning-resource-card" href="https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html" target="_blank" rel="noopener noreferrer"><span class="resource-type">Environment management</span><strong>Conda: Getting Started <span aria-hidden="true">↗</span></strong><small>Learn to create isolated environments, inspect them, and install packages reproducibly.</small></a>
    <a class="learning-resource-card" href="https://slurm.schedmd.com/documentation.html" target="_blank" rel="noopener noreferrer"><span class="resource-type">Scheduler reference</span><strong>Slurm: User Documentation <span aria-hidden="true">↗</span></strong><small>Explore job states, commands, resource requests, and scheduler concepts from the official reference.</small></a>
  </div>
</section>

> **Safe sharing rule:** never include passwords, private SSH keys, access tokens, participant information, or restricted research data in a support request.
