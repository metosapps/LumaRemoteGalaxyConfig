(() => {
  const gallery = document.querySelector('.gallery');
  const controls = document.querySelector('.gallery-buttons');
  if (!gallery || !controls) return;
  controls.hidden = false;
  const previous = controls.querySelector('[data-gallery="previous"]');
  const next = controls.querySelector('[data-gallery="next"]');
  const update = () => {
    previous.disabled = gallery.scrollLeft <= 2;
    next.disabled = gallery.scrollLeft + gallery.clientWidth >= gallery.scrollWidth - 2;
  };
  const move = direction => gallery.scrollBy({left: direction * gallery.clientWidth * .75, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
  previous.addEventListener('click', () => move(-1));
  next.addEventListener('click', () => move(1));
  gallery.addEventListener('scroll', update, {passive: true});
  window.addEventListener('resize', update);
  update();
})();
