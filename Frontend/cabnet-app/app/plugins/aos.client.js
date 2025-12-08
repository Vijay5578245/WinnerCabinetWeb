// app/plugins/aos.client.ts
import AOS from 'aos'
import 'aos/dist/aos.css'

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.hook('app:mounted', () => {
    AOS.init({
      duration: 800,
      once: true,
      offset: 50,
    })
  })
})
