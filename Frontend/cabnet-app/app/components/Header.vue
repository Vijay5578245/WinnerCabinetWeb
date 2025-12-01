<template>
  <div class="w-full h-24 bg-white/70 backdrop-blur-lg flex items-center px-7 fixed top-0 z-50 border-b border-black-200
    transition-transform duration-300 ease-in-out" :class="{ '-translate-y-full': hidden, 'translate-y-0': !hidden }">
    <strong class="text-lg">My Header</strong>

  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount } from 'vue';


const hidden = ref(false);

// Config: adjust to taste
const HIDE_DISTANCE = 300; // only start hiding after you've scrolled this far from top
const DELTA_DOWN = 10;     // scroll down this much to trigger hide
const DELTA_UP = 10;       // scroll up this much to trigger show

let lastY = 0;
let ticking = false;

function update(currentY) {
  const dy = currentY - lastY;

  // If scrolling down past thresholds -> hide
  if (dy > DELTA_DOWN && currentY > HIDE_DISTANCE) {
    hidden.value = true;
  }
  // If scrolling up enough -> show
  else if (lastY - currentY > DELTA_UP) {
    hidden.value = false;
  }

  lastY = currentY;
  ticking = false;
}

function onScroll() {
  const currentY = window.scrollY || window.pageYOffset;
  if (!ticking) {
    ticking = true;
    window.requestAnimationFrame(() => update(currentY));
  }
}

onMounted(() => {
  lastY = window.scrollY || window.pageYOffset;
  window.addEventListener('scroll', onScroll, { passive: true });
});

onBeforeUnmount(() => {
  window.removeEventListener('scroll', onScroll);
});

</script>
