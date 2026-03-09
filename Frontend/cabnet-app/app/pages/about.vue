<template>
  <main>
    <div class="relative">
      <header class="max-w-7xl mx-auto px-6 text-gray-900 pt-20">
        <!-- Hero header -->
        <h1
          class="text-5xl md:text-6xl font-extrabold leading-tight reveal"
          data-reveal-delay="0"
        >
          {{$t("about.title")}}
        </h1>
        <p class="reveal" data-reveal-delay="120">
        </p>

      </header>

      <div
        class="w-full h-30 z-10 text-lg text-gray-700 absolute bg-gradient-to-b from-white via-white/40 to-white/0"
      ></div>
    </div>

    <!-- Hero image -->
    <section class="sticky top-0 h-auto">
      <div class="">
        <img
          :src="heroImage"
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
        <!-- Scroll starts here -->

        <section
          class="flex items-center mb-12 shadow-lg gap-8 md:gap-16 flex-col md:flex-row"
          data-reveal-delay="260"
        >
          <div class="order-2">
            <h2
              class="text-3xl font-extrabold mb-4"
              data-reveal-delay="320"
            >
              CEO Eric Chen
            </h2>
            <p class="text-gray-700 mb-4 pr-5" data-reveal-delay="380">
              {{ $t("about.ceoDescription") }}
            </p>
          </div>

          <div class="" data-reveal-delay="440">
            <img
              :src="pfImage"
              alt="CEO image"
              class="w-full h-80 md:h-96 object-cover rounded shadow-lg"
              loading="lazy"
            />
          </div>
        </section>

        <section class="grid gap-8 md:grid-cols-2 items-center mb-12">
          <div class="order-1 reveal" data-reveal-delay="120">
            <h3
              class="text-xl font-semibold mb-3 reveal"
              data-reveal-delay="160"
            >
              INSIDE LAPALMA
            </h3>
            <h4 class="font-medium mb-2 reveal" data-reveal-delay="200">
              Our Vision
            </h4>
            <p class="text-gray-700 reveal" data-reveal-delay="240">
              We see design as more than aesthetics — it's a way of living that
              elevates everyday moments. Our work focuses on simplicity,
              quality, and thoughtful details that last.
            </p>
          </div>

          <div class="order-2 reveal" data-reveal-delay="300">
            <img
              :src="visionImage"
              alt="vision image"
              class="w-full h-64 md:h-80 object-cover rounded shadow-lg"
              loading="lazy"
            />
          </div>
        </section>

        <!-- MISSION: image left (bigger), text right -->
        <section class="grid gap-8 md:grid-cols-2 items-center mb-12">
          <div class="order-2 md:order-1 reveal" data-reveal-delay="120">
            <img
              :src="missionImage"
              alt="mission image"
              class="w-full h-96 md:h-[520px] object-cover rounded shadow-lg"
              loading="lazy"
            />
          </div>

          <div class="order-1 md:order-2 reveal" data-reveal-delay="220">
            <h4
              class="text-xl font-semibold mb-3 reveal"
              data-reveal-delay="260"
            >
              Our Mission
            </h4>
            <p class="text-gray-700 mb-4 reveal" data-reveal-delay="300">
              To craft furniture that balances timeless form with comfort and
              function. We prioritize sustainable choices, careful
              craftsmanship, and enduring materials so every piece feels as good
              as it looks.
            </p>

            <p class="text-gray-600 reveal" data-reveal-delay="340">
              Contact us to learn more about our process and materials.
            </p>
          </div>
        </section>

        <section
          class="mt-12 prose prose-lg max-w-none text-gray-700 reveal"
          data-reveal-delay="120"
        >
          <h2 class="text-2xl font-semibold mb-4">Get to know us</h2>
          <p>
            From our carefully curated collections to our commitment to
            sustainability, every aspect of Lapalma reflects our dedication to
            quality and design. We invite you to explore our offerings and
            discover how our furniture can enhance your living spaces.
          </p>
        </section>

        <!-- factory pictures and description -->
        <div class="h-[100px]"></div>

        <div class="flex flex-col items-center gap-3">
          <p class="text-yellow-500 text-xs font-bold tracking-[0.2em] uppercase">Our Facility</p>
          <p class="text-black font-bold text-[30px] md:text-[40px] w-full text-center">
            {{ $t("index.factory.header") }}
          </p>
          <div class="flex items-center gap-3 mt-1">
            <div class="h-px w-16 bg-gray-300"></div>
            <div class="h-1.5 w-1.5 rounded-full bg-yellow-400"></div>
            <div class="h-px w-16 bg-gray-300"></div>
          </div>
        </div>

        <section class="dotted-fade h-[2000px] relative mt-12">
          <div class="h-[75px]"></div>

          <div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 px-6 py-12">
              <div class="flex items-center justify-center">
                <section
                  class="flex flex-col h-44 md:h-64 w-64 md:w-128 bg-white shadow-lg rounded-lg overflow-hidden"
                >
                  <div>
                    <img src="/images/nvTest.jpg" alt="" />
                  </div>

                  <div>
                    <h1 class="text-gray-900 font-bold text-2xl">Title</h1>
                  </div>
                </section>
              </div>
              <div class="relative flex flex-col text-black items-center justify-center">
                <p class="text-[30px] md:text-[40px] w-full text-center">
                  TITLE is gonna be long as fuck boi holy
                </p>
                <p class="p-30">
                  some testing words to see if the card can expand with content and maintain
                  the same height as the other card. This is to test the flexbox layout and
                  see if it can handle different content sizes without breaking the design
                  or causing overflow issues. The card should be able to grow in height
                  while keeping the overall layout intact and visually appealing.
                </p>
              </div>
            </div>
          </div>
        </section>

        <!-- Large visual / CTA -->
        <section class="mt-8 reveal" data-reveal-delay="120">
          <div class="rounded overflow-hidden shadow-lg">
            <img
              :src="ctaImage"
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

<script setup>
import { onMounted, onBeforeUnmount } from "vue";
import heroImage from "/images/storeTest.jpg"; // replace with your hero image
import ctaImage from "/images/storeTest.jpg"; // large visual at bottom
import visionImage from "/images/nvTest.jpg"; // vision section image
import missionImage from "/images/nvTest.jpg"; // mission section image
import pfImage from "/images/pfTest.jpg"; // crafted simplicity image

// simple intersection observer reveal with stagger support
let observer;
onMounted(() => {
  const reveals = Array.from(document.querySelectorAll(".reveal"));
  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const el = entry.target;
        if (entry.isIntersecting) {
          // apply per-element delay from data attribute if present
          const delay = el.dataset.revealDelay ?? "0";
          el.style.transitionDelay = `${delay}ms`;
          el.classList.add("is-visible");
          observer.unobserve(el);
        }
      });
    },
    { threshold: 0.12 }
  );

  reveals.forEach((el) => observer.observe(el));
});

onBeforeUnmount(() => {
  if (observer) observer.disconnect();
});
</script>

<style scoped>
/* reveal animation: elements flow down into place */
.reveal {
  opacity: 0;
  transform: translateY(-36px); /* start slightly above -> flows down */
  transition-property: transform, opacity;
  transition-duration: 640ms;
  transition-timing-function: cubic-bezier(0.22, 0.9, 0.37, 1);
  will-change: transform, opacity;
}

/* visible state */
.reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
}

/* small responsive tweak: faster on mobile */
@media (max-width: 640px) {
  .reveal {
    transition-duration: 520ms;
    transform: translateY(-22px);
  }
}

/* slight stagger fallback if multiple elements appear at same time */
.reveal + .reveal {
  transition-delay: 80ms;
}

/* preserve existing styling */
main {
  border-radius: 10px;
}
.prose img {
  border-radius: 6px;
}
</style>
