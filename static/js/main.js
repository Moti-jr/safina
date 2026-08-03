// ─── Dark mode toggle ───────────────────────────────
const toggle   = document.getElementById('themeToggle');
const icon     = document.getElementById('themeIcon');
const htmlEl   = document.documentElement;
const saved    = localStorage.getItem('theme') || 'light';

htmlEl.setAttribute('data-bs-theme', saved);
icon.className = saved === 'dark' ? 'fa fa-sun' : 'fa fa-moon';

if (toggle) {
  toggle.addEventListener('click', () => {
    const current = htmlEl.getAttribute('data-bs-theme');
    const next    = current === 'dark' ? 'light' : 'dark';
    htmlEl.setAttribute('data-bs-theme', next);
    localStorage.setItem('theme', next);
    icon.className = next === 'dark' ? 'fa fa-sun' : 'fa fa-moon';
  });
}

// ─── Animate stats counter ──────────────────────────
function animateCounter(el) {
  const target   = parseInt(el.getAttribute('data-target'), 10);
  const duration = 2000;
  const step     = target / (duration / 16);
  let   current  = 0;

  const timer = setInterval(() => {
    current += step;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    el.textContent = Math.floor(current).toLocaleString();
  }, 16);
}

// ─── Intersection Observer for stats ────────────────
const counters = document.querySelectorAll('.stat-number[data-target]');
if (counters.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
}

// ─── Navbar scroll effect ────────────────────────────
const nav = document.getElementById('mainNav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 50);
  });
}