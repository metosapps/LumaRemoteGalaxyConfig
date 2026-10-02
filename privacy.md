# Luma Remote — Privacy Policy

## Who we are

Luma Remote (Android package com.luma.smartremote) is provided by the independent Luma Remote developer, publishing on GitHub as metosapps. For privacy questions or requests, contact chennoufo11@gmail.com. Effective date: 2 October 2026.

## TV control and local storage

Luma discovers compatible TVs on your local network and sends commands, pairing information and text you enter to the TV you select. Saved TV names, network addresses, preferences and app favorites are stored on your phone. Pairing tokens, keys and trusted certificate fingerprints are encrypted using Android Keystore. Typed text and pairing credentials are excluded from app diagnostics. Local TV protocols vary: some TVs use encrypted connections and some older TVs use unencrypted local-network protocols. Use a trusted network.

## Diagnostics and permissions

The app keeps a bounded, in-memory diagnostic list of event types and timestamps for connection troubleshooting. It does not automatically upload these diagnostics to the developer. The app requests network-related permissions and, on supported Android versions, local-network permission for TV discovery/control. It includes Samsung’s WRITE_USE_APP_FEATURE_SURVEY permission for Galaxy compatibility; Luma does not add its own Samsung survey event sender. Luma does not request contacts, camera, microphone or precise-location permission. The merged manifest also declares AD_ID and READ_BASIC_PHONE_STATE from Google’s advertising SDK, and FOREGROUND_SERVICE/WAKE_LOCK from bundled Cast/background components.

## Remote configuration and hosted pages

Luma periodically downloads a public JSON configuration over HTTPS from GitHub Pages to obtain ad switches, ad unit IDs, bounded frequency settings, support links, maintenance messages and version guidance. Requests do not contain your saved TVs, pairing credentials, typed text, purchase receipts or a Luma account identifier. GitHub receives ordinary network request information, including IP address and request metadata, when serving configuration or these pages. Configuration is cached locally. Luma has no separate account server or developer analytics upload service.

## Advertising and choices

When advertising is enabled and permitted by Google’s consent SDK, Google AdMob processes information to provide and measure ads and prevent fraud. This may include your IP address (and approximate location derived from it), ad/app-set and applicable account identifiers, ad and app interactions, and app/SDK performance information. Google uses encrypted network transport. Ads may be personalized or limited according to applicable consent, regional rules and SDK settings. These third-party advertising disclosures apply to demo requests as well as live ads; demo mode does not establish live monetization. Privacy choices appear in Settings when required by the consent SDK. You can also manage or delete the advertising ID in Android settings. A verified Pro plan removes ad requests/placements; completing an optional reward ad pauses ads for 30 minutes. Previously processed provider data is not erased by that pause.

## Samsung purchases

Optional one-time Pro, monthly and yearly subscriptions are handled by Samsung Galaxy Store when available and configured. Samsung processes account, checkout and payment information. Luma does not receive your full card details. The app sends a purchase identifier to Samsung’s receipt-verification service and uses product IDs, receipt status, acknowledgment status and subscription end dates to validate ownership. Entitlement and pending-purchase records are encrypted locally and separated from TV credentials. Samsung’s privacy terms and retention rules apply to its transaction records.

## Google Cast and other services

The Google Cast SDK communicates with Google services as needed for Cast discovery/session and media-control functionality. Google’s privacy policy applies. Selected TVs and their manufacturers process commands and text you send under their own privacy practices. Luma is not affiliated with Samsung, LG, Sony, Panasonic, Google or other TV manufacturers.

## Support communications

If you email us, we receive your address, message and any attachments you choose to send, and use them to respond and resolve the issue. Do not send pairing PINs, passwords, card details or unredacted purchase receipts. Email providers also process the message. Support correspondence is retained only as needed to resolve the request and meet applicable obligations; you may request deletion.

## Sharing, retention and deletion

We do not operate a separate service that sells your TV data. Ad providers may process data in ways treated as sharing for advertising under some laws; use the available privacy choices. Forget TV removes that TV’s saved record, pairing credentials and favorites. Clearing Android app storage or uninstalling removes Luma’s local data; Android backup is disabled. Local reward expiry and configuration cache are removed with app storage. Store/provider records follow their own retention and deletion procedures. Contact us for access, correction, deletion, objection or other rights available where you live; we cannot directly erase data held independently by Samsung, Google or GitHub.

## Security and international processing

We use Android app storage, Keystore encryption for sensitive local records, and HTTPS for configuration and receipt checks. No system can guarantee absolute security. Service providers may process data outside your country under their own safeguards and policies. Depending on your location, processing may rely on providing the service, fraud prevention, legal obligations or your consent for advertising where required.

## Children and changes

Luma is a general-purpose TV utility and is not directed at children under 13. We do not knowingly collect children’s personal information through support; contact us if you believe a child has provided it. We may update this policy as the app or providers change, revise the effective date and give additional notice where required.
