<template>
  <section class="relative w-full max-w-9xl mx-auto pt-12 pb-6">
    <div
      class="text-black flex overflow-x-scroll snap-x snap-mandatory scroll-smooth gap-10 px-10 no-scrollbar"
      ref="scrollContainer"
      @scroll="onScroll"
    >
      <div
        v-for="(image, index) in images"
        :key="index"
        class="relative snap-center flex-shrink-0 h-64 md:h-full rounded-[10px] overflow-hidden shadow-lg"
        @click="scrollToSlide(index)"
      >
        <img :src="image.src" alt="image.alt" class="w-200 h-64 md:h-128 object-cover" />
        <div class="absolute inset-0 bg-black/20"></div>
      </div>
    </div>

    <div class="sticky w-fit mx-auto bottom-2 pb-5 pt-12">

    <div
      class="rounded-[2px] flex items-center space-x-4 p-5 bg-black/40 backdrop-blur-sm z-10"
    >
      <button
        v-for="(_, index) in images"
        :key="index"
        @click="scrollToSlide(index)"
        :class="[
          'w-3 h-3 rounded-full transition-all duration-300',
          activeIndex === index ? 'bg-white scale-110' : 'bg-white/50 hover:bg-white/80',
        ]"
        :aria-lable="`Go to the slide ${index + 1}`"
      ></button>
    </div>
</div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";

const images = ref([
  {
    src:
      "https://www.apple.com/v/iphone-17-pro/d/images/overview/highlights/highlights_chip_endframe__eisesoyz6gia_large_2x.jpg",
    alt: "Image 1",
  },
  { src: "/images/nvTest.jpg", alt: "Image 2" },
  {
    src:
      "https://www.apple.com/v/iphone-17-pro/d/images/overview/highlights/highlights_apple_intelligence__bs20h6298f36_large_2x.jpg",
    alt: "Image 3",
  },
  {
    src:
      "https://www.apple.com/ca/iphone-17-pro/images/overview/highlights/highlights_ios__empnwsdz698i_large_2x.jpg",
    alt: "Image 4",
  },
]);

const scrollContainer = ref<HTMLElement | null>(null);
const activeIndex = ref(0);
let isManualScroll = false;
let scrollTimeout: ReturnType<typeof setTimeout> | null = null;

// function to a specific slide when clicking the button

const scrollToSlide = (index: number) => {
  if (!scrollContainer.value) return;

  const container = scrollContainer.value;
  const slides = container.children;
  const targetSlide = slides[index] as HTMLElement;

  if (targetSlide) {
    isManualScroll = true;
    activeIndex.value = index;

    targetSlide.scrollIntoView({
      behavior: "smooth",
      block: "nearest",
      inline: "center",
    });

    clearTimeout(scrollTimeout!);

    scrollTimeout = setTimeout(() => {
      isManualScroll = false;
    }, 500);
  }
};


const onScroll = () => {
  if (isManualScroll || !scrollContainer.value) return;

  clearTimeout(scrollTimeout!);
  scrollTimeout = setTimeout(() => {
    const container = scrollContainer.value!;
    const containerCenter = container.scrollLeft + container.clientWidth / 2;

    let closestIndex = 0;
    let minDistance = Infinity;

    Array.from(container.children).forEach((child, index) => {
      const slide = child as HTMLElement;
      const slideCenter = slide.offsetLeft + slide.offsetWidth / 2;
      const distance = Math.abs(containerCenter - slideCenter);

      if (distance < minDistance) {
        minDistance = distance;
        closestIndex = index;
      }
    });

    activeIndex.value = closestIndex;
  }, 0); // Debounce scroll event for performance
};

// Clean up timeout on component unmount
onUnmounted(() => {
  clearTimeout(scrollTimeout!);
});




</script>

<style>
@layer utilities {
  /* Chrome, Safari, Edge */
  .no-scrollbar::-webkit-scrollbar {
    display: none;
  }

  /* Firefox */
  .no-scrollbar {
    scrollbar-width: none;
    -ms-overflow-style: none; /* IE/old Edge */
  }
}
</style>
