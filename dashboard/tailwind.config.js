/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Signal AI Brand Colors
        'signal': {
          50: '#f8fafc',
          100: '#f1f5f9',
          200: '#e2e8f0',
          300: '#cbd5e1',
          400: '#94a3b8',
          500: '#64748b',
          600: '#475569',
          700: '#334155',
          800: '#1e293b',
          900: '#0f172a',
          950: '#020617'
        },
        'purple': {
          50: '#faf5ff',
          100: '#f3e8ff',
          200: '#e9d5ff',
          300: '#d8b4fe',
          400: '#c084fc',
          500: '#a855f7',
          600: '#9333ea',
          700: '#7c3aed',
          800: '#6b21a8',
          900: '#581c87',
          950: '#3b0764'
        },
        // Trading Colors
        'bullish': '#10b981', // green-500
        'bearish': '#ef4444',  // red-500
        'neutral': '#f59e0b',  // amber-500
      },
      fontFamily: {
        'sans': ['Inter', 'ui-sans-serif', 'system-ui'],
        'mono': ['JetBrains Mono', 'ui-monospace', 'monospace'],
      },
      fontSize: {
        'xs': '0.75rem',
        'sm': '0.875rem',
        'base': '1rem',
        'lg': '1.125rem',
        'xl': '1.25rem',
        '2xl': '1.5rem',
        '3xl': '1.875rem',
        '4xl': '2.25rem',
        '5xl': '3rem',
        '6xl': '3.75rem',
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '128': '32rem',
      },
      animation: {
        'pulse-slow': 'pulse 3s ease-in-out infinite',
        'bounce-slow': 'bounce 2s infinite',
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'glow': 'glow 2s ease-in-out infinite alternate',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { 
            opacity: '0',
            transform: 'translateY(20px)'
          },
          '100%': { 
            opacity: '1',
            transform: 'translateY(0)'
          },
        },
        glow: {
          '0%': { 
            boxShadow: '0 0 5px rgba(168, 85, 247, 0.3)' 
          },
          '100%': { 
            boxShadow: '0 0 20px rgba(168, 85, 247, 0.8), 0 0 30px rgba(168, 85, 247, 0.4)' 
          },
        },
      },
      backdropBlur: {
        'xs': '2px',
        'sm': '4px',
        'md': '8px',
        'lg': '16px',
        'xl': '24px',
        '2xl': '40px',
        '3xl': '64px',
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
        'signal-gradient': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'bullish-gradient': 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
        'bearish-gradient': 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)',
        'neutral-gradient': 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)',
      },
      boxShadow: {
        'glow': '0 0 20px rgba(168, 85, 247, 0.3)',
        'glow-lg': '0 0 40px rgba(168, 85, 247, 0.4)',
        'signal': '0 4px 14px 0 rgba(168, 85, 247, 0.2)',
        'signal-lg': '0 10px 25px -3px rgba(168, 85, 247, 0.3)',
      },
    },
  },
  plugins: [
    function({ addUtilities }) {
      const newUtilities = {
        '.signal-card': {
          '@apply bg-black/30 backdrop-blur-lg rounded-xl border border-purple-500/20 hover:border-purple-400/40 transition-all duration-300': {},
        },
        '.signal-button': {
          '@apply bg-gradient-to-r from-purple-600 to-pink-600 text-white font-medium rounded-lg transition-all duration-200 hover:from-purple-700 hover:to-pink-700': {},
        },
        '.signal-badge': {
          '@apply inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium': {},
        },
        '.signal-badge-bullish': {
          '@apply signal-badge bg-green-400/20 text-green-400 border border-green-400/30': {},
        },
        '.signal-badge-bearish': {
          '@apply signal-badge bg-red-400/20 text-red-400 border border-red-400/30': {},
        },
        '.signal-badge-neutral': {
          '@apply signal-badge bg-yellow-400/20 text-yellow-400 border border-yellow-400/30': {},
        },
        '.gradient-text': {
          '@apply bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent': {},
        },
        '.market-bg': {
          '@apply bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 min-h-screen': {},
        },
      }
      addUtilities(newUtilities)
    }
  ],
}