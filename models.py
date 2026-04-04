from enum import StrEnum


class ChunkType(StrEnum):
    FUNCTION = "function"
    METHOD = "method"
    CLASS = "class"
    MODULE = "module"
    DOC = "doc"
    CONFIG = "config"
    TEST = "test"


class FileChangeStatus(StrEnum):
    ADDED = "added"
    MODIFIED = "modified"
    REMOVED = "removed"
    RENAMED = "renamed"


class FindingSeverity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class FindingCategory(StrEnum):
    BUG = "bug"
    SECURITY = "security"
    PERFORMANCE = "performance"
    STYLE = "style"
    MAINTAINABILITY = "maintainability"
    TESTING = "testing"


class ReviewRisk(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN = "unknown"


class ActionType(StrEnum):
    POST_REVIEW_COMMENTS = "post_review_comments"
    CREATE_FIX_PULL_REQUEST = "create_fix_pull_request"
    UPDATE_CHECK_RUN = "update_check_run"
