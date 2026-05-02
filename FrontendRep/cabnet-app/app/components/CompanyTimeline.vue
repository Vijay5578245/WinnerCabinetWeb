<template>
  <section ref="containerRef" class="relative w-full bg-white py-24 overflow-hidden">

    <!-- Header -->
    <div class="mx-auto max-w-7xl px-6 md:px-8 mb-16">
      <SectionLabel>{{ $t('about.storyLabel') }}</SectionLabel>
      <h2 class="text-4xl md:text-5xl font-extrabold text-gray-900 leading-tight">
        {{ $t('about.storyHeadline') }}
      </h2>
      <div class="mt-5 h-px w-16 bg-yellow-400"></div>
    </div>

    <!-- Timeline body -->
    <div class="relative mx-auto max-w-7xl px-6 md:px-8">
      <!-- Track (grey) -->
      <div
        class="absolute left-[35px] md:left-[95px] top-0 bottom-0 w-px bg-gray-150"
        aria-hidden="true"
      ></div>

      <!-- Animated progress (yellow glow) -->
      <div
        ref="lineRef"
        class="timeline-progress-line absolute left-[35px] md:left-[95px] top-0 w-px origin-top"
        style="height: 0%"
        aria-hidden="true"
      ></div>

      <div class="flex flex-col gap-0">
        <div
          v-for="(entry, i) in timeline"
          :key="i"
          class="timeline-entry relative flex gap-6 md:gap-12 pl-16 md:pl-[152px] pb-20"
        >
          <!-- Dot -->
          <div
            class="timeline-dot absolute left-[22px] md:left-[82px] top-1 w-7 h-7 rounded-full border-2 border-gray-150 bg-white flex items-center justify-center z-10"
          >
            <div class="w-2.5 h-2.5 rounded-full bg-gray-300 timeline-dot-inner"></div>
          </div>

          <!-- Year (desktop, left of track) -->
          <div class="absolute left-0 top-0 hidden md:flex flex-col items-end pr-5 w-[74px]">
            <span class="text-[11px] font-black tracking-widest text-gray-400 timeline-year leading-none">
              {{ entry.year }}
            </span>
          </div>

          <!-- Content card -->
          <div class="timeline-card flex-1 min-w-0">
            <!-- Year (mobile) -->
            <span class="md:hidden text-[11px] font-black tracking-widest text-yellow-500 uppercase mb-2 block timeline-year">
              {{ entry.year }}
            </span>

            <div class="rounded-2xl border border-gray-100 bg-gray-50/60 overflow-hidden shadow-sm">

              <!-- Images -->
              <div
                v-if="entry.images.length"
                class="grid gap-px"
                :class="entry.images.length > 1 ? 'grid-cols-2' : 'grid-cols-1'"
              >
                <div
                  v-for="(img, j) in entry.images"
                  :key="j"
                  class="overflow-hidden"
                  :class="entry.images.length === 1 ? 'h-52 md:h-64' : 'h-40 md:h-52'"
                >
                  <img :src="img" alt="" class="w-full h-full object-cover" loading="lazy" />
                </div>
              </div>

              <!-- Body -->
              <div class="p-6 md:p-8">
                <div v-if="entry.stat" class="mb-5 flex items-end gap-3">
                  <span class="text-5xl md:text-6xl font-black text-yellow-400 leading-none">{{ entry.stat.value }}</span>
                  <span class="text-sm font-semibold text-gray-500 mb-1.5 leading-tight whitespace-pre-line">{{ entry.stat.label }}</span>
                </div>

                <h3 class="text-xl md:text-2xl font-extrabold text-gray-900 mb-3 leading-snug">
                  {{ entry.title }}
                </h3>
                <p class="text-gray-600 leading-relaxed text-base">{{ entry.description }}</p>

                <div v-if="entry.tags.length" class="mt-5 flex flex-wrap gap-2">
                  <span
                    v-for="tag in entry.tags"
                    :key="tag"
                    class="rounded-full bg-white border border-gray-200 px-3 py-1 text-xs font-semibold text-gray-600 tracking-wide"
                  >{{ tag }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const containerRef = ref<HTMLElement | null>(null)
const lineRef = ref<HTMLElement | null>(null)

const timeline = [
  {
    year: '2012',
    title: 'Where It All Began',
    description: 'Eric Chen founded Winner Cabinets with a single workshop and a belief that every home deserves cabinets built with care. The first commissions were local kitchen renovations — small in scale, but the start of something lasting.',
    images: ['/images/nvTest.jpg'],
    tags: ['Founded', 'Vancouver'],
    stat: null,
  },
  {
    year: '2015',
    title: 'Expanding the Workshop',
    description: 'Growing demand led to a larger facility and a dedicated team of craftsmen. We began taking on commercial millwork projects alongside residential work, doubling our capacity and range of finishes.',
    images: ['/images/nvTest.jpg', '/images/storeTest.jpg'],
    tags: ['Expansion', 'Commercial Projects'],
    stat: { value: '2×', label: 'capacity\nincreased' },
  },
  {
    year: '2018',
    title: 'Custom Design Studio Opens',
    description: 'We launched our in-house design studio, giving clients a hands-on showroom experience to select materials, hardware, and layouts before a single board is cut. Transparent pricing became our signature.',
    images: ['/images/storeTest.jpg'],
    tags: ['Design Studio', 'Showroom'],
    stat: null,
  },
  {
    year: '2021',
    title: 'Weathering the Storm',
    description: 'Through supply chain disruptions, we doubled down on local sourcing — partnering with regional suppliers to maintain quality and keep lead times predictable for every client.',
    images: ['/images/nvTest.jpg', '/images/pencilPic.jpg'],
    tags: ['Local Materials', 'Resilience'],
    stat: { value: '100%', label: 'local\nsourcing' },
  },
  {
    year: '2024',
    title: 'Trusted by Hundreds of Families',
    description: 'Today Winner Cabinets has delivered over 500 custom projects across Metro Vancouver. From starter condos to large estates, the same precision and personal service Eric started with still drives every build.',
    images: ['/images/pfTest.jpg'],
    tags: ['500+ Projects', 'Metro Vancouver'],
    stat: { value: '500+', label: 'projects\ncompleted' },
  },
]

let ctx: import('gsap').Context | null = null
let onLoadCb: (() => void) | null = null

onMounted(async () => {
  const { gsap } = await import('gsap')
  const { ScrollTrigger } = await import('gsap/ScrollTrigger')

  const container = containerRef.value
  const line = lineRef.value
  if (!container || !line) return

  ctx = gsap.context(() => {
    gsap.to(line, {
      height: '100%',
      ease: 'none',
      scrollTrigger: {
        trigger: container,
        start: 'top 80%',
        end: 'bottom 20%',
        scrub: 0.6,
        invalidateOnRefresh: true,
      },
    })

    container.querySelectorAll('.timeline-entry').forEach((entry) => {
      const card = entry.querySelector('.timeline-card')
      const dot = entry.querySelector('.timeline-dot')
      const dotInner = entry.querySelector('.timeline-dot-inner')
      const years = entry.querySelectorAll('.timeline-year')

      gsap.set([card, ...Array.from(years)], { autoAlpha: 0, y: 20 })
      gsap.set(dot, { scale: 0.4 })

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: entry,
          start: 'top 82%',
          toggleActions: 'play none none reverse',
          invalidateOnRefresh: true,
        },
      })

      tl.to(dot, { scale: 1, duration: 0.4, ease: 'back.out(2)' })
        .to(dotInner, { backgroundColor: '#f59e0b', duration: 0.3 }, '<0.05')
        .to(years, { autoAlpha: 1, y: 0, duration: 0.45, ease: 'power2.out' }, '<')
        .to(card, { autoAlpha: 1, y: 0, duration: 0.5, ease: 'power2.out' }, '<0.08')
    })
  }, container)

  if (document.readyState === 'complete') {
    ScrollTrigger.refresh()
  } else {
    onLoadCb = () => ScrollTrigger.refresh()
    window.addEventListener('load', onLoadCb)
  }
})

onUnmounted(() => {
  ctx?.revert()
  if (onLoadCb) window.removeEventListener('load', onLoadCb)
})
</script>
