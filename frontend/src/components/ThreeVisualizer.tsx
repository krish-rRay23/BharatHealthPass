'use client';

import { Canvas } from '@react-three/fiber';
import { OrbitControls, Sphere, MeshDistortMaterial } from '@react-three/drei';

export default function ThreeVisualizer() {
    return (
        <div className="h-[300px] w-full bg-black/20 rounded-xl overflow-hidden">
            <Canvas>
                <ambientLight intensity={0.5} />
                <directionalLight position={[10, 10, 5]} intensity={1} />
                <Sphere visible args={[1, 100, 200]} scale={2}>
                    <MeshDistortMaterial
                        color="#4ade80"
                        attach="material"
                        distort={0.4}
                        speed={1.5}
                    />
                </Sphere>
                <OrbitControls enableZoom={false} />
            </Canvas>
        </div>
    );
}
