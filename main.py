import sys

from colorama import Fore, Style, init

from k8s.client import get_pod_info

from analyzer.rules import analyze_pod

from analyzer.ai import ai_diagnose

init(autoreset=True)

def banner():

    print(Fore.CYAN + """

██╗  ██╗ █████╗  █████╗ 

██║ ██╔╝██╔══██╗██╔══██╗

█████╔╝ ╚█████╔╝╚█████╔╝

██╔═██╗ ██╔══██╗██╔══██╗

██║  ██╗╚█████╔╝╚█████╔╝

╚═╝  ╚═╝ ╚════╝  ╚════╝ 

Kubernetes AI Troubleshooter

""")

def main():

    banner()

    if len(sys.argv) < 3:

        print(Fore.YELLOW + "Usage:")

        print("python main.py pod <pod-name> [namespace]")

        return

    resource = sys.argv[1]

    name = sys.argv[2]

    namespace = "default"

    if len(sys.argv) == 4:

        namespace = sys.argv[3]

    if resource != "pod":

        print(Fore.RED + "Only pod diagnostics supported currently")

        return

    try:

        pod = get_pod_info(name, namespace)

        issues = analyze_pod(pod)

        print(Fore.GREEN + f"\n🔍 Diagnosing pod: {name}")

        print(Fore.CYAN + f"Namespace: {namespace}")

        if not issues:

            print(Fore.GREEN + "\n✅ No major issues detected")

        else:

            print(Fore.RED + "\n❌ Issues Found:\n")

            for issue in issues:

                print(Fore.RED + f"- {issue}")

        print(Fore.YELLOW + "\n🤖 AI Diagnosis:\n")

        ai_result = ai_diagnose(issues)

        print(Style.BRIGHT + ai_result)

    except Exception as e:

        print(Fore.RED + f"\nError: {str(e)}")

if __name__ == "__main__":

    main()
