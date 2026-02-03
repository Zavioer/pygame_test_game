#!/bin/bash
set -e

IMAGE_NAME="catch-a-bottle-test"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
EXE_PATH="${SCRIPT_DIR}/dist/CatchABottle.exe"

if [ ! -f "${EXE_PATH}" ]; then
    echo "Error: CatchABottle.exe not found in dist/"
    echo "Run ./build_windows.sh first to build the .exe"
    exit 1
fi

echo "=== Running CatchABottle.exe in Wine container ==="

# Build the test container image if it doesn't exist
if ! podman image exists "${IMAGE_NAME}"; then
    echo "Building test container image (first time only)..."
    podman build -t "${IMAGE_NAME}" -f "${SCRIPT_DIR}/Containerfile.windows-test" "${SCRIPT_DIR}"
fi

# Allow X11 connections from local containers
xhost +local: > /dev/null 2>&1

# Optional: sound device flag
SOUND_FLAG=""
if [ -e /dev/snd ]; then
    SOUND_FLAG="--device /dev/snd"
fi

echo "Starting game..."
podman run --rm \
    -e DISPLAY="${DISPLAY}" \
    -e SDL_AUDIODRIVER=dummy \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v "${SCRIPT_DIR}/dist:/app:Z" \
    --security-opt label=disable \
    --network=host \
    --ipc=host \
    ${SOUND_FLAG} \
    "${IMAGE_NAME}" \
    /app/CatchABottle.exe

# Restore X11 access
xhost -local: > /dev/null 2>&1

echo "Game exited."
