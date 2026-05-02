export default defineNuxtPlugin(() => {
  if (typeof history !== 'undefined') {
    history.scrollRestoration = 'manual'
  }
})
