# CNRS HPC Portal Redesign Direction

## Ground-truth reference

The user requested that this portal follow the existing **The Omics Hub** theme. The redesign will therefore use the Omics Hub visual language as the ground truth: deep navy structure, Omics blue navigation and action accents, cyan molecular-network details, restrained violet and gold status highlights, light readable documentation surfaces, and a scientific workstation character.

## Chosen Approach: Omics Systems Console

**Design Movement:** Editorial scientific interface design, paired with the calm technical clarity of a modern research knowledge base.

**Core Principles:** The hierarchy must be immediately scannable, technical documentation must remain primary, interfaces must feel trustworthy instead of decorative, and every complex tutorial section must retain clear navigation back to the portal.

**Color Philosophy:** Deep Navy `#123B5D` anchors the institutional research identity. Omics Blue `#2563EB` distinguishes actions and active navigation. Cyan `#22D3EE`, muted violet `#A78BFA`, and gold `#FBBF24` are used sparingly to identify computational states, pathways, and important warnings without introducing bright green accents.

**Layout Paradigm:** The homepage is a research-command landing space with a dark systems header, an asymmetric introduction pane, and a compact task-routing rail. Long technical documents use a readable two-column desktop layout with a persistent local navigation spine, collapsing into a single linear reading route on mobile.

**Signature Elements:** A molecular-network mark, thin horizontal pathway lines, dark terminal panels with a branded `TheOmicsHub@nmabbasi:~$` prompt, and compact metadata chips for operating-system or workflow context.

**Interaction Philosophy:** Navigation is concise and predictable. Links have clear focus states, dropdowns remain keyboard reachable, and documentation actions use direct labels rather than novelty interactions.

**Animation:** Hover feedback uses opacity and transform transitions shorter than 220 ms. Motion remains non-essential, subtle, and disabled for reduced-motion preferences.

**Typography System:** Manrope provides readable interface and body text; JetBrains Mono or the existing Fira Code provides code. Technical headings use compact high-weight hierarchy and generous line height rather than decorative display type.

**Brand Essence:** A precise HPC documentation portal for computational biology researchers who need reliable, practical access to shared research computing. **Personality:** rigorous, calm, enabling.

**Brand Voice:** Direct, operational, and supportive. Example lines: “Connect securely before you compute.” and “Choose the right route for your analysis.”

**Wordmark & Logo:** A compact molecular-network symbol followed by “CNRS HPC Portal” in a bold scientific wordmark treatment. The existing factual affiliation and researcher name remain visible, without creating an unauthorised CNRS logo.

**Signature Brand Color:** Omics Blue `#2563EB`.

## Validation Notes

The local desktop preview confirms the intended portal hierarchy: a dark research-computing hero with the molecular-network mark, readable text over the retained HPC image, clear primary actions, an immediately visible four-route panel, and the original operational documentation below. The hero text uses an opaque navy reading panel to preserve contrast against the visual background.

The final refinement deliberately differentiates the portal from The Omics Hub. The academy’s molecular-network mark and brand wording were replaced by a compact compute-grid marker, a mineral-blue and muted-teal institutional palette, IBM Plex typography, structured grid geometry, and the distinct `hpc@cnrs:~$` code-panel label. The mobile-width verification reports a 375 px viewport with 360 px document width, block navigation, and no horizontal overflow.

The final documentation-first revision removes the profile-led composition from the homepage. It now prioritizes six task cards and a four-step route through access, orientation, computing, and reproducibility. The refreshed 375 px verification reports a 360 px document width with no horizontal overflow, single-column task cards, and a visible flex navigation rail.

The Jekyll migration replaces copied legacy root pages with a Markdown-based documentation collection, data-driven task navigation, and reusable default and document layouts. The local Jekyll build succeeds with the GitHub Pages dependency set. The rendered homepage, SSH guide, and Conda guide confirm that the legacy content is retained in reusable layouts, with the Conda article wrapper removed so its headings and lists render correctly.

The owner approved the Jekyll migration and the six-card light-colour navigation. Commit `3958f66` is live on the CNRS GitHub Pages site. The public homepage now renders the Jekyll task-based guide, and The Omics Hub public Writing Job Scripts lesson includes its published CNRS portal reference via commit `f43740d`.

The usability refinement increases desktop header navigation to 14.72 px with 46 px targets, task-card number markers to 16 px, and card actions to 15.36 px. The six task markers retain six distinct light background colours. In a 375 px viewport, the task cards form one 332 px column with no horizontal overflow. Opening the mobile menu exposes 46 px-high navigation targets with a minimum width of 163 px. The static page remains lightweight: the live audit recorded 69 ms DOM content loading and 144 ms load completion with no slow resources.

The browser diagnosis identified the external Google Font stylesheet as the only potential text-rendering dependency. The corrected layout removes it from all public Jekyll pages and falls back to immediate system typography. The latest local preview shows substantially larger step markers, header tabs, and task labels. Its new dark documentation footer includes a concise purpose statement, direct links to every main guide, a high-visibility support route, and a Back to top action.

The final browser check confirms that public Jekyll pages now make no external font requests. Desktop navigation is 16 px with 52 px targets, each step marker is 20.48 px inside a 58 px badge, and the footer provides six direct documentation routes plus Back to top. The local page reached DOM content loaded in 143 ms and complete loading in 172 ms. At 375 px, the guide has no horizontal overflow, step badges remain 19.2 px and 54 px high, the opened menu uses 50 px targets, and footer links remain 46 px high in a single-column footer layout.

The owner approved the corrected refinement. Commit `5522989` was deployed successfully through GitHub Pages, and the live browser verifies zero external font requests, 16 px header navigation with 52 px targets, 20.48 px step markers with 58 px badges, six footer documentation routes, and a working Back to top control.

Live guide inspection found that the Conda page has a readable heading and opening structure, but its long instructions retain migration artefacts such as literal `notranslate` code-fence tokens and stale Great Lakes-specific installation wording. The Manage custom software guide is materially broken: its imported Markdown appears as one continuous paragraph containing literal heading markers, emphasis markers, and command text. The next correction must reconstruct this page into semantic headings, ordered steps, bullet lists, and fenced command examples.

After cleaning the source wrappers, the local Manage custom software guide renders as a clear semantic tutorial with headings, warnings, code panels, and troubleshooting notes. The local Conda guide now renders its code panels correctly, but its retained legacy article is still unnecessarily long and includes hard-coded historical examples. It should be replaced with a concise, current, institution-neutral workflow rather than retaining the legacy installation narrative.

Final local verification: the rewritten Conda guide now presents a concise HPC-neutral sequence for available installations, channel configuration, project environments, reproducibility exports, Slurm use, and troubleshooting. Its sections and code panels render cleanly. The footer support control now has a dedicated green hover and visible keyboard-focus treatment; this approved green is limited to the CNRS support action.

The local browser verification confirms that the footer card labelled “Open the support guide” changes from the teal outline treatment to a clearly visible green surface on mouse hover, while retaining white high-contrast text.
