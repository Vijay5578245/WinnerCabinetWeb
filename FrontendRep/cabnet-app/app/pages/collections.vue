<template>
  <main class="bg-white min-h-screen overflow-x-hidden">

    <!-- Hero -->
    <section class="relative h-[55dvh] overflow-hidden">
      <img
        src="/images/nvTest.jpg"
        alt="Our Collections"
        class="absolute inset-0 w-full h-full object-cover"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/30 to-transparent"></div>
      <div class="absolute bottom-0 left-0 px-8 md:px-12 pb-12 max-w-4xl">
        <SectionLabel class="text-yellow-400">{{ $t('collections.heroLabel') }}</SectionLabel>
        <h1 class="text-5xl md:text-6xl font-extrabold text-white leading-none tracking-tight">
          {{ $t('collections.heroTitle') }}
        </h1>
      </div>
    </section>

    <!-- Content panel -->
    <section class="relative z-10 bg-white rounded-t-2xl -mt-5 overflow-hidden">
      <div class="mx-auto max-w-6xl px-6 md:px-8 pt-16 pb-24">

        <!-- Accent -->
        <div class="flex items-center gap-3 mb-14">
          <div class="h-px w-10 bg-yellow-400"></div>
          <div class="h-1.5 w-1.5 rounded-full bg-yellow-400"></div>
          <div class="h-px w-10 bg-yellow-400"></div>
        </div>

        <!-- Gallery -->
        <div class="gallery-section">
          <SectionLabel>{{ $t('collections.galleryLabel') }}</SectionLabel>
          <h2 class="text-4xl font-extrabold text-gray-900 mb-2">{{ $t('collections.galleryTitle') }}</h2>
          <div class="h-px w-12 bg-yellow-400 mb-5"></div>
          <p class="text-gray-600 max-w-xl mb-8 leading-relaxed">{{ $t('collections.galleryBody') }}</p>

          <!-- Grid -->
          <div class="grid grid-cols-3 gap-2 max-w-2xl">
            <button
              v-for="(img, i) in galleryImages.slice(0, 6)"
              :key="i"
              class="overflow-hidden rounded-xl cursor-pointer group"
              style="aspect-ratio: 1;"
              :aria-label="`Open gallery image ${i + 1}`"
              @click="openLightbox(i)"
            >
              <img
                :src="img.src"
                :alt="img.alt"
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
                loading="lazy"
              />
            </button>
          </div>

          <button
            class="mt-6 inline-flex items-center gap-2 border border-gray-200 text-gray-800 font-medium px-6 py-3 text-sm rounded-xl hover:bg-gray-50 transition-colors"
            @click="openLightbox(0)"
          >
            {{ $t('collections.galleryCta') }}
            <span aria-hidden="true">→</span>
          </button>
        </div>

        <!-- Product Cards -->
        <div class="product-section mt-24">
          <SectionLabel>{{ $t('collections.productsLabel') }}</SectionLabel>
          <h2 class="text-4xl font-extrabold text-gray-900 mb-2">{{ $t('collections.productsTitle') }}</h2>
          <div class="h-px w-12 bg-yellow-400 mb-5"></div>
          <p class="text-gray-600 max-w-xl mb-10 leading-relaxed">{{ $t('collections.productsBody') }}</p>

          <!-- Expandable cards row -->
          <div class="flex gap-3 overflow-hidden rounded-2xl" style="height: 460px;">
            <button
              v-for="card in productCards"
              :key="card.id"
              class="relative overflow-hidden block transition-all duration-500 ease-in-out flex-1 text-left"
              :style="{ flex: hoveredCard === card.id ? 2.2 : 1 }"
              @mouseenter="hoveredCard = card.id"
              @mouseleave="hoveredCard = null"
            >
              <img
                :src="card.image"
                :alt="$t(card.titleKey)"
                class="absolute inset-0 w-full h-full object-cover transition-transform duration-500"
                :class="hoveredCard === card.id ? 'scale-105' : 'scale-100'"
                loading="lazy"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>

              <div class="absolute bottom-0 left-0 right-0 p-5">
                <p class="text-yellow-400 text-[10px] font-bold tracking-[0.2em] uppercase mb-1">
                  {{ $t(card.categoryKey) }}
                </p>
                <h3 class="text-white font-extrabold text-lg leading-tight">
                  {{ $t(card.titleKey) }}
                </h3>
                <p
                  class="text-white/60 text-sm leading-relaxed overflow-hidden transition-all duration-300"
                  :class="hoveredCard === card.id ? 'max-h-20 opacity-100 mt-2' : 'max-h-0 opacity-0'"
                >
                  {{ $t(card.descKey) }}
                </p>
                <div
                  class="mt-3 inline-flex items-center gap-1 text-yellow-400 text-xs font-bold tracking-wide transition-all duration-300"
                  :class="hoveredCard === card.id ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-2'"
                >
                  {{ $t('collections.viewCollection') }}
                  <span aria-hidden="true">→</span>
                </div>
              </div>
            </button>
          </div>
        </div>

      </div>
    </section>

    <!-- Lightbox -->
    <Teleport to="body">
      <div
        v-if="lightboxOpen"
        ref="lightboxEl"
        class="fixed inset-0 z-50 bg-black/95 flex flex-col outline-none"
        tabindex="0"
        @keydown.esc="closeLightbox"
        @keydown.left="lbNav(-1)"
        @keydown.right="lbNav(1)"
      >
        <button
          class="absolute top-5 right-6 z-10 text-white/50 hover:text-white transition-colors p-2"
          aria-label="Close gallery"
          @click="closeLightbox"
        >
          <X :size="26" />
        </button>

        <div
          ref="lbScroll"
          class="flex-1 flex overflow-x-scroll snap-x snap-mandatory scroll-smooth no-scrollbar gap-4 px-12 items-center pt-16"
          @scroll="onLbScroll"
        >
          <div
            v-for="(img, i) in galleryImages"
            :key="i"
            class="snap-center flex-shrink-0 flex items-center justify-center"
            style="width: min(80vw, 900px);"
          >
            <img
              :src="img.src"
              :alt="img.alt"
              class="max-w-full max-h-[78vh] w-full object-contain rounded-xl"
              loading="lazy"
            />
          </div>
        </div>

        <div class="flex items-center justify-center gap-8 pb-8 pt-4">
          <button
            :disabled="lbIndex === 0"
            class="text-white/50 hover:text-white transition-colors disabled:opacity-20"
            aria-label="Previous"
            @click="lbNav(-1)"
          >
            <ChevronLeft :size="36" stroke-width="1" />
          </button>
          <span class="text-white/40 text-sm tabular-nums">{{ lbIndex + 1 }} / {{ galleryImages.length }}</span>
          <button
            :disabled="lbIndex === galleryImages.length - 1"
            class="text-white/50 hover:text-white transition-colors disabled:opacity-20"
            aria-label="Next"
            @click="lbNav(1)"
          >
            <ChevronRight :size="36" stroke-width="1" />
          </button>
        </div>
      </div>
    </Teleport>

  </main>
</template>

<script setup lang="ts">
import { ref, nextTick } from 'vue'
import { X, ChevronLeft, ChevronRight } from 'lucide-vue-next'

useHead(() => ({ title: 'Collections — Winner Cabinets' }))

const galleryImages = [
  { src: '/images/nvTest.jpg',    alt: 'Kitchen cabinet project' },
  { src: '/images/storeTest.jpg', alt: 'Showroom display' },
  { src: '/images/pfTest.jpg',    alt: 'Cabinet detail' },
  { src: '/images/pencilPic.jpg', alt: 'Design planning' },
  { src: '/images/nvTest.jpg',    alt: 'Custom vanity' },
  { src: '/images/storeTest.jpg', alt: 'Installation' },
  { src: '/images/pfTest.jpg',    alt: 'Finished kitchen' },
  { src: '/images/pencilPic.jpg', alt: 'Workshop' },
]

const lightboxOpen = ref(false)
const lbIndex = ref(0)
const lbScroll = ref<HTMLElement | null>(null)
const lightboxEl = ref<HTMLElement | null>(null)
let lbManual = false
let lbTimer: ReturnType<typeof setTimeout> | null = null

const openLightbox = async (index: number) => {
  lbIndex.value = index
  lightboxOpen.value = true
  await nextTick()
  lightboxEl.value?.focus()
  scrollLbTo(index, 'instant')
}

const closeLightbox = () => { lightboxOpen.value = false }

const scrollLbTo = (index: number, behavior: ScrollBehavior = 'smooth') => {
  if (!lbScroll.value) return
  const target = lbScroll.value.children[index] as HTMLElement
  if (!target) return
  lbManual = true
  lbIndex.value = index
  target.scrollIntoView({ behavior, block: 'nearest', inline: 'center' })
  clearTimeout(lbTimer!)
  lbTimer = setTimeout(() => { lbManual = false }, 600)
}

const lbNav = (dir: number) => {
  const next = lbIndex.value + dir
  if (next < 0 || next >= galleryImages.length) return
  scrollLbTo(next)
}

const onLbScroll = () => {
  if (lbManual || !lbScroll.value) return
  clearTimeout(lbTimer!)
  lbTimer = setTimeout(() => {
    const c = lbScroll.value!
    const center = c.scrollLeft + c.clientWidth / 2
    let closest = 0, minDist = Infinity
    Array.from(c.children).forEach((child, i) => {
      const el = child as HTMLElement
      const dist = Math.abs(el.offsetLeft + el.offsetWidth / 2 - center)
      if (dist < minDist) { minDist = dist; closest = i }
    })
    lbIndex.value = closest
  }, 50)
}

const hoveredCard = ref<number | null>(null)

const productCards = [
  { id: 1, titleKey: 'collections.kitchenTitle', categoryKey: 'collections.kitchenCategory', descKey: 'collections.kitchenDesc', image: '/images/nvTest.jpg' },
  { id: 2, titleKey: 'collections.vanityTitle',  categoryKey: 'collections.vanityCategory',  descKey: 'collections.vanityDesc',  image: '/images/storeTest.jpg' },
  { id: 3, titleKey: 'collections.closetTitle',  categoryKey: 'collections.closetCategory',  descKey: 'collections.closetDesc',  image: '/images/pfTest.jpg' },
  { id: 4, titleKey: 'collections.millworkTitle', categoryKey: 'collections.millworkCategory', descKey: 'collections.millworkDesc', image: '/images/pencilPic.jpg' },
]
</script>
