<template>
  <main class="relative z-10 bg-white min-h-screen overflow-x-hidden">

    <!-- Hero banner -->
    <section class="relative bg-gray-950 pt-32 pb-20 px-6 overflow-hidden">
      <div class="dot-pattern absolute inset-0 opacity-20 pointer-events-none"></div>
      <div class="relative z-10 mx-auto max-w-4xl">
        <div class="flex items-center gap-3 mb-8">
          <div class="h-px w-10 bg-yellow-400"></div>
          <SectionLabel class="text-yellow-400">{{ $t('measurement.label') }}</SectionLabel>
        </div>
        <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-6 leading-tight">
          {{ $t('measurement.title') }}
        </h1>
        <p class="text-white/60 max-w-xl leading-relaxed">
          {{ $t('measurement.heroBody') }}
        </p>
      </div>
    </section>

    <!-- FAQ -->
    <section class="mx-auto max-w-4xl px-6 md:px-8 py-20">
      <div class="space-y-3">
        <div
          v-for="(faq, i) in faqs"
          :key="i"
          class="border border-gray-100 rounded-xl overflow-hidden shadow-sm"
        >
          <button
            class="w-full flex items-center justify-between px-6 py-5 text-left hover:bg-gray-50 transition-colors"
            :aria-expanded="openFaq === i"
            @click="openFaq = openFaq === i ? null : i"
          >
            <span class="font-bold text-gray-900 text-sm pr-4">{{ faq.q }}</span>
            <span class="shrink-0 text-yellow-500 text-xl font-bold leading-none">{{ openFaq === i ? '−' : '+' }}</span>
          </button>
          <div
            v-show="openFaq === i"
            class="px-6 pb-5 text-gray-500 text-sm leading-relaxed border-t border-gray-100 pt-4"
          >{{ faq.a }}</div>
        </div>
      </div>

      <!-- CTA -->
      <div class="mt-16 p-8 bg-yellow-50 rounded-2xl border border-yellow-200">
        <h2 class="text-xl font-extrabold text-gray-900 mb-3">Ready to get started?</h2>
        <p class="text-gray-600 text-sm mb-5 leading-relaxed">
          Stop by our Richmond showroom or give us a call to schedule a measurement appointment at a time that works for you.
        </p>
        <div class="flex flex-wrap gap-3">
          <AppButton to="/hours-and-location" size="sm">
            Find Our Showroom
          </AppButton>
          <a
            href="tel:(604) 270-4505"
            class="inline-flex items-center gap-2 border border-gray-300 text-gray-800 font-medium px-5 py-2.5 text-sm rounded-sm hover:bg-white transition-colors"
          >
            (604) 270-4505
          </a>
        </div>
      </div>
    </section>

  </main>
</template>

<script setup lang="ts">
import { ref } from 'vue'

useHead(() => ({ title: 'Measurement Services — Winner Cabinets' }))

const openFaq = ref<number | null>(null)

const faqs = [
  {
    q: 'What is the professional measurement service?',
    a: 'Our professional measurement service sends a trained specialist to your home to take precise measurements of your kitchen or bathroom space, ensuring your cabinet order fits perfectly.',
  },
  {
    q: 'Is the measurement service free?',
    a: 'Please visit our showroom or call us for current pricing on the measurement service. In many cases, the fee is credited toward your cabinet purchase.',
  },
  {
    q: 'How long does a measurement appointment take?',
    a: 'Most residential kitchens take between 30 and 60 minutes. Larger spaces or custom layouts may take a bit longer.',
  },
  {
    q: 'Do I need to prepare anything before the appointment?',
    a: 'Make sure the space is accessible and, if possible, clear appliances or furniture away from the walls. Having any existing floor plans on hand is also helpful.',
  },
  {
    q: 'How do I book a measurement appointment?',
    a: 'Stop by our Richmond showroom or give us a call at (604) 270-4505 to schedule a time that works for you.',
  },
]
</script>
