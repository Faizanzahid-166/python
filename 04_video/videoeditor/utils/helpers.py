"""Helper utilities."""
from pathlib import Path
from datetime import timedelta


def format_duration(seconds: float) -> str:
    """Format duration in seconds to human readable string.

    Args:
        seconds: Duration in seconds

    Returns:
        Formatted string like '1h 30m 45s' or '2m 15s'
    """
    if seconds < 0:
        return "0s"

    td = timedelta(seconds=int(seconds))
    total_seconds = int(td.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60

    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0 or hours > 0:
        parts.append(f"{minutes}m")
    parts.append(f"{secs}s")

    return " ".join(parts)


def ensure_path(path: str, is_dir: bool = False) -> Path:
    """Ensure path exists, create if necessary.

    Args:
        path: Path to ensure exists
        is_dir: If True, treat as directory

    Returns:
        Path object
    """
    p = Path(path)
    if is_dir:
        p.mkdir(parents=True, exist_ok=True)
    else:
        p.parent.mkdir(parents=True, exist_ok=True)
    return p


def get_file_size(path: str) -> int:
    """Get file size in bytes."""
    return Path(path).stat().st_size


def format_file_size(size_bytes: int) -> str:
    """Format file size to human readable string."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"
