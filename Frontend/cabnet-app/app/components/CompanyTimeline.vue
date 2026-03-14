<template>
  <section ref="containerRef" class="relative w-full bg-white py-15 overflow-hidden">
  <div class="absolute h-full w-full dotted-fade z-10"></div>
    <!-- section header -->
    <div class="max-w-7xl mx-auto px-6 mb-16">
      <p class="text-yellow-500 text-xs font-bold tracking-[0.2em] uppercase mb-3">Our Story</p>
      <h2 class="text-4xl md:text-5xl font-extrabold text-black leading-tight">
        Built on a decade<br />of craftsmanship
      </h2>
      <div class="mt-5 h-px w-16 bg-yellow-400"></div>
    </div>

    <!-- timeline body -->
    <div class="relative max-w-7xl mx-auto px-6">
      <!-- track: static grey line -->
      <div
        class="absolute left-8 md:left-[88px] top-0 bottom-0 w-[3px] bg-gray-100 rounded-full"
        aria-hidden="true"
      ></div>

      <!-- animated progress line (glowing yellow) -->
      <div
        ref="lineRef"
        class="timeline-line absolute left-8 md:left-[88px] top-0 w-[3px] rounded-full origin-top"
        style="height: 0%"
        aria-hidden="true"
      ></div>

      <!-- entries -->
      <div class="flex flex-col gap-0">
        <div
          v-for="(entry, i) in timeline"
          :key="i"
          class="timeline-entry relative flex gap-6 md:gap-12 pl-20 md:pl-[152px] pb-20"
        >
          <!-- dot on track -->
          <div
            class="timeline-dot absolute left-[24px] md:left-[76px] top-1.5 w-7 h-7 rounded-full border-2 border-gray-200 bg-white flex items-center justify-center"
          >
            <div class="w-2.5 h-2.5 rounded-full bg-gray-300 timeline-dot-inner"></div>
          </div>

          <!-- year label (left of track on md+) -->
          <div class="absolute left-0 top-0 hidden md:flex flex-col items-end pr-[20px] w-[68px]">
            <span class="text-[13px] font-black tracking-widest text-gray-400 timeline-year leading-none">
              {{ entry.year }}
            </span>
          </div>

          <!-- content card -->
          <div class="timeline-card flex-1 min-w-0">
            <!-- mobile year -->
            <span class="md:hidden text-[11px] font-black tracking-widest text-yellow-500 uppercase mb-2 block timeline-year">
              {{ entry.year }}
            </span>

            <!-- card shell -->
            <div class="rounded-2xl border border-gray-100 bg-gray-50/60 overflow-hidden shadow-sm">

              <!-- image strip -->
              <div
                v-if="entry.images && entry.images.length"
                class="grid gap-0.5"
                :class="entry.images.length > 1 ? 'grid-cols-2' : 'grid-cols-1'"
              >
                <div
                  v-for="(img, imgIdx) in entry.images"
                  :key="imgIdx"
                  class="overflow-hidden"
                  :class="entry.images.length === 1 ? 'h-52 md:h-72' : 'h-44 md:h-60'"
                >
                  <img
                    :src="img"
                    alt=""
                    class="w-full h-full object-cover"
                    loading="lazy"
                  />
                </div>
              </div>

              <!-- card body -->
              <div class="p-6 md:p-8">
                <!-- stat highlight (optional) -->
                <div v-if="entry.stat" class="mb-5 flex items-end gap-3">
                  <span class="text-5xl md:text-6xl font-black text-yellow-400 leading-none">{{ entry.stat.value }}</span>
                  <span class="text-sm font-semibold text-gray-500 mb-1.5 leading-tight">{{ entry.stat.label }}</span>
                </div>

                <h3 class="text-xl md:text-2xl font-extrabold text-gray-900 mb-3 leading-snug">
                  {{ entry.title }}
                </h3>
                <p class="text-gray-600 leading-relaxed text-base">
                  {{ entry.description }}
                </p>

                <!-- tags -->
                <div v-if="entry.tags && entry.tags.length" class="mt-5 flex flex-wrap gap-2">
                  <span
                    v-for="tag in entry.tags"
                    :key="tag"
                    class="rounded-full bg-white border border-gray-200 px-3 py-1 text-xs font-semibold text-gray-600 tracking-wide"
                  >
                    {{ tag }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick } from "vue";

let onLoad: (() => void) | null = null;
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const containerRef = ref<HTMLElement | null>(null);
const lineRef = ref<HTMLElement | null>(null);

const timeline = [
  {
    year: "2012",
    title: "Where It All Began",
    description:
      "Eric Chen founded Winner Cabinets with a single workshop and a belief that every home deserves cabinets built with care. The first commissions were local kitchen renovations — small in scale, but the start of something lasting.",
    images: ["/images/nvTest.jpg"],
    tags: ["Founded", "Vancouver"],
    stat: null,
  },
  {
    year: "2015",
    title: "Expanding the Workshop",
    description:
      "Growing demand led to a larger facility and a dedicated team of craftsmen. We began taking on commercial millwork projects alongside residential work, doubling our capacity and range of finishes.",
    images: ["/images/nvTest.jpg", "/images/nvTest.jpg"],
    tags: ["Expansion", "Commercial Projects"],
    stat: { value: "2×", label: "capacity\nincreased" },
  },
  {
    year: "2018",
    title: "Custom Design Studio Opens",
    description:
      "We launched our in-house design studio, giving clients a hands-on showroom experience to select materials, hardware, and layouts before a single board is cut. Transparent pricing became our signature.",
    images: ["/images/nvTest.jpg"],
    tags: ["Design Studio", "Showroom"],
    stat: null,
  },
  {
    year: "2021",
    title: "Weathering the Storm",
    description:
      "Through supply chain disruptions, we doubled down on local sourcing — partnering with regional suppliers to maintain quality and keep lead times predictable for every client.",
    images: ["/images/nvTest.jpg", "/images/nvTest.jpg"],
    tags: ["Local Materials", "Resilience"],
    stat: { value: "100%", label: "local\nsourcing" },
  },
  {
    year: "2024",
    title: "Trusted by Hundreds of Families",
    description:
      "Today Winner Cabinets has delivered over 500 custom projects across Metro Vancouver. From starter condos to large estates, the same precision and personal service Eric started with still drives every build.",
    images: ["/images/nvTest.jpg"],
    tags: ["500+ Projects", "Metro Vancouver"],
    stat: { value: "500+", label: "projects\ncompleted" },
  },
];

let ctx: gsap.Context | null = null;

onMounted(() => {
  const container = containerRef.value;
  const line = lineRef.value;
  if (!container || !line) return;

  ctx = gsap.context(() => {
    gsap.to(line, {
      height: "100%",
      ease: "none",
      scrollTrigger: {
        trigger: container,
        start: "top 80%",
        end: "bottom 20%",
        scrub: 0.6,
        invalidateOnRefresh: true,
      },
    });

    const entries = container.querySelectorAll(".timeline-entry");
    entries.forEach((entry) => {
      const card = entry.querySelector(".timeline-card");
      const dot = entry.querySelector(".timeline-dot");
      const dotInner = entry.querySelector(".timeline-dot-inner");
      const year = entry.querySelector(".timeline-year");

      gsap.set([card, year], { autoAlpha: 0, y: 24 });
      gsap.set(dot, { scale: 0.5 });

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: entry,
          start: "top 80%",
          toggleActions: "play none none reverse",
          invalidateOnRefresh: true,
        },
      });

      tl.to(dot, { scale: 1, duration: 0.45, ease: "back.out(2)" })
        .to(dotInner, { backgroundColor: "#f59e0b", duration: 0.3 }, "<0.05")
        .to(year, { autoAlpha: 1, y: 0, duration: 0.5, ease: "power2.out" }, "<")
        .to(card, { autoAlpha: 1, y: 0, duration: 0.55, ease: "power2.out" }, "<0.08");
    });
  }, container);

  if (document.readyState === "complete") {
    nextTick(() => ScrollTrigger.refresh());
  } else {
    onLoad = () => ScrollTrigger.refresh();
    window.addEventListener("load", onLoad);
  }
});

onUnmounted(() => {
  ctx?.revert();
  if (onLoad) window.removeEventListener("load", onLoad);
});
</script>

<style scoped>
.timeline-line {
  background: linear-gradient(to bottom, #fbbf24, #f59e0b, #fcd34d);
  box-shadow: 0 0 10px 2px rgba(251, 191, 36, 0.55), 0 0 24px 4px rgba(251, 191, 36, 0.2);
}

.timeline-dot {
  z-index: 2;
}
</style>
