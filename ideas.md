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
