import { createI18n } from 'vue-i18n'

// Import locale messages
import enHome from './locales/en/home.json'
import zhHome from './locales/zh/home.json'
import enMainView from './locales/en/mainView.json'
import zhMainView from './locales/zh/mainView.json'
import enStep1 from './locales/en/step1.json'
import zhStep1 from './locales/zh/step1.json'
import enStep2 from './locales/en/step2.json'
import zhStep2 from './locales/zh/step2.json'
import enStep3 from './locales/en/step3.json'
import zhStep3 from './locales/zh/step3.json'
import enStep4 from './locales/en/step4.json'
import zhStep4 from './locales/zh/step4.json'
import enStep5 from './locales/en/step5.json'
import zhStep5 from './locales/zh/step5.json'
import enGraphPanel from './locales/en/graphPanel.json'
import zhGraphPanel from './locales/zh/graphPanel.json'
import enHistory from './locales/en/history.json'
import zhHistory from './locales/zh/history.json'
import enSimulation from './locales/en/simulation.json'
import zhSimulation from './locales/zh/simulation.json'
import enReport from './locales/en/report.json'
import zhReport from './locales/zh/report.json'
import enInteraction from './locales/en/interaction.json'
import zhInteraction from './locales/zh/interaction.json'
import enCommon from './locales/en/common.json'
import zhCommon from './locales/zh/common.json'
import enProcess from './locales/en/process.json'
import zhProcess from './locales/zh/process.json'

const messages = {
  en: {
    home: enHome,
    mainView: enMainView,
    step1: enStep1,
    step2: enStep2,
    step3: enStep3,
    step4: enStep4,
    step5: enStep5,
    graphPanel: enGraphPanel,
    history: enHistory,
    simulation: enSimulation,
    report: enReport,
    interaction: enInteraction,
    common: enCommon,
    process: enProcess
  },
  zh: {
    home: zhHome,
    mainView: zhMainView,
    step1: zhStep1,
    step2: zhStep2,
    step3: zhStep3,
    step4: zhStep4,
    step5: zhStep5,
    graphPanel: zhGraphPanel,
    history: zhHistory,
    simulation: zhSimulation,
    report: zhReport,
    interaction: zhInteraction,
    common: zhCommon,
    process: zhProcess
  }
}

const i18n = createI18n({
  legacy: false,
  locale: localStorage.getItem('mirofish-lang') || 'en',
  fallbackLocale: 'en',
  messages
})

export default i18n
