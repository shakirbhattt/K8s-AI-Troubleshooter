from kubernetes import client, config

def get_pod_info(pod_name, namespace="default"):
    config.load_kube_config()

    v1 = client.CoreV1Api()

    pod = v1.read_namespaced_pod(
        name=pod_name,
        namespace=namespace
    )

    return pod
