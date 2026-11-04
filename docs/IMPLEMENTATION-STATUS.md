# WordPress migration checkpoint — 2026-11-05

## Scope
Reproduce prior static site in standalone WordPress theme. No Elementor. Exclude blog and form processing. Never modify production. Free testing only.

## Authoritative visual baseline
Sites project appgprj_6ae5cd13de9c8191bb82fe10c0380884, saved version 2.
https://net-fuhyohigai-mobile-preview.takesasa557.chatgpt.site/
251 MB, 1158 files. Source recovered to static-source at commit 353687a67dc65c56fba52fa32aecb2641c805412; 242 MB dist; do not substitute simplified current homepage for this baseline.

## Completed
- Located static preview and source version.
- Found original XML locally at source/WordPress.2026-10-27.xml.
- Inspected 9 published fixed pages (includes thanks, excluded from migration).
- Consolidated duplicate setup hooks and block pattern registration.
- Preserved untracked editor content and theme.json from previous work.
- git diff --check passed. PHP executable unavailable; PHP runtime validation NOT performed.

## Pending, in dependency order
1. Recover static source and inspect asset dependency graph.
2. Freeze non-blog route and screenshot inventory.
3. Convert common layout and TOP to standalone templates; remove Elementor runtime dependencies.
4. Migrate non-blog fixed pages preserving paths.
5. Connect standard WordPress editing and explicit initial-data import.
6. Visual comparison at 375/390/768/1440px; menus, FAQ, scrolling, links.
7. PHP and real WordPress installation/edit/save tests.
8. Package theme and publish updated Playground blueprint.

## Verification limits
Current Playground is a prior simplified theme, NOT completed reproduction.
Static preview browser currently shows sign-in wall; visual verification not completed.
No production changes, paid resources, or form sending.

## Resume
Read this file first, then inspect Git status and static-source recovery result. Do not overwrite local work or report untested items as passed. Record exact commit, source version, tests, blockers, next action after each milestone.

Baseline inventory: migration/static-baseline.json, 8 routes with SHA256 and CSS/JS dependencies. Elementor, Jeg, Elementskit runtime replacement still required.
