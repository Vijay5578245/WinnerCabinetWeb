<template>
  <main>
    <!-- Hero -->
    <section class="relative h-[55dvh] overflow-hidden">
      <img
        src="/images/storeTest.jpg"
        alt="Winner Cabinets Showroom"
        class="absolute inset-0 w-full h-full object-cover"
        loading="lazy"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/30 to-transparent"></div>
      <div class="absolute bottom-0 left-0 px-8 pb-10 max-w-4xl">
        <p class="text-yellow-400 text-xs font-bold tracking-[0.2em] uppercase mb-3">Our Location</p>
        <h1 class="text-4xl md:text-6xl font-extrabold text-white leading-tight">Hours &amp; Location</h1>
      </div>
    </section>

    <!-- Main content -->
    <section class="relative z-10 bg-white -mt-4 overflow-hidden" style="border-radius: 10px 10px 0 0;">
      <!-- Warm gradient background -->
      <div class="absolute inset-0 bg-white pointer-events-none"></div>

      <div class="relative max-w-6xl mx-auto px-6 pt-16 pb-24">

        <!-- Decorative accent -->
        <div class="flex items-center gap-3 mb-12">
          <div class="h-px w-10 bg-yellow-400"></div>
          <div class="h-1.5 w-1.5 rounded-full bg-yellow-400"></div>
          <div class="h-px w-10 bg-yellow-400"></div>
        </div>

        <!-- Showroom info + image -->
        <div class="grid md:grid-cols-2 gap-12 items-start">

          <!-- Info -->
          <div>
            <p class="text-yellow-500 text-xs font-bold tracking-[0.2em] uppercase mb-3">Richmond Showroom</p>
            <h2 class="text-4xl font-extrabold text-black mb-2">Winner Cabinets</h2>
            <div class="h-1 w-12 bg-yellow-400 mb-8"></div>

            <div class="mb-6">
              <p class="text-[10px] font-bold tracking-[0.2em] uppercase text-gray-400 mb-1">Address</p>
              <p class="text-gray-700 text-base leading-relaxed">
                160 – 4551 No 3 Rd<br />Richmond, BC V6X 2C3
              </p>
            </div>

            <div class="mb-8">
              <p class="text-[10px] font-bold tracking-[0.2em] uppercase text-gray-400 mb-1">Phone</p>
              <a
                :href="'tel:' + showroom.phone"
                class="text-gray-800 font-semibold text-base hover:text-yellow-500 transition-colors"
              >
                {{ showroom.phone }}
              </a>
            </div>

            <div class="flex flex-wrap gap-4">
              <a
                :href="showroom.mapUrl"
                target="_blank"
                rel="noopener"
                class="inline-flex items-center gap-2 bg-yellow-400 text-black font-bold px-6 py-3 text-sm hover:bg-yellow-500 transition-colors"
                style="border-radius: 10px;"
              >
                Open in Maps <span aria-hidden="true">→</span>
              </a>
              <a
                :href="'tel:' + showroom.phone"
                class="inline-flex items-center gap-2 border border-gray-300 text-black font-medium px-6 py-3 text-sm hover:bg-gray-50 transition-colors"
                style="border-radius: 10px;"
              >
                Call Us
              </a>
            </div>
          </div>

          <!-- Image -->
          <div class="overflow-hidden shadow-lg" style="border-radius: 10px;">
            <img
              :src="showroom.image"
              :alt="showroom.name"
              class="w-full h-[380px] object-cover block"
              loading="lazy"
            />
          </div>
        </div>

        <!-- Hours -->
        <div class="mt-20">
          <p class="text-yellow-500 text-xs font-bold tracking-[0.2em] uppercase mb-3">When to Visit</p>
          <h2 class="text-3xl font-extrabold text-black mb-2">Store Hours</h2>
          <div class="h-1 w-12 bg-yellow-400 mb-6"></div>
          <p class="text-gray-600 max-w-xl mb-10 leading-relaxed">
            We're open seven days a week so you can visit at your convenience.
            Our team is always on hand to help you find the perfect cabinet solution for your space.
          </p>

          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4 max-w-4xl">
            <div
              v-for="day in hours"
              :key="day.label"
              class="bg-white border border-gray-100 shadow-sm p-5"
              :class="day.label === todayLabel
                ? 'border-yellow-400 bg-yellow-50 ring-2 ring-yellow-300'
                  : ''"
              style="border-radius: 10px;"
            >
              <span
                v-if="day.label === todayLabel"
                class="inline-block text-[9px] font-bold tracking-widest uppercase text-yellow-600 bg-yellow-100 px-2 py-0.5 rounded-full mb-1"
              >Today</span>
              <p class="text-[10px] font-bold tracking-[0.2em] uppercase text-gray-400 mb-2">{{ day.label }}</p>
              <p class="text-lg font-extrabold text-black leading-tight">{{ day.open }}</p>
              <p class="text-sm text-gray-400">– {{ day.close }}</p>
            </div>
          </div>
        </div>

        <!-- FAQ section -->
        <div class="mt-20">
          <div class="flex items-center gap-3 mb-8">
            <div class="h-px w-10 bg-yellow-400"></div>
            <p class="text-yellow-400 text-xs font-bold tracking-[0.2em] uppercase">Frequently Asked Questions</p>
          </div>
          <h2 class="text-3xl md:text-4xl font-extrabold text-black mb-10 leading-tight">
            Common questions<br />about our showroom.
          </h2>

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
        </div>

      </div>
    </section>

    <Footer />
  </main>
</template>

<script setup lang="ts">
const showroom = {
  name: 'Richmond Showroom',
  phone: '(604) 270-4505',
  image: '/images/storeTest.jpg',
  mapUrl: 'https://maps.app.goo.gl/S2YgNX3ayvWys7sQA',
}

const openFaq = ref<number | null>(null)

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

const todayLabel = new Date().toLocaleDateString('en-US', {
  timeZone: 'America/Vancouver',
  weekday: 'long',
})

const hours = [
  { label: 'Monday',    open: '10:00 am', close: '7:00 pm'  },
  { label: 'Tuesday',   open: '10:00 am', close: '7:00 pm'  },
  { label: 'Wednesday', open: '10:00 am', close: '7:00 pm'  },
  { label: 'Thursday',  open: '10:00 am', close: '7:00 pm'  },
  { label: 'Friday',    open: '10:00 am', close: '7:00 pm'  },
  { label: 'Saturday',  open: '10:00 am', close: '7:00 pm'  },
  { label: 'Sunday',    open: '11:00 am', close: '6:00 pm'  },
]
</script>

<style scoped>
main {
  border-radius: 10px;
}

</style>
