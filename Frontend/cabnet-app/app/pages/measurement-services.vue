<template>

      <!-- your content -->

<div class="min-h-[200vh] bg-orange-200">...</div>

<footer class="sticky bottom-0 -z-10">
  <div class=" h-[200px] bg-black text-white flex items-center justify-center">
        © 2025 Cabnet — All rights reserved
      </div>
</footer>

     <div class="min-h-[200vh] bg-orange-200 text-black">smth</div>


<nav class="w-full flex items-center px-6 py-4 bg-white shadow">

  <!-- Middle links (centered) -->
  <div class="flex-1 flex justify-center space-x-8">
    <a href="#" class="text-gray-700 hover:text-black">Home</a>
    <a href="#" class="text-gray-700 hover:text-black">About</a>
    <a href="#" class="text-gray-700 hover:text-black">Services</a>
  </div>

  <!-- Right item -->
  <div>
    <button class="bg-black text-white px-4 py-2 rounded-full">
      Login
    </button>
  </div>

</nav>
<div class="text-black">
  <NuxtLink :to="switchLocalePath('en')">....EN</NuxtLink>
  //////
  <NuxtLink :to="switchLocalePath('zh')">....中文</NuxtLink>
</div>

</template>

<script setup>
const switchLocalePath = useSwitchLocalePath()
</script>
