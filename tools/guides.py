"""Money guides for overvue.in/guides/: plain-language articles on the questions
people search for, each pointing to the Overvue feature that helps.

Each guide: slug, title (the <title>, kept under ~50 chars), h1, desc (meta
description, under 160 chars), lede, feature (slug of a FEATURES page), and
body (HTML: h2 sections, paragraphs, lists). Read by build_pages.py.
"""

PUBLISHED = "2026-10-03"

GUIDES = [
    {
        "slug": "how-to-calculate-net-worth",
        "title": "How to Calculate Your Net Worth",
        "h1": "How to calculate your net worth, step by step",
        "desc": "Net worth is what you own minus what you owe. Here's how to add up your assets and debts, with a worked example and what to do with the number.",
        "lede": "Your net worth is the single number that says where you stand: everything you own, minus everything you owe. It takes about fifteen minutes to work out.",
        "feature": "net-worth-tracker",
        "body": """
<h2>The formula</h2>
<p><strong>Net worth = assets − liabilities.</strong> Assets are what you own that has a money value. Liabilities are what you owe to someone else. If the result is positive you own more than you owe; if it's negative, your debts are bigger than your assets for now.</p>

<h2>Step 1: List your assets</h2>
<ul>
  <li><strong>Cash and bank balances</strong>: savings and current accounts, cash at home, wallets.</li>
  <li><strong>Investments</strong>: mutual funds, stocks, fixed deposits, retirement accounts, at today's value.</li>
  <li><strong>Money owed to you</strong>: loans you've given friends or family that you expect back.</li>
  <li><strong>Big possessions</strong> (optional): a home or car at a realistic resale value. Many people leave these out and track only liquid net worth, which is easier to keep current.</li>
</ul>

<h2>Step 2: List your liabilities</h2>
<ul>
  <li><strong>Credit card balances</strong>: the full amount outstanding, not just the minimum due.</li>
  <li><strong>Loans</strong>: home, car, education and personal loans, at the principal still owed.</li>
  <li><strong>Money you've borrowed</strong> from friends or family.</li>
</ul>

<h2>Step 3: Subtract</h2>
<p>Add up each list and subtract liabilities from assets. Here's a simple example:</p>
<ul>
  <li>Bank accounts ₹1,80,000 + investments ₹3,25,000 + lent to a friend ₹5,000 = <strong>₹5,10,000 in assets</strong></li>
  <li>Credit cards ₹24,950 + borrowed ₹2,000 = <strong>₹26,950 in liabilities</strong></li>
  <li>Net worth = ₹5,10,000 − ₹26,950 = <strong>₹4,83,050</strong></li>
</ul>

<h2>What to do with the number</h2>
<p>A single snapshot matters less than the direction it moves. Work it out again each month, on the same day, and watch the trend. If it's rising, your saving and investing are outpacing your spending and debt. If it's flat or falling, look at the two levers: spend less than you earn, and pay down high-interest debt such as credit card balances first.</p>
<p>Don't compare your number with other people's. Net worth depends heavily on age, income and where you live. The useful comparison is with yourself a month or a year ago.</p>

<h2>Common mistakes</h2>
<ul>
  <li>Counting the credit limit instead of the balance you owe.</li>
  <li>Using a home's purchase price rather than what it would sell for today.</li>
  <li>Forgetting small debts and IOUs, which add up.</li>
  <li>Checking too rarely: a yearly calculation hides the habits that move it.</li>
</ul>
""",
    },
    {
        "slug": "how-to-make-a-monthly-budget",
        "title": "How to Make a Monthly Budget",
        "h1": "How to make a monthly budget you'll actually stick to",
        "desc": "A practical way to set a monthly budget: start from real spending, pick one limit, check your daily pace and adjust. No spreadsheets needed.",
        "lede": "Most budgets fail because they're too detailed to keep up with. A simple one you check every few days beats a perfect one you abandon in week two.",
        "feature": "budget-planner",
        "body": """
<h2>1. Start from what you really spend</h2>
<p>Before setting a limit, look at the last one to three months. Add up what went out on everyday spending: food, transport, shopping, bills, entertainment. This is your honest baseline. A budget set below reality with no plan for how to get there is a wish, not a budget.</p>

<h2>2. Take out the fixed costs</h2>
<p>Rent, loan EMIs, insurance and subscriptions are mostly fixed each month. Note them, and make sure your income covers them plus your savings goal before anything else.</p>

<h2>3. Set one monthly spending limit</h2>
<p>Instead of a dozen category envelopes, start with a single number for everything you spend in a month. It's far easier to keep track of, and it still tells you the one thing you need to know: are you on track or not? You can split it into categories later if one area keeps running away.</p>

<h2>4. Turn it into a daily pace</h2>
<p>Divide what's left by the days left in the month. If you have ₹17,500 left with 11 days to go, your pace is about ₹1,590 a day. That number is much easier to act on than a monthly total: it tells you whether today's dinner out fits.</p>

<h2>5. Check in, don't wait for the month to end</h2>
<p>Glance at your budget every few days. If your spending so far, continued at the same rate, would take you over by month-end, you'll know with time to change course. Waiting for the statement means finding out after the money is gone.</p>

<h2>6. Adjust honestly</h2>
<p>At the end of each month, compare the limit with what you spent. If you're always over, either the limit is unrealistic or one category needs attention. Change one thing at a time.</p>

<h2>Tips that help</h2>
<ul>
  <li>Log spending the same day. Small purchases are the ones you forget.</li>
  <li>Pay yourself first: move savings out on payday, then budget what's left.</li>
  <li>Plan for irregular costs such as birthdays, trips and annual fees with a small amount set aside each month.</li>
</ul>
""",
    },
    {
        "slug": "50-30-20-budget-rule",
        "title": "The 50/30/20 Budget Rule, Explained",
        "h1": "The 50/30/20 budget rule, explained with examples",
        "desc": "The 50/30/20 rule splits take-home pay into needs, wants and savings. How it works, a worked example, and when to adjust the percentages.",
        "lede": "The 50/30/20 rule is a simple starting point for dividing your income: half for needs, nearly a third for wants, and a fifth for savings and debt repayment.",
        "feature": "budget-planner",
        "body": """
<h2>How the rule works</h2>
<p>Take your monthly <strong>take-home pay</strong> (after tax and deductions) and split it three ways:</p>
<ul>
  <li><strong>50% needs</strong>: rent or home loan EMI, groceries, utilities, transport to work, insurance, minimum loan payments.</li>
  <li><strong>30% wants</strong>: eating out, shopping, streaming, travel, hobbies.</li>
  <li><strong>20% savings and debt</strong>: emergency fund, investments, and paying down debt beyond the minimum.</li>
</ul>

<h2>A worked example</h2>
<p>On a take-home pay of ₹80,000 a month:</p>
<ul>
  <li>Needs: ₹40,000</li>
  <li>Wants: ₹24,000</li>
  <li>Savings and extra debt payments: ₹16,000</li>
</ul>

<h2>Needs or wants?</h2>
<p>The line can blur. A basic phone plan is a need; the latest phone on EMI is mostly a want. Groceries are a need; food delivery several times a week is a want. When in doubt, ask whether you'd still pay for it if your income dropped next month.</p>

<h2>When to change the percentages</h2>
<p>The rule is a guide, not a law. In a high-rent city, needs can easily take 60% or more; then trim wants rather than savings if you can. If you have expensive debt such as a credit card balance, pushing the savings-and-debt share above 20% to clear it pays off quickly. Later, as income grows, many people move toward 50/20/30 or save even more.</p>

<h2>Making it stick</h2>
<p>Automate the 20% on payday so it never sits in your spending account. Then treat the remaining needs and wants as your monthly spending limit, and track it as the month goes on so you can see early if you're drifting.</p>
""",
    },
    {
        "slug": "how-to-track-expenses",
        "title": "How to Track Your Expenses",
        "h1": "How to track your expenses: methods that actually work",
        "desc": "Notebook, spreadsheet, bank statements or an app: the main ways to track expenses compared, and the habits that make tracking stick.",
        "lede": "Tracking expenses is the foundation of every other money habit. The best method is the one you'll keep doing, so here's how the common approaches compare.",
        "feature": "expense-tracker",
        "body": """
<h2>Why track at all?</h2>
<p>Most people underestimate what they spend on small, frequent things: coffee, snacks, rides, delivery fees. Tracking for even a month shows where money really goes, and that's usually enough to find a few easy savings.</p>

<h2>The main methods</h2>
<h3>A notebook</h3>
<p>Simple and private, and writing things down makes you notice them. The downside is adding it all up: totals and category breakdowns take manual work.</p>
<h3>A spreadsheet</h3>
<p>Flexible and free, with formulas for totals and charts. But entering data on a laptop at the end of the day is easy to skip, and spreadsheets on a phone are fiddly.</p>
<h3>Reviewing bank and card statements</h3>
<p>No daily effort, but you only see the picture after the month ends, cash spending is missing, and statement descriptions are often cryptic.</p>
<h3>An expense tracker app</h3>
<p>Logging takes seconds on the phone that's already in your hand, and totals, categories and comparisons are done for you. Apps differ in whether they connect to your bank or let you enter spending yourself; manual entry takes a moment more but keeps your bank logins private and makes you more aware of each purchase.</p>

<h2>Habits that make tracking stick</h2>
<ul>
  <li><strong>Log on the spot</strong>, or set a daily reminder at the same time each evening.</li>
  <li><strong>Keep categories few</strong>: groceries, cafes, transport, shopping, bills, entertainment covers most spending.</li>
  <li><strong>Look at the totals weekly.</strong> Tracking only helps if you look at what it tells you.</li>
  <li><strong>Don't aim for perfection.</strong> Missing one coffee doesn't ruin the picture; giving up does.</li>
</ul>

<h2>What to look for after a month</h2>
<p>Check your top three categories, compare with your income to get your savings rate, and look for the days of the week you spend most. One or two changes in your biggest categories will matter more than cutting dozens of small things.</p>
""",
    },
    {
        "slug": "what-is-a-good-savings-rate",
        "title": "What Is a Good Savings Rate?",
        "h1": "What is a good savings rate, and how do you work out yours?",
        "desc": "Your savings rate is the share of income you keep. How to calculate it, what's a good target, and practical ways to raise it.",
        "lede": "Your savings rate tells you more about your financial progress than your salary does. It's the share of your income you keep rather than spend.",
        "feature": "expense-tracker",
        "body": """
<h2>How to calculate it</h2>
<p><strong>Savings rate = (income − spending) ÷ income × 100.</strong></p>
<p>If you took home ₹1,20,000 this month and spent ₹84,000, you saved ₹36,000, a savings rate of 30%. Use take-home income, and count everything you spent, including bills and EMIs.</p>

<h2>What's a good savings rate?</h2>
<ul>
  <li><strong>Below 10%</strong>: a start, but there's little buffer if income drops.</li>
  <li><strong>10–20%</strong>: a solid, common target that builds an emergency fund and long-term investments.</li>
  <li><strong>20–30%</strong>: strong; you're building wealth steadily.</li>
  <li><strong>Above 30%</strong>: excellent, and it shortens the path to big goals considerably.</li>
</ul>
<p>The right number depends on your stage of life, income and costs. A rate that's steady or rising over time matters more than any single month.</p>

<h2>Why it matters so much</h2>
<p>A higher savings rate helps twice: you put more money aside, and you get used to living on less, so you'd need less to cover your expenses later. That's why small, lasting increases are so powerful.</p>

<h2>Ways to raise your savings rate</h2>
<ul>
  <li>Save automatically on payday, before you can spend it.</li>
  <li>Find your top spending category and trim it by 10–20%.</li>
  <li>Cancel subscriptions you rarely use.</li>
  <li>When you get a raise, save at least half of the increase.</li>
  <li>Track it monthly so you can see the effect of each change.</li>
</ul>
""",
    },
    {
        "slug": "keep-track-of-money-lent-to-friends",
        "title": "How to Keep Track of Money Lent to Friends",
        "h1": "How to keep track of money you lend to friends and family",
        "desc": "Lending money to friends is easy; remembering who owes what isn't. Simple ways to record loans and IOUs and ask for repayment without the awkwardness.",
        "lede": "Covering a friend's share of a trip or lending a relative some cash is normal. Forgetting about it, or arguing later about the amount, is what strains relationships.",
        "feature": "lend-borrow-tracker",
        "body": """
<h2>Write it down the same day</h2>
<p>Note who, how much, the date and what it was for. A record made at the time settles any later doubt about the amount, and it's far less awkward than relying on memory a month later.</p>

<h2>Agree on repayment up front</h2>
<p>A light "pay me back whenever after payday" sets an expectation without being formal. For larger amounts, agreeing on a date or a few instalments helps both sides. Sending a quick message confirming the amount gives you both a record.</p>

<h2>Count it in your finances</h2>
<p>Money you've lent is still yours, so it belongs in your net worth as an asset until it's repaid. Money you've borrowed is a debt and should be subtracted. Keeping both in view stops a friendly loan from silently distorting your picture of your own money.</p>

<h2>Asking for it back</h2>
<ul>
  <li>Keep it casual and specific: "Hey, just checking on the ₹3,000 from the Goa trip."</li>
  <li>Offer an easy way to pay, such as a UPI ID or bank transfer.</li>
  <li>If someone is struggling, agreeing on smaller instalments is better than silence.</li>
</ul>

<h2>Lend only what you could afford to lose</h2>
<p>The kindest rule for everyone: lend amounts that wouldn't hurt you if repayment took a long time. It keeps the friendship safe either way.</p>
""",
    },
    {
        "slug": "find-and-cancel-unused-subscriptions",
        "title": "How to Find and Cancel Unused Subscriptions",
        "h1": "How to find and cancel the subscriptions you don't use",
        "desc": "Streaming, apps, gym, cloud storage: subscriptions add up quietly. How to find every repeat charge, decide what to keep and stop paying for the rest.",
        "lede": "A few hundred here, a couple of thousand there. Subscriptions are designed to be easy to forget, which is why a yearly audit almost always finds money to save.",
        "feature": "subscription-tracker",
        "body": """
<h2>Step 1: Find every repeat charge</h2>
<ul>
  <li>Go through the last three months of bank and credit card statements and list anything that repeats.</li>
  <li>Check your phone's app store subscriptions page; many in-app subscriptions bill through it.</li>
  <li>Search your email for words like "renewal", "subscription" and "receipt".</li>
  <li>Don't forget yearly plans: cloud storage, software, memberships and annual card fees renew once and are easy to miss.</li>
</ul>

<h2>Step 2: See the real cost</h2>
<p>Convert everything to a monthly and a yearly figure. A ₹649 monthly plan is nearly ₹7,800 a year; seeing the annual total changes how you weigh it.</p>

<h2>Step 3: Decide what stays</h2>
<p>For each one, ask: did I use it in the last month? Would I sign up again today at this price? Is there a cheaper plan, or one I'm paying for twice (two music services, overlapping cloud storage)?</p>

<h2>Step 4: Cancel, then confirm</h2>
<p>Cancel from the service's account settings or your app store, not just by deleting the app. Note the date your access ends, and check your next statement to confirm the charge stopped.</p>

<h2>Step 5: Stay on top of renewals</h2>
<p>Keep a list of what you pay for, with each next billing date, and set a reminder a day or two before each renewal. That moment is when you can still decide to cancel. Rotating streaming services, subscribing to one at a time for the show you want, is another easy saving.</p>
""",
    },
    {
        "slug": "credit-card-statement-date-vs-due-date",
        "title": "Credit Card Statement Date vs Due Date",
        "h1": "Credit card statement date vs due date: what's the difference?",
        "desc": "The statement date closes your billing cycle; the due date is when payment is due. How they work together and how to avoid interest and late fees.",
        "lede": "Two dates on every credit card bill decide whether you pay interest. Knowing which is which is the easiest way to use a card without it costing you.",
        "feature": "credit-card-tracker",
        "body": """
<h2>The statement date</h2>
<p>The statement date (also called the billing date) is when your card's billing cycle closes. Everything you spent during the cycle is added up into a statement showing the total amount due and the minimum amount due.</p>

<h2>The due date</h2>
<p>The payment due date comes some days after the statement date; the gap is set by your card issuer and shown on the statement. Pay the <strong>total amount due</strong> by this date and you normally pay no interest on those purchases.</p>

<h2>Why the gap matters</h2>
<p>A purchase made just after the statement date won't appear until the next statement, so it has the longest time before payment is due. A purchase made just before the statement date is due soonest. You don't need to time purchases, but knowing this explains why your bill can look different from what you expect.</p>

<h2>Total due vs minimum due</h2>
<p>Paying only the minimum keeps the account in good standing, but the unpaid balance usually starts attracting interest, often at a high rate, and new purchases may lose their interest-free period. Whenever you can, pay the total amount due.</p>

<h2>How to never miss a due date</h2>
<ul>
  <li>Keep every card's due date in one place, especially if you have several cards with different cycles.</li>
  <li>Set a reminder a few days before each due date.</li>
  <li>Consider an auto-debit for at least the minimum due, as a safety net, and pay the rest manually.</li>
  <li>Track your card balances alongside your bank balances so you know the money is there.</li>
</ul>
<p class="note">Rules, grace periods and fees vary by card and issuer. Check your card's terms for the exact details.</p>
""",
    },
    {
        "slug": "how-big-should-an-emergency-fund-be",
        "title": "How Big Should Your Emergency Fund Be?",
        "h1": "How big should your emergency fund be?",
        "desc": "An emergency fund covers job loss, medical bills and urgent repairs. How much to keep, where to keep it and how to build it month by month.",
        "lede": "An emergency fund is money set aside for the unexpected: a job loss, a medical bill, an urgent repair. It's what stops a bad month from turning into debt.",
        "feature": "net-worth-tracker",
        "body": """
<h2>The usual guideline</h2>
<p>A common rule of thumb is <strong>three to six months of essential expenses</strong>. Essentials are what you'd still have to pay if your income stopped: rent or EMI, groceries, utilities, insurance, transport and minimum loan payments, not your full spending.</p>

<h2>When to aim higher or lower</h2>
<ul>
  <li><strong>Aim higher</strong> (six months or more) if your income is irregular, you're self-employed, you're the only earner, or you support dependants.</li>
  <li><strong>Three months may be enough</strong> if you have a stable job, a second household income and few fixed commitments.</li>
</ul>

<h2>Work out your number</h2>
<p>Add up a month of essentials. Say ₹45,000. Three months is ₹1,35,000; six months is ₹2,70,000. Pick a target in that range that fits your situation.</p>

<h2>Where to keep it</h2>
<p>The fund needs to be safe and quick to reach, not invested for growth. A separate savings account or another low-risk option you can access within a day or two works well. Keeping it apart from your everyday account makes it less tempting to dip into.</p>

<h2>Building it</h2>
<ul>
  <li>Start with a first milestone, such as one month of essentials.</li>
  <li>Set up an automatic transfer on payday, even a small one.</li>
  <li>Put windfalls such as bonuses or tax refunds toward it.</li>
  <li>If you use it, refill it before restarting other goals.</li>
</ul>
<p>Watching your liquid balance in your net worth each month makes progress visible, and that's motivating.</p>
""",
    },
    {
        "slug": "sinking-funds",
        "title": "Sinking Funds: Save for Trips and Big Bills",
        "h1": "Sinking funds: how to save for trips, birthdays and big bills",
        "desc": "A sinking fund spreads a known future cost over the months before it. How to set one up for trips, gifts, annual fees and other dated expenses.",
        "lede": "Most \"surprise\" expenses aren't surprises at all: birthdays, festivals, insurance renewals and holidays come round on dates you already know. A sinking fund turns them into small monthly amounts.",
        "feature": "event-countdown",
        "body": """
<h2>What a sinking fund is</h2>
<p>A sinking fund is money you set aside a little at a time for a specific cost on a known future date. Unlike an emergency fund, which is for the unexpected, a sinking fund is for things you can see coming.</p>

<h2>How to set one up</h2>
<ol>
  <li><strong>List upcoming costs with dates</strong>: a trip in four months, a family birthday, a yearly insurance premium, festival spending, a car service.</li>
  <li><strong>Estimate each amount.</strong></li>
  <li><strong>Divide by the months left.</strong> A ₹24,000 trip in four months needs ₹6,000 a month.</li>
  <li><strong>Set the money aside each payday</strong>, in a separate account or clearly earmarked.</li>
</ol>

<h2>Common things to save for</h2>
<ul>
  <li>Trips and holidays</li>
  <li>Birthdays, anniversaries and festival gifts</li>
  <li>Annual subscriptions, memberships and card fees</li>
  <li>Insurance premiums and taxes</li>
  <li>Planned repairs, a new phone or laptop</li>
</ul>

<h2>Keep the dates in view</h2>
<p>The hardest part is remembering what's coming. Keep one list of dated events with a countdown to each, and review it when you plan your monthly budget. Seeing "Goa trip in 120 days" makes it obvious how much to put aside this month.</p>

<h2>Why it works</h2>
<p>Spreading costs evens out your months, so a big bill doesn't wreck your budget or end up on a credit card. It also makes spending on planned treats guilt-free, because the money was set aside for exactly that.</p>
""",
    },
]
