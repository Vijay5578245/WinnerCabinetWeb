<template>
  <div :style="{ paddingBottom: footerHeight + 'px' }">
    <AppHeader />
    <slot />
    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const footerHeight = ref(0)
let footerRO: ResizeObserver | null = null

onMounted(() => {
  const footer = document.querySelector('footer')
  if (footer) {
    footerHeight.value = footer.offsetHeight
    footerRO = new ResizeObserver(() => { footerHeight.value = footer.offsetHeight })
    footerRO.observe(footer)
  }
})

onUnmounted(() => {
  footerRO?.disconnect()
})
</script>
