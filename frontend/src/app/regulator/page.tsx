'use client';

import { useState } from 'react';
import ThreeVisualizer from '@/components/ThreeVisualizer';

export default function RegulatorDashboard() {
    const [logs] = useState([
        { id: 1, event: "IDENTITY_VERIFIED", agent: "IdentityAgent", time: "10:00:01" },
        { id: 2, event: "CONSENT_GRANTED", agent: "IdentityAgent", time: "10:00:05" },
        { id: 3, event: "ELIGIBILITY_CHECKED", agent: "EligibilityAgent", time: "10:00:06" },
        { id: 4, event: "RISK_APPROVED", agent: "RiskAgent", time: "10:00:07" },
        { id: 5, event: "SETTLEMENT_AUTHORIZED", agent: "SettlementAgent", time: "10:00:08" },
    ]);

    return (
        <main className="min-h-screen bg-slate-900 text-white p-8">
            <h1 className="text-3xl font-bold mb-8 text-amber-500">Regulator Audit Portal</h1>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <div className="lg:col-span-2 space-y-4">
                    {logs.map((log) => (
                        <div key={log.id} className="bg-slate-800 p-4 rounded border-l-4 border-blue-500 flex justify-between">
                            <div>
                                <span className="font-mono text-blue-400 mr-4">{log.time}</span>
                                <span className="font-bold">{log.event}</span>
                            </div>
                            <div className="text-slate-400 text-sm">
                                {log.agent}
                            </div>
                        </div>
                    ))}
                </div>

                <div className="lg:col-span-1">
                    <div className="bg-slate-800 p-4 rounded-xl border border-slate-700 h-full">
                        <h2 className="text-xl font-bold mb-4">System State Replay</h2>
                        <ThreeVisualizer />
                        <p className="mt-4 text-sm text-slate-400">
                            Visualizing deterministic state transitions for Case #8372.
                        </p>
                    </div>
                </div>
            </div>
        </main>
    )
}
