(function () {
  // Scene setup
  const scene = new THREE.Scene();
  const canvas = document.getElementById("bg-3d-canvas");
  if (!canvas) return;

  const renderer = new THREE.WebGLRenderer({
    canvas,
    alpha: true,
    antialias: true,
  });
  renderer.setSize(window.innerWidth, window.innerHeight);

  // Camera setup
  const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  );
  camera.position.z = 5;

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
  scene.add(ambientLight);
  const pointLight = new THREE.PointLight(0xffffff, 0.8);
  pointLight.position.set(5, 5, 5);
  scene.add(pointLight);

  // Simple Cube Geometry for testing
  const geometry = new THREE.BoxGeometry(2, 2, 2);
  const material = new THREE.MeshStandardMaterial({
    color: 0x0077ff,
    wireframe: false,
  });
  const cube = new THREE.Mesh(geometry, material);
  scene.add(cube);

  // Mouse move interaction
  let mouseX = 0,
    mouseY = 0;
  document.addEventListener("mousemove", (event) => {
    mouseX = (event.clientX / window.innerWidth) * 2 - 1;
    mouseY = -(event.clientY / window.innerHeight) * 2 + 1;
  });

  // Animation loop
  function animate() {
    requestAnimationFrame(animate);

    // Simple rotation + mouse follow
    cube.rotation.y += 0.005 + (mouseX * 0.5 - cube.rotation.y) * 0.05;
    cube.rotation.x += 0.005 + (-mouseY * 0.5 - cube.rotation.x) * 0.05;

    renderer.render(scene, camera);
  }
  animate();

  // Handle window resize
  window.addEventListener("resize", () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
})();
