<template>
  <div ref="pageEl" class="min-h-screen w-full overflow-x-hidden bg-white">

    <!-- ── HERO ──────────────────────────────────────── -->
    <section class="relative z-10 flex h-[96dvh] w-full items-center justify-center overflow-hidden bg-black">
      <img
        src="/images/logbg2.png"
        alt="Winner Cabinets showroom"
        class="hero-image-zoom absolute inset-0 h-full w-full object-cover"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-black/25 to-black/15"></div>

      <div class="relative z-10 flex flex-col items-center px-6 text-center">
        <img
          src="/images/WClogo.png"
          alt="Winner Cabinets logo"
          class="hero-logo h-auto w-auto object-contain"
          style="max-height: min(280px, 35vw); filter: brightness(1.25) drop-shadow(0 2px 9px rgba(0,0,0,0.43)) drop-shadow(0 0 7px rgba(250,204,21,0.18));"
          loading="eager"
        />

        <p class="hero-sub mt-6 max-w-xl text-lg text-white/85 md:text-xl leading-relaxed">
          {{ $t('index.tagline') }}
        </p>

        <AppButton to="/hours-and-location" size="lg" class="hero-sub mt-8 text-white border-white/40 hover:text-black">
          {{ $t('index.heroCta') }}
        </AppButton>
      </div>

      <!-- Scroll hint -->
      <div class="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 opacity-50">
        <span class="text-[10px] font-bold uppercase tracking-[0.2em] text-white">Scroll</span>
        <div class="w-px h-8 bg-white/60 animate-pulse"></div>
      </div>
    </section>

    <!-- ── MAIN ──────────────────────────────────────── -->
    <main class="relative z-10 bg-white -mt-5 rounded-t-2xl overflow-hidden">

      <!-- DESIGN INTRO -->
      <section class="relative overflow-hidden border-t border-gray-200 bg-white px-6 pt-20 pb-0">
        <div class="absolute inset-0 bg-gradient-to-b from-amber-50/70 via-yellow-50/30 to-white pointer-events-none"></div>
        <div class="dot-pattern-fade absolute inset-0 opacity-50 pointer-events-none"></div>

        <div class="relative z-10 mx-auto max-w-7xl flex flex-col items-center gap-4 text-center">
          <!-- Ornament -->
          <div class="flex items-center gap-3">
            <div class="h-px w-10 bg-yellow-400"></div>
            <div class="h-1.5 w-1.5 rounded-full bg-yellow-400"></div>
            <div class="h-px w-10 bg-yellow-400"></div>
          </div>

          <p class="design-label text-[10px] font-bold uppercase tracking-[0.22em] text-amber-500 md:text-xs">
            {{ $t('index.designLabel') }}
          </p>

          <div class="design-headline">
            <p class="text-3xl font-extrabold text-gray-900 leading-tight md:text-5xl">
              {{ $t('index.designHeadline1') }}
            </p>
            <p class="mt-2 text-3xl font-extrabold text-gray-900 leading-tight md:text-5xl">
              {{ $t('index.designHeadline2') }}
            </p>
          </div>
        </div>

        <div class="relative z-10 mt-12 w-full">
          <ImageCarousel />
        </div>
      </section>

      <!-- STRENGTHS -->
      <section class="bg-white px-6 py-24">
        <div class="mx-auto max-w-7xl">
          <div class="strengths-header mb-14">
            <SectionLabel>{{ $t('index.strengthsLabel') }}</SectionLabel>
            <h2 class="text-4xl font-extrabold text-gray-900 leading-tight md:text-5xl">
              {{ $t('index.strengthsHeadline') }}
            </h2>
            <p class="mt-4 max-w-2xl text-gray-600 leading-relaxed">
              {{ $t('index.strengthsDescription') }}
            </p>
          </div>

          <div class="strengths-grid grid grid-cols-1 gap-10 md:grid-cols-3">
            <article
              v-for="(item, i) in strengthItems"
              :key="i"
              class="strength-col group"
              :class="i < 2 ? 'md:border-r md:border-gray-150 md:pr-10' : ''"
            >
              <span class="-mb-1 block select-none text-6xl font-black leading-none text-gray-100">
                0{{ i + 1 }}
              </span>
              <div class="mt-3 mb-4 h-px w-10 bg-yellow-400"></div>
              <h3 class="mb-3 text-2xl font-extrabold leading-tight text-gray-900">
                {{ $t(item.headerKey) }}
              </h3>
              <p class="leading-relaxed text-gray-600 text-sm">
                {{ $t(item.descKey) }}
              </p>
            </article>
          </div>

          <div class="mt-14 flex justify-start">
            <AppButton to="/about">
              {{ $t('index.strengthsAboutCta') }}
            </AppButton>
          </div>
        </div>
      </section>

      <!-- ADVANTAGE SLIDER -->
      <FeatureSlider />

      <!-- SERVICES -->
      <section class="bg-white px-6 py-24">
        <div class="mx-auto max-w-7xl">
          <div class="services-header mb-12">
            <SectionLabel>{{ $t('index.servicesLabel') }}</SectionLabel>
            <h2 class="text-4xl font-extrabold text-gray-900">{{ $t('index.servicesHeadline') }}</h2>
            <div class="mt-4 h-px w-12 bg-yellow-400"></div>
          </div>

          <div class="services-grid grid grid-cols-1 gap-6 md:grid-cols-2">
            <NuxtLink
              v-for="svc in services"
              :key="svc.id"
              :to="localePath('/collections')"
              class="service-card group relative flex overflow-hidden rounded-2xl bg-gray-900"
              style="min-height: 420px;"
            >
              <img
                :src="svc.image"
                :alt="svc.title"
                class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                loading="lazy"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent"></div>

              <div class="relative z-10 mt-auto p-8">
                <p class="text-[10px] font-bold uppercase tracking-[0.22em] text-yellow-400 mb-2">
                  {{ svc.category }}
                </p>
                <h3 class="text-2xl font-extrabold tracking-tight text-white md:text-3xl">
                  {{ $t(svc.titleKey) }}
                </h3>
                <p class="mt-2 text-sm text-white/60 leading-relaxed max-w-xs">
                  {{ $t(svc.descKey) }}
                </p>
                <span class="mt-4 inline-flex items-center gap-1 text-yellow-400 text-xs font-bold tracking-wide opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                  View Collection →
                </span>
              </div>
            </NuxtLink>
          </div>
        </div>
      </section>

      <!-- COLLECTIONS BENTO -->
      <section class="bg-white px-6 pb-24 pt-4">
        <div class="collections-grid mx-auto max-w-7xl grid grid-cols-1 gap-6 md:grid-cols-3">
          <NuxtLink
            :to="localePath('/collections')"
            class="group relative block overflow-hidden rounded-2xl bg-gray-900 md:col-span-2"
            style="min-height: 560px;"
            aria-label="View Our Collections"
          >
            <img
              src="/images/nvTest.jpg"
              alt="Winner Cabinets collection"
              class="absolute inset-0 h-full w-full object-cover transition-transform duration-700 group-hover:scale-103"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>

            <div class="relative z-10 flex h-full flex-col justify-end p-8 md:p-10">
              <SectionLabel class="text-yellow-400">{{ $t('index.collectionsLabel') }}</SectionLabel>
              <h2 class="text-3xl font-extrabold text-white leading-tight md:text-4xl">
                {{ $t('index.collectionsHeadline') }}
              </h2>
              <p class="mt-3 max-w-md text-white/80 leading-relaxed">
                {{ $t('index.collectionsBody') }}
              </p>
            </div>
          </NuxtLink>

          <NuxtLink
            :to="localePath('/collections')"
            class="group flex items-center justify-center rounded-2xl bg-yellow-400 p-8 shadow-md"
            style="min-height: 300px;"
            aria-label="Browse collections"
          >
            <div class="text-center">
              <p class="text-2xl font-extrabold text-black md:text-3xl leading-tight">
                {{ $t('index.collectionsShop') }}
              </p>
              <span
                class="mt-4 inline-flex h-12 w-12 items-center justify-center rounded-full bg-black text-xl text-yellow-400 transition-transform group-hover:translate-x-1.5"
                aria-hidden="true"
              >→</span>
            </div>
          </NuxtLink>
        </div>
      </section>

    </main>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick } from 'vue'

const localePath = useLocalePath()
const pageEl = ref<HTMLElement | null>(null)

const strengthItems = [
  { headerKey: 'index.usBoxHeader1', descKey: 'index.usBoxDescription1' },
  { headerKey: 'index.usBoxHeader2', descKey: 'index.usBoxDescription2' },
  { headerKey: 'index.usBoxHeader3', descKey: 'index.usBoxDescription3' },
]

const services = [
  {
    id: 1,
    titleKey: 'collections.kitchenTitle',
    descKey: 'collections.kitchenDesc',
    category: 'Kitchens',
    image: '/images/nvTest.jpg',
  },
  {
    id: 2,
    titleKey: 'collections.vanityTitle',
    descKey: 'collections.vanityDesc',
    category: 'Bathrooms',
    image: '/images/storeTest.jpg',
  },
  {
    id: 3,
    titleKey: 'collections.closetTitle',
    descKey: 'collections.closetDesc',
    category: 'Storage',
    image: '/images/pfTest.jpg',
  },
  {
    id: 4,
    titleKey: 'collections.millworkTitle',
    descKey: 'collections.millworkDesc',
    category: 'Specialty',
    image: '/images/pencilPic.jpg',
  },
]

let ctx: import('gsap').Context | null = null

onMounted(async () => {
  await nextTick()

  const { gsap } = await import('gsap')
  const { ScrollTrigger } = await import('gsap/ScrollTrigger')

  ctx = gsap.context(() => {
    // Hero
    gsap.from('.hero-logo', { autoAlpha: 0, duration: 1.1, ease: 'power2.out', delay: 0.2 })
    gsap.from('.hero-sub', {
      autoAlpha: 0, y: 20, duration: 0.9, ease: 'power2.out', delay: 0.5, stagger: 0.15,
    })

    // Design section
    gsap.from('.design-label', {
      autoAlpha: 0, y: 16, duration: 0.6, ease: 'power2.out',
      scrollTrigger: { trigger: '.design-label', start: 'top 88%', toggleActions: 'play none none none' },
    })
    gsap.from('.design-headline', {
      autoAlpha: 0, y: 24, duration: 0.7, ease: 'power2.out',
      scrollTrigger: { trigger: '.design-headline', start: 'top 86%', toggleActions: 'play none none none' },
    })

    // Strengths
    gsap.from('.strengths-header', {
      autoAlpha: 0, y: 20, duration: 0.65, ease: 'power2.out',
      scrollTrigger: { trigger: '.strengths-header', start: 'top 85%', toggleActions: 'play none none none' },
    })
    gsap.from('.strength-col', {
      autoAlpha: 0, y: 28, duration: 0.6, ease: 'power2.out', stagger: 0.14,
      scrollTrigger: { trigger: '.strengths-grid', start: 'top 82%', toggleActions: 'play none none none' },
    })

    // Services
    gsap.from('.services-header', {
      autoAlpha: 0, y: 20, duration: 0.65, ease: 'power2.out',
      scrollTrigger: { trigger: '.services-header', start: 'top 85%', toggleActions: 'play none none none' },
    })
    gsap.from('.service-card', {
      autoAlpha: 0, y: 28, duration: 0.6, ease: 'power2.out', stagger: 0.1,
      scrollTrigger: { trigger: '.services-grid', start: 'top 82%', toggleActions: 'play none none none' },
    })

    // Collections bento
    gsap.from('.collections-grid > *', {
      autoAlpha: 0, y: 24, duration: 0.6, ease: 'power2.out', stagger: 0.14,
      scrollTrigger: { trigger: '.collections-grid', start: 'top 82%', toggleActions: 'play none none none' },
    })

    ScrollTrigger.refresh()
  }, pageEl.value)
})

onUnmounted(() => {
  ctx?.revert()
})
</script>
