/* BASELINE — smooth scroll + progress + toast. Extend per references/motion.md */
(() => {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (typeof window.Lenis !== 'undefined' && !prefersReduced) {
    const lenis = new Lenis({ duration: 1.1, smoothWheel: true });
    if (window.gsap && window.ScrollTrigger) {
      gsap.registerPlugin(ScrollTrigger);
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((t) => lenis.raf(t * 1000));
      gsap.ticker.lagSmoothing(0);
    }
  }
  const toast = document.getElementById('toast');
  window.showToast = (msg) => { if (!toast) return; toast.textContent = msg; toast.classList.add('is-visible'); setTimeout(() => toast.classList.remove('is-visible'), 4000); };
})();
