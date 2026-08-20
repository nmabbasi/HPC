# HPC Guide Publication Checklist

- [x] Format the Conda guide title in two deliberate lines.
- [x] Re-measure fresh Conda loading behaviour and identify any actionable delay.

Fresh measurement: five uncached live document requests completed in 46–117 ms. The Conda page now also skips the two support-only stylesheet requests, reducing cold-load work without changing the guide content.
- [x] Validate and publish the Conda title and performance refinement.

Local verification: the Conda title now renders as exactly two lines, with Conda environments on the first line and on the cluster on the second.

Live verification: the deployed Conda page receives versioned stylesheets, preventing an older cached stylesheet from overriding the intended two-line title layout.
- [x] Remove the CURRENT text from active side routes while retaining their green active state.
- [x] Measure the live Conda guide loading path and address any avoidable bottleneck.

Performance finding: a fresh live Conda load reached DOM content in 84 ms, completed in 91 ms, and returned its document in 108 ms from the host. There is no measured page-level loading bottleneck to remove.
- [ ] Validate and publish the active-route and performance refinement.
- [x] Redesign the Next step control as a tab-style navigation card.
- [x] Add a green hover and keyboard-focus state to the Next step card.
- [x] Validate and publish the Next step refinement.

Local review: the Next step control now renders as a separate tab-style card beneath the documentation content. On hover it becomes a clear green tab with white text and a white arrow control.

Live verification: the Get Support page displays the direct contact as `Email: nmabbasi@gmail.com` in both contact controls.
- [x] Improve the side HPC route interaction and current-page clarity.
- [x] Apply an accessible light-green active state to the top navigation and side route.
- [x] Validate and publish the navigation-state refinement.

Verification: the local side route moved from Conda to Software correctly, with the selected top tab and selected side route both shown in light green.
- [x] Audit all six documentation routes for consistent navigation names and active-tab states.
- [x] Restore a focused learning-resources section in Get Support without displacing direct help actions.
- [x] Validate and publish the complete guide-wide navigation refinement.

Verification: a cache-bypassed live review confirmed the seven primary tabs, active-page state, direct Get Support actions, and four restored learning-resource links.
- [x] Make the Get Support route explicit in primary navigation, route cards, and help actions.
- [x] Add a clear support-link section that directs learners to the right guide before contacting support.
- [x] Validate and publish the revised Get Support navigation.
- [x] Identify every visible `CNRS` portal label, legacy Oliver contact email, and repository-origin reference.
- [x] Replace portal branding with `HPC Guide` while preserving the existing documentation routes and Jekyll build.
- [x] Replace the legacy contact email with the owner’s established email address.
- [x] Redesign the support guide into a clear triage workflow with reporting checklist, contact route, and focused self-help resources.
- [x] Verify the support guide on desktop, including the green hover and keyboard-focus treatments.
- [x] Rebuild and verify the Conda guide, custom-software guide, and green support-control hover state locally.
- [x] Commit the content and branding changes, then rename the GitHub repository to `HPC`.
- [x] Confirm the GitHub Pages URL and verify the renamed live portal after deployment.
