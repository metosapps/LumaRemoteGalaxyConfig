# Luma Remote — Galaxy configuration and policies

This repository is exclusively for **com.luma.smartremote / Galaxy Store**. It contains public configuration and policy pages, not Android source, APKs, signing material, seller credentials or TV/user data.

- [Privacy Policy](https://metosapps.github.io/LumaRemoteGalaxyConfig/privacy.html)
- [Terms of Use](https://metosapps.github.io/LumaRemoteGalaxyConfig/terms.html)
- [Support](https://metosapps.github.io/LumaRemoteGalaxyConfig/)
- [Remote JSON](https://metosapps.github.io/LumaRemoteGalaxyConfig/config_galaxy.json)

Contact: **chennoufo11@gmail.com**. GitHub Pages publishes the root of `main`.

`ads.enabled=false` keeps production advertising off. Debug builds may use official demo IDs only when `ads.test_enabled=true`, the master kill switch is on, and the build permits demo ads. Debug ignores remote live unit IDs. `kill_switches.ads_enabled=false` disables all formats in both modes. Turn individual `placements.*.enabled` off to disable specific inventory. App clients discard cached fullscreen inventory when IDs or placements change.

Before enabling production: confirm this exact signed Galaxy app is live, configure applicable AdMob Privacy & messaging, create each enabled format's own real unit under the supplied Luma App ID, obtain production enablement approval, and increment `revision`. A manifest App ID or new SDK/permission requires an app release. Do not reuse other apps' IDs or enable store-independent inventory.

Clients fetch on launch, on foreground after a one-minute request throttle, and every 15 minutes while the process remains alive. Timeout is 12 seconds with five-second connection/read limits, a 64 KiB body limit, no HTTP redirects, strict package/store/schema/publisher checks, and revision rollback rejection. Last-known-good cache is available for up to `cache_ttl_seconds` (six hours by default, maximum one day). Expired/future-dated cache disables ads. Bundled defaults and cached policy still permit normal offline launch unless an explicit cached maintenance/force-update decision applies. Restoring purchases and existing Pro ownership are preserved if new purchases are remotely disabled.

Remote automatic frequency limits can only be increased from their compiled safe minimum: fullscreen >=300 seconds and App Open >=600 seconds. Reward value stays 30 minutes in the reviewed app. Native NO_FILL does not block controls. UMP permission and verified Pro always take precedence over remote flags.

`update_mode` is `none`, `soft` or `force`; update URLs must match this exact Galaxy listing. Do not force-update until the target binary is live and available to intended users. `global.maintenance_mode` blocks entry when needed. `links` controls support and policy destinations. `features.reward_offer` controls the voluntary offer. `kill_switches.iap_enabled` only stops new Buy actions; it does not revoke verified benefits or disable Restore.

Run `python3 validate_config.py` before pushing. CI validates the configuration. Increment revision for every operational change; revert behavior with a newer revision rather than rolling revision backward. Verify both the deployed JSON and the app's actual fetched/cache state after a change; a Git commit alone does not establish CDN propagation.

## Pro tools (native app 1.7.0 / code 10)

`features.pro_macros`, `features.pro_custom_remote` and `features.pro_widgets` are independent kill switches for features compiled into the app. They do not grant Pro, install code or supply Samsung ownership. Basic TV controls and Restore remain available independently. Scene execution stops if its flag is disabled. The controls open only in app versions that contain the native features; previous clients ignore these additional keys.

Revision4 keeps production advertising disabled, all real ad units empty, minimum supported version1 and update mode none. Latest code10 describes the local build, not a claim that Galaxy Store has published it. No forced update is configured.
