import type { Config } from "tailwindcss";

const config: Config = {
    content: [
        "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
        "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
        "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
        extend: {
            colors: {
                primary: "#2563EB", // Blue 600
                secondary: "#7C3AED", // Violet 600
                success: "#059669", // Emerald 600
                warning: "#D97706", // Amber 600
                danger: "#DC2626", // Red 600
                background: "#0F172A", // Slate 900
                surface: "#1E293B", // Slate 800
            },
            backgroundImage: {
                "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
            },
        },
    },
    plugins: [],
};
export default config;
