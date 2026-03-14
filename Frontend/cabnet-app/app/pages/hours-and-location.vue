<template>
  <main>
    <!-- Hero -->
    <section class="relative h-[55vh] overflow-hidden">
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
      <div class="absolute inset-0 bg-gradient-to-b from-amber-50 via-yellow-50/40 to-white pointer-events-none"></div>

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
              :class="day.highlight ? 'border-yellow-200 bg-yellow-50/60' : ''"
              style="border-radius: 10px;"
            >
              <p class="text-[10px] font-bold tracking-[0.2em] uppercase text-gray-400 mb-2">{{ day.label }}</p>
              <p class="text-lg font-extrabold text-black leading-tight">{{ day.open }}</p>
              <p class="text-sm text-gray-400">– {{ day.close }}</p>
            </div>
          </div>
        </div>

        <!-- CTA banner -->
        <div class="mt-20 bg-black overflow-hidden relative" style="border-radius: 10px;">
          <div class="absolute inset-0 overflow-hidden">
            <img
              src="/images/storeTest.jpg"
              alt=""
              class="w-full h-full object-cover opacity-20"
              loading="lazy"
            />
          </div>
          <div class="relative z-10 px-10 py-14 flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
            <div>
              <p class="text-yellow-400 text-xs font-bold tracking-[0.2em] uppercase mb-3">Ready to visit?</p>
              <h3 class="text-3xl md:text-4xl font-extrabold text-white leading-tight">
                Come see our cabinets<br />in person.
              </h3>
              <p class="text-white/50 mt-3 max-w-md leading-relaxed">
                Our showroom experts are here Monday through Sunday to help you design
                the kitchen or bathroom of your dreams.
              </p>
            </div>
            <a
              :href="showroom.mapUrl"
              target="_blank"
              rel="noopener"
              class="shrink-0 inline-flex items-center gap-2 bg-yellow-400 text-black font-bold px-8 py-4 text-sm whitespace-nowrap hover:bg-yellow-500 transition-colors"
              style="border-radius: 10px;"
            >
              Get Directions →
            </a>
          </div>
        </div>

      </div>
    </section>

    <Footer />
  </main>
</template>

<script setup>
const showroom = {
  id: 'richmond',
  name: 'Richmond Showroom',
  shortName: 'Richmond',
  addressHtml: '160 – 4551 No 3 Rd, Richmond, BC V6X 2C3',
  hours: { week: '10:00am - 7:00pm', sun: '11:00am - 6:00pm' },
  phone: '(604) 270-4505',
  image: '/images/storeTest.jpg',
  visitRoute: '/hours-and-location',
  mapUrl: 'https://maps.app.goo.gl/S2YgNX3ayvWys7sQA',
}

const hours = [
  { label: 'Monday',    open: '10:00 am', close: '7:00 pm'  },
  { label: 'Tuesday',   open: '10:00 am', close: '7:00 pm'  },
  { label: 'Wednesday', open: '10:00 am', close: '7:00 pm'  },
  { label: 'Thursday',  open: '10:00 am', close: '7:00 pm'  },
  { label: 'Friday',    open: '10:00 am', close: '7:00 pm'  },
  { label: 'Saturday',  open: '10:00 am', close: '7:00 pm'  },
  { label: 'Sunday',    open: '11:00 am', close: '6:00 pm', highlight: true },
]
</script>

<style scoped>
main {
  border-radius: 10px;
}
</style>
