from typing import Generator, Optional

import numpy as np

import cv2


class Camera:

    def __init__(self, device_id: int) -> None:
        self._device_id = device_id
        self._camera: Optional[cv2.VideoCapture] = None

    def capture_stream(self) -> Generator[np.ndarray, None, None]:
        self._camera = cv2.VideoCapture(self._device_id)

        while self._camera is not None and self._camera.isOpened():
            is_ok, frame = self._camera.read()
            if is_ok:
                yield frame

    def release(self) -> None:
        self._camera.release()
        self._camera = None
