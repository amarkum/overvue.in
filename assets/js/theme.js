/* Overvue theme toggle: dark by default, light on request, remembered per browser. */
(function () {
  var KEY = 'overvue-theme';
  var root = document.documentElement;
  var meta = document.querySelector('meta[name="theme-color"]');
  var toggles = Array.prototype.slice.call(document.querySelectorAll('[data-theme-toggle]'));

  function current() { return root.getAttribute('data-theme') === 'light' ? 'light' : 'dark'; }
  function apply(theme) {
    root.setAttribute('data-theme', theme);
    if (meta) meta.setAttribute('content', theme === 'light' ? '#f4f5f7' : '#0a0a0c');
    toggles.forEach(function (b) {
      b.setAttribute('aria-label', theme === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
    });
  }

  apply(current());
  toggles.forEach(function (b) {
    b.addEventListener('click', function () {
      var next = current() === 'light' ? 'dark' : 'light';
      apply(next);
      try { localStorage.setItem(KEY, next); } catch (e) { /* private mode */ }
    });
  });
})();
