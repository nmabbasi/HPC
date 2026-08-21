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
  <p class="support-email">Ask the <strong>administrator of University</strong></p>
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
    <p>Use these four self-contained study prompts to strengthen command-line foundations, reproducibility habits, and shared-computing concepts.</p>
  </div>
  <div class="learning-resource-grid">
    <article class="learning-resource-card"><span class="resource-type">Practice 01</span><strong>Navigate and inspect</strong><small>Practise pwd, ls, cd, mkdir, and file permissions in a scratch directory until each command feels predictable.</small></article>
    <article class="learning-resource-card"><span class="resource-type">Practice 02</span><strong>Run a tiny job</strong><small>Submit the smallest possible scheduler task, inspect its output, then change one resource request at a time.</small></article>
    <article class="learning-resource-card"><span class="resource-type">Practice 03</span><strong>Record your environment</strong><small>Write down your shell, modules, Conda environment, tool version, and command before running a workflow.</small></article>
    <article class="learning-resource-card"><span class="resource-type">Practice 04</span><strong>Explain one error</strong><small>Keep a short error journal: what you ran, what happened, what changed, and what you learned from the retry.</small></article>
  </div>
</section>

> **Safe sharing rule:** never include passwords, private SSH keys, access tokens, participant information, or restricted research data in a support request.
