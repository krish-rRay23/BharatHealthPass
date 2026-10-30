'use client';

export default function HospitalDashboard() {
    return (
        <main className="min-h-screen bg-slate-900 text-white p-8">
            <h1 className="text-3xl font-bold mb-8 text-blue-400">Hospital Administration</h1>
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 min-h-[400px]">
                    <h2 className="text-xl font-semibold mb-4">Patient Queue</h2>
                    <p className="text-slate-500">No active patients.</p>
                </div>
                <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 min-h-[400px]">
                    <h2 className="text-xl font-semibold mb-4">Claims Status</h2>
                    <p className="text-slate-500">No active claims.</p>
                </div>
            </div>
        </main>
    )
}
