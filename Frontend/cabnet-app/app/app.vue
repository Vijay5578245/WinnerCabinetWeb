<template>
<NuxtLayout>
  <NuxtPage />
</NuxtLayout>
</template>

<script setup lang="ts">
const {locale} = useI18n();

useHead(() => ({
  title: locale.value === 'zh' ? 'Cabnet - 首页' : 'Cabnet - Home',
  htmlAttrs: {
    lang: locale.value === 'zh' ? 'zh' : 'en',
  },
}));
</script>
