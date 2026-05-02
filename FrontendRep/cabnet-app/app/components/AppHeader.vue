<template>
  <header
    class="fixed top-0 z-50 w-full transition-all duration-300"
    :class="[
      isHidden ? '-translate-y-full' : 'translate-y-0',
      isScrolled
        ? 'bg-white/80 backdrop-blur-md border-b border-black/8 shadow-sm'
        : 'bg-transparent border-transparent',
    ]"
  >
    <div class="mx-auto flex h-20 max-w-7xl items-center justify-between px-6 md:px-8">

      <!-- Logo -->
      <NuxtLink :to="localePath('/')" class="shrink-0 flex items-center gap-3" aria-label="Winner Cabinets home">
        <img
          src="/images/WClogo.png"
          alt="Winner Cabinets"
          class="h-10 w-auto object-contain"
          :class="isScrolled || isLightPage ? 'brightness-0' : 'brightness-0 invert'"
        />
        <span
          class="hidden sm:block font-extrabold text-sm tracking-tight leading-tight"
          :class="isScrolled || isLightPage ? 'text-gray-900' : 'text-white'"
        >
          Winner<br />Cabinets
        </span>
      </NuxtLink>

      <!-- Desktop nav -->
      <nav class="hidden md:flex items-center gap-8">
        <NuxtLink
          v-for="item in navItems"
          :key="item.key"
          :to="localePath(item.to)"
          class="text-sm font-medium transition-colors duration-200 relative after:absolute after:bottom-[-3px] after:left-0 after:h-px after:w-0 after:bg-yellow-400 after:transition-all hover:after:w-full"
          :class="isScrolled || isLightPage ? 'text-gray-700 hover:text-gray-900' : 'text-white/85 hover:text-white'"
        >
          {{ $t(item.labelKey) }}
        </NuxtLink>
      </nav>

      <!-- Right: lang switcher + mobile toggle -->
      <div class="flex items-center gap-1">
        <!-- Language switcher -->
        <div class="flex items-center text-sm font-medium">
          <NuxtLink
            :to="switchLocalePath('en')"
            class="px-3 py-1.5 transition-colors duration-200 rounded-sm"
            :class="[
              locale === 'en' ? 'font-bold' : 'opacity-60 hover:opacity-100',
              isScrolled || isLightPage ? 'text-gray-800' : 'text-white',
            ]"
          >EN</NuxtLink>
          <span :class="isScrolled || isLightPage ? 'text-gray-300' : 'text-white/30'">/</span>
          <NuxtLink
            :to="switchLocalePath('zh')"
            class="px-3 py-1.5 transition-colors duration-200 rounded-sm"
            :class="[
              locale === 'zh' ? 'font-bold' : 'opacity-60 hover:opacity-100',
              isScrolled || isLightPage ? 'text-gray-800' : 'text-white',
            ]"
          >中文</NuxtLink>
        </div>

        <!-- Mobile hamburger -->
        <button
          class="ml-2 md:hidden p-2 rounded-lg transition-colors"
          :class="isScrolled || isLightPage ? 'text-gray-900 hover:bg-gray-100' : 'text-white hover:bg-white/10'"
          aria-label="Toggle menu"
          @click="mobileOpen = !mobileOpen"
        >
          <svg v-if="!mobileOpen" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile menu -->
    <Transition name="mobile-menu">
      <div
        v-if="mobileOpen"
        class="md:hidden bg-white border-t border-gray-100 px-6 py-4 space-y-1 shadow-lg"
      >
        <NuxtLink
          v-for="item in navItems"
          :key="item.key"
          :to="localePath(item.to)"
          class="block py-3 text-gray-800 font-medium text-sm border-b border-gray-50 last:border-0"
          @click="mobileOpen = false"
        >
          {{ $t(item.labelKey) }}
        </NuxtLink>
      </div>
    </Transition>
  </header>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'

const localePath = useLocalePath()
const switchLocalePath = useSwitchLocalePath()
const { locale } = useI18n()
const route = useRoute()

const isScrolled = ref(false)
const isHidden = ref(false)
const mobileOpen = ref(false)

const navItems = [
  { key: 'about', to: '/about', labelKey: 'header.about' },
  { key: 'collections', to: '/collections', labelKey: 'header.collections' },
  { key: 'hours', to: '/hours-and-location', labelKey: 'header.hours' },
  { key: 'measurement', to: '/measurement-services', labelKey: 'header.measurement' },
]

// Pages where the header text must be dark (no full-bleed hero)
const lightPagePaths = ['/about', '/collections', '/hours-and-location', '/measurement-services']

const isLightPage = computed(() => {
  return lightPagePaths.some(p => route.path === localePath(p))
})

const SCROLL_THRESHOLD = 12
const HIDE_AFTER = 120
const DOWN_DELTA = 4
const UP_DELTA = 6

let lastY = 0
let ticking = false

function onScrollUpdate(y: number) {
  isScrolled.value = y > SCROLL_THRESHOLD

  if (y > HIDE_AFTER) {
    if (y - lastY > DOWN_DELTA) isHidden.value = true
    else if (lastY - y > UP_DELTA) isHidden.value = false
  } else {
    isHidden.value = false
  }

  lastY = y
  ticking = false
}

function handleScroll() {
  const y = window.scrollY
  if (!ticking) {
    ticking = true
    requestAnimationFrame(() => onScrollUpdate(y))
  }
}

onMounted(() => {
  lastY = window.scrollY
  isScrolled.value = lastY > SCROLL_THRESHOLD
  window.addEventListener('scroll', handleScroll, { passive: true })
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>
