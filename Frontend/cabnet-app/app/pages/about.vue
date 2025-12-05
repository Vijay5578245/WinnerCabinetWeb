<template>
  <main class="max-w-7xl mx-auto px-6 py-16 text-gray-900 pt-30">
    <!-- Hero header -->
    <header class="mb-12">
      <h1 class="text-5xl md:text-6xl font-extrabold leading-tight">MEET LAPALMA</h1>
      <p class="mt-4 max-w-3xl text-lg text-gray-700">
        Discover a new way of living with Lapalma's crafted simplicity. Rooted in Italian design,
        our collections combine timeless aesthetics, ergonomic comfort, and mindful innovation.
      </p>
    </header>

    <!-- Two column feature: large image left, text right -->
    <section class="mb-12 relative">
      <div class="">
        <img :src="heroImage" alt="Team and design" class="w-full h-[420px] object-cover rounded shadow-lg" loading="lazy" />
      </div>
    </section>





    <!-- INSIDE LAPALMA - Vision: text left, picture right -->
    <section class="grid gap-8 md:grid-cols-2 items-center mb-12">
      <div class="order-1">
        <h3 class="text-xl font-semibold mb-3">INSIDE LAPALMA</h3>
        <h4 class="font-medium mb-2">Our Vision</h4>
        <p class="text-gray-700">
          We see design as more than aesthetics — it’s a way of living that elevates everyday moments.
          Our work focuses on simplicity, quality, and thoughtful details that last.
        </p>
      </div>

      <div class="order-2">
        <img :src="visionImage" alt="vision image" class="w-full h-64 md:h-80 object-cover rounded shadow-lg" loading="lazy" />
      </div>
    </section>

    <!-- MISSION: image left (bigger), text right -->
    <section class="grid gap-8 md:grid-cols-2 items-center mb-12">
      <div class="order-2 md:order-1">
        <img :src="missionImage" alt="mission image" class="w-full h-96 md:h-[520px] object-cover rounded shadow-lg" loading="lazy" />
      </div>

      <div class="order-1 md:order-2">
        <h4 class="text-xl font-semibold mb-3">Our Mission</h4>
        <p class="text-gray-700 mb-4">
          To craft furniture that balances timeless form with comfort and function.
          We prioritize sustainable choices, careful craftsmanship, and enduring materials
          so every piece feels as good as it looks.
        </p>

        <p class="text-gray-600">Contact us to learn more about our process and materials.</p>
      </div>
    </section>

    <!-- Large visual / CTA -->
    <section class="mt-8">
      <div class="rounded overflow-hidden shadow-lg">
        <img :src="ctaImage" alt="Design • Craftmanship" class="w-full h-64 md:h-96 object-cover" loading="lazy" />
      </div>
    </section>
  </main>

</template>

<script setup>
import heroImage from '/images/storeTest.jpg'   // replace with your hero image  // small awards/logos image
import ctaImage from '/images/storeTest.jpg'        // large visual at bottom
import visionImage from '/images/nvTest.jpg'    // vision section image
import missionImage from '/images/nvTest.jpg'   // mission section image
</script>

<style scoped>
/* subtle page rounded corners like reference */
main { border-radius: 10px; }
.prose img { border-radius: 6px; }
</style>
