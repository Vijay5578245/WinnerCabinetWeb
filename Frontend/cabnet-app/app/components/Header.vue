<template>
  <div
    class="w-full h-24 fixed top-0 z-50 flex justify-center items-center px-7 transition-all duration-350"
    :class="[
      hidden ? '-translate-y-full pointer-events-none delay-50' : 'translate-y-0 delay-0',
      // background classes (depends on scroll)
      scrolled
        ? 'bg-white/70 backdrop-blur-lg border-black/200'
        : 'bg-transparent backdrop-blur-none border-transparent',
      // text color handled separately so we can force black on a specific page
      textClass,
    ]"
  >
    <nuxt-link to="/" class="text-lg font-bold"> Winner Cabinets </nuxt-link>

    <ul class="flex space-x-6 ml-6">
      <li><NuxtLink to="/about">{{$t("header.about")}}</NuxtLink></li>
      <li><NuxtLink to="/collections">{{$t("header.collections")}}</NuxtLink></li>
    </ul>
  </div>
</template>s

<script setup>
import { ref, onMounted, onBeforeUnmount, computed } from "vue";
import { useRoute } from "vue-router";

const hidden = ref(false);
const scrolled = ref(false);
const localePath = useLocalePath()


const route = useRoute();
// detect the hours page by path or name (adjust if your route name differs)

const contrastPages = [
  "/hours-and-location",
  "hours-and-location",
  "/about",
  "about",
  "/collections",
  "collections",
];

const isContrastPage = computed(
  () => {
    // 3. Check if the current path matches the localized path of any page in the list
  return contrastPages.some(page => route.path === localePath(page))
}
);

// text color: force black on the hours page, otherwise white at top and black when scrolled
const textClass = computed(() => {
  if (isContrastPage.value) return "text-black";
  return scrolled.value ? "text-black" : "text-white";
});

// Config: adjust to taste
const HIDE_DISTANCE = 100; // only start hiding after you've scrolled this far from top
const DELTA_DOWN = 3; // scroll down this much to trigger hide
const DELTA_UP = 5; // scroll up this much to trigger show
const SCROLL_BG_THRESHOLD = 10; // when to switch from transparent -> colored

let lastY = 0;
let ticking = false;

function update(currentY) {
  const dy = currentY - lastY;

  // toggle hide/show based on direction + thresholds
  if (dy > DELTA_DOWN && currentY > HIDE_DISTANCE) {
    hidden.value = true;
  } else if (lastY - currentY > DELTA_UP) {
    hidden.value = false;
  }

  // toggle background based on how far we've scrolled from top
  scrolled.value = currentY > SCROLL_BG_THRESHOLD;

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
  scrolled.value = lastY > SCROLL_BG_THRESHOLD;
  window.addEventListener("scroll", onScroll, { passive: true });
});

onBeforeUnmount(() => {
  window.removeEventListener("scroll", onScroll);
});
</script>
