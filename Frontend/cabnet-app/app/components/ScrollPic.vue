<template>
  <section class="w-full max-w-9xl mx-auto pt-12 pb-6 bg-white">
    <div class="relative flex h-10 md:h-20 mb-10 items-center justify-center border-t border-gray-300 ">


<div class="absolute inset-0 bg-[radial-gradient(circle_at_1px_1px,rgba(0,0,0,0.15)_1px,transparent_0)]
            [mask-image:linear-gradient(to_bottom,black_80%,transparent)] [background-size:12px_12px]"></div>

        <h2 class="tracking-widest text-gray-700 text-black mx-auto">SMTH</h2>


      <div class="rounded-[2px] flex items-center p-5 z-10 absolute right-0 top-0 text-black">
        <button @click="scrollToSlide(activeIndex - 1)">
          <ChevronLeft :size="35" stroke-width="1" :color="leftEnd"/>
        </button>
        <p class="w-12 text-center">{{ activeIndex + 1 }} / {{ images.length }}</p>
        <button @click="scrollToSlide(activeIndex + 1)">
          <ChevronRight :size="35" stroke-width="1" :color="rightEnd"/>
        </button>
      </div>
    </div>
    <div
      class="text-black flex overflow-x-scroll snap-x snap-mandatory scroll-smooth gap-10 px-10 no-scrollbar"
      ref="scrollContainer"
      @scroll="onScroll"
    >
      <div
        v-for="(image, index) in images"
        :key="index"
        class="relative snap-center flex-shrink-0 w-[80vw] md:w-200 h-64 md:h-128 rounded-[10px] overflow-hidden shadow-lg"
        @click="scrollToSlide(index)"
      >
        <img :src="image.src" alt="image.alt" class="w-full h-full object-cover" />
        <div class="absolute inset-0 bg-black/20"></div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from "vue";
import { ChevronLeft, ChevronRight } from "lucide-vue-next";

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
const leftEnd = computed(() => activeIndex.value === 0 ? "gray" : "black");
const rightEnd = computed(() => activeIndex.value === images.value.length - 1 ? "gray" : "black");

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
