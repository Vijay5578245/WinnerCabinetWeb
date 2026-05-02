<template>
  <section class="relative overflow-hidden bg-white">
    <!-- layered background decoration -->
    <div class="pointer-events-none absolute inset-0">
      <div
        class="absolute left-1/2 top-10 h-40 w-[42rem] -translate-x-1/2 rounded-3xl bg-yellow-50"
      />
      <p class="absolute text-[20px] md:text-[40px] left-1/2 top-15 md:top-20 text-lg font-bold text-gray-900 -translate-x-1/2">
        Our Advantage
      </p>
    </div>

    <div
      class="relative mx-auto max-w-6xl px-6 py-10 md:py-20 flex-col justify-center"
    >
      <!-- headline / focus point -->
      <div class="mb-10 md:mb-14">
        <p
          class="inline-flex items-center gap-2 rounded-[2px] bg-yellow-200/60 px-4 py-1 text-sm font-medium text-gray-900"
        >
          <span class="h-2 w-2 rounded-full bg-gray-900" />
          Our Advantage
        </p>
        <h2 class="mt-4 text-3xl tracking-tight text-gray-900 md:text-5xl"></h2>
      </div>

      <!-- content -->
      <div class="grid grid-cols-1 gap-10 md:grid-cols-12 md:gap-12 place-items-center">
        <!-- card side (layered) -->
        <div class="relative w-full md:col-span-5">
          <section class="flex flex-col items-center overflow-hidden rounded-lg">

              <Transition name="fade-slide" mode="out-in">
                <component
                  :is="cards[activeIndex]?.component"
                  :key="activeIndex"

                />
              </Transition>

          </section>

                <!-- dots -->
          <div class="mt-5 flex items-center justify-center gap-3">
              <button
                v-for="(card, index) in cards"
                :key="index"
                type="button"
                class="rounded-full transition-all duration-300 ease-in-out"
                :class="
                  activeIndex === index
                    ? 'bg-gray-900 w-10 h-2'
                    : 'bg-gray-300 hover:bg-gray-400 w-5 h-2'
                "
                :aria-label="`Go to slide ${index + 1}`"
                @click="activeIndex = index"
              />
            </div>
        </div>

        <!-- text side (more structure) -->
        <div class="relative w-full md:col-span-7 max-w-[560px] md:max-w-none">
          <div
            class="rounded-[7px] bg-white/70 p-7 shadow-sm ring-1 ring-black/5 backdrop-blur md:p-10"
          >
            <div class="absolute dotted-fade w-full h-full inset-0 -z-10"></div>
            <div class="flex items-center justify-between gap-4">
              <p class="text-sm font-medium text-gray-500">
                <span class="text-gray-900">0{{ activeIndex + 1 }}</span> / 0{{
                  cards.length
                }}
              </p>
              <div class="flex items-center gap-2">
                <button
                  class="inline-flex items-center gap-1.5 bg-yellow-400 hover:bg-yellow-500 text-black font-bold text-sm px-4 py-2 transition-colors"
                  style="border-radius: 10px;"
                  @click="prev"
                  aria-label="Previous slide"
                >
                  <ChevronLeft class="h-4 w-4" stroke-width="2.5" />
                  Prev
                </button>

                <button
                  class="inline-flex items-center gap-1.5 bg-yellow-400 hover:bg-yellow-500 text-black font-bold text-sm px-4 py-2 transition-colors"
                  style="border-radius: 10px;"
                  @click="next"
                  aria-label="Next slide"
                >
                  Next
                  <ChevronRight class="h-4 w-4" stroke-width="2.5" />
                </button>
              </div>
            </div>

            <Transition name="fade-slide" mode="out-in">
              <div :key="activeIndex" class="mt-6">
                <h3
                  class="text-2xl font-semibold leading-tight text-gray-900 md:text-4xl"
                >
                  {{ cards[activeIndex]?.title }}
                </h3>

                <div class="mt-4 h-px w-16 bg-yellow-300" />

                <p class="mt-5 text-base leading-relaxed text-gray-700 md:text-lg">
                  {{ cards[activeIndex]?.subtitle }}
                </p>
              </div>
            </Transition>
          </div>

        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, watch, nextTick } from "vue";
import { ChevronLeft, ChevronRight } from "lucide-vue-next";

const t = useI18n().t;

const activeIndex = ref(0);

const slideEls = ref<Array<HTMLElement | null>>([]);
const activeSlideHeight = ref<number>(0);

const setSlideRef = (el: Element | null, index: number) => {
  slideEls.value[index] = (el as HTMLElement) ?? null;
};

const measureActiveSlide = async () => {
  await nextTick();
  const el = slideEls.value[activeIndex.value];
  activeSlideHeight.value = el ? el.offsetHeight : 0;
};

watch(activeIndex, () => {
  measureActiveSlide();
});

import CardA from "@/components/ScrollCards/CardA.vue";
import CardB from "@/components/ScrollCards/CardB.vue";
import CardC from "@/components/ScrollCards/CardC.vue";

const cards = [
  {
    component: CardA,
    title: t("cards.cardA.title"),
    subtitle: t("cards.cardA.description"),
  },
  {
    component: CardB,
    title: t("cards.cardB.title"),
    subtitle: t("cards.cardB.description"),
  },
  {
    component: CardC,
    title: t("cards.cardC.title"),
    subtitle: t("cards.cardC.description"),
  },
];
const prev = () => {
  activeIndex.value = (activeIndex.value - 1 + cards.length) % cards.length;
};

const next = () => {
  activeIndex.value = (activeIndex.value + 1) % cards.length;
};

// initial measure
measureActiveSlide();
</script>

<style scoped>
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 0.28s ease, transform 0.28s ease;
}

.dotted-fade {
  background: radial-gradient(circle at 1px 1px, rgba(0, 0, 0, 0.15) 1px, transparent 0);
  background-size: 12px 12px;
  mask-image: linear-gradient(to bottom, transparent, black 10%, black 90%, transparent);
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
</style>
