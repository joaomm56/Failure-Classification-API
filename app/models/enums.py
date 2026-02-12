import enum

class SystemType(str, enum.Enum):
    api = "api"
    web_app = "web_app"
    database = "database"
    message_queue = "message_queue"
    external_service = "external_service"


class ComponentType(str, enum.Enum):
    auth = "auth"
    payments = "payments"
    users = "users"
    orders = "orders"
    cache = "cache"
    network = "network"


class ErrorType(str, enum.Enum):
    timeout = "timeout"
    connection_refused = "connection_refused"
    high_latency = "high_latency"
    out_of_memory = "out_of_memory"
    permission_denied = "permission_denied"


class SeverityLevel(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class FailureType(str, enum.Enum):
    database = "database"
    infrastructure = "infrastructure"
    deploy = "deploy"
    network = "network"
    application = "application"
    external = "external"
