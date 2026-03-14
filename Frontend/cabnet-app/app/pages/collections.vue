<template>
  <main>
    <!-- Hero -->
    <section class="relative h-[55vh] overflow-hidden">
      <img
        src="/images/nvTest.jpg"
        alt="Collections hero"
        class="absolute inset-0 w-full h-full object-cover"
        loading="lazy"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/30 to-transparent"></div>
      <div class="absolute bottom-0 left-0 px-8 pb-10 max-w-4xl">
        <p class="text-yellow-400 text-xs font-bold tracking-[0.2em] uppercase mb-3">Explore</p>
        <h1 class="text-4xl md:text-6xl font-extrabold text-white leading-tight">Our Collections</h1>
      </div>
    </section>

    <!-- Page body -->
    <section class="relative z-10 bg-white -mt-4 overflow-hidden" style="border-radius: 10px 10px 0 0;">
      <div class="absolute inset-0 bg-gradient-to-b from-amber-50 via-yellow-50/40 to-white pointer-events-none"></div>

      <div class="relative max-w-6xl mx-auto px-6 pt-16 pb-24">

        <!-- Decorative accent -->
        <div class="flex items-center gap-3 mb-12">
          <div class="h-px w-10 bg-yellow-400"></div>
          <div class="h-1.5 w-1.5 rounded-full bg-yellow-400"></div>
          <div class="h-px w-10 bg-yellow-400"></div>
        </div>

        <!-- ───────────────── GALLERY SECTION ───────────────── -->
        <div>
          <p class="text-yellow-500 text-xs font-bold tracking-[0.2em] uppercase mb-3">Our Work</p>
          <h2 class="text-4xl font-extrabold text-black mb-2">Project Gallery</h2>
          <div class="h-1 w-12 bg-yellow-400 mb-6"></div>
          <p class="text-gray-600 max-w-xl mb-8 leading-relaxed">
            A glimpse of the custom cabinet projects we've completed for our clients across the Lower Mainland.
          </p>

          <!-- Thumbnail grid -->
          <div class="grid grid-cols-3 gap-3 max-w-2xl">
            <div
              v-for="(img, i) in galleryImages.slice(0, 6)"
              :key="i"
              class="overflow-hidden cursor-pointer group"
              style="border-radius: 10px; aspect-ratio: 1;"
              @click="openLightbox(i)"
            >
              <img
                :src="img.src"
                :alt="img.alt"
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
              />
            </div>
          </div>

          <button
            @click="openLightbox(0)"
            class="mt-6 inline-flex items-center gap-2 border border-gray-300 text-black font-medium px-6 py-3 text-sm hover:bg-gray-50 transition-colors"
            style="border-radius: 10px;"
          >
            See all photos <span aria-hidden="true">→</span>
          </button>
        </div>

        <!-- ───────────────── EXPANDABLE CARDS ───────────────── -->
        <div class="mt-24">
          <p class="text-yellow-500 text-xs font-bold tracking-[0.2em] uppercase mb-3">What We Build</p>
          <h2 class="text-4xl font-extrabold text-black mb-2">Our Products</h2>
          <div class="h-1 w-12 bg-yellow-400 mb-6"></div>
          <p class="text-gray-600 max-w-xl mb-10 leading-relaxed">
            From kitchen cabinetry to bathroom vanities, explore our range of custom-built collections.
          </p>

          <div class="flex gap-3 h-[480px]">
            <a
              v-for="card in productCards"
              :key="card.id"
              :href="card.link"
              target="_blank"
              rel="noopener"
              class="relative overflow-hidden block transition-all duration-500 ease-in-out"
              style="border-radius: 10px; flex: 1;"
              :style="{ flex: hoveredCard === card.id ? '2' : '1' }"
              @mouseenter="hoveredCard = card.id"
              @mouseleave="hoveredCard = null"
            >
              <img
                :src="card.image"
                :alt="card.title"
                class="absolute inset-0 w-full h-full object-cover transition-transform duration-500"
                :class="hoveredCard === card.id ? 'scale-105' : 'scale-100'"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>

              <div class="absolute bottom-0 left-0 right-0 p-5">
                <p class="text-yellow-400 text-[10px] font-bold tracking-[0.2em] uppercase mb-1">{{ card.category }}</p>
                <h3 class="text-white font-extrabold text-lg leading-tight">{{ card.title }}</h3>
                <p
                  class="text-white/60 text-sm leading-relaxed transition-all duration-300 overflow-hidden"
                  :class="hoveredCard === card.id ? 'max-h-20 opacity-100 mt-2' : 'max-h-0 opacity-0'"
                >
                  {{ card.description }}
                </p>
                <div
                  class="mt-3 inline-flex items-center gap-1 text-yellow-400 text-xs font-bold tracking-wide transition-all duration-300"
                  :class="hoveredCard === card.id ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-2'"
                >
                  View Collection <span aria-hidden="true">→</span>
                </div>
              </div>
            </a>
          </div>
        </div>

      </div>
    </section>

    <!-- ───────────────── FULLSCREEN LIGHTBOX ───────────────── -->
    <Teleport to="body">
      <div
        v-if="lightboxOpen"
        class="fixed inset-0 z-50 bg-black/95 flex flex-col outline-none"
        tabindex="0"
        ref="lightboxEl"
        @keydown.esc="closeLightbox"
        @keydown.left="lightboxNav(-1)"
        @keydown.right="lightboxNav(1)"
      >
        <!-- Close -->
        <button
          @click="closeLightbox"
          class="absolute top-5 right-6 z-10 text-white/50 hover:text-white transition-colors p-2"
          aria-label="Close gallery"
        >
          <X :size="28" />
        </button>

        <!-- Slides -->
        <div
          class="flex-1 flex overflow-x-scroll snap-x snap-mandatory scroll-smooth no-scrollbar gap-6 px-12 items-center pt-16"
          ref="lightboxScroll"
          @scroll="onLightboxScroll"
        >
          <div
            v-for="(img, i) in galleryImages"
            :key="i"
            class="snap-center flex-shrink-0 w-[80vw] md:w-[70vw] flex items-center justify-center"
          >
            <img
              :src="img.src"
              :alt="img.alt"
              class="max-w-full max-h-[75vh] w-full object-contain"
              style="border-radius: 10px;"
            />
          </div>
        </div>

        <!-- Prev / Next -->
        <div class="flex items-center justify-center gap-8 pb-8 pt-4">
          <button
            @click="lightboxNav(-1)"
            :disabled="lightboxIndex === 0"
            class="text-white/50 hover:text-white transition-colors disabled:opacity-20"
            aria-label="Previous"
          >
            <ChevronLeft :size="36" stroke-width="1" />
          </button>
          <button
            @click="lightboxNav(1)"
            :disabled="lightboxIndex === galleryImages.length - 1"
            class="text-white/50 hover:text-white transition-colors disabled:opacity-20"
            aria-label="Next"
          >
            <ChevronRight :size="36" stroke-width="1" />
          </button>
        </div>
      </div>
    </Teleport>

    <Footer />
  </main>
</template>

<script setup lang="ts">
import { ref, nextTick } from 'vue';
import { ChevronLeft, ChevronRight, X } from 'lucide-vue-next';

const galleryImages = [
  { src: '/images/nvTest.jpg',    alt: 'Kitchen cabinet project' },
  { src: '/images/storeTest.jpg', alt: 'Showroom display' },
  { src: '/images/pfTest.jpg',    alt: 'Cabinet detail' },
  { src: '/images/pencilPic.jpg', alt: 'Design planning' },
  { src: '/images/nvTest.jpg',    alt: 'Custom vanity' },
  { src: '/images/storeTest.jpg', alt: 'Installation' },
  { src: '/images/pfTest.jpg',    alt: 'Finished kitchen' },
  { src: '/images/pencilPic.jpg', alt: 'Workshop' },
];

// Lightbox state
const lightboxOpen  = ref(false);
const lightboxIndex = ref(0);
const lightboxScroll = ref<HTMLElement | null>(null);
const lightboxEl     = ref<HTMLElement | null>(null);

let lbManual = false;
let lbTimeout: ReturnType<typeof setTimeout> | null = null;

const openLightbox = async (index: number) => {
  lightboxIndex.value = index;
  lightboxOpen.value  = true;
  await nextTick();
  lightboxEl.value?.focus();
  scrollLightboxTo(index, 'instant');
};

const closeLightbox = () => {
  lightboxOpen.value = false;
};

const scrollLightboxTo = (index: number, behavior: ScrollBehavior = 'smooth') => {
  if (!lightboxScroll.value) return;
  const target = lightboxScroll.value.children[index] as HTMLElement;
  if (!target) return;
  lbManual = true;
  lightboxIndex.value = index;
  target.scrollIntoView({ behavior, block: 'nearest', inline: 'center' });
  clearTimeout(lbTimeout!);
  lbTimeout = setTimeout(() => { lbManual = false; }, 600);
};

const lightboxNav = (dir: number) => {
  const next = lightboxIndex.value + dir;
  if (next < 0 || next >= galleryImages.length) return;
  scrollLightboxTo(next);
};

const onLightboxScroll = () => {
  if (lbManual || !lightboxScroll.value) return;
  clearTimeout(lbTimeout!);
  lbTimeout = setTimeout(() => {
    const c = lightboxScroll.value!;
    const center = c.scrollLeft + c.clientWidth / 2;
    let closest = 0, minDist = Infinity;
    Array.from(c.children).forEach((child, i) => {
      const el = child as HTMLElement;
      const dist = Math.abs(el.offsetLeft + el.offsetWidth / 2 - center);
      if (dist < minDist) { minDist = dist; closest = i; }
    });
    lightboxIndex.value = closest;
  }, 50);
};

// Expandable cards
const hoveredCard = ref<number | null>(null);

const productCards = [
  {
    id: 1,
    title: 'Kitchen Cabinetry',
    category: 'Kitchens',
    description: 'Custom-built kitchen cabinets designed for your layout and style.',
    image: '/images/nvTest.jpg',
    link: '/collections',
  },
  {
    id: 2,
    title: 'Bathroom Vanities',
    category: 'Bathrooms',
    description: 'Elegant vanity solutions that maximize space and elevate your bathroom.',
    image: '/images/storeTest.jpg',
    link: '/collections',
  },
  {
    id: 3,
    title: 'Closet Systems',
    category: 'Storage',
    description: 'Smart closet designs with full customization for any room size.',
    image: '/images/pfTest.jpg',
    link: '/collections',
  },
  {
    id: 4,
    title: 'Custom Millwork',
    category: 'Specialty',
    description: 'Built-ins, entertainment units, and bespoke pieces for any space.',
    image: '/images/pencilPic.jpg',
    link: '/collections',
  },
];
</script>

<style scoped>
main {
  border-radius: 10px;
}
</style>
