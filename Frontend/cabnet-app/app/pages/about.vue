<template>
  <main>
    <div class="relative">
      <header class="max-w-7xl mx-auto px-6 text-gray-900 pt-20">
        <!-- Hero header -->
        <h1 class="text-5xl md:text-6xl font-extrabold leading-tight">
          {{ $t("about.title") }}
        </h1>
        <p class=""></p>
      </header>

      <div
        class="w-full h-30 z-10 text-lg text-gray-700 absolute bg-gradient-to-b from-white via-white/40 to-white/0"
      ></div>
    </div>

    <!-- Hero image -->
    <section class="sticky top-0 h-auto">
      <div class="">
        <img
          src="/images/storeTest.jpg"
          alt="Team and design"
          class="h-[70vh] w-full object-cover rounded shadow-lg"
          loading="lazy"
        />
      </div>
    </section>

    <div
      class="relative z-10 bg-[linear-gradient(to_bottom,rgba(255,255,255,0.65)_0%,rgba(255,255,255,1)_7%)]"
    >
      <div
        class="h-20 pointer-events-none inset-x-0 -top-20 absolute bg-gradient-to-t from-white/65 via-white/35 to-transparent pointer-events-none"
      ></div>
      <div class="max-w-7xl pt-20 mx-auto px-6 pb-16 text-gray-900">


        <!-- Company Timeline -->
      </div>
    </div>

    <CompanyTimeline />

    <div class="relative z-10 bg-white">
      <div class="max-w-7xl pt-10 mx-auto px-6 pb-16 text-gray-900">
        <!-- Scroll starts here -->

        <section
          class="flex items-center mb-12 shadow-lg gap-8 md:gap-16 flex-col md:flex-row mt-[90px]"
        >
          <div class="order-2">
            <h2 class="text-3xl font-extrabold mb-4">CEO Eric Chen</h2>
            <p class="text-gray-700 mb-4 pr-5">
              {{ $t("about.ceoDescription") }}
            </p>
          </div>

          <div class="">
            <img
              src="/images/nvTest.jpg"
              alt="CEO image"
              class="w-full h-80 md:h-96 object-cover rounded shadow-lg"
              loading="lazy"
            />
          </div>
        </section>

        <section class="grid gap-8 md:grid-cols-2 items-center mb-12">
          <div class="order-1">
            <h3 class="text-xl font-semibold mb-3">INSIDE LAPALMA</h3>
            <h4 class="font-medium mb-2">Our Vision</h4>
            <p class="text-gray-700">
              We see design as more than aesthetics — it's a way of living that elevates
              everyday moments. Our work focuses on simplicity, quality, and thoughtful
              details that last.
            </p>
          </div>

          <div class="order-2">
            <img
              src="/images/nvTest.jpg"
              alt="vision image"
              class="w-full h-64 md:h-80 object-cover rounded shadow-lg"
              loading="lazy"
            />
          </div>
        </section>

        <!-- MISSION: image left (bigger), text right -->
        <section class="grid gap-8 md:grid-cols-2 items-center mb-12">
          <div class="order-2 md:order-1">
            <img
              src="/images/nvTest.jpg"
              alt="mission image"
              class="w-full h-96 md:h-[520px] object-cover rounded shadow-lg"
              loading="lazy"
            />
          </div>

          <div class="order-1 md:order-2">
            <h4 class="text-xl font-semibold mb-3">Our Mission</h4>
            <p class="text-gray-700 mb-4">
              To craft furniture that balances timeless form with comfort and function. We
              prioritize sustainable choices, careful craftsmanship, and enduring
              materials so every piece feels as good as it looks.
            </p>

            <p class="text-gray-600">
              Contact us to learn more about our process and materials.
            </p>
          </div>
        </section>

        <section class="mt-12 prose prose-lg max-w-none text-gray-700">
          <h2 class="text-2xl font-semibold mb-4">Get to know us</h2>
          <p>
            From our carefully curated collections to our commitment to sustainability,
            every aspect of Lapalma reflects our dedication to quality and design. We
            invite you to explore our offerings and discover how our furniture can enhance
            your living spaces.
          </p>
        </section>

        <!-- Large visual / CTA -->
        <section class="mt-8">
          <div class="rounded overflow-hidden shadow-lg">
            <img
              src="/images/nvTest.jpg"
              alt="Design • Craftmanship"
              class="w-full h-64 md:h-96 object-cover"
              loading="lazy"
            />
          </div>
        </section>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
</script>

<style scoped>
main {
  border-radius: 10px;
}
</style>
