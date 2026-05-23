def analyze_pod(pod):
    issues = []

    status = pod.status
    spec = pod.spec

    # Check pod phase
    if status.phase != "Running":
        issues.append(f"Pod phase is {status.phase}")

    # Container checks
    if status.container_statuses:

        for c in status.container_statuses:

            # CrashLoopBackOff
            if c.state.waiting:
                if c.state.waiting.reason == "CrashLoopBackOff":
                    issues.append(
                        f"Container '{c.name}' in CrashLoopBackOff"
                    )

            # Restart count
            if c.restart_count > 3:
                issues.append(
                    f"Container '{c.name}' restarted {c.restart_count} times"
                )

    # Resource limits
    for container in spec.containers:

        resources = container.resources

        if not resources:
            issues.append(
                f"Container '{container.name}' missing resources config"
            )
            continue

        if not resources.limits:
            issues.append(
                f"Container '{container.name}' missing resource limits"
            )

        if not resources.requests:
            issues.append(
                f"Container '{container.name}' missing resource requests"
            )

        # Latest tag detection
        if ":latest" in container.image:
            issues.append(
                f"Container '{container.name}' using latest image tag"
            )

    return issues
