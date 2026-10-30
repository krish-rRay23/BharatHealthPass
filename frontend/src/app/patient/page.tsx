'use client';

import { useEffect, useState } from 'react';
import { useUserStore } from '@/store/userStore';
import { identityApi } from '@/lib/api';
import { motion } from 'framer-motion';
import { ShieldCheck, Activity, CreditCard } from 'lucide-react';

export default function PatientDashboard() {
    const { userId, name, isAuthenticated } = useUserStore();
    const [kycData, setKycData] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [treatmentLoading, setTreatmentLoading] = useState(false);
    const [activeTreatment, setActiveTreatment] = useState<string | null>(null);

    const handleStartTreatment = async () => {
        if (!userId) return;
        setTreatmentLoading(true);
        try {
            // 1. Grant Consent for TREATMENT_AUTH
            const res = await identityApi.grantConsent(userId, "TREATMENT_AUTH");
            console.log("Consent Granted:", res.data);

            // 2. In a real app, we'd wait for WebSocket pushes.
            // For prototype, we'll simulate the "Processing" delay and assume success
            // since the Orchestrator runs in the background.
            setTimeout(() => {
                setTreatmentLoading(false);
                setActiveTreatment(`BHP-${Math.random().toString(36).substr(2, 6).toUpperCase()}`);
            }, 3000);

        } catch (err) {
            console.error("Failed to start treatment", err);
            setTreatmentLoading(false);
            alert("Failed to initiate treatment. Check console.");
        }
    };

    useEffect(() => {
        if (userId) {
            // Mock fetch
            setTimeout(() => {
                setKycData({
                    kyc_verified: true,
                    document_type: "AADHAAR",
                    assurance_level: "HIGH"
                });
                setLoading(false);
            }, 1000);
        }
    }, [userId]);

    if (!isAuthenticated) {
        return <div className="p-24 text-white">Please Login First</div>;
    }

    return (
        <main className="min-h-screen bg-slate-900 text-white p-8">
            <header className="flex justify-between items-center mb-12 border-b border-slate-700 pb-4">
                <div>
                    <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400">
                        Welcome, {name}
                    </h1>
                    <p className="text-slate-400">BHP ID: {userId}</p>
                </div>
                <div className="flex items-center gap-2 px-4 py-2 bg-emerald-500/10 rounded-full text-emerald-400 border border-emerald-500/20">
                    <ShieldCheck size={20} />
                    <span className="font-semibold">Identity Verified</span>
                </div>
            </header>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                {/* Card 1: Coverage */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    className="bg-slate-800 p-6 rounded-2xl border border-slate-700"
                >
                    <div className="flex items-center gap-3 mb-4">
                        <Activity className="text-blue-400" />
                        <h2 className="text-xl font-semibold">Active Coverage</h2>
                    </div>
                    <div className="text-3xl font-bold mb-2">₹ 5,00,000</div>
                    <p className="text-sm text-slate-400">Policy #POL_8372... (Active)</p>
                </motion.div>

                {/* Card 2: Consents */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: 0.1 }}
                    className="bg-slate-800 p-6 rounded-2xl border border-slate-700"
                >
                    <div className="flex items-center gap-3 mb-4">
                        <ShieldCheck className="text-emerald-400" />
                        <h2 className="text-xl font-semibold">Consent Artifacts</h2>
                    </div>
                    <ul className="space-y-3">
                        <li className="flex justify-between text-sm p-2 bg-slate-900 rounded">
                            <span>Treatment Auth</span>
                            <span className="text-emerald-400">Active</span>
                        </li>
                        <li className="flex justify-between text-sm p-2 bg-slate-900 rounded">
                            <span>Data Sharing</span>
                            <span className="text-gray-500">Expired</span>
                        </li>
                    </ul>
                </motion.div>

                {/* Card 3: Upcoming Payments */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: 0.2 }}
                    className="bg-slate-800 p-6 rounded-2xl border border-slate-700"
                >
                    <div className="flex items-center gap-3 mb-4">
                        <CreditCard className="text-amber-400" />
                        <h2 className="text-xl font-semibold">Settlements</h2>
                    </div>
                    <div className="text-center py-8 text-slate-500">
                        No pending settlements.
                    </div>
                </motion.div>
            </div>

            {/* Action Area */}
            <section className="mt-12">
                <h3 className="text-xl font-bold mb-6">Quick Actions</h3>
                <div className="flex gap-4">
                    <button
                        onClick={handleStartTreatment}
                        disabled={treatmentLoading}
                        className="px-6 py-3 bg-blue-600 rounded-lg hover:bg-blue-700 transition flex items-center gap-2 disabled:opacity-50"
                    >
                        {treatmentLoading ? (
                            <span className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                        ) : (
                            <ShieldCheck size={20} />
                        )}
                        {treatmentLoading ? 'Authorizing...' : 'Start New Treatment'}
                    </button>
                    <button className="px-6 py-3 bg-slate-700 rounded-lg hover:bg-slate-600 transition">
                        View History
                    </button>
                </div>

                {activeTreatment && (
                    <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="mt-6 p-4 bg-emerald-500/10 border border-emerald-500/30 rounded-lg text-emerald-400"
                    >
                        <h4 className="font-bold flex items-center gap-2"><ShieldCheck size={18} /> Authorization Granted</h4>
                        <p className="text-sm opacity-80 mt-1">
                            Use Token <strong>{activeTreatment}</strong> at the Hospital Desk.
                        </p>
                    </motion.div>
                )}
            </section>
        </main>
    );
}
