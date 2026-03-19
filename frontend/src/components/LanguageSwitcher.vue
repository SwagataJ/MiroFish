<template>
  <button class="lang-switcher" @click="toggleLanguage" :title="currentLocale === 'en' ? 'Switch to Chinese' : 'Switch to English'">
    {{ currentLocale === 'en' ? 'ZH' : 'EN' }}
  </button>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const { locale } = useI18n({ useScope: 'global' })

const currentLocale = locale

const toggleLanguage = () => {
  const newLang = locale.value === 'en' ? 'zh' : 'en'
  locale.value = newLang
  localStorage.setItem('mirofish-lang', newLang)
}
</script>

<style scoped>
.lang-switcher {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: inherit;
  padding: 4px 12px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  letter-spacing: 0.5px;
  border-radius: 2px;
}

.lang-switcher:hover {
  border-color: rgba(255, 255, 255, 0.6);
  background: rgba(255, 255, 255, 0.1);
}
</style>
