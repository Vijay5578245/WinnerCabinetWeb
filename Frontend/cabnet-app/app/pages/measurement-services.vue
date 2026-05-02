<template>
  <main class="bg-white min-h-screen">
    <section class="max-w-4xl mx-auto px-6 py-20">
      <div class="flex items-center gap-3 mb-8">
        <div class="h-px w-10 bg-yellow-400"></div>
        <p class="text-yellow-400 text-xs font-bold tracking-[0.2em] uppercase">Frequently Asked Questions</p>
      </div>
      <h1 class="text-4xl md:text-5xl font-extrabold text-black mb-12 leading-tight">
        Measurement Services<br />— FAQ
      </h1>

      <div class="space-y-4">
        <div
          v-for="(faq, i) in faqs"
          :key="i"
          class="border border-gray-100 shadow-sm overflow-hidden"
          style="border-radius: 10px;"
        >
          <button
            class="w-full flex items-center justify-between px-6 py-5 text-left hover:bg-gray-50 transition-colors"
            @click="openFaq = openFaq === i ? null : i"
          >
            <span class="font-bold text-black text-sm pr-4">{{ faq.q }}</span>
            <span class="shrink-0 text-yellow-400 text-lg font-bold">{{ openFaq === i ? '−' : '+' }}</span>
          </button>
          <div v-show="openFaq === i" class="px-6 pb-5 text-gray-500 text-sm leading-relaxed border-t border-gray-100 pt-4">
            {{ faq.a }}
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
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
