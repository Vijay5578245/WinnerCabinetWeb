<template>
  <main class="bg-white min-h-screen overflow-x-hidden">

    <!-- Hero -->
    <section class="relative h-[55dvh] overflow-hidden">
      <img
        src="/images/storeTest.jpg"
        alt="Winner Cabinets showroom"
        class="absolute inset-0 w-full h-full object-cover"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/30 to-transparent"></div>
      <div class="absolute bottom-0 left-0 px-8 md:px-12 pb-12 max-w-4xl">
        <SectionLabel class="text-yellow-400">{{ $t('hours.heroLabel') }}</SectionLabel>
        <h1 class="text-5xl md:text-6xl font-extrabold text-white leading-none tracking-tight">
          {{ $t('hours.heroTitle') }}
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

        <!-- Showroom info -->
        <div class="grid md:grid-cols-2 gap-12 items-start mb-20">
          <div>
            <SectionLabel>{{ $t('hours.showroomLabel') }}</SectionLabel>
            <h2 class="text-4xl font-extrabold text-gray-900 mb-2">{{ $t('hours.showroomName') }}</h2>
            <div class="h-px w-12 bg-yellow-400 mb-8"></div>

            <div class="mb-5">
              <p class="text-[10px] font-bold tracking-[0.2em] uppercase text-gray-400 mb-1">{{ $t('hours.addressLabel') }}</p>
              <p class="text-gray-700 text-base leading-relaxed">
                160 – 4551 No 3 Rd<br />Richmond, BC V6X 2C3
              </p>
            </div>

            <div class="mb-8">
              <p class="text-[10px] font-bold tracking-[0.2em] uppercase text-gray-400 mb-1">{{ $t('hours.phoneLabel') }}</p>
              <a
                :href="'tel:' + showroom.phone"
                class="text-gray-900 font-semibold text-base hover:text-yellow-500 transition-colors"
              >{{ showroom.phone }}</a>
            </div>

            <div class="flex flex-wrap gap-3">
              <a
                :href="showroom.mapUrl"
                target="_blank"
                rel="noopener noreferrer"
                class="inline-flex items-center gap-2 bg-yellow-400 hover:bg-yellow-500 text-black font-bold px-6 py-3 text-sm rounded-xl transition-colors"
              >
                {{ $t('hours.mapCta') }}
                <span aria-hidden="true">→</span>
              </a>
              <a
                :href="'tel:' + showroom.phone"
                class="inline-flex items-center gap-2 border border-gray-200 text-gray-800 font-medium px-6 py-3 text-sm rounded-xl hover:bg-gray-50 transition-colors"
              >
                {{ $t('hours.callCta') }}
              </a>
            </div>
          </div>

          <div class="overflow-hidden rounded-2xl shadow-lg">
            <img
              :src="showroom.image"
              :alt="showroom.name"
              class="w-full h-96 object-cover block"
              loading="lazy"
            />
          </div>
        </div>

        <!-- Store hours -->
        <div class="mb-20">
          <SectionLabel>{{ $t('hours.hoursLabel') }}</SectionLabel>
          <h2 class="text-3xl font-extrabold text-gray-900 mb-2">{{ $t('hours.hoursTitle') }}</h2>
          <div class="h-px w-12 bg-yellow-400 mb-5"></div>
          <p class="text-gray-600 max-w-xl mb-10 leading-relaxed">{{ $t('hours.hoursBody') }}</p>

          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3 max-w-3xl">
            <div
              v-for="day in hours"
              :key="day.label"
              class="rounded-xl p-5 border transition-all"
              :class="day.label === todayLabel
                ? 'border-yellow-400 bg-yellow-50 ring-2 ring-yellow-300/50'
                : 'border-gray-100 bg-white shadow-sm'"
            >
              <span
                v-if="day.label === todayLabel"
                class="inline-block text-[9px] font-bold tracking-widest uppercase text-yellow-700 bg-yellow-100 px-2 py-0.5 rounded-full mb-1"
              >{{ $t('hours.today') }}</span>
              <p class="text-[10px] font-bold tracking-[0.2em] uppercase text-gray-400 mb-2">{{ day.label }}</p>
              <p class="text-lg font-extrabold text-gray-900 leading-tight">{{ day.open }}</p>
              <p class="text-sm text-gray-400">– {{ day.close }}</p>
            </div>
          </div>
        </div>

        <!-- FAQ -->
        <div>
          <div class="flex items-center gap-3 mb-8">
            <div class="h-px w-10 bg-yellow-400"></div>
            <SectionLabel>{{ $t('hours.faqLabel') }}</SectionLabel>
          </div>
          <h2 class="text-3xl md:text-4xl font-extrabold text-gray-900 mb-10 leading-tight">
            {{ $t('hours.faqTitle') }}
          </h2>

          <div class="space-y-3 max-w-3xl">
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
        </div>

      </div>
    </section>

  </main>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

useHead(() => ({ title: 'Hours & Location — Winner Cabinets' }))

const showroom = {
  name: 'Richmond Showroom',
  phone: '(604) 270-4505',
  image: '/images/storeTest.jpg',
  mapUrl: 'https://maps.app.goo.gl/S2YgNX3ayvWys7sQA',
}

const openFaq = ref<number | null>(null)
const todayLabel = ref('')

// Hydration-safe: only resolve today's label on the client
onMounted(() => {
  todayLabel.value = new Date().toLocaleDateString('en-US', {
    timeZone: 'America/Vancouver',
    weekday: 'long',
  })
})

const faqs = [
  {
    q: 'Do I need an appointment to visit the showroom?',
    a: 'No appointment is needed — walk-ins are always welcome. Our showroom is open Monday through Saturday from 10:00 am to 7:00 pm, and Sunday from 11:00 am to 6:00 pm.',
  },
  {
    q: 'Do you offer custom cabinet sizes and finishes?',
    a: 'Yes. We carry a wide range of door styles, finishes, and hardware options. Our in-store consultants can help you mix and match to suit your kitchen or bathroom layout.',
  },
  {
    q: 'Can I get a quote before purchasing?',
    a: 'Absolutely. Bring in your measurements or ask about our professional measurement service, and we will prepare a detailed quote for you at no charge.',
  },
  {
    q: 'Does Winner Cabinets offer installation services?',
    a: 'We can connect you with trusted local installers who work with our products regularly. Ask a showroom consultant for details during your visit.',
  },
  {
    q: 'What areas do you serve?',
    a: 'Our Richmond showroom serves the Greater Vancouver area, including Richmond, Vancouver, Burnaby, Surrey, and surrounding municipalities.',
  },
]

const hours = [
  { label: 'Monday',    open: '10:00 am', close: '7:00 pm' },
  { label: 'Tuesday',   open: '10:00 am', close: '7:00 pm' },
  { label: 'Wednesday', open: '10:00 am', close: '7:00 pm' },
  { label: 'Thursday',  open: '10:00 am', close: '7:00 pm' },
  { label: 'Friday',    open: '10:00 am', close: '7:00 pm' },
  { label: 'Saturday',  open: '10:00 am', close: '7:00 pm' },
  { label: 'Sunday',    open: '11:00 am', close: '6:00 pm' },
]
</script>
