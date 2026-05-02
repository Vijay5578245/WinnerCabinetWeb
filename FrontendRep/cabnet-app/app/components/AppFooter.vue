<template>
  <footer class="fixed bottom-0 left-0 right-0 z-0 bg-neutral-950 text-white">
    <div class="mx-auto max-w-7xl px-6 md:px-8 pt-16 pb-10 grid grid-cols-1 md:grid-cols-3 gap-12">

      <!-- Brand -->
      <div>
        <p class="font-extrabold text-xl mb-3 tracking-tight text-white">
          Winner Cabinets
        </p>
        <p class="text-white/50 text-sm leading-relaxed whitespace-pre-line">{{ $t('footer.tagline') }}</p>
        <div class="mt-6 h-px w-10 bg-yellow-400"></div>
      </div>

      <!-- Navigation -->
      <div>
        <p class="text-white/40 text-[10px] font-bold tracking-[0.2em] uppercase mb-5">
          {{ $t('footer.exploreLabel') }}
        </p>
        <ul class="space-y-3">
          <li v-for="link in footerLinks" :key="link.to">
            <NuxtLink
              :to="localePath(link.to)"
              class="text-white/55 hover:text-white transition-colors text-sm"
            >
              {{ $t(link.labelKey) }}
            </NuxtLink>
          </li>
        </ul>
      </div>

      <!-- Visit -->
      <div>
        <p class="text-white/40 text-[10px] font-bold tracking-[0.2em] uppercase mb-5">
          {{ $t('footer.visitLabel') }}
        </p>
        <p class="text-white/50 text-sm leading-relaxed mb-5">
          {{ $t('footer.visitBody') }}
        </p>
        <NuxtLink
          :to="localePath('/hours-and-location')"
          class="inline-flex items-center gap-2 text-yellow-400 text-sm font-medium hover:text-yellow-300 transition-colors"
        >
          {{ $t('footer.visitCta') }}
          <span class="text-base leading-none" aria-hidden="true">→</span>
        </NuxtLink>
      </div>
    </div>

    <!-- Bottom bar -->
    <div class="border-t border-white/8">
      <div class="mx-auto max-w-7xl px-6 md:px-8 py-5 flex flex-col md:flex-row items-center justify-between gap-2">
        <p class="text-white/25 text-xs">{{ $t('footer.copyright') }}</p>
        <p class="text-white/18 text-xs tracking-widest uppercase">{{ $t('footer.quality') }}</p>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const localePath = useLocalePath()

const footerLinks = [
  { to: '/about', labelKey: 'header.about' },
  { to: '/collections', labelKey: 'header.collections' },
  { to: '/measurement-services', labelKey: 'header.measurement' },
  { to: '/hours-and-location', labelKey: 'header.hours' },
]
</script>
