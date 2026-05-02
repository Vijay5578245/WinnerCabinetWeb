<template>
  <div ref="pageRef" class="min-h-screen w-full overflow-x-hidden bg-white">
    <!-- HERO -->
    <section class="relative flex h-[96dvh] w-full items-center justify-center overflow-hidden bg-black px-6 text-center">
      <img
        src="/images/logbg2.png"
        alt="Hero image showing cabinets"
        class="hero-zoom absolute inset-0 h-full w-full object-cover"
        loading="lazy"
      />

      <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-black/10"></div>

      <div class="relative z-10 flex flex-col items-center">
        <img
          src="/images/WClogo.png"
          alt="Winner Cabinets logo"
          class="hero-logo h-auto max-h-[280px] w-auto object-contain md:max-h-[350px]"
          loading="lazy"
        />

        <p class="hero-text mt-6 max-w-2xl text-lg text-white/90 md:text-xl">
          {{ $t("index.tagline") }}
        </p>

        <ButtonToLink
          to="/hours-and-location"
          class="hero-text mt-6 px-10 py-4 text-white hover:bg-gradient-to-r hover:from-yellow-500 hover:to-yellow-100/80 md:px-20 md:py-5"
        >
          Find A Showroom
        </ButtonToLink>
      </div>
    </section>

    <main class="relative z-10 bg-white">
      <!-- DESIGN INTRO -->
      <section class="relative overflow-hidden rounded-t-[18px] border-t border-gray-300 bg-white px-6 pb-0 pt-20">
        <div class="absolute inset-0 bg-gradient-to-b from-amber-50 via-yellow-50/40 to-white"></div>
        <div class="dotted-fade absolute inset-0"></div>

        <div class="relative z-10 mx-auto flex max-w-7xl flex-col items-center gap-3 text-center md:gap-7">
          <div class="flex items-center gap-3">
            <div class="h-px w-10 bg-yellow-400"></div>
            <div class="h-1.5 w-1.5 rounded-full bg-yellow-400"></div>
            <div class="h-px w-10 bg-yellow-400"></div>
          </div>

          <p class="design-header text-[10px] font-bold uppercase tracking-widest text-amber-500 md:text-[20px]">
            {{ $t("index.designLine1") }}
          </p>

          <div class="design-header">
            <p class="text-[25px] font-bold text-black md:text-[50px]">
              {{ $t("index.designLine2") }}
            </p>
            <p class="text-[25px] font-bold text-black md:text-[50px]">
              {{ $t("index.designLine3") }}
            </p>
          </div>
        </div>

        <div class="relative z-10 mt-8 w-full">
          <ScrollPic />
        </div>
      </section>

      <!-- STRENGTHS -->
      <section class="bg-white px-6 py-20">
        <div class="mx-auto max-w-7xl">
          <div class="mb-12">
            <p class="mb-3 text-xs font-bold uppercase tracking-[0.2em] text-yellow-500">
              Our Strengths
            </p>

            <h2 class="text-4xl font-extrabold text-black">
              {{ $t("index.usHeader") }}
            </h2>
          </div>

          <div class="strengths-grid grid grid-cols-1 gap-10 md:grid-cols-3">
            <article class="strength-col border-gray-200 md:border-r md:pr-8">
              <span class="-mb-2 block select-none text-[72px] font-black leading-none text-gray-100">
                01
              </span>
              <div class="mb-4 h-1 w-10 bg-yellow-400"></div>
              <h3 class="mb-4 text-3xl font-extrabold leading-tight text-gray-900">
                {{ $t("index.usBoxHeader1") }}
              </h3>
              <p class="leading-relaxed text-gray-600">
                {{ $t("index.usBoxDescription1") }}
              </p>
            </article>

            <article class="strength-col border-gray-200 md:border-r md:pr-8">
              <span class="-mb-2 block select-none text-[72px] font-black leading-none text-gray-100">
                02
              </span>
              <div class="mb-4 h-1 w-10 bg-yellow-400"></div>
              <h3 class="mb-4 text-3xl font-extrabold leading-tight text-gray-900">
                {{ $t("index.usBoxHeader2") }}
              </h3>
              <p class="leading-relaxed text-gray-600">
                {{ $t("index.usBoxDescription2") }}
              </p>
            </article>

            <article class="strength-col">
              <span class="-mb-2 block select-none text-[72px] font-black leading-none text-gray-100">
                03
              </span>
              <div class="mb-4 h-1 w-10 bg-yellow-400"></div>
              <h3 class="mb-4 text-3xl font-extrabold leading-tight text-gray-900">
                {{ $t("index.usBoxHeader3") }}
              </h3>
              <p class="leading-relaxed text-gray-600">
                {{ $t("index.usBoxDescription3") }}
              </p>
            </article>
          </div>

          <div class="mt-12 flex justify-center">
            <ButtonToLink
              to="/about"
              class="px-20 py-5 hover:bg-gradient-to-r hover:from-yellow-400 hover:to-yellow-100"
            >
              About
            </ButtonToLink>
          </div>
        </div>
      </section>

      <ScrollCard />

      <!-- SERVICES: NEW CLEAN VERSION -->
      <section class="bg-white px-6 py-24 text-black">
        <div class="mx-auto">
          <div class="services-header mb-12">
            <p class="mb-3 text-xs font-bold uppercase tracking-[0.2em] text-yellow-500">
              What We Offer
            </p>

            <h2 class="text-4xl font-extrabold text-black">
              Our Services
            </h2>

            <div class="mt-4 h-px w-16 bg-yellow-400"></div>
          </div>

          <div class="services-grid grid grid-cols-1 gap-8 md:grid-cols-2">
            <NuxtLink
              to="/collections"
              class="service-card group relative flex min-h-[460px] overflow-hidden rounded-xl bg-gray-900 p-8 md:min-h-[560px] md:p-10"
            >
              <img
                src="/images/pencilPic.jpg"
                alt=""
                class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                loading="lazy"
              />

              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent"></div>

              <div class="relative z-10 mt-auto">
                <h3 class="text-3xl font-extrabold tracking-tight text-white md:text-4xl">
                  Fresh and Modern<br />
                  Website Design
                </h3>

                <p class="mt-3 text-xs uppercase tracking-[0.25em] text-white/70">
                  Starting from $2100
                </p>
              </div>
            </NuxtLink>

            <NuxtLink
              to="/collections"
              class="service-card group relative flex min-h-[460px] overflow-hidden rounded-xl bg-gray-900 p-8 md:min-h-[560px] md:p-10"
            >
              <img
                src="/images/pencilPic.jpg"
                alt=""
                class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                loading="lazy"
              />

              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent"></div>

              <div class="relative z-10 mt-auto">
                <h3 class="text-3xl font-extrabold tracking-tight text-white md:text-4xl">
                  Product Design
                </h3>

                <p class="mt-3 text-xs uppercase tracking-[0.25em] text-white/70">
                  Starting from $1200
                </p>

                <p class="mt-8 text-xs text-white/50">
                  *Minimum 3 months commitment
                </p>
              </div>
            </NuxtLink>

            <NuxtLink
              to="/collections"
              class="service-card group relative flex min-h-[460px] overflow-hidden rounded-xl bg-gray-900 p-8 md:p-10"
            >
              <img
                src="/images/pencilPic.jpg"
                alt=""
                class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                loading="lazy"
              />

              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent"></div>

              <div class="relative z-10 mt-auto">
                <h3 class="text-3xl font-extrabold tracking-tight text-white md:text-4xl">
                  Packaging Design
                </h3>

                <p class="mt-3 text-xs uppercase tracking-[0.25em] text-white/70">
                  Starting from $1499
                </p>
              </div>
            </NuxtLink>

            <NuxtLink
              to="/collections"
              class="service-card group relative flex min-h-[460px] overflow-hidden rounded-xl bg-gray-900 p-8 md:p-10"
            >
              <img
                src="/images/pencilPic.jpg"
                alt=""
                class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                loading="lazy"
              />

              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent"></div>

              <div class="relative z-10 mt-auto">
                <h3 class="text-3xl font-extrabold tracking-tight text-white md:text-4xl">
                  Full Time Monthly<br />
                  Commitment
                </h3>

                <p class="mt-3 text-xs uppercase tracking-[0.25em] text-white/70">
                  Starting from $4500/month
                </p>

                <p class="mt-8 text-xs text-white/50">
                  *Minimum 3 months commitment
                </p>
              </div>
            </NuxtLink>
          </div>
        </div>
      </section>

      <!-- COLLECTIONS -->
      <section class="bg-white px-6 pb-24 pt-4">
        <div class="collections-section mx-auto grid max-w-7xl grid-cols-1 gap-8 md:grid-cols-3">
          <NuxtLink
            to="/collections"
            class="group relative block min-h-[550px] overflow-hidden rounded-xl bg-gray-900 shadow md:col-span-2 md:min-h-[670px]"
            aria-label="View Collections"
          >
            <img
              src="/images/nvTest.jpg"
              alt=""
              class="absolute inset-0 h-full w-full object-cover"
              loading="lazy"
            />

            <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>

            <div class="relative z-10 flex h-full flex-col justify-end p-8">
              <h2 class="text-3xl font-extrabold text-white">
                Our Collections
              </h2>

              <p class="mt-3 max-w-xl text-white/90">
                Explore our diverse range of cabinet collections, each designed to
                meet different styles and needs.
              </p>
            </div>
          </NuxtLink>

          <NuxtLink
            to="/collections"
            class="group flex min-h-[550px] items-center justify-center rounded-xl bg-yellow-400 p-8 shadow-md md:min-h-[670px]"
            aria-label="Go shopping - Find a showroom"
          >
            <div class="flex items-center gap-4 text-2xl font-extrabold text-black md:text-3xl">
              <span>Go shopping</span>

              <span
                class="inline-flex h-10 w-10 items-center justify-center rounded-full bg-black text-lg text-yellow-400 transition-transform group-hover:translate-x-1"
                aria-hidden="true"
              >
                →
              </span>
            </div>
          </NuxtLink>
        </div>
      </section>
    </main>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import { nextTick, onMounted, onUnmounted, ref } from "vue";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const pageRef = ref<HTMLElement | null>(null);
let ctx: gsap.Context | null = null;

onMounted(async () => {
  await nextTick();

  ctx = gsap.context(() => {
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
      delay: 0.45,
    });

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

    ScrollTrigger.refresh();
  }, pageRef.value);
});

onUnmounted(() => {
  ctx?.revert();
});
</script>

<style scoped>
.hero-zoom {
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
