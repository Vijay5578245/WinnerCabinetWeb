<template>
  <header
    class="fixed top-0 z-50 w-full h-24 px-7 transition-all duration-[350ms]"
    :class="[
      hidden ? '-translate-y-full pointer-events-none delay-[50ms]' : 'translate-y-0 delay-0',
      scrolled
        ? 'bg-white/70 backdrop-blur-lg border-b border-black/10'
        : 'bg-transparent backdrop-blur-none border-transparent',
      textClass,
    ]"
  >
    <div class="grid grid-cols-3 items-center h-full w-full">
      <div></div>

      <nav class="flex items-center justify-center gap-6 whitespace-nowrap">
        <NuxtLink to="/" class="text-lg font-bold">
          Winner Cabinets
        </NuxtLink>

        <NuxtLink to="/about">
          {{ $t("header.about") }}
        </NuxtLink>

        <NuxtLink to="/collections">
          {{ $t("header.collections") }}
        </NuxtLink>
      </nav>

      <div class="flex justify-end items-center whitespace-nowrap shrink-0">
        <NuxtLink
          class="cursor-pointer px-4 py-2"
          :class="locale === 'en' ? 'font-bold' : ''"
          :to="switchLocalePath('en')"
        >
          English
        </NuxtLink>

        <span>/</span>

        <NuxtLink
          class="cursor-pointer px-4 py-2"
          :class="locale === 'zh' ? 'font-bold' : ''"
          :to="switchLocalePath('zh')"
        >
          中文
        </NuxtLink>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, computed } from "vue";
import { useRoute } from "vue-router";

const hidden = ref(false);
const scrolled = ref(false);
const localePath = useLocalePath();
const { locale, setLocale } = useI18n();
const switchLocalePath = useSwitchLocalePath()


const route = useRoute();

const switchLang = async (lang) => {
  await setLocale(lang);
  navigateTo(window.location.pathname, { replace: true })
};
// detect the hours page by path or name (adjust if your route name differs)

const contrastPages = [
  "/hours-and-location",
  "hours-and-location",
  "/about",
  "about",
  "/collections",
  "collections",
];

const isContrastPage = computed(() => {
  // 3. Check if the current path matches the localized path of any page in the list
  return contrastPages.some((page) => route.path === localePath(page));
});

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
