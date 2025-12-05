<template>


  <!-- Hero / fullscreen video header (accounts for fixed header with pt-24) -->
  <section class="relative h-screen pt-24 overflow-hidden">
    <!-- Background video (decorative) -->
    <video
      class="absolute inset-0 w-full h-full object-cover"
      autoplay
      muted
      loop
      playsinline
      preload="metadata"
      poster=""
      aria-hidden="true"
      tabindex="-1"
    >
      <source src="/videos/testVid.mp4" type="video/mp4" />
      <source src="/videos/testVid.mp4" type="video/webm" />
      <!-- fallback image will be used if video unsupported -->
    </video>

    <!-- dim / color overlay for better text contrast -->
    <div class="absolute inset-0 bg-gradient-to-b from-black/20 via-black/10 to-black/40"></div>

    <!-- centered content -->
    <div class="relative z-10 flex flex-col items-center justify-center h-full text-center px-6">
      <h1 class="text-white text-4xl sm:text-5xl md:text-6xl font-extrabold leading-tight max-w-4xl">
        Bring Comfort To Your Home
      </h1>
      <p class="text-white/90 mt-4 text-lg md:text-xl max-w-2xl">
        Designed for living, built for lasting comfort.
      </p>

      <NuxtLink
        to="/hours-and-location"
        class="mt-8 inline-block bg-white/90 text-black font-medium py-3 px-6 rounded-md shadow hover:bg-white transition"
      >
        Find a Showroom
      </NuxtLink>
    </div>
  </section>

  <!-- page content below the hero -->
  <main class="bg-gray-100">
    <div class="max-w-6xl mx-auto py-16 px-6">
      <p class="text-center">Scroll down to see the header behavior and the rest of the page content.</p>
      <!-- ...rest of page content... -->
    </div>
  </main>
</template>

<script setup>
// no script needed for the static hero; keep page lightweight
</script>
