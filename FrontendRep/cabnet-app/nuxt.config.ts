export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  app: {
    head: {
      title: 'Winner Cabinets',
      meta: [
        { name: 'description', content: 'Custom cabinets crafted with precision. Built to last. Winner Cabinets — Richmond, BC.' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      ],
      bodyAttrs: {
        class: 'bg-white text-gray-900',
      },
    },
  },
  devtools: { enabled: true },
  modules: ['@nuxt/eslint', '@nuxt/ui', '@nuxt/scripts', '@nuxtjs/i18n', '@nuxt/fonts'],
  css: ['@/assets/css/main.css'],
  fonts: {
    processCSSVariables: true,
  },
  i18n: {
    strategy: 'prefix',
    defaultLocale: 'zh',
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: 'i18n_redirected',
      redirectOn: 'root',
    },
    locales: [
      { code: 'en', iso: 'en-US', name: 'English', file: 'en.json' },
      { code: 'zh', iso: 'zh-CN', name: '中文', file: 'zh.json' },
    ],
  },
  runtimeConfig: {
    public: {
      apiBaseUrl: '',
    },
  },
})
