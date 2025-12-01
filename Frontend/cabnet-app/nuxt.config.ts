import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  app: {
    head: {
      title: 'Winner Cabinets',
      meta: [
        { name: 'description', content: 'My awesome site' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      ],
      bodyAttrs: {
        class: 'bg-slate-900 text-white',    // global body classes
      },
    },
  },
  devtools: { enabled: true },
  modules: ['@nuxt/eslint', '@nuxt/ui', '@nuxt/scripts'],
  css: ['@/assets/css/main.css'],
  vite: {
    plugins : [
      tailwindcss(),
    ],
  },
})
