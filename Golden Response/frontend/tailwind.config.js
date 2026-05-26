/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      fontFamily: {
        display: ['Fraunces', 'serif'],
        sans: ['Space Grotesk', 'ui-sans-serif', 'system-ui']
      },
      colors: {
        ember: {
          50: '#fff7ed',
          100: '#ffedd5',
          300: '#fdba74',
          500: '#f97316',
          700: '#c2410c'
        },
        pine: {
          100: '#dbe9df',
          300: '#9ebaa5',
          500: '#557c66',
          700: '#244636'
        },
        ink: {
          50: '#f6f5f2',
          100: '#edeae3',
          700: '#413a33',
          900: '#1d1916'
        }
      },
      boxShadow: {
        soft: '0 18px 60px rgba(29, 25, 22, 0.12)',
        glow: '0 10px 40px rgba(249, 115, 22, 0.18)'
      },
      backgroundImage: {
        haze:
          'radial-gradient(circle at top left, rgba(249, 115, 22, 0.22), transparent 36%), radial-gradient(circle at bottom right, rgba(85, 124, 102, 0.26), transparent 34%)'
      }
    }
  },
  plugins: []
};
