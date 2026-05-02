<template>
  <section class="w-full pb-8">
    <!-- Controls bar -->
    <div class="relative flex h-14 items-center border-t border-gray-200 mb-6 px-6 md:px-0">
      <div class="absolute inset-0 dot-pattern-fade opacity-60 pointer-events-none"></div>
      <div class="absolute right-0 top-0 flex items-center h-full pr-6 md:pr-0 z-10">
        <button
          class="p-1 transition-colors disabled:opacity-25 hover:text-yellow-500"
          :disabled="activeIndex === 0"
          aria-label="Previous image"
          @click="go(activeIndex - 1)"
        >
          <ChevronLeft :size="28" stroke-width="1.5" />
        </button>
        <span class="w-16 text-center text-sm text-gray-500 tabular-nums">
          {{ activeIndex + 1 }} / {{ images.length }}
        </span>
        <button
          class="p-1 transition-colors disabled:opacity-25 hover:text-yellow-500"
          :disabled="activeIndex === images.length - 1"
          aria-label="Next image"
          @click="go(activeIndex + 1)"
        >
          <ChevronRight :size="28" stroke-width="1.5" />
        </button>
      </div>
    </div>

    <!-- Scroll strip -->
    <div
      ref="track"
      class="flex overflow-x-scroll snap-x snap-mandatory scroll-smooth gap-4 px-6 no-scrollbar"
      @scroll="onScroll"
    >
      <div
        v-for="(img, i) in images"
        :key="i"
        class="snap-center flex-shrink-0 relative overflow-hidden rounded-xl cursor-pointer"
        style="width: min(80vw, 780px); height: clamp(220px, 40vw, 500px);"
        @click="go(i)"
      >
        <img
          :src="img.src"
          :alt="img.alt"
          class="w-full h-full object-cover transition-transform duration-500"
          :class="activeIndex === i ? 'scale-100' : 'scale-105'"
          loading="lazy"
        />
        <div class="absolute inset-0 bg-black/15 transition-opacity duration-300" :class="activeIndex === i ? 'opacity-0' : 'opacity-100'"></div>
      </div>
    </div>

    <!-- Dot indicator -->
    <div class="flex justify-center gap-2 mt-5">
      <button
        v-for="(_, i) in images"
        :key="i"
        class="rounded-full transition-all duration-300"
        :class="activeIndex === i ? 'bg-gray-900 w-6 h-1.5' : 'bg-gray-300 w-3 h-1.5 hover:bg-gray-400'"
        :aria-label="`Go to image ${i + 1}`"
        @click="go(i)"
      />
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onUnmounted } from 'vue'
import { ChevronLeft, ChevronRight } from 'lucide-vue-next'

const images = [
  { src: '/images/storeTest.jpg', alt: 'Winner Cabinets showroom interior' },
  { src: '/images/nvTest.jpg',    alt: 'Custom kitchen cabinetry' },
  { src: '/images/pfTest.jpg',    alt: 'Cabinet detail craftsmanship' },
  { src: '/images/pencilPic.jpg', alt: 'Design planning process' },
]

const track = ref<HTMLElement | null>(null)
const activeIndex = ref(0)
let manualFlag = false
let debounceTimer: ReturnType<typeof setTimeout> | null = null

const go = (index: number) => {
  if (!track.value) return
  const clamped = Math.max(0, Math.min(index, images.length - 1))
  const slide = track.value.children[clamped] as HTMLElement
  if (!slide) return

  manualFlag = true
  activeIndex.value = clamped
  slide.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' })

  clearTimeout(debounceTimer!)
  debounceTimer = setTimeout(() => { manualFlag = false }, 600)
}

const onScroll = () => {
  if (manualFlag || !track.value) return
  clearTimeout(debounceTimer!)
  debounceTimer = setTimeout(() => {
    const el = track.value!
    const center = el.scrollLeft + el.clientWidth / 2
    let closest = 0
    let minDist = Infinity
    Array.from(el.children).forEach((child, i) => {
      const c = child as HTMLElement
      const dist = Math.abs(c.offsetLeft + c.offsetWidth / 2 - center)
      if (dist < minDist) { minDist = dist; closest = i }
    })
    activeIndex.value = closest
  }, 60)
}

onUnmounted(() => { clearTimeout(debounceTimer!) })
</script>
