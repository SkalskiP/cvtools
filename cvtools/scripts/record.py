import cv2
import argparse

from cvtools.io.sink import FrameSink
from cvtools.io.source import Camera
from dataclasses import dataclass


@dataclass
class RecordSpec:
    device_id: int
    frame_interval: int
    target_directory_path: str


def get_record_spec() -> RecordSpec:
    parser = argparse.ArgumentParser(description='Video Record')
    parser.add_argument("--device-id", "-d", dest="device_id", type=int, required=True)
    parser.add_argument("--target-directory-path", "-t", dest="target_directory_path", type=str, required=True)
    parser.add_argument("--frame-interval", "-i", dest="frame_interval", type=int, required=False, default=1)
    args = parser.parse_args()
    return RecordSpec(
        device_id=args.device_id,
        target_directory_path=args.target_directory_path,
        frame_interval=args.frame_interval
    )


if __name__ == '__main__':
    spec = get_record_spec()
    source = Camera(device_id=spec.device_id)
    sink = FrameSink(target_directory_path=spec.target_directory_path, frame_interval=spec.frame_interval)

    for frame in source.capture_stream():

        cv2.imshow('preview', frame)
        sink.persist(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            source.release()

    cv2.destroyAllWindows()
