### 1. **Corepack (The Modern Way)**
You learned that you don't need to manually `npm install -g pnpm`. By using **Corepack**, you use the package manager built into Node.js, making your Docker images smaller and builds faster.

### 2. **Docker Lifecycle Management**
*   **`up --build`**: How to force Docker to re-read your changes and rebuild images.
*   **`down`**: How to cleanly stop services and remove internal networks.
*   **`image prune -a`**: How to recover GBs of disk space by deleting "dangling" and old images.

### 3. **Reverse Proxying (Nginx)**
You learned how to use Nginx as a **Receptionist**. It solves the **CORS** problem by making the Frontend and Backend appear to be on the same "site" (`localhost:8080`), even though they are separate containers.

### 4. **Docker Networking & Service Discovery**
You learned that inside a Docker network, containers don't use IP addresses. They talk to each other using their **Service Names** (e.g., `http://backend:7000`).

### 5. **Volume Shadowing (The Conflict Fix)**
You learned a critical lesson: **Mounting a local folder over a container folder hides the files inside the image.** We fixed the `ERR_EMPTY_RESPONSE` by removing the volume that was accidentally deleting your Nginx config.

### 6. **Environment Detection**
You implemented logic in your HTML to detect if it's running in **Docker** (port 8080) or **Local/Netlify**, allowing your code to switch API URLs automatically.

**You are now handling Docker like a Full-Stack Engineer.** Great work!