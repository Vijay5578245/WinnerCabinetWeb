<template>

<NuxtLink
        :to="props.to"
        class="relative mt-8 inline-block text-black font-medium rounded-[2px] shadow
        transition border border-yellow-300 transition-colors duration-300"
        :class="props.class"
      >

          <div
    class="absolute inset-0 z-0
           bg-[radial-gradient(circle_at_1px_1px,rgba(0,0,0,0.15)_1px,transparent_0)]
            [background-size:12px_12px] backdrop-blur-sm"
  ></div>

        <p class="relative">
        <slot />
        </p>

      </NuxtLink>
</template>

<script setup lang="ts">

const props = defineProps<{
  to: string,
  class?: string
}>();


</script>
