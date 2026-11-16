/* BASELINE — fixed-canvas three.js stage. Replace the composition, keep the discipline:
   one procedural hero object, ACES tonemap, scroll-driven camera path, reduced-motion honored. */
import * as THREE from 'three';
const canvas = document.getElementById('webgl');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const clamp01 = (v) => Math.min(1, Math.max(0, v));
try {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(36, innerWidth / innerHeight, 0.1, 80);
  camera.position.set(0, 0.3, 6.5);
  const key = new THREE.DirectionalLight(0xffffff, 2.2); key.position.set(4, 4, 3); scene.add(key, new THREE.AmbientLight(0xffffff, 1.0));
  const hero = new THREE.Mesh(new THREE.IcosahedronGeometry(1.2, 1), new THREE.MeshStandardMaterial({ color: 0x8f8f96, metalness: 0.9, roughness: 0.35 }));
  scene.add(hero);
  window.addEventListener('resize', () => { camera.aspect = innerWidth / innerHeight; camera.updateProjectionMatrix(); renderer.setSize(innerWidth, innerHeight); });
  const clock = new THREE.Clock();
  const tick = () => {
    requestAnimationFrame(tick);
    const t = clock.getElapsedTime();
    const p = clamp01(window.scrollY / Math.max(1, document.documentElement.scrollHeight - innerHeight));
    if (!reduceMotion) hero.rotation.y = t * 0.12 + p * Math.PI;
    camera.position.x = Math.sin(p * Math.PI * 1.4) * 1.6;
    camera.lookAt(0, 0, 0);
    renderer.render(scene, camera);
  };
  tick();
} catch (e) { console.warn('WebGL unavailable, running without 3D stage.', e); canvas.style.display = 'none'; }
