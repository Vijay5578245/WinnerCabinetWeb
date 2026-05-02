<template>
  <NuxtLink
    :to="to"
    class="inline-flex items-center justify-center gap-2 border border-yellow-400/60 font-medium rounded-sm transition-all duration-200 hover:bg-yellow-400 hover:border-yellow-400 hover:text-black focus:outline-none focus-visible:ring-2 focus-visible:ring-yellow-400"
    :class="sizeClasses"
  >
    <slot />
  </NuxtLink>
</template>

<script setup lang="ts">
interface Props {
  to: string
  size?: 'sm' | 'md' | 'lg'
}

const props = withDefaults(defineProps<Props>(), { size: 'md' })

const sizeClasses = computed(() => {
  if (props.size === 'sm') return 'px-5 py-2.5 text-sm'
  if (props.size === 'lg') return 'px-10 py-5 text-base'
  return 'px-8 py-4 text-sm'
})
</script>
