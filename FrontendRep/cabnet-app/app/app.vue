<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
const { locale } = useI18n()

useHead(() => ({
  htmlAttrs: { lang: locale.value },
  title: locale.value === 'zh' ? 'Winner Cabinets — 首页' : 'Winner Cabinets — Home',
}))
</script>
