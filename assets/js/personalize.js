/* Overvue demo personalisation.
   The mockups are written for India (₹, Indian banks). This script re-skins them for the
   visitor's region: currency + number format, bank and card names, a first name, the greeting
   and live month / due dates. Nothing leaves the browser; region comes from the time zone
   (strongest "where am I" signal), then the browser language. Preview any region with ?region=US. */
(function () {
  var PROFILES = {
    IN: { locale: 'en-IN', currency: 'INR', scale: 1,   unit: 'rupee',  name: 'Aarav',     banks: [['HDFC Bank', 'Savings'], ['SBI', 'Savings'], ['Kotak', 'Current']],            cards: ['HDFC Regalia', 'Axis Flipkart'] },
    US: { locale: 'en-US', currency: 'USD', scale: .1,  unit: 'dollar', name: 'Emma',      banks: [['Chase', 'Checking'], ['Bank of America', 'Savings'], ['Ally', 'Savings']],     cards: ['Amex Gold', 'Chase Sapphire'] },
    GB: { locale: 'en-GB', currency: 'GBP', scale: .1,  unit: 'pound',  name: 'Oliver',    banks: [['Barclays', 'Current'], ['Monzo', 'Current'], ['HSBC', 'Savings']],             cards: ['Amex Platinum', 'Barclaycard'] },
    CA: { locale: 'en-CA', currency: 'CAD', scale: .2,  unit: 'dollar', name: 'Liam',      banks: [['RBC', 'Chequing'], ['TD', 'Savings'], ['Tangerine', 'Savings']],              cards: ['Amex Cobalt', 'Scotia Visa'] },
    AU: { locale: 'en-AU', currency: 'AUD', scale: .2,  unit: 'dollar', name: 'Charlotte', banks: [['CommBank', 'Everyday'], ['ANZ', 'Savings'], ['Up', 'Saver']],                cards: ['Amex Explorer', 'Westpac Altitude'] },
    NZ: { locale: 'en-NZ', currency: 'NZD', scale: .2,  unit: 'dollar', name: 'Sophie',    banks: [['ANZ', 'Everyday'], ['ASB', 'Savings'], ['Kiwibank', 'Savings']],              cards: ['Amex Airpoints', 'ANZ Visa'] },
    SG: { locale: 'en-SG', currency: 'SGD', scale: .2,  unit: 'dollar', name: 'Wei Ling',  banks: [['DBS', 'Savings'], ['OCBC', '360 Account'], ['UOB', 'One Account']],           cards: ['DBS Altitude', 'Citi Rewards'] },
    AE: { locale: 'en-AE', currency: 'AED', scale: .5,  unit: 'dirham', name: 'Omar',      banks: [['Emirates NBD', 'Current'], ['ADCB', 'Savings'], ['Mashreq', 'Savings']],       cards: ['Skywards Card', 'ADCB Touchpoints'] },
    JP: { locale: 'ja-JP', currency: 'JPY', scale: 20,  unit: 'yen',    name: 'Yuki',      banks: [['MUFG', 'Ordinary'], ['SMBC', 'Savings'], ['Rakuten Bank', 'Savings']],          cards: ['Rakuten Card', 'JCB Gold'] },
    DE: { locale: 'de-DE', currency: 'EUR', scale: .1,  unit: 'euro',   name: 'Lena',      banks: [['Sparkasse', 'Giro'], ['N26', 'Current'], ['ING', 'Savings']],                 cards: ['Amex Gold', 'Barclays Visa'] },
    FR: { locale: 'fr-FR', currency: 'EUR', scale: .1,  unit: 'euro',   name: 'Louis',     banks: [['BNP Paribas', 'Current'], ['Boursorama', 'Savings'], ['Revolut', 'Current']],  cards: ['Amex Gold', 'Visa Premier'] },
    ES: { locale: 'es-ES', currency: 'EUR', scale: .1,  unit: 'euro',   name: 'Lucía',     banks: [['CaixaBank', 'Current'], ['BBVA', 'Savings'], ['Revolut', 'Current']],          cards: ['Amex Gold', 'Visa Oro'] },
    IT: { locale: 'it-IT', currency: 'EUR', scale: .1,  unit: 'euro',   name: 'Giulia',    banks: [['Intesa Sanpaolo', 'Current'], ['UniCredit', 'Savings'], ['Fineco', 'Current']], cards: ['Amex Gold', 'Carta Oro'] },
    NL: { locale: 'nl-NL', currency: 'EUR', scale: .1,  unit: 'euro',   name: 'Sanne',     banks: [['ING', 'Current'], ['Rabobank', 'Savings'], ['bunq', 'Current']],               cards: ['Amex Gold', 'ICS Visa'] },
    IE: { locale: 'en-IE', currency: 'EUR', scale: .1,  unit: 'euro',   name: 'Aoife',     banks: [['AIB', 'Current'], ['Bank of Ireland', 'Savings'], ['Revolut', 'Current']],     cards: ['Amex Gold', 'AIB Visa'] }
  };
  // Countries without a full profile: currency + a rough INR→currency factor so the demo stays plausible.
  var CURRENCIES = {
    AT: 'EUR', BE: 'EUR', PT: 'EUR', FI: 'EUR', GR: 'EUR', LU: 'EUR', SK: 'EUR', SI: 'EUR', EE: 'EUR', LV: 'EUR', LT: 'EUR', CY: 'EUR', MT: 'EUR', HR: 'EUR',
    CH: 'CHF', SE: 'SEK', NO: 'NOK', DK: 'DKK', PL: 'PLN', CZ: 'CZK', HU: 'HUF', TR: 'TRY', IL: 'ILS', RU: 'RUB', ZA: 'ZAR', NG: 'NGN', KE: 'KES', EG: 'EGP',
    BR: 'BRL', MX: 'MXN', AR: 'ARS', CN: 'CNY', HK: 'HKD', TW: 'TWD', KR: 'KRW', MY: 'MYR', ID: 'IDR', TH: 'THB', PH: 'PHP', VN: 'VND',
    PK: 'PKR', BD: 'BDT', LK: 'LKR', NP: 'NPR', SA: 'SAR', QA: 'QAR', KW: 'KWD', BH: 'BHD', OM: 'OMR'
  };
  var SCALE = { EUR: .1, CHF: .1, SEK: .11, NOK: .12, DKK: .077, PLN: .045, CZK: .26, HUF: 4.2, TRY: .42, ILS: .043, RUB: 1, ZAR: .21, NGN: 18, KES: 1.5, EGP: .58,
    BRL: .065, MXN: .22, ARS: 12, CNY: .085, HKD: .092, TWD: .37, KRW: 16, MYR: .052, IDR: 185, THB: .4, PHP: .66, VND: 290,
    PKR: 3.3, BDT: 1.4, LKR: 3.5, NPR: 1.6, SAR: .044, QAR: .043, KWD: .0036, BHD: .0044, OMR: .0045 };
  var UNIT = { EUR: 'euro', CHF: 'franc', SEK: 'krona', NOK: 'krone', DKK: 'krone', PLN: 'złoty', CZK: 'koruna', HUF: 'forint', TRY: 'lira', ILS: 'shekel', RUB: 'ruble',
    ZAR: 'rand', NGN: 'naira', KES: 'shilling', EGP: 'pound', BRL: 'real', MXN: 'peso', ARS: 'peso', CNY: 'yuan', HKD: 'dollar', TWD: 'dollar', KRW: 'won',
    MYR: 'ringgit', IDR: 'rupiah', THB: 'baht', PHP: 'peso', VND: 'dong', PKR: 'rupee', BDT: 'taka', LKR: 'rupee', NPR: 'rupee', SAR: 'riyal', QAR: 'riyal',
    KWD: 'dinar', BHD: 'dinar', OMR: 'rial' };
  var GENERIC = { name: 'Alex', banks: [['HSBC', 'Current'], ['Citi', 'Savings'], ['Revolut', 'Current']], cards: ['Amex Gold', 'Visa Signature'] };

  var TZ = {
    'Asia/Kolkata': 'IN', 'Asia/Calcutta': 'IN', 'Europe/London': 'GB', 'Europe/Dublin': 'IE', 'Europe/Berlin': 'DE', 'Europe/Paris': 'FR', 'Europe/Madrid': 'ES',
    'Europe/Rome': 'IT', 'Europe/Amsterdam': 'NL', 'Europe/Brussels': 'BE', 'Europe/Vienna': 'AT', 'Europe/Lisbon': 'PT', 'Europe/Zurich': 'CH', 'Europe/Stockholm': 'SE',
    'Europe/Oslo': 'NO', 'Europe/Copenhagen': 'DK', 'Europe/Helsinki': 'FI', 'Europe/Warsaw': 'PL', 'Europe/Prague': 'CZ', 'Europe/Budapest': 'HU', 'Europe/Athens': 'GR',
    'Europe/Istanbul': 'TR', 'Europe/Moscow': 'RU', 'Asia/Jerusalem': 'IL', 'Asia/Dubai': 'AE', 'Asia/Riyadh': 'SA', 'Asia/Qatar': 'QA', 'Asia/Kuwait': 'KW', 'Asia/Bahrain': 'BH',
    'Asia/Muscat': 'OM', 'Asia/Karachi': 'PK', 'Asia/Dhaka': 'BD', 'Asia/Colombo': 'LK', 'Asia/Kathmandu': 'NP', 'Asia/Singapore': 'SG', 'Asia/Kuala_Lumpur': 'MY',
    'Asia/Jakarta': 'ID', 'Asia/Bangkok': 'TH', 'Asia/Manila': 'PH', 'Asia/Ho_Chi_Minh': 'VN', 'Asia/Saigon': 'VN', 'Asia/Hong_Kong': 'HK', 'Asia/Taipei': 'TW',
    'Asia/Shanghai': 'CN', 'Asia/Seoul': 'KR', 'Asia/Tokyo': 'JP', 'Pacific/Auckland': 'NZ', 'Africa/Johannesburg': 'ZA', 'Africa/Lagos': 'NG', 'Africa/Nairobi': 'KE',
    'Africa/Cairo': 'EG', 'America/Sao_Paulo': 'BR', 'America/Mexico_City': 'MX', 'America/Argentina/Buenos_Aires': 'AR', 'America/Buenos_Aires': 'AR',
    'America/Toronto': 'CA', 'America/Vancouver': 'CA', 'America/Edmonton': 'CA', 'America/Winnipeg': 'CA', 'America/Halifax': 'CA', 'America/Regina': 'CA', 'America/St_Johns': 'CA',
    'America/New_York': 'US', 'America/Chicago': 'US', 'America/Denver': 'US', 'America/Los_Angeles': 'US', 'America/Phoenix': 'US', 'America/Anchorage': 'US',
    'America/Detroit': 'US', 'America/Boise': 'US', 'America/Indiana/Indianapolis': 'US', 'America/Indianapolis': 'US', 'America/Kentucky/Louisville': 'US', 'Pacific/Honolulu': 'US'
  };

  function detectRegion() {
    try {
      var tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
      if (TZ[tz]) return TZ[tz];
      if (/^Australia\//.test(tz)) return 'AU';
    } catch (e) {}
    var langs = (navigator.languages && navigator.languages.length) ? navigator.languages : [navigator.language || ''];
    for (var i = 0; i < langs.length; i++) {
      var m = /[-_]([A-Za-z]{2})(?:[-_]|$)/.exec(langs[i]);
      if (m) return m[1].toUpperCase();
    }
    try { if (window.Intl && Intl.Locale && langs[0]) return new Intl.Locale(langs[0]).maximize().region || null; } catch (e) {}
    return null;
  }

  function profileFor(region) {
    if (!region) return null;
    if (PROFILES[region]) return PROFILES[region];
    var cur = CURRENCIES[region];
    if (!cur) return null;
    return { locale: 'en-' + region, currency: cur, scale: SCALE[cur] || .1, unit: UNIT[cur] || null,
             name: GENERIC.name, banks: GENERIC.banks, cards: GENERIC.cards };
  }

  function moneyFormatter(p) {
    var opts = { style: 'currency', currency: p.currency, maximumFractionDigits: 0, minimumFractionDigits: 0 };
    try { return new Intl.NumberFormat(p.locale, Object.assign({ currencyDisplay: 'narrowSymbol' }, opts)); }
    catch (e) { try { return new Intl.NumberFormat(p.locale, opts); } catch (e2) { return null; } }
  }

  function convert(inr, scale) {
    var v = inr * scale;
    var step = scale >= 100 ? 100 : scale >= 10 ? 10 : 1;
    return Math.round(v / step) * step;
  }

  function each(sel, fn) { Array.prototype.forEach.call(document.querySelectorAll(sel), fn); }

  var override = /[?&]region=([A-Za-z]{2})/.exec(location.search);
  var region = override ? override[1].toUpperCase() : detectRegion();
  var p = profileFor(region);
  var locale = p ? p.locale : (navigator.language || 'en-IN');

  // Greeting + live dates run for everyone, in the visitor's own language conventions.
  var now = new Date(), h = now.getHours();
  var greet = h < 5 ? 'Good evening,' : h < 12 ? 'Good morning,' : h < 17 ? 'Good afternoon,' : 'Good evening,';
  each('[data-greet]', function (el) { el.textContent = greet; });
  try {
    var monthFmt = new Intl.DateTimeFormat(locale, { month: 'long' });
    var prev = new Date(now.getFullYear(), now.getMonth() - 1, 1);
    each('[data-month]', function (el) { el.textContent = monthFmt.format(now); });
    each('[data-prev-month]', function (el) { el.textContent = monthFmt.format(prev); });
    var dayFmt = new Intl.DateTimeFormat(locale, { day: 'numeric', month: 'short' });
    each('[data-due]', function (el) { el.textContent = dayFmt.format(new Date(now.getTime() + Number(el.getAttribute('data-due')) * 864e5)); });
  } catch (e) {}

  if (!p) return; // unknown region: keep the Indian demo as written in the HTML

  var fmt = moneyFormatter(p);
  if (fmt) each('[data-inr]', function (el) { el.textContent = fmt.format(convert(Number(el.getAttribute('data-inr')), p.scale)); });
  each('[data-name]', function (el) { el.textContent = p.name; });
  each('[data-initial]', function (el) { el.textContent = p.name.charAt(0).toUpperCase(); });
  each('[data-bank]', function (el) { var b = p.banks[Number(el.getAttribute('data-bank'))]; if (b) el.textContent = b[0]; });
  each('[data-bank-type]', function (el) { var b = p.banks[Number(el.getAttribute('data-bank-type'))]; if (b) el.textContent = b[1]; });
  each('[data-bank-initial]', function (el) { var b = p.banks[Number(el.getAttribute('data-bank-initial'))]; if (b) el.textContent = b[0].charAt(0).toUpperCase(); });
  each('[data-card]', function (el) { var c = p.cards[Number(el.getAttribute('data-card'))]; if (c) el.textContent = c; });
  if (p.unit) each('[data-unit]', function (el) { el.textContent = p.unit; });
  document.documentElement.setAttribute('data-region', region);
})();
