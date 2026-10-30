'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import { useRouter } from 'next/navigation';
import { identityApi } from '@/lib/api';
import { useUserStore } from '@/store/userStore';

export default function Home() {
    const [mobile, setMobile] = useState('');
    const [error, setError] = useState('');
    const router = useRouter();
    const setAuth = useUserStore((state) => state.setAuth);

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');

        if (!mobile) {
            setError("Please enter a mobile number");
            return;
        }

        try {
            const res = await identityApi.login(mobile, "Demo User");
            if (res.data) {
                setAuth(res.data.user_id, "Demo User");
                router.push('/patient');
            }
        } catch (err: any) {
            console.error(err);
            setError(`Login Failed: ${err.message || 'Server Error. Check console.'}`);

            // Helpful hint for the user if they look at the UI
            if (err.code === 'ECONNREFUSED') {
                setError('Cannot reach backend. Is it running?');
            }
        }
    };

    return (
        <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gradient-to-br from-gray-900 to-black text-white overflow-hidden relative">
            <div className="absolute inset-0 z-0 opacity-20 bg-[url('/grid.svg')]"></div>

            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8 }}
                className="z-10 text-center max-w-2xl"
            >
                <h1 className="text-6xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400">
                    Bharat Health Pass
                </h1>
                <p className="text-xl text-gray-400 mb-12">
                    Agent-Orchestrated National Healthcare Access.
                    Zero Upfront Payments. 100% Consent Driven.
                </p>

                <form onSubmit={handleLogin} className="flex flex-col gap-4 max-w-md mx-auto">
                    <input
                        type="text"
                        placeholder="Enter Mobile Number"
                        value={mobile}
                        onChange={(e) => setMobile(e.target.value)}
                        className="px-6 py-4 rounded-lg bg-white/10 border border-white/20 focus:outline-none focus:border-blue-500 text-white placeholder-gray-500 backdrop-blur-md"
                    />
                    {error && (
                        <div className="p-3 bg-red-500/20 border border-red-500/50 rounded-lg text-red-200 text-sm text-center">
                            {error}
                        </div>
                    )}
                    <button
                        type="submit"
                        className="px-6 py-4 rounded-lg bg-blue-600 hover:bg-blue-700 transition font-semibold"
                    >
                        Login via OTP
                    </button>
                </form>
            </motion.div>
        </main>
    )
}
