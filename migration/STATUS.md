# WordPress reproduction checkpoint — 2026-11-06

Not complete. Scope: nine non-blog routes; no contact forms, no Elementor runtime.

## Verified
- v0.3.0: fresh WordPress CLI instance serves all nine routes with HTTP 200, no detected PHP errors.
- 101 unique HTML-linked local assets return HTTP 200. This does not cover all CSS/srcset dependencies.
- v0.3.0 ZIP installed successfully via WordPress Playground admin (WordPress 7.1.4 observed in UI).
- Browser theme activation was blocked by automatic approval review: custom ZIP PHP execution requires user confirmation at action time. No bypass attempted.

## Latest source
- v0.3.1 fixes internal fragment links for subdirectory installation, duplicate wp_head title, and WP 404 query flag.
- Python build and JS syntax checks pass. v0.3.1 has not yet been installed or runtime-tested after the activation block.
- Built ZIP: 62,808,458 bytes; 307 captured assets; nine HTML routes.
- ZIP saved as fuhyo-reproduction.zip, Library id libfile_c15c76e1642c8191b5cbfa0a9e10e181.

## Remaining
1. Obtain confirmation to activate custom theme in isolated WordPress Playground; upload latest ZIP and activate.
2. Desktop/mobile visual and menu/FAQ/carousel interaction QA; correct differences.
3. Two source-media files absent from capture (Cybersecurity GIF and Japanese-named MP4); currently retain original-domain URLs, availability unverified.
4. Publish verified theme package to GitHub and update playground/blueprint.json. Existing launcher still installs old simplified theme and must NOT be described as completed reproduction.

Original source: https://net-fuhyohigai-taisaku.co.jp/
Captured static reference: https://net-fuhyohigai-mobile-preview.takesasa557.chatgpt.site
