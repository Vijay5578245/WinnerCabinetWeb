<template>
  <main class="max-w-6xl mx-auto px-6 py-30">
    <h1 class="text-3xl md:text-4xl font-extrabold text-center mb-12 text-black">Hours and Locations</h1>

    <section class="space-y-12">
      <article id="richmond" class="grid gap-8 items-center md:grid-cols-2">
        <!-- text -->
        <div class="prose max-w-none">
          <h2 class="text-xl font-semibold underline decoration-2 decoration-current mb-2">{{ showroom.name }}</h2>

          <p class="text-sm text-gray-700 mb-4" v-html="showroom.addressHtml"></p>

          <div class="space-y-2 mb-4">
            <p><strong>Mon - Sat:</strong> {{ showroom.hours.week }}</p>
            <p><strong>Sun:</strong> {{ showroom.hours.sun }}</p>
            <p><strong>Phone:</strong> <a :href="'tel:' + showroom.phone" class="underline">{{ showroom.phone }}</a></p>
          </div>

          <div class="flex gap-4">
            <NuxtLink v-if="showroom.visitRoute" :to="showroom.visitRoute" class="inline-block bg-amber-400 text-white px-5 py-2 rounded-full shadow hover:brightness-95">
              Visit our {{ showroom.shortName }} Showroom
            </NuxtLink>

            <a v-if="showroom.mapUrl" :href="showroom.mapUrl" target="_blank" rel="noopener" class="inline-block border border-gray-300 px-4 py-2 text-black rounded-md text-sm hover:bg-gray-50">
              Open on map
            </a>
          </div>
        </div>

        <!-- image -->
        <div class="w-full rounded overflow-hidden shadow-lg">
          <img
            :src="showroom.image"
            :alt="showroom.name + ' photo'"
            class="w-full h-64 md:h-56 object-cover block"
            loading="lazy"
          />
        </div>
      </article>
    </section>
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
  image: '/images/storeTest.jpg', // put your image at public/images/storeTest.jpg
  visitRoute: '/hours-and-location', // adjust if needed
  mapUrl: 'https://maps.app.goo.gl/S2YgNX3ayvWys7sQA'
}
</script>

<style scoped>
/* small rounded page bottom like screenshot */
main {
  border-radius: 10px;
}
@media (min-width: 768px) {
  img { border-radius: 6px; }
}
</style>
