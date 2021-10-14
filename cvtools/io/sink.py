import os
import cv2
import numpy as np


class FrameSink:

    def __init__(self, target_directory_path: str, frame_interval: int) -> None:
        self._target_directory = target_directory_path
        self._frame_interval = frame_interval
        self._frame_idx = 0

    def persist(self, frame: np.ndarray) -> None:
        os.makedirs(self._target_directory, exist_ok=True)

        if self._frame_idx % self._frame_interval == 0:
            file_name = f"frame-{self._frame_idx:05d}.png"
            file_path = os.path.join(self._target_directory, file_name)
            cv2.imwrite(file_path, frame)
        self._frame_idx += 1
