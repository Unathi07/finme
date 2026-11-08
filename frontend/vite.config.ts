import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
export default defineConfig({ root: '.', envDir: '..', plugins: [react(), tailwindcss()], test: { globals: true, environment: 'jsdom', setupFiles: './src/test-setup.ts' } });
