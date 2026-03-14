<template>
  <section class="relative flex flex-col h-96 md:h-148 w-90 md:w-128 overflow-hidden rounded-lg">
    <!-- coral/rose gradient -->
    <div class="absolute inset-0 bg-gradient-to-br from-orange-400 via-rose-400 to-pink-400"></div>

    <!-- photo with blend mode -->
    <img
      src="/images/nvTest.jpg"
      alt=""
      class="absolute inset-0 h-full w-full object-cover"
    />

    <!-- floating decorative circles -->

    <!-- content -->
    <div class="relative z-10 flex flex-col h-full p-7 justify-between">
      <!-- badge -->
      <span class="self-start bg-white/90 rounded-full px-3 py-1.5 text-[10px] font-bold text-orange-800 tracking-[0.15em] uppercase shadow-sm">
        03 — Promise
      </span>

      <!-- bottom block -->

    </div>
  </section>
</template>

<script setup lang="ts">
import { ShieldCheck } from "lucide-vue-next";
</script>
