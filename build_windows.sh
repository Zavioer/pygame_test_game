#!/bin/bash
set -e

IMAGE_NAME="catch-a-bottle-builder"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="${SCRIPT_DIR}/dist"

echo "=== Building Windows .exe for Catch a Bottle! ==="

# Build the container image if it doesn't exist
if ! podman image exists "${IMAGE_NAME}"; then
    echo "Building container image (first time only)..."
    podman build -t "${IMAGE_NAME}" -f "${SCRIPT_DIR}/Containerfile.windows" "${SCRIPT_DIR}"
fi

# Clean previous build output
rm -rf "${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

# Run PyInstaller inside the container
echo "Running PyInstaller in Wine container..."
podman run --rm \
    -v "${SCRIPT_DIR}:/src:Z" \
    "${IMAGE_NAME}" \
    --noconfirm --clean \
    --log-level=INFO \
    catch_a_bottle.spec

echo ""
if [ -f "${OUTPUT_DIR}/CatchABottle.exe" ]; then
    echo "=== Build successful! ==="
    echo "Output: ${OUTPUT_DIR}/CatchABottle.exe"
else
    echo "=== Build failed - .exe not found ==="
    exit 1
fi
