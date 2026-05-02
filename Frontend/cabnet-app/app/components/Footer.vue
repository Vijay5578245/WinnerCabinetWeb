<template>
  <footer class="relative z-0 bg-black text-white">
    <!-- Main footer content -->
    <div
      class="max-w-7xl mx-auto px-6 md:px-8 pt-16 pb-10 grid grid-cols-1 md:grid-cols-3 gap-12"
    >
      <!-- Brand column -->
      <div>
        <p class="text-white font-extrabold text-xl mb-3 tracking-tight">
          Winner Cabinets
        </p>

        <p class="text-white/50 text-sm leading-relaxed">
          Crafted with precision.<br />
          Built to last.
        </p>

        <div class="mt-6 h-px w-12 bg-yellow-400"></div>
      </div>

      <!-- Navigation column -->
      <div>
        <p
          class="text-white/40 text-[10px] font-bold tracking-[0.2em] uppercase mb-5"
        >
          Explore
        </p>

        <ul class="space-y-3">
          <li>
            <NuxtLink
              to="/about"
              class="text-white/60 hover:text-white transition-colors text-sm"
            >
              About Us
            </NuxtLink>
          </li>

          <li>
            <NuxtLink
              to="/collections"
              class="text-white/60 hover:text-white transition-colors text-sm"
            >
              Collections
            </NuxtLink>
          </li>

          <li>
            <NuxtLink
              to="/measurement-services"
              class="text-white/60 hover:text-white transition-colors text-sm"
            >
              Measurement Services
            </NuxtLink>
          </li>

          <li>
            <NuxtLink
              to="/hours-and-location"
              class="text-white/60 hover:text-white transition-colors text-sm"
            >
              Hours &amp; Location
            </NuxtLink>
          </li>
        </ul>
      </div>

      <!-- CTA column -->
      <div>
        <p
          class="text-white/40 text-[10px] font-bold tracking-[0.2em] uppercase mb-5"
        >
          Visit Us
        </p>

        <p class="text-white/50 text-sm leading-relaxed mb-5">
          Experience our cabinets in person at one of our showrooms.
        </p>

        <NuxtLink
          to="/hours-and-location"
          class="inline-flex items-center gap-2 text-yellow-400 text-sm font-medium hover:text-yellow-300 transition-colors"
        >
          Find a Showroom
          <span class="text-base leading-none">→</span>
        </NuxtLink>
      </div>
    </div>

    <!-- Bottom bar -->
    <div class="border-t border-white/10">
      <div
        class="max-w-7xl mx-auto px-6 md:px-8 py-5 flex flex-col md:flex-row items-center justify-between gap-2"
      >
        <p class="text-white/30 text-xs">
          © 2025 Winner Cabinets — All rights reserved
        </p>

        <p class="text-white/20 text-xs tracking-widest uppercase">
          Quality built into every detail
        </p>
      </div>
    </div>
  </footer>
</template>
