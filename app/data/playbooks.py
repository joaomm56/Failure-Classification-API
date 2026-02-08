PLAYBOOKS = {
    "database": [
        "Check slow queries",
        "Verify indexes",
        "Inspect connection pool",
        "Check database CPU and memory usage"
    ],
    "infrastructure": [
        "Check CPU and memory usage",
        "Verify autoscaling rules",
        "Inspect disk I/O"
    ],
    "deploy": [
        "Rollback last deployment",
        "Verify environment variables",
        "Check configuration changes"
    ],
    "network": [
        "Check network latency",
        "Inspect firewall rules",
        "Verify DNS resolution"
    ],
    "application": [
        "Inspect application logs",
        "Check recent code changes",
        "Review exception stack traces"
    ],
    "external": [
        "Check third-party service status",
        "Apply retries or circuit breakers"
    ]
}
