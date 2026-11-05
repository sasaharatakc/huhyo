# Migration checkpoint

2026-11-06: NOT COMPLETE; do not advertise visual parity.

Source: Sites appgprj_6ae5cd13de9c8191bb82fe10c0380884 at commit 353687a67dc65c56fba52fa32aecb2641c805412. Recover source through Sites credentials, then run build-wordpress.py in its root.

Scope: 9 non-blog routes. Forms excluded. Original static CSS/HTML retained, Elementor JS removed. FAQ and menu replacements written; browser behavior remains unverified. Source contains plugin-named CSS directories but no PHP plugins installed.

Build output: wordpress-build-v2/fuhyo-reproduction.zip, 62,808,180 bytes. 307 dependent assets. HTTP test in fresh WordPress PHP 8.3: 9/9 return 200, no PHP errors, no Elementor script URLs.

Remaining: missing source GIF and MP4; fix external-media URL handling; inspect CSS and srcset resolution; visual comparison at mobile/tablet/desktop; test navigation/FAQ/carousel behavior; confirm hooks and page editing; test ZIP upload; publish only verified build. Current public GitHub theme/launcher is still the earlier simplified theme, not this migration.
