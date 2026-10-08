# Smart TV Remote Control — website, Galaxy configuration and policies

This repository is exclusively for **com.luma.smartremote / Galaxy Store**. It contains public configuration and policy pages, not Android source, APKs, signing material, seller credentials or TV/user data.

- [Privacy Policy](https://metosapps.github.io/LumaRemoteGalaxyConfig/privacy.html)
- [Terms of Use](https://metosapps.github.io/LumaRemoteGalaxyConfig/terms.html)
- [Support](https://metosapps.github.io/LumaRemoteGalaxyConfig/)
- [Remote JSON](https://metosapps.github.io/LumaRemoteGalaxyConfig/config_galaxy.json)

Contact: **chennoufo11@gmail.com**. GitHub Pages publishes the root of `main`.

`ads.enabled=false` keeps production advertising off. Debug builds may use official demo IDs only when `ads.test_enabled=true`, the master kill switch is on, and the build permits demo ads. Debug ignores remote live unit IDs. `kill_switches.ads_enabled=false` disables all formats in both modes. Turn individual `placements.*.enabled` off to disable specific inventory. App clients discard cached fullscreen inventory when IDs or placements change.

Before enabling production: confirm this exact signed Galaxy app is live, configure applicable AdMob Privacy & messaging, create each enabled format's own real unit under the package-specific AdMob App ID, obtain production enablement approval, and increment `revision`. A manifest App ID or new SDK/permission requires an app release. Do not reuse other apps' IDs or enable store-independent inventory.

Clients fetch on launch, on foreground after a one-minute request throttle, and every 15 minutes while the process remains alive. Timeout is 12 seconds with five-second connection/read limits, a 64 KiB body limit, no HTTP redirects, strict package/store/schema/publisher checks, and revision rollback rejection. Last-known-good cache is available for up to `cache_ttl_seconds` (six hours by default, maximum one day). Expired/future-dated cache disables ads. Bundled defaults and cached policy still permit normal offline launch unless an explicit cached maintenance/force-update decision applies. Restoring purchases and existing Pro ownership are preserved if new purchases are remotely disabled.

Legacy shared fullscreen frequency stays >=300 seconds and App Open >=600 seconds. Version 1.7.5 adds separate bounded interstitial controls below. Reward duration is compiled: 30 minutes through version 1.7.3 and 120 minutes from version 1.7.4. Native NO_FILL does not block controls. UMP permission and verified Pro always take precedence over remote flags.

`update_mode` is `none`, `soft` or `force`; update URLs must match this exact Galaxy listing. Do not force-update until the target binary is live and available to intended users. `global.maintenance_mode` blocks entry when needed. `links` controls support and policy destinations. `features.reward_offer` controls the voluntary offer. `kill_switches.iap_enabled` only stops new Buy actions; it does not revoke verified benefits or disable Restore.

Run `python3 validate_config.py` before pushing. CI validates the configuration. Increment revision for every operational change; revert behavior with a newer revision rather than rolling revision backward. Verify both the deployed JSON and the app's actual fetched/cache state after a change; a Git commit alone does not establish CDN propagation.

## Pro tools (native app 1.7.0 / code 10)

`features.pro_macros`, `features.pro_custom_remote` and `features.pro_widgets` are independent kill switches for features compiled into the app. They do not grant Pro, install code or supply Samsung ownership. Basic TV controls and Restore remain available independently. Scene execution stops if its flag is disabled. The controls open only in app versions that contain the native features; previous clients ignore these additional keys.

Revision4 keeps production advertising disabled, all real ad units empty, minimum supported version1 and update mode none. Latest code10 describes the local build, not a claim that Galaxy Store has published it. No forced update is configured.

## Public landing page

The root page introduces Smart TV Remote Control, its supported Wi-Fi controls, 20 app languages, compatible TV integrations and optional Remote Pro tools. Seven approved screenshot cards and an actual simulator UI capture are delivered as optimized WebP images. Privacy, Terms and email support remain available at their existing destinations.

The Galaxy Store CTA currently says **Coming to Galaxy Store**. Replace it with the verified public listing link after release. Screenshots are previews; no universal compatibility, verified production billing, live ads or store publication is implied. No trackers, signup forms or external fonts were added.

`index.html`, `style.css` and `site.js` are static; GitHub Pages publishes them directly. Gallery scrolling and FAQ answers remain accessible without JavaScript. Validate layout at desktop and phone widths, verify all local assets and policy links, then run `python3 validate_config.py` before publishing. Website-only updates do not change the configuration revision.

## Pre-release advertising hold (revision 5)

Production and demo advertising are disabled (`ads.enabled=false`, `ads.test_enabled=false`, `kill_switches.ads_enabled=false`). Pro feature switches and IAP remain enabled. Latest code12 identifies the local1.7.2 build; it does not claim Galaxy Store publication. Update mode remains `none`. Enable advertising only after this exact app is live and the publisher authorizes it, with real per-format units and applicable consent configured.

## Production advertising configuration (revision 6, 2026-10-08)

The exact Galaxy listing `com.luma.smartremote` / Content ID `000009310242` was verified as For Sale, and the publisher explicitly requested activation. Six separate production ad units were created and verified in publisher `pub-3289974964220873`, under app `ca-app-pub-3289974964220873~6139840770` (AdMob display name `Remote1Codex`). Both production switches are on; test ads remain off. Pro ownership, consent, lifecycle, reward opt-in and frequency caps still gate ad requests. Existing compatible APKs can fetch this configuration without a new binary.

**Serving is currently blocked by AdMob**, separately from these remote flags: Policy center reports `Disabled ad serving` / `App store verification` for this exact package. The Samsung store link is correct, and AdMob reports that another review was requested on October 8, 2026. No serving approval or real impression has been verified. Eligible clients will use these units after Google clears the issue; do not treat configuration activation as Google approval.

To turn advertisements off, set `kill_switches.ads_enabled=false` and `ads.enabled=false`, increment revision beyond the current deployed value, validate, deploy, and verify the published endpoint. Do not roll back to revision 5.

## Native advertising update 1.7.4 / code 14

The signed local build grants two hours without any ads after a completed optional reward, and creates interstitial opportunities when returning to Devices after at least two navigation actions. The five-minute fullscreen and ten-minute App Open minimums remain. A connected TV no longer blocks advertisements in Devices or Settings; pairing, reconnecting and TV-control screens remain protected. No store upload or publication is implied. Public policies disclose both old and new reward durations. Both AdMob reward units describe one `Ad-free session` so their shared metadata remains correct for old and new app versions; the app explains the version-specific duration before opting in. Configuration revision 6, production unit IDs and update settings are unchanged.

## Interstitial frequency controls (1.7.5 / code 15)

These optional keys under `ads` are read by code 15 and later. Earlier APKs ignore them and retain their existing limits; keep the legacy `fullscreen_interval_seconds` at 300 or more. App Open keeps its ten-minute minimum. No timer schedules interstitials: eligibility is checked only when returning to Devices after navigation. A shorter interval creates more opportunities, not a guaranteed number of impressions.

| Key | Current value | Accepted range / meaning |
|---|---:|---|
| `interstitial_interval_seconds` | 120 | 60–3600; minimum since any fullscreen ad attempt |
| `interstitial_every_n_actions` | 2 | 2–20 navigation actions since the last automatic fullscreen ad |
| `interstitial_max_per_session` | 20 | 1–50 interstitial attempts per app process; resets after process restart |
| `interstitial_initial_grace_seconds` | 120 | 60–600 after starting the process |
| `interstitial_notice_ms` | 1000 | 1000–3000; localized Showing ads notice before a ready interstitial |

For more opportunities set interval to 60, actions to 2 and session limit to 20. For fewer use interval 600, actions 6 and limit 5. To disable use `ads.placements.interstitial.enabled=false`. Consent, verified Pro, two-hour reward pauses, background, pairing, TV controls, dialogs and purchase gates remain mandatory. Google requires at most one interstitial for every two user actions and natural breaks; interval limits are app design choices, not Google guarantees: https://support.google.com/admob/answer/6201362?hl=en .

The notice starts only for already-loaded inventory. It is cancelled on Back/dismissal, background, route change, invalid host, consent/Pro/pairing change or configuration change. The ad is rechecked after the notice; expired opportunities never appear later. No notice is displayed for no-fill. All 20 app languages include this label. Reward pauses remain 120 minutes and are not controlled by these frequency keys.

Edit this package's `config_galaxy.json`, increase `revision`, run `python3 validate_config.py`, commit/push and verify the Pages endpoint. Do not change the App ID, unit IDs or store update fields to tune frequency. The client refreshes on launch/foreground (maximum once per minute) and every 15 minutes during continuous use; publication and client fetching are separate checks. Version code 15 is a local signed release candidate until uploaded/reviewed in Galaxy Store. These controls cannot add this behavior to an older APK.
