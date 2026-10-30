import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface UserState {
    userId: string | null;
    name: string | null;
    isAuthenticated: boolean;
    setAuth: (userId: string, name: string) => void;
    logout: () => void;
}

export const useUserStore = create<UserState>()(
    persist(
        (set) => ({
            userId: null,
            name: null,
            isAuthenticated: false,
            setAuth: (userId, name) => set({ userId, name, isAuthenticated: true }),
            logout: () => set({ userId: null, name: null, isAuthenticated: false }),
        }),
        {
            name: 'bhp-user-storage',
            storage: {
                getItem: (name) => {
                    const str = localStorage.getItem(name);
                    return str ? JSON.parse(str) : null;
                },
                setItem: (name, value) => {
                    localStorage.setItem(name, JSON.stringify(value));
                },
                removeItem: (name) => localStorage.removeItem(name),
            },
        }
    )
);
