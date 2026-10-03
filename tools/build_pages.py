#!/usr/bin/env python3
"""Generates the text pages (privacy, terms, support, FAQ, 404), the feature pages, the guides (tools/guides.py) and sitemap.xml from a shared shell.

Run from the repo root:  python3 tools/build_pages.py
index.html is hand-written and not touched here.
"""
from datetime import date
from pathlib import Path

from guides import GUIDES, PUBLISHED

ROOT = Path(__file__).resolve().parent.parent

SHELL = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#081316">
  <link rel="canonical" href="https://overvue.in{path}">
  {robots}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Overvue">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://overvue.in{path}">
  <meta property="og:image:alt" content="Overvue personal finance app">
  <meta property="og:locale" content="en_IN">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{full_title}">
  <meta name="twitter:description" content="{desc}">
  <meta property="og:image" content="https://overvue.in/assets/img/og-image.png">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script>(function(){{try{{var t=localStorage.getItem('overvue-theme');if(t==='light'||t==='dark'){{document.documentElement.setAttribute('data-theme',t);}}}}catch(e){{}}}})();</script>
  <link rel="stylesheet" href="/assets/css/style.css">
{schema}</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="i-apple" viewBox="0 0 24 24"><path d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701"/></symbol>
  <symbol id="i-play" viewBox="0 0 24 24"><path d="M22.018 13.298l-3.919 2.218-3.515-3.493 3.543-3.521 3.891 2.202a1.49 1.49 0 0 1 0 2.594zM1.337.924a1.486 1.486 0 0 0-.112.568v21.017c0 .217.045.419.124.6l11.155-11.087L1.337.924zm12.207 10.065l3.258-3.238L3.45.195a1.466 1.466 0 0 0-.946-.179l11.04 10.973zm0 2.067l-11 10.933c.298.036.612-.016.906-.183l13.324-7.54-3.23-3.21z"/></symbol>
  <symbol id="i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol>
  <symbol id="i-moon" viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></symbol>
</svg>
<header class="nav">
  <div class="wrap">
    <a href="/" class="brand" aria-label="Overvue home"><img src="/assets/img/mark.png" alt="" width="28" height="28"> Overvue</a>
    <nav class="nav-links" aria-label="Primary">
{nav}
      <button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch to light theme"><svg class="sun" aria-hidden="true"><use href="#i-sun"/></svg><svg class="moon" aria-hidden="true"><use href="#i-moon"/></svg></button>
      <a class="btn btn-primary btn-sm" href="/#get">Get the app</a>
    </nav>
  </div>
</header>
{main}
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a href="/" class="brand" aria-label="Overvue home"><img src="/assets/img/mark.png" alt="" width="28" height="28"> Overvue</a>
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
{foot_features}
      <nav class="foot-col" aria-label="Help">
        <h4>Help</h4>
        <a href="/guides/">Money guides</a>
        <a href="/faq/">FAQ</a>
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

import json
from html import escape

# Feature pages: one per search intent. Each gets its own title, description, FAQ (FAQPage schema) and breadcrumb.
FEATURES = [
    {
        "slug": "net-worth-tracker", "nav": "Net worth tracker", "art": "welcome",
        "title": "Net Worth Tracker App",
        "desc": "Track your net worth in one place. Overvue adds up your bank balances and money lent, subtracts card debt and loans, and shows the trend over time.",
        "h1": "A net worth tracker that gives you one number you can trust",
        "lede": "Overvue adds up everything you own and subtracts everything you owe, so you always know what you're actually worth today, not just what's sitting in one account.",
        "sections": [
            ("How Overvue calculates your net worth", "<p>Your net worth is your liquid balances plus money you've lent, minus debt such as credit card balances and money you've borrowed. Overvue shows the total as a hero number on the Home screen and splits it into liquid cash, money lent and debt, so you can see what's moving it.</p>"),
            ("Watch your net worth over time", "<p>A trend chart tracks how your net worth changes month to month, with the change shown in both amount and percentage. It's the quickest way to see whether you're really getting ahead.</p>"),
            ("No bank logins needed", "<p>Overvue is manual-entry. You add your accounts and balances yourself, so the app never asks for bank passwords, card PINs or one-time codes.</p>"),
        ],
        "ticks": ["Net worth as a single hero number", "Breakdown into liquid cash, money lent and debt", "Month-over-month trend chart", "Works with any default currency"],
        "faq": [
            ("What is a net worth tracker?", "A net worth tracker adds up what you own (cash, bank balances, money owed to you) and subtracts what you owe (credit card balances, loans) to give you one figure for your overall financial position."),
            ("Does Overvue connect to my bank to track net worth?", "No. You enter balances yourself, so Overvue never needs your bank credentials."),
            ("Does money I've lent count toward my net worth?", "Yes. Money you've lent counts as an asset, and money you've borrowed counts as debt."),
        ],
    },
    {
        "slug": "expense-tracker", "nav": "Expense tracker", "art": "spending",
        "title": "Expense Tracker App",
        "desc": "Log expenses and income in a couple of taps, see spending by category, compare with last month and track your savings rate with Overvue.",
        "h1": "An expense tracker that explains where your money went",
        "lede": "Log an expense or income in a couple of taps from the + button, and Overvue turns it into clear stats: spending by category, trends against last month and your savings rate.",
        "sections": [
            ("Log spending in seconds", "<p>Tap +, enter the amount, pick a category and the account it came from. Expenses, income and card payments all go through the same quick flow, and your balances update instantly.</p>"),
            ("Spending by category", "<p>The Stats screen breaks down where your money went this month by category, so you can spot the food delivery habit or the subscription you forgot about.</p>"),
            ("Trends and savings rate", "<p>Compare this month with last month and see your savings rate, the share of your income you kept. Turn on Overvue AI if you'd like short notes on what changed.</p>"),
            ("A daily nudge", "<p>An optional daily reminder prompts you to log the day's spending, so your numbers stay accurate without effort.</p>"),
        ],
        "ticks": ["Expenses, income and card payments in one flow", "Spending by category", "Month-over-month comparison", "Savings rate", "Optional daily logging reminder"],
        "faq": [
            ("Is Overvue a free expense tracker?", "Overvue is launching on iPhone and Android. Check the App Store or Google Play listing for current pricing."),
            ("Can I track income as well as expenses?", "Yes. You can log income alongside expenses, and Overvue uses both to work out your savings rate."),
            ("Does Overvue read my SMS or bank statements?", "No. You log transactions yourself; Overvue doesn't read your messages or connect to your bank."),
        ],
    },
    {
        "slug": "budget-planner", "nav": "Budget planner", "art": "budget",
        "title": "Monthly Budget Planner App",
        "desc": "Set one monthly budget, see what's left to spend per day and get a month-end forecast so overspending never sneaks up on you.",
        "h1": "A monthly budget planner that warns you early",
        "lede": "Set one monthly spending limit and Overvue keeps score. The bar turns from teal to amber to red as you spend, and a forecast shows where the month will land.",
        "sections": [
            ("One simple monthly limit", "<p>No envelopes to juggle. Set a single monthly budget and Overvue tracks every expense against it, showing how much you've spent and the percentage used.</p>"),
            ("Left to spend, per day", "<p>See how much is left this month and what that means per day for the days remaining, so you know exactly what today's budget is.</p>"),
            ("Month-end spending forecast", "<p>Based on your current daily pace, Overvue projects your month-end spend and tells you whether you're on track to stay under budget, and by how much.</p>"),
        ],
        "ticks": ["One monthly spending limit, tracked daily", "Left to spend and your per-day pace", "Month-end forecast from your current spending", "Colour-coded progress from teal to amber to red"],
        "faq": [
            ("How does the budget forecast work?", "Overvue takes how much you've spent so far this month, works out your daily pace, and projects it to the end of the month."),
            ("Can I change my budget mid-month?", "Yes. You can edit your monthly limit at any time and the progress and forecast update straight away."),
        ],
    },
    {
        "slug": "lend-borrow-tracker", "nav": "Lend & borrow tracker", "art": "lend",
        "title": "Money Lent & Borrowed Tracker App",
        "desc": "Keep track of money you've lent to friends or borrowed from them. Overvue counts it toward your net worth so nothing slips through.",
        "h1": "Track money you've lent and borrowed, without the awkward reminders",
        "lede": "Lent a friend money for a trip? Borrowed from family? Log it in Overvue and it counts toward your net worth, so you always know who owes whom.",
        "sections": [
            ("Log loans to and from friends", "<p>Record money you've lent or borrowed with the person's name and amount, straight from the + button. Mark repayments as they come in.</p>"),
            ("Counted in your net worth", "<p>Money you've lent is added to your net worth as an asset, and money you've borrowed is subtracted as debt, so your total reflects reality.</p>"),
            ("Never lose track", "<p>Everything sits in one list instead of scattered chat messages, so a forgotten loan doesn't quietly disappear.</p>"),
        ],
        "ticks": ["Money lent and money borrowed in one place", "Counted toward your net worth", "Logged from the same quick + flow", "Synced across your devices"],
        "faq": [
            ("Can I track money I lent to a friend?", "Yes. Log it as money lent and Overvue keeps it in your net worth until it's repaid."),
            ("Does Overvue message the person who owes me?", "No. Your entries are private to your account; Overvue doesn't contact anyone."),
        ],
    },
    {
        "slug": "credit-card-tracker", "nav": "Credit card tracker", "art": "card",
        "title": "Credit Card Bill & Due Date Tracker App",
        "desc": "Keep credit cards next to your bank accounts, track card payments and see when each bill is due with Overvue.",
        "h1": "Keep your credit cards and their due dates in view",
        "lede": "Overvue keeps your credit cards right next to your bank accounts, tracks card spending and payments, and shows when each bill is due.",
        "sections": [
            ("Cards and banks together", "<p>Add savings and current accounts and credit cards through one simple flow. Card balances count as debt in your net worth, so you see your true position.</p>"),
            ("Track card payments", "<p>Log card spending and bill payments as you go. When you pay a card from a bank account, both balances update.</p>"),
            ("Due dates at a glance", "<p>Each card shows when its bill is due, so a missed payment or late fee doesn't catch you out.</p>"),
        ],
        "ticks": ["Credit cards alongside bank accounts", "Card payments tracked", "Bill due dates shown on each card", "Card balances counted as debt"],
        "faq": [
            ("Do I need to link my credit card?", "No. You add the card and its balance yourself; Overvue never asks for card numbers, PINs or passwords."),
            ("Does Overvue remind me about card bills?", "Each card shows its due date in the app, and you can turn on a daily reminder to keep your entries up to date."),
        ],
    },
    {
        "slug": "subscription-tracker", "nav": "Subscription tracker", "art": "bell",
        "title": "Subscription Tracker App",
        "desc": "Track every subscription in one place: see your monthly and yearly cost, what renews in the next 30 days, and get a reminder before each charge.",
        "h1": "A subscription tracker that tells you before you're charged",
        "lede": "Streaming, music, the gym, cloud storage. Overvue adds up every repeat charge, shows what's coming in the next 30 days and reminds you before each one renews.",
        "sections": [
            ("What your subscriptions really cost", "<p>Overvue totals your active subscriptions as a monthly figure and a yearly one, so a handful of small charges can't hide. Monthly and yearly plans are both counted.</p>"),
            ("The next 30 days at a glance", "<p>A timeline shows each upcoming charge from today to 30 days out, and the list groups them into this week and this month, soonest first, with the card or account each one is billed to.</p>"),
            ("A reminder before each charge", "<p>Overvue reminds you before a subscription renews, so you have time to cancel the ones you no longer use. Pause a subscription and it drops out of your totals.</p>"),
        ],
        "ticks": ["Monthly and yearly totals", "Upcoming charges for the next 30 days", "The card or account each one bills to", "A reminder before each renewal", "Pause without deleting"],
        "faq": [
            ("Does Overvue find my subscriptions automatically?", "No. You add each subscription yourself, picking from popular services or entering your own, so Overvue never needs access to your bank or email."),
            ("Can I track yearly subscriptions?", "Yes. Set a subscription to monthly or yearly and Overvue includes it in both the monthly and yearly totals."),
        ],
    },
    {
        "slug": "event-countdown", "nav": "Event countdown", "art": "calendar",
        "title": "Event Countdown App for Trips & Birthdays",
        "desc": "Count down to trips, birthdays, loan end dates and tax deadlines in Overvue. Yearly events roll over on their own, so you never miss one.",
        "h1": "Count down to the dates that matter to your money",
        "lede": "A trip you're saving for, a birthday gift to budget, the month your car loan ends, a tax deadline. Overvue keeps them in one list with the days left to each.",
        "sections": [
            ("Next up, front and centre", "<p>The soonest event sits at the top with a big days-left count, its date and any note you added, like \"flights booked, hotel not yet\".</p>"),
            ("Yearly events roll over", "<p>Mark birthdays, anniversaries and annual deadlines as yearly and Overvue moves them to the next year once the day passes.</p>"),
            ("Plan around what's coming", "<p>Every other event is listed soonest first, so you can see what's ahead and set money aside in good time.</p>"),
        ],
        "ticks": ["Days left to each event", "Yearly events that repeat on their own", "Notes on any event", "Ready-made types like trips, birthdays and loan EMIs"],
        "faq": [
            ("What can I count down to?", "Anything with a date: trips, birthdays, anniversaries, the end of a loan, a tax filing deadline or a goal of your own."),
            ("What happens when an event passes?", "Yearly events move to next year automatically. One-off events move to a Passed list, where you can remove them or set a new date."),
        ],
    },
    {
        "slug": "ai-money-assistant", "nav": "AI money assistant", "art": "ai",
        "title": "AI Money Assistant for Your Finances",
        "desc": "Overvue AI answers questions about your money and writes short notes on your month, from your own data. Off until you turn it on; chats aren't stored.",
        "h1": "An AI money assistant that knows your numbers",
        "lede": "Ask \"Where did my money go this month?\" or \"Can I cover my card bills?\" and get a clear answer worked out from your own accounts, budget and spending.",
        "sections": [
            ("Notes on your month", "<p>With Overvue AI on, the Stats tab adds a few short notes on what changed: a category that's climbing, a good savings month, a habit worth a look. Tap one to ask a follow-up.</p>"),
            ("Ask in plain words", "<p>Type a question or start from a suggested one picked for your month. Answers use your balances, budget, card bills and transactions, and suggest follow-up questions you might want to ask next.</p>"),
            ("Off until you turn it on", "<p>Overvue AI is opt-in. Before it starts, Overvue shows exactly what the AI sees: amounts, dates, categories, notes and account nicknames, never your email, password or card numbers. Chats aren't stored, and you can switch AI off in Settings at any time.</p>"),
            ("Part of Overvue Pro", "<p>Overvue AI is part of Overvue Pro: up to 150 questions a month and fresh insights up to four times a day. Every new account gets all of Pro free for its first 30 days.</p>"),
        ],
        "ticks": ["Short notes on what changed this month", "Answers from your own accounts and budget", "Opt-in, with what it sees spelled out first", "Chats aren't stored", "Free for your first 30 days, then part of Pro"],
        "faq": [
            ("Is Overvue AI on by default?", "No. It stays off until you turn it on, and you can turn it off again in Settings."),
            ("What data does the AI see?", "Your balances, budget and transactions: amounts, dates, categories, notes and account nicknames. Never your email, password or card numbers."),
            ("Are my AI chats saved?", "No. Overvue's AI service reads your data only while answering, and chats aren't stored."),
            ("Can the AI give financial advice?", "It explains your own numbers, but it isn't a financial adviser and answers can be wrong, so check anything important before acting on it."),
        ],
    },
]

GENERAL_FAQ = [
    ("What is Overvue?", "Overvue is a personal finance app for iPhone and Android that shows your real net worth in one place: banks, cards, spending, budgets and money lent or borrowed."),
    ("Does Overvue connect to my bank?", "No. You add balances and transactions yourself, so Overvue never needs your bank credentials."),
    ("How is my net worth calculated?", "Your liquid balances plus money you've lent, minus debt such as credit card balances and money you've borrowed."),
    ("Is my data private?", "Your data is stored under your own account in Google Firebase with access rules so only you can read it. Overvue has no ads and doesn't sell your data."),
    ("Does it work across devices?", "Yes. Your entries sync to your account, so they follow you between phones."),
    ("Can I use a currency other than rupees?", "Yes. Choose your default currency in Settings."),
    ("Is there a light mode?", "Yes. Dark mode is the default; switch to light or system appearance in Settings."),
    ("How do I delete my account?", "Email support@overvue.in from your sign-up address and we'll remove your account and its data."),
]

STORES = """      <div class="stores stores-center" aria-label="Download Overvue">
        <a class="store-badge" href="https://apps.apple.com/app/overvue/id0000000000" target="_blank" rel="noopener" aria-label="Download Overvue on the App Store"><svg aria-hidden="true"><use href="#i-apple"/></svg><span><small>Download on the</small><b>App Store</b></span></a>
        <a class="store-badge" href="https://play.google.com/store/apps/details?id=app.overvue.in" target="_blank" rel="noopener" aria-label="Get Overvue on Google Play"><svg aria-hidden="true"><use href="#i-play"/></svg><span><small>Get it on</small><b>Google Play</b></span></a>
      </div>"""

def art(name, cls="art"):
    return (f'<img class="{cls} art-dark" src="/assets/illustrations/{name}-dark.svg" alt="" width="168" height="126">'
            f'<img class="{cls} art-light" src="/assets/illustrations/{name}-light.svg" alt="" width="168" height="126">')

def nav_html(current):
    items = "\n".join(
        f'          <a href="/{f["slug"]}/"{" aria-current=\"page\"" if current == f["slug"] else ""}>{escape(f["nav"])}</a>'
        for f in FEATURES)
    return f"""      <div class="nav-menu">
        <a href="/features/" class="nav-menu-btn" aria-haspopup="true">Features</a>
        <div class="nav-menu-panel">
{items}
          <a href="/features/" class="all">All features</a>
        </div>
      </div>
      <a href="/guides/"{" aria-current=\"page\"" if current.startswith("guides") else ""}>Guides</a>
      <a href="/faq/">FAQ</a>"""

FOOT_FEATURES = '      <nav class="foot-col" aria-label="Features">\n        <h4>Features</h4>\n' + "\n".join(
    f'        <a href="/{f["slug"]}/">{escape(f["nav"])}</a>' for f in FEATURES) + "\n      </nav>"

def ld(obj):
    return '  <script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>\n"

def faq_ld(faq):
    return ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})

def crumbs_ld(*trail):
    return ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": "https://overvue.in" + u} for i, (n, u) in enumerate(trail)]})

def faq_html(faq):
    return "\n".join(f'      <details class="faq-item"><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in faq)

def cta():
    return f"""<section class="feat-cta">
  <div class="wrap">
    <div class="cta-box">
      <h2>Know where you stand.</h2>
      <p>Overvue is launching on iPhone and Android.</p>
{STORES}
    </div>
  </div>
</section>"""

def doc_main(body):
    return f'<main class="doc">\n  <div class="wrap">\n{body}\n  </div>\n</main>'

def guide_links(f):
    mine = [g for g in GUIDES if g["feature"] == f["slug"]]
    if not mine:
        return ""
    items = "\n".join(f'        <li><a href="/guides/{g["slug"]}/">{escape(g["h1"])}</a></li>' for g in mine)
    return f"      <h2>Guides</h2>\n      <ul>\n{items}\n      </ul>"

def feature_main(f):
    secs = "\n".join(f"      <h2>{escape(h)}</h2>\n      {b}" for h, b in f["sections"])
    ticks = "\n".join(f"        <li>{escape(t)}</li>" for t in f["ticks"])
    related = "\n".join(
        f'      <a class="card rel" href="/{o["slug"]}/">{art(o["art"])}<h3>{escape(o["nav"])}</h3><p>{escape(o["desc"])}</p></a>'
        for o in FEATURES if o is not f)
    return f"""<main>
<section class="feat-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/features/">Features</a> / <span>{escape(f["nav"])}</span></nav>
    {art(f["art"], "feat-art")}
    <h1>{escape(f["h1"])}</h1>
    <p class="lede">{escape(f["lede"])}</p>
  </div>
</section>
<section class="doc feat-body">
  <div class="wrap">
{secs}
      <ul class="ticks">
{ticks}
      </ul>
      <h2>Frequently asked questions</h2>
{faq_html(f["faq"])}
{guide_links(f)}
  </div>
</section>
<section class="divider">
  <div class="wrap">
    <div class="sec-head"><h2>More from Overvue</h2></div>
    <div class="grid">
{related}
    </div>
  </div>
</section>
{cta()}
</main>"""

def hub_main():
    cards = "\n".join(
        f'      <a class="card rel" href="/{f["slug"]}/">{art(f["art"])}<h3>{escape(f["title"])}</h3><p>{escape(f["desc"])}</p></a>'
        for f in FEATURES)
    return f"""<main>
<section class="feat-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <span>Features</span></nav>
    <h1>Personal finance features, all in one app</h1>
    <p class="lede">Overvue is a net worth tracker, expense tracker, budget planner, subscription tracker and AI money assistant in one place, with no bank logins and no ads.</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="grid">
{cards}
    </div>
  </div>
</section>
{cta()}
</main>"""

FEATURE_BY_SLUG = {f["slug"]: f for f in FEATURES}

def words(html):
    import re
    return len(re.sub(r"<[^>]+>", " ", html).split())

def guide_card(g):
    return (f'      <a class="card rel guide-card" href="/guides/{g["slug"]}/"><span class="eyebrow">{max(1, round(words(g["body"]) / 200))} min read</span>'
            f'<h3>{escape(g["h1"])}</h3><p>{escape(g["desc"])}</p></a>')

def guide_main(g):
    f = FEATURE_BY_SLUG[g["feature"]]
    related = [o for o in GUIDES if o is not g and o["feature"] == g["feature"]] + [o for o in GUIDES if o is not g and o["feature"] != g["feature"]]
    minutes = max(1, round(words(g["body"]) / 200))
    return f"""<main>
<article>
<section class="feat-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/guides/">Guides</a> / <span>{escape(g["title"])}</span></nav>
    <h1>{escape(g["h1"])}</h1>
    <p class="lede">{escape(g["lede"])}</p>
    <p class="guide-meta">{minutes} min read · Updated <time datetime="{PUBLISHED}">{date.fromisoformat(PUBLISHED).strftime("%-d %B %Y")}</time></p>
  </div>
</section>
<section class="doc feat-body guide-body">
  <div class="wrap">
{g["body"].strip()}
    <aside class="guide-cta">
      {art(f["art"], "feat-art")}
      <div><h2>Do this in Overvue</h2><p>{escape(f["lede"])}</p><p><a href="/{f["slug"]}/">See the {escape(f["nav"].lower())}</a></p></div>
    </aside>
    <p class="note">This guide is general information, not financial advice. Your situation may differ, so check the details that apply to you.</p>
  </div>
</section>
</article>
<section class="divider">
  <div class="wrap">
    <div class="sec-head"><h2>More money guides</h2></div>
    <div class="grid">
{chr(10).join(guide_card(o) for o in related[:3])}
    </div>
  </div>
</section>
{cta()}
</main>"""

def guides_hub():
    return f"""<main>
<section class="feat-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <span>Guides</span></nav>
    <h1>Money guides</h1>
    <p class="lede">Plain-language guides to budgeting, tracking spending, net worth, credit cards and saving. Short, practical and free.</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="grid">
{chr(10).join(guide_card(g) for g in GUIDES)}
    </div>
  </div>
</section>
{cta()}
</main>"""

def article_ld(g):
    return ld({"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"],
               "datePublished": PUBLISHED, "dateModified": PUBLISHED, "inLanguage": "en-IN",
               "mainEntityOfPage": f"https://overvue.in/guides/{g['slug']}/",
               "image": "https://overvue.in/assets/img/og-image.png",
               "author": {"@type": "Organization", "name": "Overvue", "url": "https://overvue.in/"},
               "publisher": {"@type": "Organization", "name": "Overvue", "logo": {"@type": "ImageObject", "url": "https://overvue.in/assets/img/apple-touch-icon.png"}}})

FAQ_BODY = "    <h1>Frequently asked questions</h1>\n    <p class=\"meta\">Quick answers about the Overvue personal finance app.</p>\n" + faq_html(GENERAL_FAQ) + \
    '\n    <p style="margin-top:32px">Still stuck? See <a href="/support/">Support</a> or email <a href="mailto:support@overvue.in">support@overvue.in</a>.</p>'

PAGES = [
    ("privacy-policy/index.html", "/privacy-policy/", "Privacy Policy", "How the Overvue personal finance app collects, stores and protects your data. No bank logins, no ads and we never sell your personal information.", doc_main(PRIVACY), True, ""),
    ("terms-of-service/index.html", "/terms-of-service/", "Terms of Service", "The terms for using the Overvue personal finance app and website, including your account, your content and our disclaimer.", doc_main(TERMS), True, ""),
    ("support/index.html", "/support/", "Help & Support", "Get help with the Overvue app: contact support, report a bug, request account deletion or find answers to common questions.", doc_main(SUPPORT), True, ""),
    ("faq/index.html", "/faq/", "Frequently Asked Questions", "Answers to common questions about Overvue: bank connections, net worth, privacy, currencies, sync and account deletion.",
     doc_main(FAQ_BODY), True, faq_ld(GENERAL_FAQ) + crumbs_ld(("Home", "/"), ("FAQ", "/faq/"))),
    ("features/index.html", "/features/", "Personal Finance App Features", "Overvue features: net worth tracker, expense tracker, monthly budget planner, lend and borrow tracker and credit card due dates, in one app.",
     hub_main(), True, crumbs_ld(("Home", "/"), ("Features", "/features/"))),
    ("404.html", "/404.html", "Page not found", "Page not found.", doc_main(NOTFOUND), False, ""),
]
for f in FEATURES:
    path = f"/{f['slug']}/"
    PAGES.append((f"{f['slug']}/index.html", path, f["title"], f["desc"], feature_main(f), True,
                  faq_ld(f["faq"]) + crumbs_ld(("Home", "/"), ("Features", "/features/"), (f["nav"], path))))

PAGES.append(("guides/index.html", "/guides/", "Money Guides: Budgeting, Saving & Net Worth",
              "Free, plain-language guides to budgeting, tracking expenses, net worth, credit cards, subscriptions and saving.",
              guides_hub(), True, crumbs_ld(("Home", "/"), ("Guides", "/guides/"))))
for g in GUIDES:
    path = f"/guides/{g['slug']}/"
    PAGES.append((f"guides/{g['slug']}/index.html", path, g["title"], g["desc"], guide_main(g), True,
                  article_ld(g) + crumbs_ld(("Home", "/"), ("Guides", "/guides/"), (g["title"], path))))

for out, path, title, desc, main, indexable, schema in PAGES:
    robots = "" if indexable else '<meta name="robots" content="noindex">'
    current = path.strip("/")
    target = ROOT / out
    target.parent.mkdir(parents=True, exist_ok=True)
    html = SHELL.format(full_title=escape(f"{title} — Overvue"), desc=escape(desc), path=path, robots=robots, main=main, schema=schema,
                                   nav=nav_html(current), foot_features=FOOT_FEATURES)
    target.write_text(html, encoding="utf-8")
    print("wrote", out)
    # Slashless copy so /support etc. resolve without a redirect; its canonical still points at the slash URL.
    if out.endswith("/index.html"):
        (ROOT / (out[:-len("/index.html")] + ".html")).write_text(html, encoding="utf-8")

# ---------- Sitemap ----------
import re
import subprocess

TODAY = date.today().isoformat()

def lastmod(rel):
    """Date of the last commit that changed a file, or today if it has changes not yet committed.
    Honest dates keep search engines trusting lastmod (the deploy checks out full history for this)."""
    try:
        dirty = subprocess.run(["git", "status", "--porcelain", "--", rel], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        if dirty:
            return TODAY
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", rel], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        return out or TODAY
    except OSError:
        return TODAY

HOME = (ROOT / "index.html").read_text(encoding="utf-8")
SHOTS = list(dict.fromkeys(re.findall(r'data-shot="([a-z0-9-]+)"', HOME)))
home_images = "".join(
    f"    <image:image><image:loc>https://overvue.in/assets/shots/in/{n}-{t}.webp</image:loc></image:image>\n"
    for n in SHOTS for t in ("dark", "light"))
home_images += "    <image:image><image:loc>https://overvue.in/assets/img/og-image.png</image:loc></image:image>\n"

def url(path, rel, images=""):
    return f"  <url>\n    <loc>https://overvue.in{path}</loc>\n    <lastmod>{lastmod(rel)}</lastmod>\n{images}  </url>\n"

def page_images(main):
    arts = list(dict.fromkeys(re.findall(r'/assets/illustrations/([a-z]+)-dark\.svg', main)))
    return "".join(f"    <image:image><image:loc>https://overvue.in/assets/illustrations/{a}-dark.svg</image:loc></image:image>\n" for a in arts[:1])

entries = url("/", "index.html", home_images) + "".join(
    url(p[1], p[0], page_images(p[4])) for p in PAGES if p[5])
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    + entries + "</urlset>\n", encoding="utf-8")
print("wrote sitemap.xml")

# ---------- llms.txt (https://llmstxt.org) ----------
def md(html):
    """Just enough HTML-to-Markdown for the generated pages and guides."""
    t = html
    t = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", t, flags=re.S)
    t = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", t, flags=re.S)
    t = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1", t, flags=re.S)
    t = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", t, flags=re.S)
    t = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f"[{m.group(2)}]({m.group(1) if m.group(1).startswith(('http', 'mailto')) else 'https://overvue.in' + m.group(1)})", t, flags=re.S)
    t = re.sub(r"</p>|<br>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = t.replace("&amp;", "&").replace("&quot;", '"').replace("&#x27;", "'")
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n[ \t]+", "\n", t)
    return re.sub(r"\n{3,}", "\n\n", t).strip()

INTRO = """# Overvue

> Overvue is a personal finance app for iPhone and Android that answers one question: how much money do you actually have right now? It puts bank accounts, credit cards, spending, a monthly budget, subscriptions, upcoming events and money lent or borrowed in one place, and shows your net worth. Entries are added by hand: Overvue never asks for bank logins and does not connect to banks. No ads, and personal data is not sold.

Key facts:

- Platforms: iOS and Android. Website: https://overvue.in. Support: support@overvue.in
- Net worth = liquid balances + money lent - debt (credit card balances and money borrowed)
- Budget: one monthly spending limit, what's left per day, and a month-end forecast from the current pace
- Subscriptions: monthly and yearly totals, charges due in the next 30 days, a reminder before each renewal
- Events: countdowns to trips, birthdays, loan end dates and deadlines; yearly events repeat
- Overvue AI (optional, off until turned on): short notes on the month and answers to questions about your own money. It sees amounts, dates, categories, notes and account nicknames, never email, password or card numbers; chats are not stored. Overvue AI is part of Overvue Pro (up to 150 questions a month); every new account gets all of Pro free for its first 30 days
- Data syncs to the user's own account (Google Firebase) with per-user access rules
- Works in many currencies; banks and card issuers from 27 countries are built in
"""

def link(path, title, desc):
    return f"- [{title}](https://overvue.in{path}): {desc}"

llms = [INTRO,
        "## Features\n",
        *[link(f"/{f['slug']}/", f["title"], f["desc"]) for f in FEATURES],
        "\n## Guides\n",
        *[link(f"/guides/{g['slug']}/", g["h1"][0].upper() + g["h1"][1:], g["desc"]) for g in GUIDES],
        "\n## Help\n",
        link("/faq/", "Frequently asked questions", "Bank connections, net worth, privacy, currencies, sync and account deletion."),
        link("/support/", "Support", "How to contact the team, report a bug or request account deletion."),
        "\n## Optional\n",
        link("/privacy-policy/", "Privacy Policy", "What the app collects, where it is stored and your rights."),
        link("/terms-of-service/", "Terms of Service", "The terms for using Overvue."),
        link("/llms-full.txt", "Full text", "Every feature page, guide and the FAQ as one Markdown file."),
        ""]
(ROOT / "llms.txt").write_text("\n".join(llms), encoding="utf-8")
print("wrote llms.txt")

full = [INTRO, "\n# Features\n"]
for f in FEATURES:
    full.append(f"\n## {f['title']}\n\nURL: https://overvue.in/{f['slug']}/\n\n{f['lede']}\n")
    for h, b in f["sections"]:
        full.append(f"### {h}\n\n{md(b)}\n")
    full.append("\n".join(f"- {t}" for t in f["ticks"]) + "\n")
    full.append("\n".join(f"**{q}** {a}" for q, a in f["faq"]) + "\n")
full.append("\n# Guides\n")
for g in GUIDES:
    full.append(f"\n## {g['h1'][0].upper() + g['h1'][1:]}\n\nURL: https://overvue.in/guides/{g['slug']}/\n\n{g['lede']}\n\n"
                + ("\n" + md(g["body"])).replace("\n### ", "\n#### ").replace("\n## ", "\n### ").strip() + "\n")
full.append("\n# Frequently asked questions\n")
full.append("\n".join(f"**{q}** {a}\n" for q, a in GENERAL_FAQ))
(ROOT / "llms-full.txt").write_text("\n".join(full).replace("\n\n\n", "\n\n"), encoding="utf-8")
print("wrote llms-full.txt")
