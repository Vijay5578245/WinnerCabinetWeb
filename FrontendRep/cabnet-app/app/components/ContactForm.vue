<template>
  <div>
    <!-- Success -->
    <div v-if="success" class="py-8 text-center">
      <div class="inline-flex items-center justify-center w-12 h-12 rounded-full bg-yellow-400/20 mb-4">
        <svg class="w-6 h-6 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
        </svg>
      </div>
      <p class="text-white font-extrabold text-lg mb-1">Message sent!</p>
      <p class="text-white/50 text-sm">We'll get back to you shortly.</p>
    </div>

    <!-- Form -->
    <form v-else class="space-y-5" @submit.prevent="submit">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
        <label class="flex flex-col gap-1.5">
          <span class="text-[10px] font-bold uppercase tracking-[0.18em] text-white/50">Name *</span>
          <input
            v-model="form.name"
            type="text"
            required
            placeholder="Jane Smith"
            class="bg-white/10 border border-white/15 text-white placeholder:text-white/25 px-4 py-3 text-sm rounded-lg focus:outline-none focus:border-yellow-400 transition-colors"
          />
        </label>

        <label class="flex flex-col gap-1.5">
          <span class="text-[10px] font-bold uppercase tracking-[0.18em] text-white/50">Email *</span>
          <input
            v-model="form.email"
            type="email"
            required
            placeholder="jane@email.com"
            class="bg-white/10 border border-white/15 text-white placeholder:text-white/25 px-4 py-3 text-sm rounded-lg focus:outline-none focus:border-yellow-400 transition-colors"
          />
        </label>

        <label class="flex flex-col gap-1.5">
          <span class="text-[10px] font-bold uppercase tracking-[0.18em] text-white/50">Phone</span>
          <input
            v-model="form.phone"
            type="tel"
            placeholder="(604) 000-0000"
            class="bg-white/10 border border-white/15 text-white placeholder:text-white/25 px-4 py-3 text-sm rounded-lg focus:outline-none focus:border-yellow-400 transition-colors"
          />
        </label>

        <label class="flex flex-col gap-1.5">
          <span class="text-[10px] font-bold uppercase tracking-[0.18em] text-white/50">Service *</span>
          <input
            v-model="form.service"
            type="text"
            required
            placeholder="Kitchen cabinets, bathroom..."
            class="bg-white/10 border border-white/15 text-white placeholder:text-white/25 px-4 py-3 text-sm rounded-lg focus:outline-none focus:border-yellow-400 transition-colors"
          />
        </label>
      </div>

      <label class="flex flex-col gap-1.5">
        <span class="text-[10px] font-bold uppercase tracking-[0.18em] text-white/50">Message *</span>
        <textarea
          v-model="form.message"
          required
          rows="4"
          placeholder="Tell us about your project..."
          class="bg-white/10 border border-white/15 text-white placeholder:text-white/25 px-4 py-3 text-sm rounded-lg focus:outline-none focus:border-yellow-400 transition-colors resize-none"
        />
      </label>

      <!-- Honeypot -->
      <input
        v-model="form.website"
        type="text"
        class="absolute -left-[9999px]"
        tabindex="-1"
        autocomplete="off"
        aria-hidden="true"
      />

      <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4">
        <button
          type="submit"
          :disabled="loading"
          class="shrink-0 inline-flex items-center gap-2 bg-yellow-400 hover:bg-yellow-500 disabled:opacity-60 disabled:cursor-not-allowed text-black font-bold px-8 py-3 text-sm rounded-xl transition-colors"
        >
          <span v-if="loading" class="inline-block w-4 h-4 border-2 border-black/30 border-t-black rounded-full animate-spin" />
          {{ loading ? 'Sending…' : 'Send Message →' }}
        </button>
        <p v-if="formError" class="text-red-400 text-sm">{{ formError }}</p>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits<{ submitted: [] }>()

const form = ref({ name: '', email: '', phone: '', service: '', message: '', website: '' })
const loading = ref(false)
const success = ref(false)
const formError = ref('')
const config = useRuntimeConfig()

const submit = async () => {
  loading.value = true
  success.value = false
  formError.value = ''

  if (form.value.website) {
    loading.value = false
    success.value = true
    return
  }

  try {
    const response = await fetch(`${config.public.apiBaseUrl}/contact/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form.value),
    })
    if (!response.ok) throw new Error('Failed to submit')
    success.value = true
    form.value = { name: '', email: '', phone: '', service: '', message: '', website: '' }
    emit('submitted')
  } catch (err) {
    formError.value = err instanceof Error ? err.message : 'An unknown error occurred'
  } finally {
    loading.value = false
  }
}
</script>
