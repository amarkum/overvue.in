/* Overvue demo personalisation.
   The phone mockups are written for India (₹, lakh grouping). This script re-skins them for the
   visitor's region: currency and number format, a first name with the avatar's initials, the
   greeting, and live month and chart dates. Nothing leaves the browser; region comes from the
   time zone (strongest "where am I" signal), then the browser language.
   Preview any region with ?region=US. Money formats mirror the app's lib/core/formatters/currency.dart. */
(function () {
  var PROFILES = {
    IN: { locale: 'en-IN', currency: 'INR', scale: 1,  unit: 'rupee',  name: 'Aarav',     full: 'Aarav Sharma' },
    US: { locale: 'en-US', currency: 'USD', scale: .1, unit: 'dollar', name: 'Emma',      full: 'Emma Johnson' },
    GB: { locale: 'en-GB', currency: 'GBP', scale: .1, unit: 'pound',  name: 'Oliver',    full: 'Oliver Smith' },
    CA: { locale: 'en-CA', currency: 'CAD', scale: .2, unit: 'dollar', name: 'Liam',      full: 'Liam Tremblay' },
    AU: { locale: 'en-AU', currency: 'AUD', scale: .2, unit: 'dollar', name: 'Charlotte', full: 'Charlotte Wilson' },
    NZ: { locale: 'en-NZ', currency: 'NZD', scale: .2, unit: 'dollar', name: 'Sophie',    full: 'Sophie Taylor' },
    SG: { locale: 'en-SG', currency: 'SGD', scale: .2, unit: 'dollar', name: 'Wei Ling',  full: 'Wei Ling Tan' },
    AE: { locale: 'en-AE', currency: 'AED', scale: .5, unit: 'dirham', name: 'Omar',      full: 'Omar Al Mansoori' },
    JP: { locale: 'en-JP', currency: 'JPY', scale: 20, unit: 'yen',    name: 'Yuki',      full: 'Yuki Sato' },
    DE: { locale: 'en-DE', currency: 'EUR', scale: .1, unit: 'euro',   name: 'Lena',      full: 'Lena Müller' },
    FR: { locale: 'en-FR', currency: 'EUR', scale: .1, unit: 'euro',   name: 'Louis',     full: 'Louis Martin' },
    ES: { locale: 'en-ES', currency: 'EUR', scale: .1, unit: 'euro',   name: 'Lucía',     full: 'Lucía García' },
    IT: { locale: 'en-IT', currency: 'EUR', scale: .1, unit: 'euro',   name: 'Giulia',    full: 'Giulia Rossi' },
    NL: { locale: 'en-NL', currency: 'EUR', scale: .1, unit: 'euro',   name: 'Sanne',     full: 'Sanne de Vries' },
    IE: { locale: 'en-IE', currency: 'EUR', scale: .1, unit: 'euro',   name: 'Aoife',     full: 'Aoife Murphy' }
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
  var GENERIC = { name: 'Alex', full: 'Alex Morgan' };

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
             name: GENERIC.name, full: GENERIC.full };
  }

  function moneyFormatter(p) {
    var opts = { style: 'currency', currency: p.currency, maximumFractionDigits: 0, minimumFractionDigits: 0 };
    try { return new Intl.NumberFormat(p.locale, Object.assign({ currencyDisplay: 'narrowSymbol' }, opts)); }
    catch (e) { try { return new Intl.NumberFormat(p.locale, opts); } catch (e2) { return null; } }
  }

  function convert(inr, scale) {
    var v = inr * scale;
    if (v < 0) return -convert(-inr, scale);
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
  var greet = h < 12 ? 'Good morning' : h < 17 ? 'Good afternoon' : 'Good evening'; // same rule as the app's HomeHeader
  each('[data-greet]', function (el) { el.textContent = greet; });
  try {
    var monthFmt = new Intl.DateTimeFormat(locale, { month: 'long' });
    var prev = new Date(now.getFullYear(), now.getMonth() - 1, 1);
    each('[data-month]', function (el) { el.textContent = monthFmt.format(now); });
    each('[data-prev-month]', function (el) { el.textContent = monthFmt.format(prev); });
    var monthYearFmt = new Intl.DateTimeFormat(locale, { month: 'long', year: 'numeric' });
    each('[data-month-year]', function (el) { el.textContent = monthYearFmt.format(now); });
    var shortMonthYearFmt = new Intl.DateTimeFormat(locale, { month: 'short', year: 'numeric' });
    each('[data-month-short-year]', function (el) { el.textContent = shortMonthYearFmt.format(now); });
    // Chart x-axis: days of the current month ("1 Oct" / "Oct 1"), last tick = the month's last day.
    var dayFmt = new Intl.DateTimeFormat(locale, { day: 'numeric', month: 'short' });
    var lastDay = new Date(now.getFullYear(), now.getMonth() + 1, 0).getDate();
    each('[data-day]', function (el) {
      var d = el.getAttribute('data-day') === 'last' ? lastDay : Number(el.getAttribute('data-day'));
      el.textContent = dayFmt.format(new Date(now.getFullYear(), now.getMonth(), d));
    });
  } catch (e) {}

  if (!p) return; // unknown region: keep the Indian demo as written in the HTML

  var fmt = moneyFormatter(p);
  // Compact figures mirror the app's formatMoney(compact: true): only from 1,00,000 up; lakh/crore for rupees, K/M/B elsewhere.
  function symbolOf() {
    try { return fmt.formatToParts(1).filter(function (x) { return x.type === 'currency'; }).map(function (x) { return x.value; }).join(''); }
    catch (e) { return ''; }
  }
  function compact(v) {
    var abs = Math.abs(v), f = function (n) { return n.toFixed(1); }, s;
    if (p.currency === 'INR') s = abs >= 1e7 ? f(abs / 1e7) + 'Cr' : f(abs / 1e5) + 'L';
    else s = abs >= 1e9 ? f(abs / 1e9) + 'B' : abs >= 1e6 ? f(abs / 1e6) + 'M' : f(abs / 1e3) + 'K';
    return (v < 0 ? '-' : '') + symbolOf() + s;
  }
  // Short figures mirror formatMoneyShort: always abbreviated from 1,000, trailing ".0" dropped (₹50K, $12.5K, ₹1.2L).
  function short(v) {
    var abs = Math.abs(v), f = function (n) { var s = n.toFixed(1); return s.slice(-2) === '.0' ? s.slice(0, -2) : s; }, s;
    if (p.currency === 'INR' && abs >= 1e5) s = abs >= 1e7 ? f(abs / 1e7) + 'Cr' : f(abs / 1e5) + 'L';
    else s = abs >= 1e9 ? f(abs / 1e9) + 'B' : abs >= 1e6 ? f(abs / 1e6) + 'M' : abs >= 1e3 ? f(abs / 1e3) + 'K' : String(Math.round(abs));
    return (v < 0 ? '-' : '') + symbolOf() + s;
  }
  if (fmt) each('[data-inr]', function (el) {
    var v = convert(Number(el.getAttribute('data-inr')), p.scale);
    if (el.hasAttribute('data-short')) el.textContent = short(v);
    else el.textContent = (el.hasAttribute('data-compact') && Math.abs(v) >= 100000) ? compact(v) : fmt.format(v);
  });
  each('[data-name]', function (el) { el.textContent = p.name; });
  var words = p.full.split(' ').filter(Boolean);
  var initials = (words[0].charAt(0) + (words.length > 1 ? words[words.length - 1].charAt(0) : '')).toUpperCase();
  each('[data-initial]', function (el) { el.textContent = initials; });
  if (p.unit) each('[data-unit]', function (el) { el.textContent = p.unit; });
  document.documentElement.setAttribute('data-region', region);
})();
