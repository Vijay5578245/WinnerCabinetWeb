<template>
  <section class="relative overflow-hidden bg-gray-50 py-24">
    <div class="mx-auto max-w-7xl px-6 md:px-8">

      <div class="grid grid-cols-1 gap-12 md:grid-cols-2 md:gap-16 items-center">

        <!-- Visual card -->
        <div class="w-full">
          <Transition name="fade-slide" mode="out-in">
            <component :is="cards[activeIndex].component" :key="activeIndex" />
          </Transition>

          <!-- Dot nav -->
          <div class="mt-5 flex items-center gap-2">
            <button
              v-for="(_, i) in cards"
              :key="i"
              class="rounded-full transition-all duration-300"
              :class="activeIndex === i ? 'bg-gray-900 w-8 h-2' : 'bg-gray-300 w-4 h-2 hover:bg-gray-400'"
              :aria-label="`Go to slide ${i + 1}`"
              @click="activeIndex = i"
            />
          </div>
        </div>

        <!-- Text content -->
        <div class="relative">
          <div class="rounded-2xl bg-white p-8 shadow-sm ring-1 ring-black/5 md:p-10">
            <!-- Counter + controls -->
            <div class="flex items-center justify-between mb-6">
              <p class="text-sm text-gray-400 tabular-nums">
                <span class="text-gray-900 font-bold">0{{ activeIndex + 1 }}</span>
                &nbsp;/&nbsp;0{{ cards.length }}
              </p>
              <div class="flex items-center gap-2">
                <button
                  class="flex items-center gap-1 bg-yellow-400 hover:bg-yellow-500 text-black font-bold text-xs px-4 py-2 rounded-lg transition-colors"
                  aria-label="Previous slide"
                  @click="prev"
                >
                  <ChevronLeft class="h-3.5 w-3.5" stroke-width="2.5" />
                  Prev
                </button>
                <button
                  class="flex items-center gap-1 bg-yellow-400 hover:bg-yellow-500 text-black font-bold text-xs px-4 py-2 rounded-lg transition-colors"
                  aria-label="Next slide"
                  @click="next"
                >
                  Next
                  <ChevronRight class="h-3.5 w-3.5" stroke-width="2.5" />
                </button>
              </div>
            </div>

            <Transition name="fade-slide" mode="out-in">
              <div :key="activeIndex">
                <h3 class="text-2xl font-extrabold text-gray-900 leading-tight md:text-3xl">
                  {{ cards[activeIndex].title }}
                </h3>
                <div class="mt-4 h-px w-12 bg-yellow-400"></div>
                <p class="mt-5 text-base leading-relaxed text-gray-600">
                  {{ cards[activeIndex].subtitle }}
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
import { ref } from 'vue'
import { ChevronLeft, ChevronRight } from 'lucide-vue-next'
import CardA from '@/components/FeatureCards/CardA.vue'
import CardB from '@/components/FeatureCards/CardB.vue'
import CardC from '@/components/FeatureCards/CardC.vue'

const { t } = useI18n()

const activeIndex = ref(0)

const cards = [
  { component: CardA, title: t('cards.cardA.title'), subtitle: t('cards.cardA.description') },
  { component: CardB, title: t('cards.cardB.title'), subtitle: t('cards.cardB.description') },
  { component: CardC, title: t('cards.cardC.title'), subtitle: t('cards.cardC.description') },
]

const prev = () => { activeIndex.value = (activeIndex.value - 1 + cards.length) % cards.length }
const next = () => { activeIndex.value = (activeIndex.value + 1) % cards.length }
</script>
