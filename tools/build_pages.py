#!/usr/bin/env python3
"""Generates the text pages (privacy, terms, support, 404) from a shared shell.

Run from the repo root:  python3 tools/build_pages.py
index.html is hand-written and not touched here.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SHELL = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Overvue</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#0a0a0c">
  <link rel="canonical" href="https://overvue.in{path}">
  {robots}
  <meta property="og:title" content="{title} — Overvue">
  <meta property="og:image" content="https://overvue.in/assets/img/og-image.png">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script>(function(){{try{{var t=localStorage.getItem('overvue-theme');if(t==='light'||t==='dark'){{document.documentElement.setAttribute('data-theme',t);}}}}catch(e){{}}}})();</script>
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="i-apple" viewBox="0 0 24 24"><path d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701"/></symbol>
  <symbol id="i-play" viewBox="0 0 24 24"><path d="M22.018 13.298l-3.919 2.218-3.515-3.493 3.543-3.521 3.891 2.202a1.49 1.49 0 0 1 0 2.594zM1.337.924a1.486 1.486 0 0 0-.112.568v21.017c0 .217.045.419.124.6l11.155-11.087L1.337.924zm12.207 10.065l3.258-3.238L3.45.195a1.466 1.466 0 0 0-.946-.179l11.04 10.973zm0 2.067l-11 10.933c.298.036.612-.016.906-.183l13.324-7.54-3.23-3.21z"/></symbol>
  <symbol id="i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol>
  <symbol id="i-moon" viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></symbol>
</svg>
<header class="nav">
  <div class="wrap">
    <a href="/" class="brand" aria-label="Overvue home"><img src="/assets/img/mark.png" alt="" width="26" height="28"> Overvue</a>
    <nav class="nav-links" aria-label="Primary">
      <a href="/#features">Features</a>
      <a href="/support/">Support</a>
      <button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch to light theme"><svg class="sun" aria-hidden="true"><use href="#i-sun"/></svg><svg class="moon" aria-hidden="true"><use href="#i-moon"/></svg></button>
      <a class="btn btn-primary btn-sm" href="/#get">Get the app</a>
    </nav>
  </div>
</header>
<main class="doc">
  <div class="wrap">
{body}
  </div>
</main>
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a href="/" class="brand" aria-label="Overvue home"><img src="/assets/img/mark.png" alt="" width="26" height="28"> Overvue</a>
        <p>Your banks, cards, budgets and the money you've lent or borrowed, in one place. One number you can trust.</p>
        <div class="stores foot-stores" aria-label="Download Overvue">
          <a class="store-badge" href="https://apps.apple.com/app/overvue/id0000000000" target="_blank" rel="noopener" aria-label="Download Overvue on the App Store"><svg aria-hidden="true"><use href="#i-apple"/></svg><span><small>Download on the</small><b>App Store</b></span></a>
          <a class="store-badge" href="https://play.google.com/store/apps/details?id=app.overvue.in" target="_blank" rel="noopener" aria-label="Get Overvue on Google Play"><svg aria-hidden="true"><use href="#i-play"/></svg><span><small>Get it on</small><b>Google Play</b></span></a>
        </div>
      </div>
      <nav class="foot-col" aria-label="Product">
        <h4>Product</h4>
        <a href="/#features">Features</a>
        <a href="/#how">How it works</a>
        <a href="/#privacy">Privacy</a>
        <a href="/#get">Get the app</a>
      </nav>
      <nav class="foot-col" aria-label="Help">
        <h4>Help</h4>
        <a href="/support/">Support</a>
        <a href="mailto:support@overvue.in">support@overvue.in</a>
      </nav>
      <nav class="foot-col" aria-label="Legal">
        <h4>Legal</h4>
        <a href="/privacy-policy/">Privacy Policy</a>
        <a href="/terms-of-service/">Terms of Service</a>
      </nav>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Overvue. All rights reserved.</span>
      <span>Apple and the App Store are trademarks of Apple Inc. Google Play is a trademark of Google LLC.</span>
    </div>
  </div>
</footer>
<script src="/assets/js/theme.js"></script>
</body>
</html>
"""

PRIVACY = """    <h1>Privacy Policy</h1>
    <p class="meta">Last updated: 2 October 2026</p>

    <p>Overvue ("we", "us") is a personal finance app that helps you see your net worth, spending and budgets in one place. This policy explains what information the app handles, why, and the choices you have. We have tried to keep it plain and short.</p>

    <h2>Information you give us</h2>
    <ul>
      <li><strong>Account details</strong> — your email address and, if you choose, your name and profile photo. If you sign in with Google or Apple, we receive the basic profile information they share with us (such as your name and email address).</li>
      <li><strong>Financial entries you add</strong> — account names and balances, credit cards, expenses, income, budgets, money lent or borrowed, reminders, notes and to-dos. Overvue is manual-entry: you decide what to add.</li>
      <li><strong>Preferences</strong> — such as your default currency and appearance (dark, light or system).</li>
      <li><strong>Messages to support</strong> — anything you send us at support@overvue.in.</li>
    </ul>

    <h2>What we do not collect</h2>
    <ul>
      <li>We never ask for your bank or card passwords, PINs, or one-time codes, and we do not connect to your bank accounts.</li>
      <li>We do not use advertising or third-party analytics SDKs in the app.</li>
      <li>We do not sell your personal data.</li>
    </ul>

    <h2>How we use information</h2>
    <ul>
      <li>To provide the app — signing you in, storing your entries, and syncing them across your devices.</li>
      <li>To calculate and display your net worth, insights and budget progress.</li>
      <li>To respond to support requests and keep the service secure.</li>
    </ul>

    <h2>Where your data is stored</h2>
    <p>Overvue uses Google Firebase (Firebase Authentication, Cloud Firestore and Cloud Storage) to run the service. Your data is stored under your user account and is protected by access rules so that only you can read and write it. Google processes this data on our behalf under its own terms and privacy commitments. Data may be processed in countries other than your own.</p>

    <h2>Permissions</h2>
    <p>The app needs internet access to sync. If you choose to set a profile photo, the app asks to access a photo from your library; it only reads the photo you select.</p>

    <h2>Sharing</h2>
    <p>We do not share your personal data with third parties except (a) the service providers that host the app, as described above, and (b) where required by law or to protect rights and safety.</p>

    <h2>Retention and deletion</h2>
    <p>We keep your data for as long as your account exists. To delete your account and the data associated with it, email <a href="mailto:support@overvue.in">support@overvue.in</a> from the address you signed up with and we will process the request. You can also edit or delete individual entries inside the app at any time.</p>

    <h2>Security</h2>
    <p>We use industry-standard safeguards, including encrypted connections and per-user access rules. No method of storage or transmission is completely secure, so we cannot guarantee absolute security — please also protect your device and sign-in credentials.</p>

    <h2>Children</h2>
    <p>Overvue is not directed to children under 13, and we do not knowingly collect their personal information.</p>

    <h2>Your rights</h2>
    <p>Depending on where you live, you may have rights to access, correct, export or delete your personal data, or to withdraw consent. Contact us at <a href="mailto:support@overvue.in">support@overvue.in</a> and we will help.</p>

    <h2>Changes to this policy</h2>
    <p>If we change this policy, we will update the date above and, for material changes, notify you in the app or by email.</p>

    <h2>Contact</h2>
    <p>Questions about privacy? Email <a href="mailto:support@overvue.in">support@overvue.in</a>.</p>
"""

TERMS = """    <h1>Terms of Service</h1>
    <p class="meta">Last updated: 2 October 2026</p>

    <p>These terms govern your use of the Overvue app and website at overvue.in. By creating an account or using Overvue you agree to them. If you do not agree, please do not use the service.</p>

    <h2>The service</h2>
    <p>Overvue is a personal finance tool that lets you record accounts, transactions, budgets and loans, and view your net worth and related insights. It runs on information you enter yourself.</p>

    <h2>Not financial advice</h2>
    <p>Overvue is for personal organisation and information only. Nothing in the app — including insights, health metrics or projections — is financial, investment, tax or legal advice. Figures depend on what you enter, so please verify them against your official bank and card statements before relying on them for decisions.</p>

    <h2>Your account</h2>
    <ul>
      <li>You must provide accurate information and keep your sign-in credentials secure.</li>
      <li>You are responsible for activity under your account.</li>
      <li>You must be at least 13 years old, or the minimum age in your country to use online services, whichever is higher.</li>
    </ul>

    <h2>Acceptable use</h2>
    <p>Do not misuse the service: no attempting to access other users' data, reverse engineering the service beyond what law allows, disrupting or overloading it, or using it for unlawful purposes.</p>

    <h2>Your content</h2>
    <p>You keep ownership of the data you enter. You grant us a limited licence to store and process it solely to operate the service for you, as described in our <a href="/privacy-policy/">Privacy Policy</a>.</p>

    <h2>Availability and changes</h2>
    <p>We work to keep Overvue reliable but do not promise it will be uninterrupted or error-free. We may add, change or remove features, and we may update these terms; continued use after an update means you accept the new terms.</p>

    <h2>Disclaimer and limitation of liability</h2>
    <p>The service is provided "as is" and "as available", without warranties of any kind to the extent permitted by law. To the extent permitted by law, Overvue and its owners are not liable for indirect or consequential losses, or for losses arising from decisions made using information in the app.</p>

    <h2>Termination</h2>
    <p>You may stop using Overvue and request account deletion at any time (see the Privacy Policy). We may suspend or end access for violations of these terms.</p>

    <h2>Governing law</h2>
    <p>These terms are governed by the laws of India, and the courts of India will have jurisdiction, subject to any mandatory consumer rights in your place of residence.</p>

    <h2>Contact</h2>
    <p>Questions about these terms? Email <a href="mailto:support@overvue.in">support@overvue.in</a>.</p>
"""

SUPPORT = """    <h1>Support</h1>
    <p class="meta">We're a small team and we read every message.</p>

    <h2>Contact us</h2>
    <p>Email <a href="mailto:support@overvue.in">support@overvue.in</a> for help, bug reports, feature ideas, or account and data requests. Please include your device model, OS version and app version if you're reporting a problem.</p>

    <h2>Common questions</h2>
    <p><strong>Does Overvue connect to my bank?</strong><br>No. You add balances and transactions yourself, so Overvue never needs your bank credentials.</p>
    <p><strong>How is my net worth calculated?</strong><br>Your liquid balances plus money you've lent, minus debt such as credit card balances and money you've borrowed.</p>
    <p><strong>Can I use light mode?</strong><br>Yes. Dark mode is the default; switch to light or system appearance in Settings.</p>
    <p><strong>How do I delete my account and data?</strong><br>Email <a href="mailto:support@overvue.in">support@overvue.in</a> from your sign-up address and we'll remove your account and its data. See the <a href="/privacy-policy/">Privacy Policy</a> for details.</p>
    <p><strong>My profile photo won't load.</strong><br>Check your connection and try re-selecting the photo in Settings → Profile. If it persists, email us.</p>
"""

NOTFOUND = """    <h1>Page not found</h1>
    <p class="meta">That page doesn't exist — or it moved.</p>
    <p><a href="/">Back to the Overvue home page</a></p>
"""

PAGES = [
    ("privacy-policy/index.html", "/privacy-policy/", "Privacy Policy", "How Overvue handles your information.", PRIVACY, True),
    ("terms-of-service/index.html", "/terms-of-service/", "Terms of Service", "The terms for using Overvue.", TERMS, True),
    ("support/index.html", "/support/", "Support", "Get help with the Overvue app.", SUPPORT, True),
    ("404.html", "/404.html", "Page not found", "Page not found.", NOTFOUND, False),
]

for out, path, title, desc, body, indexable in PAGES:
    robots = "" if indexable else '<meta name="robots" content="noindex">'
    target = ROOT / out
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(SHELL.format(title=title, desc=desc, path=path, robots=robots, body=body), encoding="utf-8")
    print("wrote", out)
