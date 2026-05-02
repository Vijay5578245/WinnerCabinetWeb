<template>
  <main class="bg-white min-h-screen overflow-x-hidden">

    <!-- Hero -->
    <section class="relative h-[60dvh] overflow-hidden">
      <img
        src="/images/storeTest.jpg"
        alt="Winner Cabinets showroom"
        class="absolute inset-0 w-full h-full object-cover"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/25 to-transparent"></div>
      <div class="absolute bottom-0 left-0 px-8 md:px-12 pb-12 max-w-4xl">
        <SectionLabel class="text-yellow-400">{{ $t('about.storyLabel') }}</SectionLabel>
        <h1 class="text-5xl md:text-7xl font-extrabold text-white leading-none tracking-tight">
          {{ $t('about.title') }}
        </h1>
      </div>
    </section>

    <!-- White lift-up panel -->
    <div class="relative z-10 bg-white rounded-t-2xl -mt-5">

      <!-- CEO Section -->
      <section class="mx-auto max-w-7xl px-6 md:px-8 pt-16 pb-20">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 md:gap-16 items-center">
          <div>
            <SectionLabel>{{ $t('about.visionLabel') }}</SectionLabel>
            <h2 class="text-3xl md:text-4xl font-extrabold text-gray-900 mb-5 leading-tight">
              {{ $t('about.ceoName') }}
            </h2>
            <div class="h-px w-12 bg-yellow-400 mb-6"></div>
            <p class="text-gray-600 leading-relaxed">
              {{ $t('about.ceoDescription') }}
            </p>
          </div>

          <div class="overflow-hidden rounded-2xl shadow-lg">
            <img
              src="/images/nvTest.jpg"
              alt="CEO Eric Chen"
              class="w-full h-80 md:h-96 object-cover"
              loading="lazy"
            />
          </div>
        </div>
      </section>

      <!-- Timeline -->
      <CompanyTimeline />

      <!-- Vision + Mission -->
      <section class="mx-auto max-w-7xl px-6 md:px-8 py-20">

        <!-- Vision -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center mb-20">
          <div>
            <SectionLabel>{{ $t('about.visionLabel') }}</SectionLabel>
            <h3 class="text-2xl md:text-3xl font-extrabold text-gray-900 mb-4">
              {{ $t('about.visionTitle') }}
            </h3>
            <div class="h-px w-12 bg-yellow-400 mb-5"></div>
            <p class="text-gray-600 leading-relaxed">{{ $t('about.visionBody') }}</p>
          </div>

          <div class="overflow-hidden rounded-2xl shadow-sm">
            <img
              src="/images/nvTest.jpg"
              alt="Our vision"
              class="w-full h-64 md:h-80 object-cover"
              loading="lazy"
            />
          </div>
        </div>

        <!-- Mission -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
          <div class="order-2 md:order-1 overflow-hidden rounded-2xl shadow-sm">
            <img
              src="/images/pfTest.jpg"
              alt="Our mission"
              class="w-full h-80 md:h-[440px] object-cover"
              loading="lazy"
            />
          </div>

          <div class="order-1 md:order-2">
            <h3 class="text-2xl md:text-3xl font-extrabold text-gray-900 mb-4">
              {{ $t('about.missionTitle') }}
            </h3>
            <div class="h-px w-12 bg-yellow-400 mb-5"></div>
            <p class="text-gray-600 leading-relaxed mb-4">{{ $t('about.missionBody1') }}</p>
            <p class="text-gray-500 text-sm leading-relaxed">{{ $t('about.missionBody2') }}</p>
          </div>
        </div>

      </section>

      <!-- Know us CTA banner -->
      <section class="relative overflow-hidden bg-gray-950 py-20 px-6">
        <img
          src="/images/nvTest.jpg"
          alt=""
          class="absolute inset-0 w-full h-full object-cover opacity-30"
          aria-hidden="true"
          loading="lazy"
        />
        <div class="relative z-10 mx-auto max-w-3xl text-center">
          <h2 class="text-3xl md:text-4xl font-extrabold text-white mb-5 leading-tight">
            {{ $t('about.knowUsTitle') }}
          </h2>
          <p class="text-white/65 leading-relaxed mb-8 max-w-xl mx-auto">
            {{ $t('about.knowUsBody') }}
          </p>
          <AppButton to="/collections" size="lg" class="text-white border-white/40 hover:text-black">
            {{ $t('header.collections') }}
          </AppButton>
        </div>
      </section>

    </div>

  </main>
</template>

<script setup lang="ts">
definePageMeta({ layout: 'no-footer' })

useHead(() => ({
  title: 'About Us — Winner Cabinets',
}))
</script>
