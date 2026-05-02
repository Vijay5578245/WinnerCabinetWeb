<template>
  <div
    class="relative overflow-hidden"
    :class="wrapperClass"
    :style="cssVars"
    aria-hidden="true"
  >
    <div class="absolute inset-0 stripes-layer" />
    <div v-if="$slots.default" class="relative">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  wrapperClass?: string
  angle?: number
  stripe?: number
  gap?: number
  color?: string
  base?: string
  opacity?: number
}

const props = withDefaults(defineProps<Props>(), {
  wrapperClass: 'h-16 w-full rounded-xl',
  angle: 25,
  stripe: 10,
  gap: 10,
  color: '#FACC15',
  base: 'transparent',
  opacity: 1,
})

const cssVars = computed(() => ({
  '--s-angle': `${props.angle}deg`,
  '--s-size': `${props.stripe}px`,
  '--s-gap': `${props.gap}px`,
  '--s-color': props.color,
  '--s-base': props.base,
  '--s-opacity': `${props.opacity}`,
} as Record<string, string>))
</script>

<style scoped>
.stripes-layer {
  opacity: var(--s-opacity);
  background: repeating-linear-gradient(
    var(--s-angle),
    var(--s-color) 0,
    var(--s-color) var(--s-size),
    var(--s-base) var(--s-size),
    var(--s-base) calc(var(--s-size) + var(--s-gap))
  );
}
</style>
