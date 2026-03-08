<!-- components/DiagonalStripes.vue -->
<template>
  <div
    class="relative overflow-hidden"
    :class="wrapperClass"
    :style="stripeVars"
    aria-hidden="true"
  >
    <!-- pattern layer -->
    <div class="absolute inset-0 stripes" />

    <!-- optional content slot -->
    <div v-if="$slots.default" class="relative">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
type Props = {
  /**
   * Wrapper classes like: "h-16 rounded-xl"
   */
  wrapperClass?: string

  /**
   * Stripe angle in degrees. (e.g. 20, 30, 45)
   */
  angle?: number

  /**
   * Stripe thickness in px.
   */
  stripe?: number

  /**
   * Gap thickness in px (space between stripes).
   */
  gap?: number

  /**
   * Stripe color (any CSS color).
   */
  color?: string

  /**
   * Background under the stripes (usually transparent).
   */
  base?: string

  /**
   * Opacity of stripe layer (0 ~ 1).
   */
  opacity?: number
}

const props = withDefaults(defineProps<Props>(), {
  wrapperClass: "h-16 w-full rounded-xl",
  angle: 25,
  stripe: 10,
  gap: 10,
  color: "#FACC15", // Tailwind yellow-400-ish
  base: "transparent",
  opacity: 1,
})

const stripeVars = computed(() => {
  return {
    "--stripe-angle": `${props.angle}deg`,
    "--stripe-size": `${props.stripe}px`,
    "--stripe-gap": `${props.gap}px`,
    "--stripe-color": props.color,
    "--stripe-base": props.base,
    "--stripe-opacity": `${props.opacity}`,
  } as Record<string, string>
})
</script>

<style scoped>
.stripes {
  opacity: var(--stripe-opacity);
  background:
    repeating-linear-gradient(
      var(--stripe-angle),
      var(--stripe-color) 0,
      var(--stripe-color) var(--stripe-size),
      var(--stripe-base) var(--stripe-size),
      var(--stripe-base) calc(var(--stripe-size) + var(--stripe-gap))
    );
}
</style>
