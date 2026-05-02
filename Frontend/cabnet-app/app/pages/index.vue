<template>
  <section
    ref="heroRef"
    class="bg-white flex flex-col items-center justify-center h-[96vh] text-center px-6 w-full z-5 overflow-hidden relative"
  >
    <img
      src="/images/logbg2.png"
      alt="Hero image showing cabinets"
      class="absolute opacity-100 w-full h-full object-cover hero-zoom"
      loading="lazy"
    />
    <div
      class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent pointer-events-none"
    ></div>
    <img
      src="/images/WClogo.png"
      alt="Hero image showing cabinets"
      class="hero-logo absolute opacity-100 max-h-[350px] h-auto w-auto object-cover left-1/2 top-3/7 -translate-x-1/2 -translate-y-1/2"
      loading="lazy"
    />

    <div class="hero-text absolute z-20 flex flex-col items-center top-2/3">
      <p class="text-white/90 mt-4 text-lg md:text-xl max-w-2xl">
        {{ $t("index.tagline") }}
      </p>

      <ButtonToLink
        to="/hours-and-location"
        class="py-5 px-20 text-white hover:bg-gradient-to-r hover:from-yellow-500 hover:to-yellow-100/80"
      >
        Find A Showroom
      </ButtonToLink>
    </div>
  </section>

  <!-- page content below the hero -->

  <main class="relative -top-4 z-10">



    <section class="bg-white rounded-t-[18px] overflow-hidden">

      <!-- Cards about how we works, what we do -->

      <div class="border-t border-gray-300"></div>
      <section
        class="flex flex-col justify-center items-center gap-3 md:gap-7 px-6 pt-20 pb-0 relative overflow-hidden"
      >
        <!-- warm gradient + dotted pattern layered -->
        <div class="absolute inset-0 bg-gradient-to-b from-amber-50 via-yellow-50/40 to-white pointer-events-none"></div>
        <div class="absolute inset-0 dotted-fade pointer-events-none"></div>

        <!-- decorative accent -->
        <div class="relative flex items-center gap-3 mb-2">
          <div class="h-px w-10 bg-yellow-400"></div>
          <div class="h-1.5 w-1.5 rounded-full bg-yellow-400"></div>
          <div class="h-px w-10 bg-yellow-400"></div>
        </div>
        <p class="design-header relative text-amber-500 font-bold text-[10px] md:text-[20px] tracking-widest uppercase">
          {{ $t("index.designLine1") }}
        </p>
        <div class="design-header relative flex flex-col justify-center items-center">
          <p class="text-black font-bold text-[25px] md:text-[50px]">
            {{ $t("index.designLine2") }}
          </p>
          <p class="text-black font-bold text-[25px] md:text-[50px]">
            {{ $t("index.designLine3") }}
          </p>
        </div>

              <ScrollPic />


      </section>

      <section class="pt-10">
        <div class="flex flex-col pt-16 mb-4 pl-6">
          <p class="text-yellow-500 text-xs font-bold tracking-[0.2em] uppercase mb-3 px-6">Our Strengths</p>
          <div class="text-left px-6">
            <h2 class="text-4xl font-extrabold text-black">{{ $t("index.usHeader") }}</h2>
          </div>
        </div>

        <section
          class="flex flex-col items-center justify-center bg-white pt-20 pb-20 px-8"
        >

          <div class="strengths-grid max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-12">
            <div class="strength-col flex flex-col items-start border-r border-gray-200 pr-8">
              <span class="text-[72px] font-black text-gray-100 leading-none select-none -mb-2">01</span>
              <div class="w-10 h-1 bg-yellow-400 mb-4"></div>
              <h3 class="text-3xl font-extrabold text-gray-900 leading-tight mb-4">
                {{ $t("index.usBoxHeader1") }}
              </h3>
              <p class="text-gray-600 mb-8 leading-relaxed">
                {{ $t("index.usBoxDescription1") }}
              </p>
            </div>

            <div class="strength-col flex flex-col items-start border-r border-gray-200 pr-8">
              <span class="text-[72px] font-black text-gray-100 leading-none select-none -mb-2">02</span>
              <div class="w-10 h-1 bg-yellow-400 mb-4"></div>
              <h3 class="text-3xl font-extrabold text-gray-900 leading-tight mb-4">
                {{ $t("index.usBoxHeader2") }}
              </h3>
              <p class="text-gray-600 mb-8 leading-relaxed">
                {{ $t("index.usBoxDescription2") }}
              </p>
            </div>

            <div class="strength-col flex flex-col items-start">
              <span class="text-[72px] font-black text-gray-100 leading-none select-none -mb-2">03</span>
              <div class="w-10 h-1 bg-yellow-400 mb-4"></div>
              <h3 class="text-3xl font-extrabold text-gray-900 leading-tight mb-4">
                {{ $t("index.usBoxHeader3") }}
              </h3>
              <p class="text-gray-600 mb-8 leading-relaxed">
                {{ $t("index.usBoxDescription3") }}
              </p>
            </div>
          </div>

          <div class="py-10">
            <ButtonToLink
              to="/about"
              class="py-5 px-20 hover:bg-gradient-to-r hover:from-yellow-400 hover:to-yellow-100"
            >
              About
            </ButtonToLink>
          </div>
        </section>

      </section>

      <ScrollCard />






    </section>

    <!-- the section for 4 blocks -->

    <section class="w-full bg-white text-black pt-20 border-t border-gray-300">
      <div class="mx-auto max-w-[90vw] py-0">
        <!-- Section header -->
        <div class="services-header mb-10">
          <p class="text-yellow-500 text-xs font-bold tracking-[0.2em] uppercase mb-3">What We Offer</p>
          <h2 class="text-4xl font-extrabold text-black">Our Services</h2>
          <div class="mt-4 h-px w-16 bg-yellow-400"></div>
        </div>
        <!-- GRID: 2 columns on md+, 1 column on mobile -->
        <div class="services-grid grid grid-cols-1 md:grid-cols-2 gap-12">
          <!-- LEFT COLUMN (stack) -->
          <div class="flex flex-col gap-18">
            <!-- Big card -->
            <div class="service-card relative p-10 overflow-hidden h-[60vh] group">
              <div class="absolute inset-0 z-0">
                <img
                  src="/images/pencilPic.jpg"
                  alt=""
                  class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                />
              </div>

              <div class="absolute inset-0 z-10 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>

              <div class="relative z-20">
                <h3 class="text-3xl md:text-4xl font-extrabold tracking-tight text-white">
                  Fresh and Modern<br />Website Design
                </h3>
                <p class="mt-3 text-xs tracking-widest uppercase text-white/60">
                  Starting from $2100
                </p>

              </div>
            </div>

            <!-- Small card -->
            <div class="service-card relative p-10 overflow-hidden h-[40vh] group">
              <div class="absolute inset-0 z-0">
                <img
                  src="/images/pencilPic.jpg"
                  alt=""
                  class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                />
              </div>

              <div class="absolute inset-0 z-10 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>

              <div class="relative z-20">
                <h3 class="text-3xl font-extrabold tracking-tight text-white">Packaging Design</h3>
                <p class="mt-3 text-xs tracking-widest uppercase text-white/60">
                  Starting from $1499
                </p>


              </div>
            </div>
          </div>

          <!-- RIGHT COLUMN (stack) -->
          <div class="flex flex-col gap-18">
            <!-- Small card -->
            <div class="service-card relative p-10 overflow-hidden h-[40vh] group">
              <div class="absolute right-0 inset-y-0 z-0 w-full">
                <img
                  src="/images/pencilPic.jpg"
                  alt=""
                  class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                />
              </div>

              <div class="absolute inset-0 z-10 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
              <div class="relative z-20">
                <h3 class="text-3xl font-extrabold tracking-tight text-white">Product Design</h3>
                <p class="mt-3 text-xs tracking-widest uppercase text-white/60">
                  Starting from $1200
                </p>



                <p class="mt-8 text-xs text-white/40">*Minimum 3 months commitment</p>
              </div>
            </div>

            <!-- Big card -->
            <div class="service-card relative p-10 overflow-hidden h-[60vh] group">
              <div class="absolute inset-y-0 right-0 z-0 w-full">
                <img
                  src="/images/pencilPic.jpg"
                  alt=""
                  class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                />
              </div>

              <div class="absolute inset-0 z-10 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
              <div class="relative z-20">
                <h3 class="text-3xl md:text-4xl font-extrabold tracking-tight text-white">
                  Full Time Monthly<br />Commitment
                </h3>
                <p class="mt-3 text-xs tracking-widest uppercase text-white/60">
                  Starting from $4500/month
                </p>



                <p class="mt-8 text-xs text-white/40">*Minimum 3 months commitment</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>



    <div class="bg-white pt-20">
      <section
        class="collections-section max-w-[95vw] mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch py-12"
      >
        <!-- Large image/content card (left) -->
        <NuxtLink
          to="/collections"
          class="md:col-span-2 relative rounded-lg overflow-hidden shadow group block min-h-[550px] md:min-h-[670px] focus:outline-none"
          aria-label="View Collections"
        >
          <img
            src="/images/nvTest.jpg"
            alt=""
            class="absolute inset-0 w-full h-full object-cover"
            loading="lazy"
          />

          <div
            class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent pointer-events-none"
          ></div>

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

        <!-- Bold CTA panel (right) -->
        <NuxtLink
          to="/hours-and-location"
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
        </NuxtLink>
      </section>
    </div>
  </main>

  <Footer />
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const localePath = useLocalePath();
const heroRef = ref<HTMLElement | null>(null);

let ctx: gsap.Context | null = null;

onMounted(() => {
  ctx = gsap.context(() => {
    // Hero: logo and tagline/button fade in on load
    gsap.from(".hero-logo", {
      autoAlpha: 0,
      duration: 1,
      ease: "power2.out",
      delay: 0.2,
    });
    gsap.from(".hero-text", {
      autoAlpha: 0,
      y: 24,
      duration: 0.9,
      ease: "power2.out",
      delay: 0.5,
    });

    // Design section headings
    gsap.from(".design-header", {
      autoAlpha: 0,
      y: 20,
      duration: 0.7,
      ease: "power2.out",
      stagger: 0.12,
      scrollTrigger: {
        trigger: ".design-header",
        start: "top 85%",
        toggleActions: "play none none none",
      },
    });

    // Our Strengths columns stagger
    gsap.from(".strength-col", {
      autoAlpha: 0,
      y: 32,
      duration: 0.65,
      ease: "power2.out",
      stagger: 0.15,
      scrollTrigger: {
        trigger: ".strengths-grid",
        start: "top 80%",
        toggleActions: "play none none none",
      },
    });

    // What We Offer header
    gsap.from(".services-header", {
      autoAlpha: 0,
      y: 20,
      duration: 0.7,
      ease: "power2.out",
      scrollTrigger: {
        trigger: ".services-header",
        start: "top 85%",
        toggleActions: "play none none none",
      },
    });

    // Service cards stagger
    gsap.from(".service-card", {
      autoAlpha: 0,
      y: 28,
      duration: 0.65,
      ease: "power2.out",
      stagger: 0.12,
      scrollTrigger: {
        trigger: ".services-grid",
        start: "top 80%",
        toggleActions: "play none none none",
      },
    });

    // Collections section items stagger
    gsap.from(".collections-section > *", {
      autoAlpha: 0,
      y: 24,
      duration: 0.65,
      ease: "power2.out",
      stagger: 0.15,
      scrollTrigger: {
        trigger: ".collections-section",
        start: "top 80%",
        toggleActions: "play none none none",
      },
    });
  }, heroRef.value);
});

onUnmounted(() => {
  ctx?.revert();
});
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
    transform: scale(1.05);
  }
}
</style>
