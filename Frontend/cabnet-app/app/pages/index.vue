<template>
  <section
    class="bg-white flex flex-col items-center justify-center h-[96vh] text-center px-6 w-full z-5 overflow-hidden relative"
  >
    <img
      src="/images/logbg2.png"
      alt="Hero image showing cabinets"
      class="absolute opacity-100 w-full object-cover hero-zoom"
      loading="lazy"
    />
    <div
      class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent pointer-events-none"
    ></div>
    <img
      src="/images/WClogo.png"
      alt="Hero image showing cabinets"
      class="absolute opacity-100 h-[350px] object-cover top-40 left-70"
      loading="lazy"
    />

    <div class="absolute z-20 flex flex-col items-center top-130">
      <p class="text-white/90 mt-4 text-lg md:text-xl max-w-2xl">
        {{ $t("index.tagline") }}
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

  <main class="relative -top-4 z-10">
    <!-- comapny views -->
    <section class="bg-gray-100 h-[2000px] rounded-t-[18px]">
      <div class="flex pt-16 mb-12 pl-6">
        <div class="text-center px-6">
          <h2 class="text-4xl font-extrabold text-black">Why Choose Winner Cabinets?</h2>
        </div>
      </div>

      <section class="bg-white py-16 px-8">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-12">
          <div class="flex flex-col items-start border-r border-gray-300 pr-8">
            <p class="text-sm font-bold text-gray-900 mb-2">November 2024</p>

            <h3 class="text-xl font-extrabold text-gray-900 leading-tight mb-4">
              Magic Quadrant™ for Cloud ERP for Service-Centric Enterprises
            </h3>

            <p class="text-gray-700 mb-8 leading-relaxed">
              Learn why Gartner named Oracle (Fusion Cloud ERP) a Leader in Gartner® Magic
              Quadrant™ for Cloud ERP for Service-Centric Enterprises.
            </p>
          </div>

          <div class="flex flex-col items-start border-r border-gray-300 pr-8">
            <p class="text-sm font-bold text-gray-900 mb-2">November 2024</p>

            <h3 class="text-xl font-extrabold text-gray-900 leading-tight mb-4">
              Magic Quadrant™ for Cloud ERP for Service-Centric Enterprises
            </h3>

            <p class="text-gray-700 mb-8 leading-relaxed">
              Learn why Gartner named Oracle (Fusion Cloud ERP) a Leader in Gartner® Magic
              Quadrant™ for Cloud ERP for Service-Centric Enterprises.
            </p>
          </div>

          <div class="flex flex-col items-start">
            <p class="text-sm font-bold text-gray-900 mb-2">November 2024</p>

            <h3 class="text-xl font-extrabold text-gray-900 leading-tight mb-4">
              Magic Quadrant™ for Cloud ERP for Service-Centric Enterprises
            </h3>

            <p class="text-gray-700 mb-8 leading-relaxed">
              Learn why Gartner named Oracle (Fusion Cloud ERP) a Leader in Gartner® Magic
              Quadrant™ for Cloud ERP for Service-Centric Enterprises.
            </p>
          </div>

        </div>
      </section>


    </section>

    <!-- the section for 4 blocks -->

    <section class="w-full bg-white text-black">
      <div class="mx-auto max-w-[90vw] py-16">
        <!-- GRID: 2 columns on md+, 1 column on mobile -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
          <!-- LEFT COLUMN (stack) -->
          <div class="flex flex-col gap-18">
            <!-- Big card -->

            <!-- content -->
            <div class="relative p-10 overflow-hidden h-[60vh]">
              <div class="absolute inset-0 z-0">
                <img
                  src="/images/pencilPic.jpg"
                  alt=""
                  class="h-full w-full object-cover opacity-80"
                />
              </div>

              <div class="absolute inset-0 z-10 bg-white/20"></div>

              <div class="relative z-20">
                <h3 class="text-3xl md:text-4xl font-extrabold tracking-tight">
                  Fresh and Modern<br />Website Design
                </h3>
                <p class="mt-3 text-xs tracking-widest uppercase text-black/60">
                  Starting from $2100
                </p>

                <NuxtLink
                  to="/measurement-services"
                  class="mt-6 inline-flex items-center rounded-full border border-black/25 px-5 py-2 text-sm text-black/80 transition hover:border-black/70"
                >
                  Learn More
                </NuxtLink>
              </div>
            </div>

            <!-- Small card -->

            <div class="relative p-10 overflow-hidden h-[40vh]">
              <div class="absolute inset-0 z-0">
                <img
                  src="/images/pencilPic.jpg"
                  alt=""
                  class="h-full w-full object-cover opacity-80"
                />
              </div>

              <div class="absolute inset-0 z-10 bg-white/20"></div>

              <div class="relative z-20">
                <h3 class="text-3xl font-extrabold tracking-tight">Packaging Design</h3>
                <p class="mt-3 text-xs tracking-widest uppercase text-black/60">
                  Starting from $1499
                </p>

                <NuxtLink
                  to="/measurement-services"
                  class="mt-6 inline-flex items-center rounded-full border border-black/25 px-5 py-2 text-sm text-black/80 transition hover:border-black/70"
                >
                  Learn More
                </NuxtLink>
              </div>
            </div>
          </div>

          <!-- RIGHT COLUMN (stack) -->
          <div class="flex flex-col gap-18">
            <!-- Small card -->

            <div class="relative p-10 overflow-hidden h-[40vh]">
              <div class="absolute right-0 inset-y-0 z-0 w-[550px]">
                <img
                  src="/images/pencilPic.jpg"
                  alt=""
                  class="h-full w-full object-cover opacity-80"
                />
              </div>

              <div class="absolute inset-0 z-10 bg-white/20"></div>
              <div class="relative z-20">
                <h3 class="text-3xl font-extrabold tracking-tight">Product Design</h3>
                <p class="mt-3 text-xs tracking-widest uppercase text-black/60">
                  Starting from $1200
                </p>

                <NuxtLink
                  to="/measurement-services"
                  class="mt-6 inline-flex items-center rounded-full border border-black/25 px-5 py-2 text-sm text-black/80 transition hover:border-black/70"
                >
                  Learn More
                </NuxtLink>

                <p class="mt-8 text-xs text-black/50">*Minimum 3 months commitment</p>
              </div>
            </div>

            <!-- Big card -->

            <div class="relative p-10 overflow-hidden h-[60vh]">
              <div class="absolute inset-y-0 right-0 z-0 w-[550px]">
                <img
                  src="/images/pencilPic.jpg"
                  alt=""
                  class="h-full w-full object-cover opacity-80"
                />
              </div>

              <div class="absolute inset-0 z-10 bg-white/20"></div>
              <div class="relative z-20">
                <h3 class="text-3xl md:text-4xl font-extrabold tracking-tight">
                  Full Time Monthly<br />Commitment
                </h3>
                <p class="mt-3 text-xs tracking-widest uppercase text-black/60">
                  Starting from $4500/month
                </p>

                <NuxtLink
                  to="/measurement-services"
                  class="mt-6 inline-flex items-center rounded-full border border-black/25 px-5 py-2 text-sm text-black/80 transition hover:border-black/70"
                >
                  Learn More
                </NuxtLink>

                <p class="mt-8 text-xs text-black/50">*Minimum 3 months commitment</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="bg-white">
      <section
        class="max-w-[95vw] mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch py-12"
      >
        <!-- Large image/content card (left) -->
        <NuxtLink
          to="/collections"
          class="md:col-span-2 relative rounded-lg overflow-hidden shadow group block min-h-[550px] md:min-h-[670px] focus:outline-none"
          aria-label="View Collections"
        >
          <!-- background image -->
          <img
            src="/images/nvTest.jpg"
            alt=""
            class="absolute inset-0 w-full h-full object-cover"
            loading="lazy"
          />

          <!-- subtle overlay for contrast -->
          <div
            class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent pointer-events-none"
          ></div>

          <!-- text overlay: moves up on hover and CTA fades in -->
          <div
            class="relative z-10 flex flex-col justify-end h-full p-6 transform transition-all duration-300 group-hover:-translate-y-2"
          >
            <h2
              class="text-white text-3xl font-extrabold mb-2 transition-transform duration-300 group-hover:-translate-y-2"
            >
              Our Collections
            </h2>
            <p
              class="text-white/90 max-w-xl transition-transform duration-300 group-hover:-translate-y-1"
            >
              Explore our diverse range of cabinet collections, each designed to meet
              different styles and needs.
            </p>
          </div>
        </NuxtLink>

        <!-- Bold CTA panel (right) - keep heights consistent -->
        <a
          :href="localePath('collections')"
          class="group block rounded-lg overflow-hidden shadow-md bg-yellow-400 flex items-center justify-center min-h-[550px] md:min-h-[670px]"
          aria-label="Go shopping - Find a showroom"
        >
          <div class="w-full h-full flex items-center justify-center px-6">
            <div
              class="text-black font-extrabold text-2xl md:text-3xl flex items-center gap-4"
            >
              <span>Go shopping</span>
              <span
                class="inline-flex items-center justify-center w-10 h-10 bg-black text-yellow-400 rounded-full text-lg transition-transform transform group-hover:translate-x-1"
                aria-hidden="true"
              >
                →
              </span>
            </div>
          </div>
        </a>
      </section>
    </div>
  </main>

  <Footer />
</template>

<script setup>
// no script needed for the static hero; keep page lightweight
const localePath = useLocalePath();
</script>

<style scoped>
.hero-zoom {
  opacity: 1;
  animation: zoomIn 5s ease-out forwards;
}

@keyframes zoomIn {
  from {
    transform: scale(1);
  }
  to {
    transform: scale(1.05); /* zoom in by 20% */
  }
}
</style>
